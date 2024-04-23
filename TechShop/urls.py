from django.contrib import admin
from products.views import *
from shop.views import *
from feedback.views import *
from django.conf.urls.static import static
from django.conf import settings
from orders.views import *
from product_price.views import *
from django.urls import path, include
from person.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/list/', ProductListView.as_view()),
    path('shops/list/', ShopListView.as_view()),
    path('shop/<int:shop_id>/', ShopById.as_view()),
    path('product/<int:product_id>/', ProductById.as_view()),
    path('product/', ProductById.as_view()),
    path('products/search/', ProductSearchList.as_view()),
    path('feedback/<int:product_id>/product/', FeedBackByProduct.as_view()),
    path('feedback/<int:review_id>/', FeedBackByProduct.as_view()),
    path('order/create/', CreateOrderCartView.as_view()),
    path('shops/<int:product_id>/product/', ShopsByProductId.as_view()),
    path('products/<int:shop_id>/shop/', ProductsByShopId.as_view()),
    path('orders/', OrderListView.as_view()),
    path('order/<int:order_id>', OrderChange.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('users/', UserListView.as_view()),
    path('whoami/', UserMyProfile.as_view()),
    path('dict/categories/', CategoriesList.as_view()),
    path('dict/brands/', BrandList.as_view()),
    path('dict/colors/', ColorList.as_view()),
    path('product_prices/my_list/', ProductPriceList.as_view()),
    path('product_prices/add/', ProductPriceOper.as_view()),
    path('product_prices/delete/<int:product_price_id>', ProductPriceOper.as_view()),
    path('product_prices/change/<int:product_price_id>/', ProductPriceOper.as_view()),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)