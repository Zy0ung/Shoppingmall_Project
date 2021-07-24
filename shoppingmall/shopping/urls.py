from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('create/', views.create, name="create"),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('order/<str:id>/', views.order, name='order'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_finished/', views.order_finished, name='order_finished'),
]