from django.db import models
# from member.models import Member # 순환구조가 되므로 이렇게 가져오면 안됨'

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=128,verbose_name='상품명')
    price=models.IntegerField(verbose_name='가격')
    product_type=models.CharField(max_length=8,verbose_name='상품 유형',
        choices=(
            ('단품','단품'),
            ('세트','세트'),
         )
    )
    # date and time field
    # auto_now_add : 해당 데이터를 넣는 시점의 시간이 자동으로 들어감
    tstamp=models.DateTimeField(auto_now_add=True,verbose_name='등록일시')
    
    class Meta:
        db_table='shinhan_product'
        verbose_name='상품'
        verbose_name_plural='상품'

    def __str__(self):
        return f"{self.id}/{self.name}  : {self.price}원 : {self.product_type}"


class Comment(models.Model):
    # 사용자 외래키
    # 장고에서는 문자열로 앱명.모델명으로 표현할 수 있음
    # 이러면 순환참조를 할 일이 없음
    member=models.ForeignKey('member.Member',on_delete=models.CASCADE,verbose_name="사용자")
    # 상품 외래키
    product=models.ForeignKey('product.Product',on_delete=models.CASCADE,verbose_name="상품")
    # 댓글 내용
    content=models.TextField(verbose_name='내용')
    # tstamp
    tstamp=models.DateTimeField(auto_now_add=True,verbose_name='등록 일시')

    class Meta:
        db_table='shinhan_product_comment'
        verbose_name='상품 댓글'
        verbose_name_plural='상품 댓글'

    def __str__(self):
        return f"{self.id}/{self.member}  / {self.product} / {self.content}"


class Like(models.Model):
    member=models.ForeignKey('member.Member',on_delete=models.CASCADE,verbose_name="사용자")
    product=models.ForeignKey('product.Product',on_delete=models.CASCADE,verbose_name="상품")

    class Meta:
        db_table='shinhan_product_like'
        verbose_name='상품 좋아요'
        verbose_name_plural='상품 좋아요'
