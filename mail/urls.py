from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),  # Logout URL
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_emails, name='sent_emails'),
    path('compose/', views.compose_email, name='compose_email'),
    path('email_log/<str:email_address>/', views.email_log, name='email_log'),
    # Other URL patterns
]
