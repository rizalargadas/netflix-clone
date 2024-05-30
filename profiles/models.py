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
    pin = models.CharField(max_length=4, null=True, blank=True)
    enter_pin = models.CharField(max_length=4, null=True, blank=True)
    confirm_pin = models.CharField(max_length=4, null=True, blank=True)
    account = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='profiles')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
