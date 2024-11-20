from django.db import models
from property.models import Property
from django.contrib.auth.models import User
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user.username} favorited {self.property.title}"
