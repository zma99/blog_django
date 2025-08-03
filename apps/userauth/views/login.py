from django.contrib.auth.views import LoginView
from apps.userauth.forms.loginForm import StyledAuthenticationForm
from django.urls import reverse_lazy

class UsernameLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('index')
    authentication_form = StyledAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('index')
