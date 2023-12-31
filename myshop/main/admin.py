from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from main.models import Customer, Catalog, Product, ProductProperty, ProductPropertyContent, ProductProp


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_1c')


class ProductPropertyInline(admin.StackedInline):
    model = ProductProperty
    extra = 1


class ProductPropertyContentInline(admin.StackedInline):
    model = ProductProp
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_1c')

    inlines = (ProductPropertyContentInline, )


