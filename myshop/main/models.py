from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.views import generic
from phonenumber_field.modelfields import PhoneNumberField


class CustomerManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Необходимо указать номер телефона')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number,  password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone_number,  password, **extra_fields)


class Customer(AbstractUser):
    username = None
    email = models.EmailField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    is_read_pd = models.BooleanField(default=False)
    phone_number = PhoneNumberField(unique=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    date_joined = models.DateTimeField(
        'Дата регистрации',
        default=timezone.now
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='media/avatars/')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'

    objects = CustomerManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} : {self.phone_number}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Catalog(models.Model):

    name = models.CharField('Название каталога', max_length=150)
    code_1c = models.PositiveIntegerField(verbose_name='Код каталога из 1С')

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self) -> str:
        return f'{self.code_1c} -> {self.name}'


class Product(models.Model):

    name = models.CharField('Наименование товара', max_length=200)
    description = models.TextField()
    code_1c = models.PositiveIntegerField('Код из 1С')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return f'{self.name[:20]}'


class ProductUnit(models.Model):
    name = models.CharField('Единица измерения', max_length=50)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self) -> str:
        return f'{self.name}'


class ProductProperty(models.Model):
    title = models.CharField('Наименование свойства', max_length=100)
    value = models.CharField('Значение свойства', max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self) -> str:
        return f'{self.title} - {self.value}'


class ProductPropertyContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    property = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['content_type', 'object_id'])]


class ProductProp(models.Model):
    name = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    property = GenericForeignKey('content_type', 'object_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Color(ProductProp):
    value = models.CharField(max_length=100)


class Weight(ProductProp):
    value = models.DecimalField(max_digits=6, decimal_places=3)
