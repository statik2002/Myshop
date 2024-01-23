from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
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
    email = models.EmailField(max_length=256, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Фамилия')
    is_read_pd = models.BooleanField(default=False, verbose_name='Соглашение прочтено')
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    date_joined = models.DateTimeField(
        'Дата регистрации',
        default=timezone.now
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='media/avatars/', verbose_name='Аватар')
    likes = models.ManyToManyField('Product', verbose_name='Лайкнутые товары', blank=True)

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
    code_1c = models.PositiveIntegerField(verbose_name='Код каталога из 1С', blank=True, null=True)
    image = models.ImageField(upload_to='media/catalog_images', verbose_name='Изображение', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Показывается', default=True)
    slug = models.SlugField(max_length=200)
    order = models.IntegerField(verbose_name='Порядок', default=1)  # Для сортировки
    icon = models.CharField(max_length=250, verbose_name='Код иконки', blank=True, null=True)  # html код иконки

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self) -> str:
        return f'{self.name[:20]}'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self) -> str:
        return f'{self.title}'


class ProductImage(models.Model):
    product = models.ForeignKey('Product', verbose_name='Товар',
                                on_delete=models.CASCADE, related_name='product_images')
    alt = models.CharField(max_length=100, verbose_name='Alt изображения')
    image = models.ImageField(upload_to='media/product_images', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self) -> str:
        return f'{self.alt[:20]}'


class Product(models.Model):

    name = models.CharField('Наименование товара', max_length=200)
    description = models.TextField(verbose_name='Описание')
    available = models.BooleanField(verbose_name='Показывается', default=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products', verbose_name='В каталоге')
    slug = models.SlugField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг', default=0.0)  # 0.0
    tags = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True)
    show_count = models.BigIntegerField(verbose_name='Кол-во показов', default=0)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-create_date', 'show_count']

    def __str__(self) -> str:
        return f'{self.name[:20]}'


class ProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties')
    code_1c = models.PositiveIntegerField('Код из 1С', blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name='Color')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Размер скидки',
                                   default=0.0)  # 000 000 000.00 сумма скидки
    weight = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Weight')
    width = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Ширина см')  # 000.00 в см
    height = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Высота см')  # 000.00 в см
    length = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Длинна см')  # 000.00 в см
    quantity = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Количество', default=0.0)  # 000 000.000
    image = models.ImageField(upload_to='media/products/')

    class Meta:
        verbose_name = 'Product property'
        verbose_name_plural = 'Product properties'

    def __str__(self) -> str:
        return f'{self.color}'
