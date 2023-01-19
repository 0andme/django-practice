from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer
from .paginations import ProductLargePagination

# 뷰 = 컨트롤러

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class=ProductSerializer
    pagination_class=ProductLargePagination
    
    def get_queryset(self):
        """
        get with param(name)
        """
        name=self.request.query_params.get('name')

        products=Product.objects.all()

        if name:
            products=products.filter(name__contains=name)
       
        return products.order_by('id')
    
    def get(self,request,*args,**kwargs):
        # 쿼리셋 가져오기
        # 직렬화하기
        # 클라이언트 단에 retyrn Response하기

        # mixins.ListModelMixin의 list를 호출
        return self.list(request,args,kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)