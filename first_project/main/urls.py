from django.urls import path
from . views import home_page, about_us ,contact_us,blog_detail
app_name = "blog"
urlpatterns = [
    path('', home_page,name = "home"),
    path('about_us', about_us,name = "about_us"),
    path('contact_us', contact_us,name = "contact_us"),
    path('blog-detail/<int:pk>',blog_detail,name = "blog-detail")
]