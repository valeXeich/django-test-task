from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .models import CustomUser
from .forms import LoginForm


class UserListView(ListView):
    queryset = CustomUser.objects.filter(is_superuser=False)
    template_name = 'user_list.html'
    context_object_name = 'users'


class LoginView(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
            else:
                return HttpResponse('Invalid login')
