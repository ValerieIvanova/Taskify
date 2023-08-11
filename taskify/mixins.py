from django.contrib.auth.mixins import AccessMixin
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from taskify.tasksApp.models import Task


class AnonymousRequiredMixin(AccessMixin):
    """
    Mixin to allow only anonymous users to access the view.
    Redirects authenticated users to the Dashboard page.
    """

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().handle_no_permission()


class UserOwnershipMixin:
    """
    Mixin to check if the user owns the object.
    Raises 404 if the user is not the owner.
    """

    user_obj = ''

    def check_user_ownership(self, obj):
        user = getattr(obj, self.user_obj)
        if str(user) != str(self.request.user):
            raise Http404

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.check_user_ownership(obj)
        return obj

    def get_task_by_pk(self):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        self.check_user_ownership(task)
        return task

    def get_task_by_reminder(self):
        task = get_object_or_404(Task, reminder=self.object)
        self.check_user_ownership(task)
        return task
