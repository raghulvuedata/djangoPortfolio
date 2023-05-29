from rest_framework import serializers
from rest_framework.fields import ImageField
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = ImageField(max_length=None, use_url=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'bio', 'skills', 'profile_picture', 'work_experience', 'hobbies']
