from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from crispy_forms import helper
from crispy_forms import layout
from django.http import JsonResponse
from django.utils.http import is_safe_url

# Create your views here.

from registration.models import Registration
from apply.models import Application


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=50
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(),
        max_length=50
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_id = "loginForm"
        self.helper.add_input(layout.Submit('submit', 'Login'))



class LoginView(FormView):
    form_class = LoginForm
    template_name = "backoffice/login.html"
    success_url = "/backoffice"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('backoffice:index')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        next_url = self.request.POST.get('next', self.request.GET.get('next', '/'))
        next_url = next_url if is_safe_url(next_url, self.request.get_host()) else None
        user = authenticate(username=username, password=password) 
        if user.is_authenticated:
            login(self.request, user)
            if next_url is not None:
                return redirect(next_url)
            return super().form_valid(form)
        else:
            return render(self.request, self.template_name, {'form': form, 'pass_error': True})

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('backoffice:login')
    

class AccountView(LoginRequiredMixin, TemplateView):
    template_name = "backoffice/index_a.html"
    login_url = "/backoffice/login"

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.profile.member_group == 1:
            data = Registration.objects.all()
            return render(self.request, self.template_name, {'data': data})
        else:
            data = Application.objects.all()
            return render(self.request, "backoffice/index_b.html", {'data': data})