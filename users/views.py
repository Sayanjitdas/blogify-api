from django.core import exceptions
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers, status,permissions
from rest_framework.authtoken.models import Token

from .serializers import UserRegistrationSerializer,UserDetailsSerializer

USER = get_user_model()

class UserRegistrationAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self,request,*args,**kwargs):

        print(request.data)
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPIView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self,request):
        token = request.headers.get('Authorization').split(' ')[1]
        return Token.objects.get(key=token).user
        
    def get(self,request,*args,**kwargs):
        try:
            user_obj = self.get_object(request)
            serializer = UserDetailsSerializer(user_obj,context={"request":request})
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,*args,**kwargs):
        try:
            user_obj = self.get_object(request)
            print(request)
            print(request.data.get('profile_pic'))
            serializer = UserDetailsSerializer(instance=user_obj,data=request.data,context={"request":request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AuthorDetailAPIView(RetrieveAPIView):

    queryset = USER.objects.all()
    serializer_class = UserDetailsSerializer
    lookup_field = 'email'