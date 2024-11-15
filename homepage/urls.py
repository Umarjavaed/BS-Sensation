from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('index2/', views.index2, name='index2'),
    path('index2/<int:product_id>/', views.index2_product, name='index2_product'),     
]
