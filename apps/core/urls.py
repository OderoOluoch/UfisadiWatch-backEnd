from django.urls import path 
from . import views

urlpatterns = [
    path('tender-create/', views.tenderCreate, name='tender-create'),
    path('tender-list/', views.tenderList, name='tender-list'),
    path('tender-detail/<int:pk>', views.tenderDetail, name='tender-detail'),
    path('tender-update/<int:pk>', views.tenderUpdate, name='tender-update'),
    path('tender-delete/<int:pk>', views.tenderDelete, name='tender-delete'),

]
