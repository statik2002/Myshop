from django.contrib import admin

from main.models import Customer, Catalog, Product, ProductProperty


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_1c')


class ProductPropertyInline(admin.StackedInline):
    model = ProductProperty


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_1c')

    inlines = (ProductPropertyInline, )

