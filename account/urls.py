from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
        path('register/', views.register_view, name='register'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('profile/', views.profile_view, name='profile'),
        path("delete-account/", views.delete_account, name="delete_account"),
        path('activate/<uidb64>/<token>/', views.activate, name='activate_account'),
        path('activation', views.activation_view, name='activation'),
        path('activation/complete', views.activation_complete_view, name='activated'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

