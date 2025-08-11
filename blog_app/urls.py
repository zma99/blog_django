"""
URL configuration for blog_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from .views import IndexView
from django.contrib.auth.decorators import login_required
from django_ckeditor_5 import views as ckeditor5_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("auth/", include("apps.userauth.urls")),
    path("posts/", include("apps.posts.urls")),
    path("user/", include("apps.users.urls")),

    #CKEditor 5
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('ckeditor5/upload_file/', login_required(ckeditor5_views.upload_file), name='ckeditor5_upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
