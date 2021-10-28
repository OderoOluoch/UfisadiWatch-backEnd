from django.urls import path 
from . import views

urlpatterns = [
    path('tender-create/', views.productCreate, name='product-create'),
    path('product-list/', views.productList, name='product-list'),
    path('product-detail/<int:pk>', views.productDetail, name='product-detail'),
    path('product-update/<int:pk>', views.productUpdate, name='product-update'),
    path('product-delete/<int:pk>', views.productDelete, name='product-delete'),
    path('user/', views.UserApiView.as_view())

]
