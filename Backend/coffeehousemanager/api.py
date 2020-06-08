from rest_framework import viewsets, permissions

# model
from coffeehousemanager.models import Position
from coffeehousemanager.models import Staff
from coffeehousemanager.models import ProductType
from coffeehousemanager.models import Product
from coffeehousemanager.models import Invoice

# serializers
from coffeehousemanager.serializers import PositionSerializers
from coffeehousemanager.serializers import StaffSerializers
from coffeehousemanager.serializers import ProductTypeSerializers
from coffeehousemanager.serializers import ProductSerializers
from coffeehousemanager.serializers import InvoiceSerializers

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PositionSerializers



class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StaffSerializers


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductTypeSerializers
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializers
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InvoiceSerializers