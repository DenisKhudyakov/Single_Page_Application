from django.db import models


class Registry(models.Model):
    """
    Класс для реестра логистической компании
    таблица должна содержать:
    1) Дата отгрузки
    2) Название отправителя
    3) Количество мест
    4) Расстояние
    """
    date = models.DateField(auto_now=True, verbose_name='Дата отгрузки')
    name = models.CharField(max_length=50, verbose_name='Название отправителя')
    count = models.IntegerField(verbose_name='Количество мест')
    distance = models.IntegerField(verbose_name='Расстояние')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Реестр'
        verbose_name_plural = 'Реестры'