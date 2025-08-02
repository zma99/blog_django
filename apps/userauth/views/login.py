from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class UsernameLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('index')
    authentication_form = AuthenticationForm    # por defecto usa username

    def get_success_url(self):
        return reverse_lazy('index')
