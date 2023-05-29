from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default='')
    skills = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    work_experience = models.TextField()
    hobbies = models.TextField(default='')

    def __str__(self):
        return self.name
