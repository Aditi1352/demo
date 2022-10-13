from atexit import register
from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='app-home'),
    path("about/",views.about,name='app-about'),
    path("login/",views.login,name='app-login'),
    path("signup/",views.signup,name='app-signup')
]

