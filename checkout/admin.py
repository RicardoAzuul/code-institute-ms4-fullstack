from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    """ Adds OrderLineItem as an editable field to Orders """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Makes orders available for editing via the admin portal """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields=('order_number', 'date',
                        'delivery_cost', 'order_total',
                        'grand_total', 'original_cart', 'stripe_payment_id',)

    fields=('order_number', 'user_profile', 'date', 'full_name',
                'email', 'phone_number', 'country',
                'postcode', 'town_or_city', 'street_address1',
                'street_address2', 'county', 'delivery_cost',
                'order_total', 'grand_total', 'original_cart', 'stripe_payment_id',)

    list_display=('order_number', 'date', 'full_name',
                'order_total', 'delivery_cost',
                 'grand_total',)
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)