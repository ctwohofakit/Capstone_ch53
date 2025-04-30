from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")

def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["firstname"]
            last_name=form.cleaned_data["lastname"]
            email=form.cleaned_data["email"]
            subject=form.cleaned_data["subject"]
            message=form.cleaned_data["message"]

            message_body=(
                f"This is an email from interview project\n"
                f"Name: {first_name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n"
                f"Message: {message}"
            )
            send_mail(
                "Email form MockInterview",
                message_body,
                email,
                ["ctwohoda@gmail.com"]
            )
            return redirect("contact")
        else:
            print("Invalid from data")
        return redirect("contact")
    else:
        form=ContactForm()
    return render(request,"pages/contact.html", {"form":form})
