"""RTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_product_form),
    path('buytxnsaved', views.buy_product),
    path('sell', views.sell_product_form),
    path('selltxnsaved', views.sell_product),
    path('newproducttype', views.product_type_form),
    path('tsubmitted', views.product_type_save),
    path('tlist', views.product_type_list),
    path('newproduct', views.product_form),
    path('psubmitted', views.product_save),
    path('plist', views.product_list),
    path('buyhistory', views.buy_history),
    path('sellhistory', views.sell_history),
    path('product-json/<str:pt>/', views.get_json_product_data),
]
