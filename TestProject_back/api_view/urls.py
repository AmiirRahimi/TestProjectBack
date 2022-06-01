from django.urls import path
from .views import Login, Register , ProductList , ProductDetails

urlpatterns = [
    path('register' , Register.as_view()),
    path('login' , Login.as_view()),
    path('product/list' , ProductList.as_view()),
    path('product/details' , ProductDetails.as_view()),
]
