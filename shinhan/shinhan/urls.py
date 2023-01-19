from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import main,detail, write
from member.views import signin,signout,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/<int:pk>/',detail),
    path('product/write/',write),
    path('member/login/',signin),
    path('member/logout/',signout),
    path('member/register/',register),
    path('',main),

]

urlpatterns+=static('media',document_root=settings.MEDIA_ROOT)
