from django.contrib import admin
from django.urls import path, include
from mail.views import inbox, sent_emails, compose_email, email_log, home

urlpatterns = [
    # Uncomment the following lines if you need admin or authentication routes
    # path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),

    # Main app routes
    path('', home, name='home'),  # Home page
    path('inbox/', inbox, name='inbox'),  # Inbox page
    path('sent/', sent_emails, name='sent_emails'),  # Sent emails page
    path('compose/', compose_email, name='compose'),  # Compose email page
    path('email-log/<str:email_address>/', email_log, name='email_log'),  # Email log page for Log Info button
]
