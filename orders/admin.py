from django.contrib import admin
from .models import Order, OrderItem, PaymentMethod, Delivery, History


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'payment', 'delivery']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(PaymentMethod, PaymentAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Delivery, DeliveryAdmin)


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order', 'date']
    list_filter = ['date']


admin.site.register(History, HistoryAdmin)