from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Member
from django.contrib.auth.hashers import check_password,make_password
# 비즈니스 로직을 만드는 뷰 = 컨트롤러

# 회원가입 페이지 노출
# 회원가입 기능 구현
def register(request):
    if request.method=='POST':
        user_id=request.POST.get('user_id')
        password=make_password(request.POST.get('password'))
        name=request.POST.get('name')
        age=request.POST.get('age')

        # 이미 있는 아이디가 아닐 때
        if not Member.objects.filter(user_id=user_id).exists():
            member=Member(
                user_id=user_id,
                password=password,
                name=name,
                age=age
            )

            member.save()
            return redirect('/member/login/')

    return render(request,'register.html')


# 로그인 페이지
# 기능 1 - 로그인 화면 출력
# 기능 2 - 아이디 비번 입력받아 로그인 처리
def login(request):   

    if request.method=="POST":

        user_id=request.POST.get('user_id')
        password=request.POST.get('password')

        if Member.objects.filter(user_id=user_id).exists():
            # user_id값이 유니크 라고 설정했으므로
            # user_id값으로 get을 사용할 수 있음
            member=Member.objects.get(user_id=user_id)

            # db data와 사용자 입력 값 비교 

            if check_password(password,member.password):
                # 세션키를 담은 쿠키 생성
                request.session['user_pk']=member.id
                request.session['user_id']=member.user_id
                return redirect('/')
            else :
                pass # login fail
        
             
    return render(request,'login.html')



def logout(request):
    
    #  세션에 해당 키 값이 없는 경우 고려
    if 'user_pk' in request.session:
        del ( request.session['user_pk'])

    if 'user_id' in request.session:
        del ( request.session['user_id'])

    return redirect('/')


# -------------------------------------------------------------
    
    # class 객체 변수를 만드는 코드
    # member=Member()
    # member.name="meme"
    # member.age=40

    # 모든 데이터를 가져오는 all
    # members=Member.objects.all() 

    # member=Member.objects.get(pk=1) 
    
    # member=Member.objects.get(pk=100) 
    # Member matching query does not exist
    # 만약 위와 같이 없는 데이터에 대해 접근을 시도하면 위와 같은 메시지 출력됨

    # 매개변수에 맞는 데이터를 가져오는 함수 get
    # pk 란 프라이머리 키 / 
    # get 의 결과는 한개만 있어야하므로 pk를 이용하는 경우가 많음
    # member=Member.objects.get(pk=1)
    # 위의 코드와 동일 => member=Member.objects.get(id=1)
     
    # save를 하면 쿼리를 날리지 않아도 알아서 데이터를 테이블에 저장해줌
    # member.save()

    # 특정 조건을 만족하는 데이터만 가져오는 함수 filter
    # age__gte : 필드이름 __ 조건
    # members=Member.objects.filter(age__gte=35)
    # members=Member.objects.filter(name='meme')
    # members=Member.objects.filter(name__contains='meme')

    # members=Member.objects.get(name='test') 
    # 위의 코드 여러 개의 데이터가 검색되면 에러가 나옴
    # members=Member.objects.filter(name='test').first() 
    # 그래서 위와같이 필터를 씌우고 하나를 가져오라고 함


    # 여러 함수를 chaining할 수 있음
    # members=Member.objects.filter(name__contains='me').order_by('-age') 

    
    # name__contains : 이름에 특정 문자열이 포함되는 데이터만 추출
    # members=Member.objects.filter(name__contains='me')


    # null 인data만 찾고 싶을 때 __isnull 


    # return render(request,'index.html',{'members':members})
    # return  HttpResponse("<h1>22<h1>")
   