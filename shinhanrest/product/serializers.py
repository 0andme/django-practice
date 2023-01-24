from rest_framework import serializers
from .models import Product,Comment,Like

class ProductSerializer(serializers.ModelSerializer):
    # 필드만 만든 것임 = 필수값이 아니라고 알아서 지정해줌
    # 데이터를 클라이언트에 전달할 때 사용함
    # 메서드 필드이기 때문에 아래처럼 get함수를 만들어야 함
    comment_count=serializers.SerializerMethodField()
    like_count=serializers.SerializerMethodField()

    # get_필드명(self,obj) / 함수명 규칙이 정해져 있음
    # obj : 시리얼 라이즈로 전달된 객체 Product를 의미함
    # 필드만 만든 것에 직접 데이터를 연결하는 부분
    def get_comment_count(self,obj):
        # product=obj
        # product_id=obj.id
        # product__pk=obj.id
        
        # 밑의 코드는 상품별로 매번 동작하게 되는데 이미는 쿼리 셀렉트 문을 n번 하게 되는 것임
        # return Comment.objects.filter(product=obj).count()
        # 상품 1 : 댓글 n의 관계 일때 외래키를 적었을때 모델명_set이 생긴다

        # 모델명(소문자로 변경)_set
        # 외래키로 연결된 모델을 가지고 오는 법 
        # 상품에 연결된 모델코멘트를 가져올 수 있음
        # 장고는 상품 obj에서 댓글로 접근할수 있게 미리 자동으로 만들어 둠
        return obj.comment_set.all().count()

    # 좋아요 필드 값 추가
    def get_like_count(self,obj):
        return obj.like_set.all().count()

    # ModelSerializer 에게 모델이 뭔지만 알려주는 것임
    # 그러면 알아서 필드와 값을 매칭해서 직렬화해줌
    class Meta:
        model=Product
        # fields =['id','name'] # postman 호출결과로 id와 name값만 나옴
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

class CommentCreateSerializer(serializers.ModelSerializer):

    # 로그인한 사용자를 자동으로 가져오는 방법


    # 1. 방법 1
    # def validate(self, attrs):

    #     request = self.context.get('request')
    #     if request and request.user.is_authenticated:
    #         attrs['member']=request.user
    #     else :
    #         raise ValidationError('member is required')
    #     # 최종 검증된 data return
    #     return attrs 


    # 방법 2
    # 멤버를 가려버림
    # HiddenField 값이 숨겨져 있기때문에
    # 값을 직접 지정할 수 있음
    member=serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False,
        
    )

    # validate_member()/  validate_필드명 / 필드명을 검증하는데 사용하는 함수
    # 그 필드를 알아서 검증해줌 
    # value안에 request 유저 변수가 들어옴

    def validate_member(self, value):
        # 헤더에 토근을 넣어주지 않았을 때
        if not value.is_authenticated :
            raise serializers.ValidationError('member is required')
        return value
    

    class Meta:
        model=Comment
        fields="__all__"
        # postman에서 사용자에 대한 정보를 숨김
        extra_kwargs={'member':{'required':False}}


class LikeCreateSerializer(serializers.ModelSerializer):

    # 로그인 여부 상관없이 그냥 넣어주는 코드이기 때문에
    # 아래 validate_member가 필요함
    member=serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        required=False,
        
    )
    def validate_member(self, value):
        # 헤더에 토큰을 넣어주지 않았을 때
        if not value.is_authenticated :
            raise serializers.ValidationError('member is required')
        return value

    class Meta:
        model=Like
        fields="__all__"
        extra_kwargs={'member':{'required':False}}

