from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, AssignmentForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task, CustomUser
from django.conf import settings
from django.views.generic import (
    CreateView,
)


def home(request):
    return render(request, 'front/home.html')


class SignUpForm(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


# def userSignup(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful")
#             return redirect('home')
#         messages.error(request, 'Unsuccessful signup. Cross-check the information')
#     form = CustomUserCreationForm()
#     return render(request, 'account/signup.html', {"form": form})


# @login_required
# def task_details(request):
#     if request.method == 'POST':
#         form = AssignmentForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = Task.client
#             form.save()
#             user.save_form_data()
#             return redirect('home')
#     else:
#         form = AssignmentForm()
#     return render(request, 'front/task.html', {
#         'form': form
#     })


class CreateAssignmentInstance(LoginRequiredMixin, CreateView):
    form_class = AssignmentForm
    template_name = 'front/task.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)
