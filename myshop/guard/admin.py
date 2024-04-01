from django.contrib import admin
from http.client import responses
from guard.models import Ban, Metrica, RequestHistory, ResponseErrors


@admin.register(Ban)
class BanAdmin(admin.ModelAdmin):
    pass


class RequestHistoryInlines(admin.StackedInline):
    model = RequestHistory
    extra = 0


@admin.register(Metrica)
class MetricaAdmin(admin.ModelAdmin):
    inlines = [RequestHistoryInlines]


@admin.register(ResponseErrors)
class ResponseErrorsAdmin(admin.ModelAdmin):
    fields = ('session_key', 'date', 'ip', 'user_agent', 'error_code', 'error_describe', 'request')
    readonly_fields = ('error_describe', 'request')