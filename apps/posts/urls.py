from django.urls import path
from .views.create import CreatePostView
from .views.list import PostListView
from .views.detail import PostDetailView
from .views.edit import PostUpdateView
from .views.delete import PostDeleteView
from .views.likes import PostLikeView
# from .views.comments import add_comment


app_name = 'posts'

urlpatterns = [
    # path('<int:post_id>/comment/', add_comment, name='add_comment'),
    path('nuevo/', CreatePostView.as_view(), name='post_create'),
    path('list/', PostListView.as_view(), name='list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/like/', PostLikeView.as_view(), name='like'),
]
