from typing import Any
from django.contrib.admin import SimpleListFilter
from django.db.models.query import QuerySet
from django.db.models import Prefetch
from django.db.models import Count

from main.models import ProductImage


class ProductGtZero(SimpleListFilter):

    title = 'Товары с остатком > 0'
    parameter_name = 'products_gt_0'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('gt_0', 'С остатком > 0')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        
        if self.value() == 'gt_0':
            return queryset.filter(quantity__gt=0)
        

class ProductWithImages(SimpleListFilter):

    title = 'Товары с картинками'
    parameter_name = 'product_with_images'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('is_images', 'С картинками'),
            ('no_images', 'Без картинок')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        
        if self.value() == 'is_images':
            queryset = queryset.prefetch_related('product_images').annotate(image_count=Count('product_images__image'))

            return queryset.filter(image_count__gt=0)
        
        if self.value() == 'no_images':
            queryset = queryset.prefetch_related('product_images').annotate(image_count=Count('product_images__image'))
            return queryset.filter(image_count__lt=1)


class ProductWithDiscount(SimpleListFilter):

    title = 'Товары со скидкой'
    parameter_name = 'products_with_discount'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('with_discount', 'Со скидкой'),
            ('without_discount', 'Без скидки')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        
        if self.value() == 'with_discount':
            return queryset.filter(discount__gt=0)
        
        if self.value() == 'without_discount':
            return queryset.filter(discount=0)