from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,mixins,status
from .serializers import MemberSerializer
# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


# class MemberRegisterView(APIView):
#     def post(self,request,*args,**kwargs):
#         """
#         POST /api/member
#         회원가입 기능
#         """
#         username=request.data.get('username')
#         password=request.data.get('password')
#         tel=request.data.get('tel')
#         user_status='일반'

#         if Member.objects.filter(username=username).exists():
#             return Response(
#                 {'detail':'Already used'},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         member= Member(
#             username=username,
#             password=make_password(password),
#             tel=tel,
#             status=user_status)
        
#         member.save()

#         return Response(status=status.HTTP_201_CREATED)

