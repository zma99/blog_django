from django.urls import path
from django.contrib.auth.views import LogoutView
from .views.login import UsernameLoginView
from .views.signup import SignupView
from .views.passwordReset import PasswordResetView
from .views.passwordConfirmReset import PasswordResetConfirmView

urlpatterns = [
    path('login/', UsernameLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

]