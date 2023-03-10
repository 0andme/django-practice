from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product',include('product.urls')),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/member', include('member.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
