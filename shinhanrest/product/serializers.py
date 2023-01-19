from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    # ModelSerializer 에게 모델이 뭔지만 알려주는 것임
    # 그러면 알아서 필드와 값을 매칭해서 직렬화해줌
    class Meta:
        model=Product
        # fields =['id','name'] # postman 호출결과로 id와 name값만 나옴
        fields="__all__"