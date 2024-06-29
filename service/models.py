from django.db import models

from users.models import Masseur, User

NULLABLE = {'blank': True, 'null': True}


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, unique=True)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='services/images/', **NULLABLE)
    icon = models.ImageField(verbose_name='Иконка', upload_to='services/icons/', **NULLABLE)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=0, **NULLABLE)
    top_service = models.BooleanField(verbose_name='Топ услуга', default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Apppointment(models.Model):

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Почта", **NULLABLE)
    name = models.CharField(max_length=100, **NULLABLE, verbose_name='Имя')
    surname = models.CharField(max_length=100, **NULLABLE, verbose_name='Фамилия')
    phone = models.CharField(max_length=100, **NULLABLE, verbose_name='Телефон')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, **NULLABLE, verbose_name="Массаж")
    masseur = models.ForeignKey(Masseur, on_delete=models.CASCADE, **NULLABLE, verbose_name='Массажист')
    date = models.DateTimeField(verbose_name='Дата и время записи', **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} {self.surname}" if self.name and self.surname else "Appointment"

    class Meta:
        verbose_name = "Запись на массаж"
        verbose_name_plural = "Записи на массаж"
