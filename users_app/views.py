from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from products_app.models import Basket
from .models import Users

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main-page"))
    else:      
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

class UserRegisterView(CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login-page")

class ProfileUpdateView(UpdateView):
    model = Users
    form_class = UserProfileForm
    template_name = "users/profile.html"
    def get_success_url(self):
        return reverse_lazy("profile-page", args=(self.object.id, ))

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data()
        context["baskets"] = Basket.objects.filter(user=self.object)
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main-page"))

# def profile_view(request):
#     if request.method == "POST":
#         user = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if user.is_valid():
#             user.save()
#             messages.success(request, "Malumotlar yangilandi!")
#             return HttpResponseRedirect(reverse("profile-page"))
#     else:
#         form = UserProfileForm(instance=request.user)
#     basket = Basket.objects.filter(user=request.user)
#     context = {
#         "form": form,
#         "baskets": basket,
#     }
#     return render(request, "users/profile.html", context)

# def register_view(request):
#     if request.method == "POST":
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Siz ro'yxatdan o'tdingiz!")
#             return HttpResponseRedirect(reverse("login-page"))
#     else:
#         form = UserRegisterForm()
#     context = {
#         "form": form
#     }
#     return render(request, "users/register.html", context)