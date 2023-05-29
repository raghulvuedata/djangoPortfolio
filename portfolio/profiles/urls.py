from django.urls import path
from .views import home
from django.urls import path
from .views import ProfileCreateView, ProfileUpdateView, ProfileDeleteView


app_name = 'profiles'

urlpatterns = [
    path('home/', home, name='home'),
    path('api/profiles/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('api/profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('api/profiles/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
