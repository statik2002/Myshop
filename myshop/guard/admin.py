from django.contrib import admin

from guard.models import Ban, Metrica, RequestHistory


@admin.register(Ban)
class BanAdmin(admin.ModelAdmin):
    pass


class RequestHistoryInlines(admin.StackedInline):
    model = RequestHistory
    extra = 0


@admin.register(Metrica)
class MetricaAdmin(admin.ModelAdmin):
    inlines = [RequestHistoryInlines]