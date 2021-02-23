from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buyy', views.buy_product_form),
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
    path('delete_product', views.product_delete_form),
    path('product_deleted', views.product_delete),
]
