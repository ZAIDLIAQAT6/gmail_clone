from django.contrib import admin
from django.urls import path, include
from mail.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inbox/', include('mail.urls')),
    path('sent/', include('mail.urls')),
    path('compose/', include('mail.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),  # Add this line for the home page
]
