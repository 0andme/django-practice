from django.db import models

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
        return f"{self.name}  : {self.price}원 : {self.product_type}"