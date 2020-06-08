from django.contrib import admin

# Register your models here.
from coffeehousemanager.models import Position
from coffeehousemanager.models import Staff
from coffeehousemanager.models import ProductType
from coffeehousemanager.models import Product
from coffeehousemanager.models import Invoice

admin.site.register (Position)
admin.site.register (Staff)
admin.site.register (ProductType)
admin.site.register (Product)
admin.site.register (Invoice)
