from django.urls import path,include
from rest_framework import routers
from .product.views import (
    CategoryViewset,
    ProductViewset
)
from .home.views import (
    BannerViewset,
)
from .order.views import (
    OrderViewset,CartDetails
)


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewset, 'categories')
router.register(r'products', ProductViewset, 'products')
router.register(r'banners', BannerViewset, 'banners')
router.register(r'orders', OrderViewset, 'orders')


urlpatterns = [
    path('', include(router.urls)),
    path('get_cart_details/', CartDetails.as_view(), name = 'cart_details'),
]