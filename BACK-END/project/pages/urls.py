from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.index, name='index'),
    path('about' ,views.about, name='about'),
    path('login/' ,views.login_view, name='login'),
    path('register' ,views.register, name='register'),
    path('contact' ,views.contact_view, name='contact'),
]