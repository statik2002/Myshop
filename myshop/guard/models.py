from django.utils import timezone
from django.db import models


class Ban(models.Model):
    ip = models.GenericIPAddressField()
    first_attempt = models.DateTimeField(default=timezone.now, verbose_name='Первая попытка')
    attempt_count = models.SmallIntegerField(verbose_name='Кол-во попыток')
    blocked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Бан'
        verbose_name_plural = 'Баны'

    def __str__(self) -> str:
        return f'IP: {self.ip} - Попыток: {self.attempt_count} - Блокировка: {self.blocked}'
    

class RequestHistory(models.Model):
    metrica = models.ForeignKey('Metrica', on_delete=models.CASCADE, related_name='requests_history')
    path = models.CharField(max_length=1000)
    


class Metrica(models.Model):
    session_key = models.CharField(max_length=500, verbose_name='Ключ сессии')
    first_request = models.DateTimeField(default=timezone.now, verbose_name='Первое обращение')
    last_request = models.DateTimeField(default=timezone.now, verbose_name='Последнее обращение')
    ip = models.GenericIPAddressField(verbose_name='IP адрес')
    user_agent = models.CharField(max_length=1000, verbose_name='User agent')


    class Meta:
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'

    def __str__(self) -> str:
        return f'Lasst request: {self.last_request}, IP: {self.ip}, UserAgent: {self.user_agent}'