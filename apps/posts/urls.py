from django.urls import path
from .views.create import CreatePostView
from .views.list import PostListView
from .views.detail import PostDetailView
from .views.edit import PostUpdateView
from .views.delete import PostDeleteView
from .views.likes import PostLikeView
from .views.comment import CommentUpdateAjaxView, CommentCreateAjaxView, CommentDeleteView
from .views.report_post import ReportPostView
from .views.deleted_post import deletedPost

app_name = "posts"

urlpatterns = [
    # Posts
    path("nuevo/", CreatePostView.as_view(), name="post_create"),
    path("list/", PostListView.as_view(), name="list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/like/", PostLikeView.as_view(), name="like"),
    path("posts/category/<slug:slug>/", PostListView.as_view(), name="posts_by_category"),
    path("posts/<int:post_id>/report/", ReportPostView.as_view(), name="report"),
    path('post/<int:pk>/deleted/', deletedPost, name='deleted_post'),

    # Comments
    path("comment/<int:pk>/create/", CommentCreateAjaxView.as_view(), name="comment_create"),
    path("comment/<int:pk>/edit/", CommentUpdateAjaxView.as_view(), name="comment_edit"),
    path("comment/delete/", CommentDeleteView.as_view(), name="comment_delete"),
]
