from django.contrib import admin

from main.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

