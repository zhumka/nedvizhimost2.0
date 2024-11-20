from django.contrib import admin
from .models import Property,PropertyType,PropertyImage

admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyImage)