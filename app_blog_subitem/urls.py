from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.urls import path
import blog.views as bv
app_name='blog'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('article/<int:article_id>/', views.article_page,name='article_page'),
    path('edit/<int:article_id>/',views.edit_page,name='edit_page'),
    path('action/',views.edit_action,name='edit_action'),
]