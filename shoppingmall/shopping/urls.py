from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('<str:id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]