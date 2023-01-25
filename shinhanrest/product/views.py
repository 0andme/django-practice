from rest_framework import generics,mixins,status
from .models import Product,Comment,Like
from .serializers import (
    ProductSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    LikeCreateSerializer,
)
from rest_framework.response import Response
from .paginations import ProductLargePagination
from rest_framework.permissions import IsAuthenticated
# 뷰 = 컨트롤러

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):

    serializer_class=ProductSerializer
    pagination_class=ProductLargePagination
    permission_classes=[IsAuthenticated]
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

# 모든 상품의 모든 댓글을 불러오는 기능은 
# 사실상 말이 안됨

# class  CommentListView(
#     mixins.ListModelMixin,
#     generics.GenericAPIView,
# ):
#     serializer_class=CommentSerializer

#     def get_queryset(self):
#         comments=Comment.objects.all()
#         return comments.order_by('-id')
    
#     def get(self,request,*args,**kwargs):
#        return self.list(request,args,kwargs)


class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    """
    /product/{product_id}/comment
    """
    serializer_class=CommentSerializer

    def get_queryset(self):
        product_id=self.kwargs.get('product_id')

        if product_id:
            # product_id 대신 product / product__pk / product__id라고 써도 되는 이유
            # __ 언더바 두개의 의미 : product가 가지고 있는 기능적인 것 = product가 가진 필드에 접근할 수 있음
            # 결론 : 아이디를 써도 되고(디비에서 직접 가져옴: 가장 빠르게 접근) 필드명을 써도 됨
            return Comment.objects.filter(product_id=product_id).order_by('-id')
        
        return Comment.objects.none()

    def get(self,requset,*args,**kwargs):
        # 여기서 prodict의 pk가 들어옴
        return self.list(requset,args,kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class=CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):

        return self.create(request, args, kwargs)
    

class LikeCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class=LikeCreateSerializer

    def get_queryset(self):
        return Like.objects.all()

    def post(self, request, *args, **kwargs):
        
        product_id=request.data.get('product')
        member=request.user
        
        # 이미 해당 상품에 1이 찍혀있으면
        if  Like.objects.filter(member=member,product_id=product_id).exists():
            Like.objects.filter(member=member,product_id=product_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return self.create(request, args, kwargs)

