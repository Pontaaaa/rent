from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Rent.urls")),
    path('signin/', views.sign_in_modal, name='signin'),
    path('signup/', views.sign_up_modal, name='signup'),
]
