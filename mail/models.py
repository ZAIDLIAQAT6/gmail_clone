from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=255)
    sender = models.EmailField()
    recipient = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Email(models.Model):
    subject = models.CharField(max_length=255)
    sender = models.EmailField()
    recipient = models.EmailField()
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
