from django.contrib import admin
from .models import Customer, Restaurant, Item, Menu, Order, orderItem, User

admin.site.site_header = 'Fresh Food Adminstration'


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'f_name',
        'l_name',
        'city',
        'phone',
        'address'
    )


class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'rname',
        'info',
        'min_ord',
        'location',
        'r_logo',
        'status',
        'approved'
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'fname',
        'category',
        'image',
        'description'
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'r_id',
        'price',
        'quantity'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'total_amount',
        'orderedBy',
        'delivery_addr',
        'r_id',
        'status'
    )


class orderItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_id',
        'ord_id',
        'quantity'
    )


admin.site.register(User)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(orderItem, orderItemAdmin)
