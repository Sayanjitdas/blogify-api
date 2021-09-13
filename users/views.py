from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions

from .serializers import UserRegistrationSerializer


class UserRegistrationAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self,request,*args,**kwargs):

        print(request.data)
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


