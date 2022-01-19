from django.urls import path
from . views import home_page, about_us ,contact_us

urlpatterns = [
    path('', home_page),
    path('about_us', about_us),
    path('contact_us', contact_us)
]