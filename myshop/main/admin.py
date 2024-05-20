from decimal import Decimal
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from main.models import (
        Cart, Customer, Catalog, Feedback, MainMenuItem, MainSlider, Order, OrderStatus, PickPoint, Product, 
        ProductInCart, ProductInOrder, ProductQuestion, ProductRating, ProductUnit, SubMenuItem, Tag, ProductProperty, 
        ProductImage, SimplePage
    )
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from main.list_filters import ProductGtZero, ProductWithDiscount, ProductWithImages


class LikedProductsInline(admin.StackedInline):
    model = Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email', 'first_name', 'last_name', 'is_active', 'ban_status')
    readonly_fields = ('id',)
    raw_id_fields = ('likes', )



@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'is_active', )
    list_editable = ('is_active', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class ProductPropertyInline(admin.StackedInline):
    model = ProductProperty
    extra = 1


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'tumbnail', 'quantity', 'first_price', 'online_price', 'margin', 'total_price', 'price', 'discount', 'available', 'catalog')
    prepopulated_fields = {'slug': ['name']}
    list_editable = ('available', 'catalog', 'online_price', 'discount')
    raw_id_fields = ('tags',)
    search_fields = ['name', 'code_1c', 'id']
    search_help_text = 'Поиск по наименованию или коду из 1С'
    readonly_fields = ('show_count', 'rating', 'tumbnail', 'margin', 'total_price')
    list_filter = ('available', ProductGtZero, ProductWithImages, ProductWithDiscount)

    inlines = (ProductImageInline, ProductPropertyInline, )

    def get_rating(self, obj):
        try:
            rating = ProductRating.objects.get(product=obj)
            return rating.value
        except ObjectDoesNotExist:
            return 0.0
        
    def tumbnail(self, obj):
        #print(obj)
        product_image = ProductImage.objects.filter(product=obj).first()
        if product_image:
            return mark_safe(f'<img style="border: 1px solid #00af64" src="{product_image.image.url}" width="80" height="80" />')
        else:
            return mark_safe(f'No image')
        
    def margin(self, obj):
        if obj.first_price == 0.0:
            return 0.0
        
        if obj.discount > 0:
            discount = obj.online_price * obj.discount / 100
        else:
            discount = 0
        magrin = Decimal((obj.online_price - discount - obj.first_price) / obj.first_price * 100).quantize(Decimal('1.00'))
        if magrin < 0:
            return format_html(f'<b style="color: red;">{magrin}</b>')
        
        return format_html(f'<b>{magrin}</b>')
    
    def total_price(self, obj):
        if obj.discount > 0:
            discount = obj.online_price * obj.discount / 100
        else:
            discount = 0
        total = Decimal(obj.online_price - discount).quantize(Decimal('1.00'))
        if total < obj.first_price:
            return format_html(f'<b style="color: red;">{total}</b>')
        else:
            return format_html(f'<b>{total}</b>')



class ProductsInOrderInline(admin.StackedInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_create', 'order_update', 'order_status', 'get_total_amount')
    list_editable = ['order_status']
    inlines = (ProductsInOrderInline, )


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


class ProductsInCartAdmin(admin.StackedInline):
    model = ProductInCart
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductsInCartAdmin]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'post_at', 'rating', 'is_show')
    readonly_fields = ('product', )
    list_editable = ('is_show',)


@admin.register(ProductQuestion)
class ProductQuestion(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'created', 'is_show')
    list_editable = ('is_show',)


@admin.register(PickPoint)
class PickPointAdmin(admin.ModelAdmin):
    pass


class SubMenuItemInline(admin.StackedInline):
    model = SubMenuItem
    extra =1


@admin.register(MainMenuItem)
class MainMenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    
    inlines = (SubMenuItemInline,)


@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    pass


@admin.register(SimplePage)
class SimplePageAdmin(admin.ModelAdmin):
    pass

