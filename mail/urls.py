from django.contrib import admin
from django.urls import path, include
from mail.views import inbox,sent_emails,compose_email

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('inbox/', include('mail.urls')),
    # path('sent/', include('mail.urls')),
    # path('compose/', include('mail.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('inbox', inbox, name='inbox'),  # Add this line for the home page
    path('sent_emails', sent_emails, name= 'sent_emails'),
    path('compose_email', compose_email,  name='compose'),
]
