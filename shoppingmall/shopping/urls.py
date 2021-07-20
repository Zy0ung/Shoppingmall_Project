from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('<str:id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)