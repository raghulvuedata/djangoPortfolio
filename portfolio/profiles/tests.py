from django.test import TestCase
import pytest
from .serializers import ProfileSerializer
from .models import Profile
import logging

@pytest.mark.django_db
def test_profile_serializer():
    # Create a test profile object
    profile = Profile.objects.create(
        name='John Doe',
        bio='Test bio',
        skills='Test skills',
        work_experience='Test work experience',
        hobbies='Test hobbies'
    )

    # Serialize the profile object
    serializer = ProfileSerializer(instance=profile)
    logging.info('This is an serializer ', serializer)
    # Ensure the serialized data matches the expected values
    assert serializer.data['name'] == 'John Doe'
    assert serializer.data['bio'] == 'Test bio'
    assert serializer.data['skills'] == 'Test skills'
    assert serializer.data['work_experience'] == 'Test work experience'
    assert serializer.data['hobbies'] == 'Test hobbies'

