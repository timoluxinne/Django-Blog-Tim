from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<str:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', about, name='about')
]
