
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskify.common.urls')),
    path('tasks/', include('taskify.tasksApp.urls')),
    path('profile/', include('taskify.profileApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
