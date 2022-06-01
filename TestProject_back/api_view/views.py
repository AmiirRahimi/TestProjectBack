from django.shortcuts import render
from numpy import true_divide
from rest_framework.views import APIView , Response
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Products
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Register(APIView):
    def post(self , request):
        data = request.data
        user = User.objects.create_user(username = data['username'] , email = data['email'] , password = data['password'])
        return Response(get_tokens_for_user(user) ,status = status.HTTP_200_OK)

class Login(APIView):
    def post(self , request):
        data = request.data
        print(data['password'] , 'l')
        user = authenticate(username = data['username'] , password = data['password'])
        if user is not None:
            login(request , user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class ProductList(APIView):
    def get(self , request):
        products = Products.objects.all()
        serializer = ProductSerializer(products , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class ProductDetails(APIView):
    def post(self , request):
        data = int(request.data['params']['id'])
        product = Products.objects.filter(id = data).first()
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
        



