from django.db import models
from django.contrib.auth.models import User
class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_for_rent = models.BooleanField(default=False)  # Продажа или аренда
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    posted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='active')  # active/deleted/sold

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.property.title}"
