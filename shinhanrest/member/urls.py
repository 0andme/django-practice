from django.urls import path
from . import views


urlpatterns=[
    path('',views.CreateMemberView.as_view())
]