from django.contrib import admin
from main.models import Customer, Catalog, Product, Tag, ProductProperty, ProductImage


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')


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
    list_display = ('id', 'name', 'quantity', 'available', 'rating', 'show_count', 'create_date')
    prepopulated_fields = {'slug': ['name']}
    list_editable = ('available', )
    raw_id_fields = ('tags', )
    search_fields = ['name', 'code_1c']
    search_help_text = 'Поиск по наименованию или коду из 1С'
    readonly_fields = ('show_count', 'rating')
    list_filter = ('available', )

    inlines = (ProductImageInline, ProductPropertyInline)




