
from django.urls import path
from . import views
urlpatterns = [
    path('',views.secured_app_view,name='Home'),
]
