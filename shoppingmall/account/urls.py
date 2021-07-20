from django.urls import path
from . import views


urlpatterns = [
    path('account/signup', views.signup, name='signup'),
    path('account/user_login', views.user_login, name='user_login'),
    path('account/user_logout', views.user_logout, name='user_logout'),
    path('account/mypage', views.mypage, name="mypage"),
]
