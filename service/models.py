from django.db import models

class Equipment(models.Model):
    TECH_TYPE_CHOICES = [
        ('tractor', 'Трактор'),
        ('combine', 'Комбайн'),
        ('plow', 'Плуг'),
        ('seeder', 'Сеялка'),
        ('sprayer', 'Опрыскиватель'),
        ('harvester', 'Уборочная машина'),
        ('mower', 'Косилка'),
        ('baler', 'Пресс-подборщик'),
        ('cultivator', 'Культиватор'),
        ('fertilizer_spreader', 'Разбрасыватель удобрений'),
    ]

    SERVICE_TYPE_CHOICES = [
        ('harvest_wheat', 'Сбор пшеницы'),
        ('harvest_corn', 'Сбор кукурузы'),
        ('harvest_potatoes', 'Сбор картофеля'),
        ('harvest_sunflower', 'Сбор подсолнечника'),
        ('harvest_rice', 'Сбор риса'),
        ('harvest_beets', 'Сбор свёклы'),
        ('plowing', 'Вспашка'),
        ('seeding', 'Посев'),
        ('spraying', 'Опрыскивание'),
        ('fertilizing', 'Внесение удобрений'),
        ('mowing', 'Косилка'),
        ('baling', 'Скирдообразование'),
        ('cultivating', 'Культивация'),
        ('soil_compaction', 'Уплотнение почвы'),
        ('field_rolling', 'Каткование поля'),
        ('weeding', 'Прополка'),
        ('irrigation', 'Орошение'),
        ('transport_grain', 'Транспортировка зерна'),
        ('transport_hay', 'Транспортировка сена'),
        ('transport_fertilizers', 'Транспортировка удобрений'),
        ('load_unload', 'Погрузка/разгрузка'),
        ('mulching', 'Мульчирование'),
    ]

    provider_id = models.UUIDField()
    equipment_type = models.CharField(max_length=50, choices=TECH_TYPE_CHOICES)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    availability_status = models.BooleanField(default=True)
    price_per_hectar = models.DecimalField(max_digits=7, decimal_places=2)
    price_per_hour = models.DecimalField( max_digits=5, decimal_places=2)  # max_digits увеличен для больших цен
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_equipment_type_display()} - {self.get_service_type_display()}"

