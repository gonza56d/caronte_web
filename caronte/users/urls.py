# Django
from django.urls import path
# Project
from .views import LoginView, LogoutView, SignupView, set_theme_view


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('set_theme/<str:theme>/', set_theme_view, name='set_theme')
]
