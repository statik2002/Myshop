from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from main.models import Cart, Customer, Catalog, Order, OrderStatus, Product, ProductInOrder, ProductRating, Tag, ProductProperty, ProductImage
from django.contrib.auth.admin import UserAdmin


class LikedProductsInline(admin.StackedInline):
    model = Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'login_fail_counter', 'ban_status')
    readonly_fields = ('id',)
    raw_id_fields = ('likes', )



@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


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
    list_display = ('id', 'name', 'quantity', 'available', 'rating', 'show_count', 'create_date', 'get_rating')
    prepopulated_fields = {'slug': ['name']}
    list_editable = ('available', )
    raw_id_fields = ('tags',)
    search_fields = ['name', 'code_1c', 'id']
    search_help_text = 'Поиск по наименованию или коду из 1С'
    readonly_fields = ('show_count', 'rating')
    list_filter = ('available', )

    inlines = (ProductImageInline, ProductPropertyInline)

    def get_rating(self, obj):
        try:
            rating = ProductRating.objects.get(product=obj)
            return rating.value
        except ObjectDoesNotExist:
            return 0.0


class ProductsInOrderInline(admin.StackedInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAmin(admin.ModelAdmin):
    inlines = (ProductsInOrderInline, )


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass