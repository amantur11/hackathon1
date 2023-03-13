from django.contrib import admin
from .models import Order, OrderInfo, OrderProduct


class OrderInfoInline(admin.TabularInline):
    model = OrderInfo
    max_num = 1

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('price', 'new_price', 'size_range', 'color', 'image_tag')


class OrderProductAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline, OrderInfoInline,]
    readonly_fields = ('data',)


admin.site.register(Order, OrderProductAdmin)