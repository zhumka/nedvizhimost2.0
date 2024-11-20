from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
        path('register/', views.register_view, name='register'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('activate/<uidb64>/<token>/', views.activate, name='activate'),
        path('activation', views.activation_view, name='activation'),
        path('activation/complete', views.activation_complete_view, name='activated'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

