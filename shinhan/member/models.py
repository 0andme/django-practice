from django.db import models

# Create your models here.
# 모델은 데이터 베이스

class Member(models.Model):
    name=models.CharField(max_length=128,verbose_name='이름')
    age=models.IntegerField(verbose_name='나이')
    # unique=True
    # 데이터가 동일한 값이면 안된다는 제약
    user_id=models.CharField(unique=True, verbose_name='아이디',max_length=128)
    password=models.CharField(verbose_name='비밀번호',max_length=255)

    # 관리자 페이지에서 회원 클릭시 나오는 모델 부분 변경
    class Meta:
        verbose_name='회원'
        verbose_name_plural='회원'

    # 회원 클릭시 나오는 데이터 목록에서
    # Member object (1)-> 회원의 이름
    # 로 데이터가 잡힘

    # __str__
    # 클래스의 객체의 이름을 변경하고 싶을 때 사용
    def __str__(self):
        return f"{self.name} : {self.age}세"