
from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome_view,name='Home'),
    path('profile/', views.getProfile, name='profile'),
    path('profile/update/', views.updateProfile, name='update-profile'),
]
