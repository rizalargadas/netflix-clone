from django.db import models
from core.models import CustomUser


class ProfileImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles/images')

    def __str__(self):
        return self.name


def get_default_profile_image():
    return ProfileImage.objects.get(name='default_profile')


class Profile(models.Model):
    name = models.CharField(max_length=50)
    is_kid = models.BooleanField(default=False, null=True, blank=True)
    avatar = models.ForeignKey(
        ProfileImage, on_delete=models.CASCADE, default=get_default_profile_image)
    pin = models.PositiveIntegerField(blank=True, null=True)
    account = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='profiles')

    def __str__(self):
        return self.name
