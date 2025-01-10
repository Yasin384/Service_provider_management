from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Equipment
from .serializers import EquipmentSerializer

USER_SERVICE_API = "https://manageuser.up.railway.app"

def get_user_from_token(token):
    headers = {'Authorization':f'Bearer{token}'}
    response = requests.get(f'{USER_SERVICE_API}/api/me',headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code = 401:
        raiseException('invalid or expired token')
    else:
        raise Exception(f"Failed to connect to User Management Service: {response.status_code}")
class EquipmentListCreateView(APIView):
    def get(self,request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response({'error':'Authorization header missing'},status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split('')[1]
        try:
            user_data = get_user_from_token(token)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        provider_id = user_data['id']
        equipment = Equipment.objects.filter(proider_id=provider_id)
        serializer = EquipmentSerializer(equipment,many=True)
        returnResponse(serializer.data, status = status.HTTP_200_OK)

        def post(self,request):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return Response({'error':'Authorization header missing'})
            token = auth_header.split('')[1]
            try:
                user_data= get_user_from_token(token)
            except Exception as e:
                return Response({'error':str(e)},status = status.HTTP_401_UNAUTHORIZED)
            provider_id = user_data['id']
            data = request.data.copy()
            data['provider_id'] = provider_id

            serializer = EquipmentSerializer(data=data)
            if serilaizer.is_valid():
                serializer.save()
                return Response(serializer.data,status)
class EquipmentDetailView(APIView):
    def get_object(self,pk,provider_id):
        try:
            return Equipment.objects.get(pk=pk,provider_id=provider_id)
        except Equipment.DoesNotExist:
            return None
    def get(self,request,pk):
        auth_header=request.header.get('Authorization')
        if not auth_header:
            return Response({'error':'Authorization header is missing!!!'})
        token = auth_header.split('')[1]
        try:
            user_data=get_user_from_token(token)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTT_401_UNAUTHORIZED)
        provider_id = user_data['id'] 
        equipment = self.get_object(pk,provider_id)
        if not equipment:
            return Response('No equipment')
        serializer=EquipmentSerializer(equipment)       
        return Response(serializer.data,status = status.HTTP_200_OK)
    def patch(self,request,pk):
        auth_header = request.header.get('Authorization')
        if not auth_header:
            return Response('missing auth header')
        token = auth_header.split('')[1]
        try:
            user_data = get_user_from_token(token)
        except Exception as e:
            return Response('UnAuthorized')
        provider_id = user_data['id']
        equipment = self.get_object(pk = pk , provider_id = provider_id)
        if not equipment:
            return Response('there is no equipment obj')
        serializer = EquipmentSerializer(equipment)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_401_BAD_REQUEST)
    def delete(self,request,pk):
        auth_header=request.header.get('Authorization')
        if not auth_header:
            return Response('no header auth')
        token = auth_header.split('')[1]
        try:
            user_data = get_user_from_token(token)
        except Exception as e:
            return Response('Unauthorized')
        provider_id = user_data['id']
        equipment = self.get_object(pk=pk,provider_id=provider_id)
        equipment.dalate()
        return Response('Equipment was deleted succesfully',status=status.HTTP_204_NO_CONTENT)
