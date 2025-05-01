from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CategoryListView, dashboard

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('categoria/<str:categoria>/', CategoryListView.as_view(), name='post_category_list'),
    path('dashboard/', dashboard, name='dashboard'),
]