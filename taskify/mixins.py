from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AnonymousRequiredMixin(AccessMixin):
    """
    Mixin to allow only anonymous users to access the view.
    Redirects authenticated users away from the view.
    """

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().handle_no_permission()