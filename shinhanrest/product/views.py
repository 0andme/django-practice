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

        print(request.user)

        # mixins.ListModelMixin의 list를 호출
        return self.list(request,args,kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)


class ProductDetailView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=ProductSerializer
    
    # 데이터 전체를 보내주면
    # retrieve 안에서 알아서 pk인 것을 알아서 찾아줌
    # kwargs 안에 pk가 들어 있고 
    # GenericAPIView 안에  lookup_field = 'pk'코드가 있음

    def get_queryset(self):
        # 권한 확인 코드 -> 그에 따른 쿼리셋을 제어해서 권한에 따라 데이터를 다르게 보여줄 수 있음
        # 물론 get쪽에서 권한 코드를 넣어도 됨

        return Product.objects.all().order_by('id')
    
    def get(self,requset,*args,**kwargs):
        return self.retrieve(requset,args,kwargs)

    def delete(self,requset,*args,**kwargs):
        return self.destroy(requset,args,kwargs)

    def put(self,requset,*args,**kwargs):
        return self.partial_update(requset,args,kwargs)

    