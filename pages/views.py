import requests
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")

def terms_view(request):
    return render(request, "pages/terms.html")

def privacy_view(request):
    return render(request, "pages/privacy.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #  verify reCAPTCHA portion
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": settings.RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            cap_response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
            result = cap_response.json()

            if result.get("success"):
                first_name=form.cleaned_data["firstname"]
                last_name=form.cleaned_data["lastname"]
                email   = form.cleaned_data["email"]
                subject = form.cleaned_data["subject"]
                message = form.cleaned_data["message"]

                body = (
                    "This is an email from the interview project\n"
                    f"Name: {first_name}\n"
                    f"Email: {email}\n"
                    f"Subject: {subject}\n"
                    f"Message: {message}"
                )
                send_mail(
                    "Message from MockInterview",
                    body,
                    email,
                    ["ctwohoda@gmail.com"],
                )
                messages.success(request, "Your message has been sent!")
                return redirect("contact")
            else:
                messages.error(request, "reCAPTCHA verification failed. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
