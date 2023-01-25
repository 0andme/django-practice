from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from .models import Member

from rest_framework import generics,mixins,status
from .serializers import MemberSerializer
# Create your views here.

class MemberRegisterView(APIView):
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        tel=request.data.get('tel')
        user_status='일반'

        member= Member(
            username=username,
            password=make_password(password),
            tel=tel,
            status=user_status)
        
        member.save()

        return Response(status=status.HTTP_201_CREATED)


# class CreateMemberView2(
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     serializer_class=MemberSerializer

#     def create(self, request, *args, **kwargs):
#         return self.create(request, args, kwargs)