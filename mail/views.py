from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Email

@login_required
def inbox(request):
    emails = Email.objects.filter(recipient="zaidliaqat99@gmail.com")
    return render(request, "mail/inbox.html", {"emails": emails})
    

@login_required
def sent_emails(request):
    emails = Email.objects.filter(sender=request.user)
    return render(request, "mail/sent.html", {"emails": emails})

@login_required
def compose_email(request):
    if request.method == "POST":
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

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # You will create this template next

