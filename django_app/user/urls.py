from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import UserListView, LoginView

urlpatterns = [
    path('', UserListView.as_view(), name='main'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

