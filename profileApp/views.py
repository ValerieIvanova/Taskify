from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from taskify.mixins import AnonymousRequiredMixin
from taskify.profileApp.forms import ProfileCreateForm, ProfileLoginForm
from taskify.profileApp.models import Profile


class RegisterView(AnonymousRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile/register.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, self.object)
        return result

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(RegisterView, self).get(*args, **kwargs)


class CustomLoginView(AnonymousRequiredMixin, LoginView):
    template_name = 'profile/custom_login.html'
    redirect_authenticated_user = True
    form_class = ProfileLoginForm
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, errors=form.errors))


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'profile/custom_logout.html'
    next_page = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Perform the logout if the user confirms
        if 'confirm-logout' in request.POST:
            return super().post(request, *args, **kwargs)

        return redirect('dashboard')