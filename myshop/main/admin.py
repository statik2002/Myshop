from decimal import Decimal
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from main.models import (
        Cart, Customer, Catalog, Feedback, MainMenuItem, MainSlider, Order, OrderStatus, PickPoint, Product, 
        ProductInCart, ProductInOrder, ProductQuestion, ProductRating, ProductUnit, SubMenuItem, Tag, ProductProperty, 
        ProductImage
    )
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe


class LikedProductsInline(admin.StackedInline):
    model = Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'first_name', 'last_name', 'login_fail_counter', 'ban_status')
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
    list_display = ('name', 'tumbnail', 'quantity', 'first_price', 'online_price', 'margin', 'price', 'available', 'catalog')
    prepopulated_fields = {'slug': ['name']}
    list_editable = ('available', 'catalog', 'online_price')
    raw_id_fields = ('tags',)
    search_fields = ['name', 'code_1c', 'id']
    search_help_text = 'Поиск по наименованию или коду из 1С'
    readonly_fields = ('show_count', 'rating', 'tumbnail', 'margin')
    list_filter = ('available', )

    inlines = (ProductImageInline, ProductPropertyInline)

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
        return Decimal(obj.online_price*100/obj.first_price - 100).quantize(Decimal('1.00'))



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