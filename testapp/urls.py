"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
import sys 
sys.path.insert(1, '.')
from restapp import views

from pages.views import Home_view, Contact_view, About_view
# from products.views import (
#     product_detail_view,
#     product_create_view,
#     dynamic_lookup_view,
#     product_list,
# )

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('', Home_view, name='home'),
    path('contact/', Contact_view),
    path('about/', About_view),
    # path('product/', product_detail_view),
    # path('create/', product_create_view),
    # path('products/<int:id>/', dynamic_lookup_view, name='product'),
    # path('product-list/', product_list, name='product-detail'),

    # Rest framework

    path('url', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest', include('restapp.urls'))
]
