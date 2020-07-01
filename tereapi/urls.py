
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from productos.views import CervezaViewSet

router = DefaultRouter()
router.register(r'productos',CervezaViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
