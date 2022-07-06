from django.urls import path
from Nasa import views

app_name = 'Nasa'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('post/', views.Post.as_view(), name='post'),
    path('Nasa/<slug:slug>', views.Nasa_Detail, name='Nasa-Detail'),
]
