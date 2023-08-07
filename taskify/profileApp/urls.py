from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, UserProfileEdit, UserProfileDetails, \
    UserProfileDelete

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', UserProfileEdit.as_view(), name='edit_user_profile'),
    path('details/<int:pk>/', UserProfileDetails.as_view(), name='details_user_profile'),
    path('delete/<int:pk>/', UserProfileDelete.as_view(), name='delete_user_profile'),
]
