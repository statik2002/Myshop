from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

from main.models import Customer, Catalog, Product, Color, Metrics, Tag


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


class ColorInline(admin.TabularInline):
    model = Color
    extra = 1


class MetricsInline(admin.TabularInline):
    model = Metrics
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_1c', 'price', 'discount', 'available', 'rating', 'quantity', 'show_count', 'create_date')
    prepopulated_fields = {'slug': ['name']}
    list_editable = ('available', )
    raw_id_fields = ('tags', )
    search_fields = ['name', 'code_1c']
    search_help_text = 'Поиск по наименованию или коду из 1С'
    readonly_fields = ('show_count', 'rating')
    list_filter = ('available', )

    inlines = (ColorInline, MetricsInline)




