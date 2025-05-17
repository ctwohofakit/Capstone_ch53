from django.urls import path
from . import views

urlpatterns=[
    path("", views.home_view, name="home"),
    path("contact",views.contact_view, name="contact"),
    path("terms",views.terms_view, name="terms"),
    path("privacy",views.privacy_view, name="privacy"),
]