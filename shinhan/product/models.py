from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 모델 = 데이터 베이스 
class Product(models.Model):
    # null=True ->  models.SET_NULL # 상품 데이터 전부 널처리 하기
    # default=1 -> models.SET_DEFAULT # 상품 데이터 디폴트 값으로 변경하기

    # ForeignKey : 외래키
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="회원")

    # CharField는 최대 길이 작성 필수
    # 길이 제한이 애매한 데이터에는 텍스트 필드 사용하면 됨
    # 스키마를 내가 정해놔야함
    title= models.CharField(max_length=128,verbose_name='상품명')
    # 텍스트 필드 : 길이 지정 없어도 됨
    content= models.TextField(verbose_name='상품 내용')
    # 숫자형
    price= models.IntegerField(verbose_name='가격')
    location= models.CharField(max_length=256,verbose_name='위치')
    # 파일 -이미지
    # null=True :  데이터 베이스에서의 속성 값이 비어있을 수 있음
    # blank=True : 사용자 쪽에서 빈 값을 넣을 때 오류를 없앰
    # 위 두 개의 코드는 함께 쓰자
    image=models.FileField(null=True,blank=True,verbose_name='이미지')

    # 회원정보가 들어가야함
    # user_id 를 직접 또 넣어주거나 서버에서 가져오거나 하면됨
    # 그러나 만약 유저 아이디가 변경된다면 ? -> 이미 사용된 부분이랑 매치가 안되니까 찾을 수 없게됨
    # 연결이 끊김
    # 직접 연결이 아니라 유저정보를 가리기기만 하면됨
    class Meta:
        db_table='shinhan_product'
        verbose_name='상품'
        verbose_name_plural='상품'
