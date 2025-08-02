from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from apps.users.models import Profile
from apps.userauth.forms.signupForm import SignupForm

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)

        login(self.request, user)
        return super().form_valid(form)