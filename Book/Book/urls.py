from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Rent.urls")),
    path('signin/', views.sign_in_modal, name='signin'),
    path('signup/', views.sign_up_modal, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]