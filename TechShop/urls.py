"""
URL configuration for TechShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import *
from feedback.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/list/', ProductListView.as_view()),
    path('product/<int:product_id>/', ProductById.as_view()),
    path('product/', ProductById.as_view()),
    path('product/search/', ProductSearchList.as_view()),
    path('feedback/<int:product_id>/product/', FeedBackByProduct.as_view())
]
