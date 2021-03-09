# Django
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('caronte.index.urls', 'index'), namespace='index')),
    path('users/', include(('caronte.users.urls', 'users'), namespace='users')),
]
