
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from productos.views import CervezaViewSet
from posts.views import PostsViewSet

router = DefaultRouter()
router.register(r'productos',CervezaViewSet)
router.register(r'posts',PostsViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
