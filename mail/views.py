from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Email

@login_required
def inbox(request):
    # Fetch emails where the logged-in user is the recipient
    emails = Email.objects.filter(recipient=request.user.email)
    return render(request, "mail/inbox.html", {"emails": emails})

@login_required
def sent_emails(request):
    # Fetch emails where the logged-in user is the sender
    emails = Email.objects.filter(sender=request.user)
    return render(request, "mail/sent.html", {"emails": emails})

@login_required
def compose_email(request):
    if request.method == "POST":
        # Create a new email and save it
        recipient = request.POST["recipient"]
        subject = request.POST["subject"]
        body = request.POST["body"]
        Email.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=body
        )
        return redirect("sent_emails")
    return render(request, "mail/compose.html")

@login_required
def email_log(request, email_address):
    # Fetch all emails related to the given email address
    emails = Email.objects.filter(sender=email_address) | Email.objects.filter(recipient=email_address)
    return render(request, "mail/email_log.html", {"emails": emails, "email_address": email_address})

def home(request):
    return render(request, "home.html")  # You will create this template next
