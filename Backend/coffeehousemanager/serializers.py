from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

# model
from coffeehousemanager.models import Position
from coffeehousemanager.models import Staff
from coffeehousemanager.models import ProductType
from coffeehousemanager.models import Product
from coffeehousemanager.models import Invoice

class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = "PositionName"


class StaffSerializers(serializers.ModelSerializer):
    PositionName = serializers.StringRelatedField(source="Position")
    Image = Base64ImageField(required=False)

    class Meta:
        model = Staff
        fields = "__all__"


class ProductTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    Image = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = "__all__"

class InvoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"
