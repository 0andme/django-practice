from django.urls import path
from . import views


urlpatterns=[
    path("/like",views.LikeCreateView.as_view()),
    path("/<int:product_id>/comment",views.CommentListView.as_view()),
    path("/<int:pk>",views.ProductDetailView.as_view()),
    path("/comment",views.CommentCreateView.as_view()), 
    path("",views.ProductListView.as_view()),
]



# ProductListView는 class이기 때문에 as_view()를 url로 변환해주어야함
# urlpatterns=[
#     # API를 만들때는 
#     path("/<int:pk>",views.ProductDetailView.as_view()),
#     path("",views.ProductListView.as_view()),
# ]