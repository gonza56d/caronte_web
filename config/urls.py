# Django
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('caronte.index.urls', 'index'), namespace='index')),
    path('details/', include(('caronte.details.urls', 'details'), namespace='details')),
    path('periods/', include(('caronte.periods.urls', 'periods'), namespace='periods')),
    path('users/', include(('caronte.users.urls', 'users'), namespace='users')),
]
