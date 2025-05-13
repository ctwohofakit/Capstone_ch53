from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import AccountSignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib import messages

# Create your views here.
class SignUpView(CreateView):
    template_name="registration/signup.html"
    form_class=AccountSignupForm
    success_url=reverse_lazy("interview_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        #auto-createan empyty profile
        UserProfile.objects.create(user=self.object)
        return response




@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method=="POST":
        password_form=PasswordChangeForm(request.user, request.POST)
        profile_form=ProfileForm(request.POST, request.FILES, instance=profile)

        if "profile_submit" in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Info updated!")
                return redirect("profile")
            else:
                messages.error(request, "Profile update failed. Please try again.")

        elif "password_submit" in request.POST:
            if password_form.is_valid():
                password_form.save()
                messages.success(request, "Password updated!")
                return redirect("profile")
            else:
                messages.error(request, "Password update failed. Please try again.")
    else:
        profile_form  = ProfileForm(instance=profile)
        password_form = PasswordChangeForm(request.user)

    return render(request,"accounts/profile.html",{
        "profile_form":profile_form,
        "password_form":password_form,
    })


