from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, TiendaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tiendas', TiendaViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls
