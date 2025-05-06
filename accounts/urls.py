from django.conf import settings
from django.urls import path
from .views import SignUpView,profile_view
from django.conf.urls.static import static
from . import models


urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile_view, name="profile"),
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)