from django.contrib import admin

# Register your models here.
from .models import Menu,Order,Order_Items,Addition,Topping,Shopping_Cart
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Order_Items)
admin.site.register(Addition)
admin.site.register(Topping)
admin.site.register(Shopping_Cart)