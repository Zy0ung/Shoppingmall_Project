from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/signup', views.signup, name='signup'),
    path('account/user_login', views.user_login, name='user_login'),
    path('account/user_logout', views.user_logout, name='user_logout'),
    path('account/mypage', views.mypage, name="mypage"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
