import decimal
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import Count, Sum
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
import uuid
from tinymce.models import HTMLField


class CustomerManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        cart = Cart.objects.create()
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.cart = cart
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number,  password=None, **extra_fields):
        user = self.create_user(phone_number, password=password, **extra_fields)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username=None
    first_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Фамилия')
    is_read_pd = models.BooleanField(default=False, verbose_name='Соглашение прочтено')
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    is_active = models.BooleanField('is_active', default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField('email')
    date_joined = models.DateTimeField(
        'Дата регистрации',
        default=timezone.now
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар')
    likes = models.ManyToManyField('Product', verbose_name='Лайкнутые товары', blank=True)
    personal_discount = models.SmallIntegerField(verbose_name='Персональная скидка', default=0)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='customer')
    pickpoint = models.ForeignKey('PickPoint', on_delete=models.CASCADE, related_name='pickpoints', null=True, blank=True)

    login_fail_counter = models.SmallIntegerField(default=0, verbose_name='Счетчик неудачных входов')
    ban_status = models.BooleanField(default=False, verbose_name='Бан или нет')
    ban_time = models.DateTimeField(verbose_name='Время бана', null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'

    objects = CustomerManager()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} : {self.phone_number} : {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Catalog(models.Model):

    name = models.CharField('Название каталога', max_length=150)
    code_1c = models.PositiveIntegerField(verbose_name='Код каталога из 1С', unique=True)
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
    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self) -> str:
        return f'{self.alt[:20]}'


class ProductUnit(models.Model):
    long_name = models.CharField(max_length=50, verbose_name='Длинное наименование')
    short_name = models.CharField(max_length=10, verbose_name='Короткое наименование')

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self) -> str:
        return f'{self.short_name}'


class Product(models.Model):

    name = models.CharField('Наименование товара', max_length=200)
    description = models.TextField(verbose_name='Описание', default='Нет описания', null=True, blank=True)
    available = models.BooleanField(verbose_name='Показ', default=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products', verbose_name='В каталоге', blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг', default=0.0)  # 0.0
    tags = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True)
    show_count = models.BigIntegerField(verbose_name='Кол-во показов', default=0)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    first_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Закуп. цена', default=0.0)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Розн. цена', default=0.0)
    online_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Онлайн цена', default=0.0)
    discount = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Размер скидки',
                                   default=0.0)  # 000 000 000.00 сумма скидки
    code_1c = models.PositiveIntegerField('Код из 1С', unique=True)
    quantity = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Количество',
                                   default=0.0)  # 000 000.000
    unit = models.ForeignKey(ProductUnit, on_delete=models.CASCADE, related_name='product_unit', null=True, blank=True, verbose_name='Еденица измерения')
    

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-create_date', 'show_count']

    def __str__(self) -> str:
        return f'{self.name[:20]}'


class ProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties', verbose_name='Товар')
    color = models.CharField(max_length=50, verbose_name='Цвет', default='', blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Вес кг.', default=0)
    width = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Ширина м.', default=0)  # 000.00 в см
    height = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Высота м.', default=0)  # 000.00 в см
    length = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Длинна м.', default=0)  # 000.00 в см
    description = models.TextField(verbose_name='Описание для свойства', default='', blank=True)
    material = models.CharField(max_length=250, verbose_name='Материал\состав', default='', blank=True)
    expiration_date = models.SmallIntegerField(verbose_name='Срок годности. Месяцев', default=0)
    production_origin = models.CharField('Страна производитель', max_length=200, default='', blank=True)

    class Meta:
        verbose_name = 'Product property'
        verbose_name_plural = 'Product properties'

    def __str__(self) -> str:
        return f'{self.color}'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_carts')
    quantity = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Количество в корзине', default='1.0')
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зафиксированая цена')
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='products')

    def total(self) -> decimal:
        return self.quantity * self.fixed_price


class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self) -> str:
        return f'Корзина пользователя: {self.uuid}, кол-во товаров: '
    

class ProductRating(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='his_rating')
    value = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг', default=0.0)  # 0.0
    counter = models.IntegerField(verbose_name='Кол-во оценок', default=0)

    class Meta:
        verbose_name = 'Рейтинг товара'
        verbose_name_plural = 'Рейтинги товаров'

    def __str__(self) -> str:
        return f'{self.product.name} : {self.value} ({self.counter})'


class CustomerBan(models.Model):

    def ban_delta(self):
        return timezone.now() + timezone.timedelta(days=1)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bans')
    ban_datetime = models.DateTimeField(default=timezone.now, verbose_name='Время бана')
    ban_reazon = models.CharField(max_length=500, verbose_name='Причина бана')
    ban_before = models.DateTimeField(default=ban_delta, verbose_name='Бан до:')

    class Meta:
        verbose_name = 'Бан пользователя'
        verbose_name_plural = 'Баны пользователей'

    def __str__(self) -> str:
        return f'Пользователь: {self.customer.phone_number} забанен {self.ban_datetime} по причине {self.ban_reazon} до {self.ban_before}'
    
    
class CustomerLoginFail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='login_failed')
    login_fail_last_time = models.DateTimeField(default=timezone.now, verbose_name='Время последннего неудачного входа')
    login_fail_counter = models.SmallIntegerField(default=1, verbose_name='Счетчик неудачных входов')
    login_fail_total_counter = models.PositiveIntegerField(default=1, verbose_name='Счетчик всех неудачных входов')

    class Meta:
        verbose_name = 'Счетчик неудачных входов пользователя'
        verbose_name_plural = 'Счетчики неудачных входов пользователей'

    def __str__(self) -> str:
        return (f'Пользователь: {self.customer.phone_number}'
                f'последний неудачный вход {self.login_fail_last_time},' 
                f'кол-во неудачных входов до бана {self.login_fail_counter},'
                f'всего неудачных входов {self.login_fail_total_counter}')
    

class OrderStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name='Наименование статуса заказа')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural= 'Статусы заказов'

    def __str__(self) -> str:
        return self.status


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_order')
    quantity = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Количество в корзине', default='1.0')
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зафиксированая цена', default='0.00')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products')

    def total(self) -> decimal:
        return self.quantity * self.fixed_price


class Order(models.Model):
    order_create = models.DateTimeField(default=timezone.now, verbose_name='Дата и время заказа')
    order_update = models.DateTimeField(default=timezone.now, verbose_name='Дата и время изменения заказа')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, related_name='orders_status', default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='user_orders', default=None)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return (
                f'Заказ №: {self.pk} от пользователя: {self.customer.phone_number},'
                f' дата создания: {self.order_create.strftime("%Y-%m-%d %H:%M")} co статусом: {self.order_status.status},'
                f' Позиций: {self.get_position_count_order()},'
                f' На сумму: {self.get_total_amount():.2f} Руб.'
            )
    
    def get_position_count_order(self) -> int:
        position_count = ProductInOrder.objects.filter(order=self).annotate(Count('product'))
        return len(position_count)

    def get_total_amount(self) -> decimal:
        products = ProductInOrder.objects.filter(order=self)
        total = 0
        for product in products:
            total += product.quantity * product.fixed_price
        return total


class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_feedbacks', verbose_name='Товар')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_feedbacks', verbose_name='Покупатель')
    post_at = models.DateTimeField(default=timezone.now, verbose_name='Дата отзыва')
    positive = models.TextField(verbose_name='Положительные моменты', blank=True, null=True)
    negative = models.TextField(verbose_name='Отрицательные моменты', blank=True, null=True)
    summary = models.TextField(verbose_name='Общий отзыв')
    rating = models.SmallIntegerField(verbose_name='Рейтинг')

    is_show = models.BooleanField(verbose_name='Отображается', default=False)

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def __str__(self) -> str:
        return f'Отзыв пользователя: {self.customer.phone_number}, Дата: {self.post_at}, Рейтинг: {self.rating}, Показ: {self.is_show}'


class ProductQuestion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions', verbose_name='Товар')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_questions', verbose_name='Покупатель')
    question_text = models.TextField(verbose_name='Тескт вопроса')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата и время создания')
    is_show = models.BooleanField(default=False, verbose_name='Опубликован')


    class Meta:
        verbose_name = 'Вопрос к товару'
        verbose_name_plural = 'Вопросы к тоаварам'

    def __str__(self) -> str:
        return f'Вопрос от пользователя: {self.customer.first_name} {self.customer.last_name}, к товару: {self.product.pk}, {self.created}'
    

class PickPoint(models.Model):
    name = models.CharField('Пункт выдачи', max_length=100)
    address = models.CharField('Адрес', max_length=200)
    phone = PhoneNumberField(verbose_name='Телефон', null=True, blank=True)
    rating = models.SmallIntegerField('Рейтинг', default=0)

    class Meta:
        verbose_name = 'Пункт выдачи'
        verbose_name_plural = 'Пункты выдачи'

    def __str__(self) -> str:
        return f'{self.name} ___ {self.address}'
    

class SubMenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Пункт подменю')
    link = models.CharField(max_length=250, verbose_name='Ссылка на страницу')
    menu_item = models.ForeignKey('MainMenuItem', on_delete=models.CASCADE, related_name='submen')

    class Meta:
        verbose_name = 'Элемент подменю'
        verbose_name_plural = 'Элементы подменю'

    def __str__(self) -> str:
        return f'{self.name}'


class MainMenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Пункт главного меню')
    link = models.CharField(max_length=250, verbose_name='Ссылка на страницу')

    class Meta:
        verbose_name = 'Элемент главного меню'
        verbose_name_plural = 'Элементы главного меню'

    def __str__(self) -> str:
        return f'{self.name}'
    

class MainSlider(models.Model):
    name = models.CharField(max_length=200, verbose_name='Главный слайдер')
    link = models.URLField(max_length=200, verbose_name='Ссылка', blank=True, null=True)
    image = models.ImageField(upload_to='sliders')
    title = models.CharField(max_length=100, verbose_name='Заголовок слайда')
    text = models.CharField(max_length=200, verbose_name='Текст слайда')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
    
    def __str__(self) -> str:
        return f'{self.name}'
    

class SimplePage(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = HTMLField()
    is_active = models.BooleanField(default=True, verbose_name='Показ')

    class Meta:
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'

    def __str__(self) -> str:
        return f'{self.title}'