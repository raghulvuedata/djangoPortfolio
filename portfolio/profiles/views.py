from django.shortcuts import render
from .models import Profile

from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

def home(request):
    profile = Profile.objects.first()  # have only one profile object
    context = {'profile': profile}
    return render(request, 'profiles/home.html', context)

class ProfileCreateView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDeleteView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
