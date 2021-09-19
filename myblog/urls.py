from django.urls import path
from .views import AddPostView, DeletePostview, HomeView, ArticleDetailView, UpdatePostView, DeletePostview, AddCategoryView, CategoryView
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('add_category/',AddCategoryView.as_view(), name='add_category'),
    path('artilce/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('artilce/<int:pk>/remove', DeletePostview.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    

]
