from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('all_products/',views.all_product,name="all_product"),
    path('filter/<str:user>',views.product_filter,name="filter"),
    path('all_products/order/',views.price_order,name="product_order"),


]