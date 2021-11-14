from django.urls import path
from boss import views
urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('ourworks',views.ourworks, name='ourworks'),
]
