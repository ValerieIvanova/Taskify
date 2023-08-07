from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from taskify.mixins import AnonymousRequiredMixin
from taskify.profileApp.forms import UserCreateForm, UserLoginForm
from taskify.profileApp.models import UserProfile

UserModel = get_user_model()


class RegisterView(AnonymousRequiredMixin, CreateView):
    model = UserModel
    template_name = 'profile/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(RegisterView, self).get(*args, **kwargs)


class CustomLoginView(AnonymousRequiredMixin, LoginView):
    template_name = 'profile/custom_login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm
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


class UserProfileEdit(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'age', 'profile_picture']
    template_name = 'profile/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('details_user_profile', kwargs={'pk': self.object.user.id})


class UserProfileDetails(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile/details_profile.html'
    context_object_name = 'user_profile'


class UserProfileDelete(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('index')
