from django.db import models

from users.models import Course, Masseur, User

NULLABLE = {'blank': True, 'null': True}


class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, unique=True)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='services/images/', **NULLABLE)
    icon = models.ImageField(verbose_name='Иконка', upload_to='services/icons/', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    price = models.DecimalField(verbose_name='Стоимость', decimal_places=None, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Apppointment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Имя клиента')
    surname = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Фамилия клиента')
    phone = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Телефон клиента')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    masseur = models.ForeignKey(Masseur, on_delete=models.CASCADE, **NULLABLE, verbose_name='Массажист')
    date = models.DateField(verbose_name='Дата и время записи', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись на массаж"
        verbose_name_plural = "Записи на массаж"
