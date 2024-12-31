from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Email
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, "mail/home.html")  # Landing page template


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to the 'next' parameter or to the inbox page by default
            next_url = request.GET.get('next', reverse('inbox'))  # Default to inbox if no 'next' parameter
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    # If GET request or failed login, redirect to login page
    return render(request, "mail/login.html")


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")
    return render(request, "mail/register.html")


@login_required
def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirects to the login page after logout


@login_required
def inbox(request):
    # Fetch emails where the logged-in user is the recipient and order by timestamp (sent time)
    emails = Email.objects.filter(recipient=request.user).order_by("-timestamp") 
    return render(request, "mail/inbox.html", {"emails": emails})



@login_required
def sent_emails(request):
    # Fetch emails where the logged-in user is the sender
    emails = Email.objects.filter(sender=request.user.email).order_by("-timestamp")  # Order by most recent email
    return render(request, "mail/sent.html", {"emails": emails})


@login_required
def compose_email(request):
    if request.method == "POST":
        recipient = request.POST["recipient"]
        subject = request.POST["subject"]
        body = request.POST["body"]
        
        # Create and save the email
        email = Email.objects.create(
            sender=request.user.email,
            recipient=recipient,
            subject=subject,
            body=body
        )
        
        messages.success(request, "Email sent successfully.")
        return redirect("sent_emails")
    
    return render(request, "mail/compose.html")


@login_required
def email_log(request, email_address):
    emails = Email.objects.filter(sender=email_address)  # Filter by sender's email
    emails = emails.order_by("-timestamp")  # Order by timestamp (most recent first)
    return render(request, 'mail/email_log.html', {'emails': emails})
