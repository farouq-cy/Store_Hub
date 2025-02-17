from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('index/' ,views.index, name='index'),
    path('about/' ,views.about, name='about'),
    path('login/' ,views.user_login, name='login'),
    path('register/' ,views.register, name='register'),
    path('contact/' ,views.contact_view, name='contact'),
    path('allproducts/' ,views.allproducts, name='allproducts'),
    path('wishlist/' ,views.wishlist, name='wishlist'),
    path('toggle-like/<int:product_id>/', toggle_like, name='toggle_like'),
]