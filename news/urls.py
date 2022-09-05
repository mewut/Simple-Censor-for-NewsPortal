from django.urls import path
from django.contrib import admin
from .views import News, PostDetail

urlpatterns = [
    path('', News.as_view()),
    path('<int:pk>', PostDetail.as_view())

]