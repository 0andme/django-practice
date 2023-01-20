from rest_framework import serializers
from .models import Product,Comment

class ProductSerializer(serializers.ModelSerializer):
    
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
