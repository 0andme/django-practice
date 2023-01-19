from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer
# 뷰 = 컨트롤러

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class=ProductSerializer
    
    def get_queryset(self):
        # 파라미터를 받아서 filter하면 되겠다...
        name=self.request.query_params.get('name')
        price=self.request.query_params.get('price')
        product_type=self.request.query_params.get('product_type')
        
        products=Product.objects.all()

        if name:
            products=products.filter(name=name)
        if price:
            products=products.filter(price=price)
        if product_type:
            products=products.filter(product_type=product_type)
        
        return products.order_by('id')
    
    def get(self,request,*args,**kwargs):
        # 쿼리셋 가져오기
        # 직렬화하기
        # 클라이언트 단에 retyrn Response하기

        # mixins.ListModelMixin의 list를 호출
        return self.list(request,args,kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)