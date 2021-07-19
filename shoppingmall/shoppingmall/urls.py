"""shoppingmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account import views as a
from shopping import views as s
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', s.home, name='home'),
    path('detail/', s.detail, name='detail'),
    path('account/signup', a.signup, name='signup'),
    path('account/user_login', a.user_login, name='user_login'),
    path('account/user_logout', a.user_logout, name='user_logout'),
    path('account/mypage', a.mypage, name="mypage"),
    path('new/', s.new, name="new"),
    path('create/', s.create, name="create"),
    path('<str:id>', s.detail, name="detail"),
    path('edit/<str:id>', s.edit, name='edit'),
    path('update/<str:id>', s.update, name='update'),
    path('delete/<str:id>', s.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
