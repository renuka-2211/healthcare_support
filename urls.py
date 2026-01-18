from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupportRequestViewSet, health_tip

router = DefaultRouter()
router.register('requests', SupportRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('health-tip/', health_tip),
]
