from django.urls import path, include
from . import views
from .views import HomeView, Articles_detail_View, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    CategoryView

urlpatterns = [
    #path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('articles/<int:pk>',Articles_detail_View.as_view(),name="article-detail"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('articles/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('articles/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/',CategoryView, name='category'),


]