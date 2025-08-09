from django.urls import path
from .views.create import CreatePostView
from .views.list import PostListView
from .views.detail import PostDetailView
from .views.edit import PostUpdateView
from .views.delete import PostDeleteView
from .views.likes import PostLikeView
from .views.comment import CommentUpdateAjaxView, CommentCreateAjaxView

app_name = "posts"

urlpatterns = [
    path("nuevo/", CreatePostView.as_view(), name="post_create"),
    path("list/", PostListView.as_view(), name="list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/like/", PostLikeView.as_view(), name="like"),
    path(
        "comment/<int:pk>/edit/", CommentUpdateAjaxView.as_view(), name="comment_edit"
    ),
    path(
        "comment/<int:pk>/create/",
        CommentCreateAjaxView.as_view(),
        name="comment_create",
    ),
    path(
        "posts/category/<slug:slug>/", PostListView.as_view(), name="posts_by_category"
    ),
]
