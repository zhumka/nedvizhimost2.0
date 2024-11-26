from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='C:/Users/user/Desktop/img/', default='avatars/default.jpg')

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

