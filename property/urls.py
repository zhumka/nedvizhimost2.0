from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='home'),
    path('advertisements/',views.advertisements_view,name='advertisements')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)