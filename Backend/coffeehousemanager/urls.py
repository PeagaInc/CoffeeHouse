from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api import PositionViewSet
from .api import StaffViewSet
from .api import ProductTypeViewSet
from .api import ProductViewSet
from .api import InvoiceViewSet


router = routers.DefaultRouter()
router.register('position', PositionViewSet)
router.register('staff', StaffViewSet)
router.register('producttype', ProductTypeViewSet)
router.register('product', ProductViewSet)
router.register('invoice', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
