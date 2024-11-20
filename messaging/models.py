from django.db import models
from django.contrib.auth.models import User
from property.models import Property

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
