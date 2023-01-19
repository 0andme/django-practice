from django.apps import AppConfig


class MemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member'
    # 관리자 페이지에서 앱의 이름을 MEMBER가 아닌 값으로 변경
    verbose_name='회원'