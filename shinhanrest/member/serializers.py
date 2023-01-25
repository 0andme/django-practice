from rest_framework import serializers
from .models import Member
from django.contrib.auth.hashers import make_password

class MemberSerializer(serializers.ModelSerializer):
    # 회원가입 시 패스워드가 그대로 노출되는 것을 막아보자
    def validate_password(self, value):
        # 유효성 검사가 끝난 값을 반환
        if len(value) < 8 : 
            raise serializers.ValidationError('Too short password')
        # 암호화 하여 반환하면 된다.
        return make_password(value)

    class Meta:
        model=Member
        fields=('id','username','tel','password')
        extra_kwargs={
            'id': {
                'read_only':True,
            },
            'password': {
                'write_only':True,
            }
        }