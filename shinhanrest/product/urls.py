from django.urls import path
from . import views


urlpatterns=[
    path("/<int:product_id>/comment",views.CommentListView.as_view()),
    # path("/comment",views.CommentListView.as_view()), # 모든 상품의 모든 코멘트라는 url이라는 의미가 이상함
    path("/<int:pk>",views.ProductDetailView.as_view()),
    path("",views.ProductListView.as_view()),
]



# ProductListView는 class이기 때문에 as_view()를 url로 변환해주어야함
# urlpatterns=[
#     # API를 만들때는 
#     path("/<int:pk>",views.ProductDetailView.as_view()),
#     path("",views.ProductListView.as_view()),
# ]