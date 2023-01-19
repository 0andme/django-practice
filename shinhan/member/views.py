from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import check_password,make_password
# django 내의 User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# 비즈니스 로직을 만드는 뷰 = 컨트롤러

# 회원가입 페이지
def register(request):
    if request.method=='POST':

      User.objects.create_user(
        request.POST.get('user_id'),
        request.POST.get('email'),
        request.POST.get('password'),
        
      )
      
      return redirect('/member/login/')

    return render(request,'register.html')

# 로그인 페이지
def signin(request):   
    if request.method=="POST":
        user_id=request.POST.get('user_id')
        password=request.POST.get('password')

        # 인증하는 함수 사용자의 아이디와 비밀번호를 확인하는 함수
        user=authenticate(request,username=user_id,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
                    
    return render(request,'login.html')

# 로그아웃 기능
def signout(request):
    
    logout(request)

    return redirect('/')

