
from django.contrib.auth.hashers import check_password
from .models import Member

# 장고가 인증을 확인 할때 들어올 클래스 MemberAuth
# 필요한 함수만 만들어 주면 됨 
class MemberAuth:

    def authenticate(self,request,username=None,password=None,*args,**kwargs):
        if not username or not password:
            # 둘 중 하나가 없어도 로그인 처리는 해줄게
            if request.user.is_authenticated:
                return request.user
            return None
        try:
            member=Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if check_password(password,member.password):
            if member.status=='일반':
                return member # 로그인 성공
        return None

    def get_user(self,pk):
        try:
            member=Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None # = return 
        
        # >>> if member.is_active and member.status == '일반 else None
        # member.is_active : 계정 활성화 여부 | 장고가 이미 가지고 있는 값
        # member.status | 내가 만든 값
        # 위의 인증단계에서 이미 걸러지기 때문에 불필요한 코드
        return member  # if member.is_active and member.status == '일반 else None