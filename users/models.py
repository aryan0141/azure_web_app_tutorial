from codecs import encode
from encodings import utf_8
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from .manager import UserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    isDeleted = models.BooleanField(verbose_name="Soft User Deletion", default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Resume(models.Model):
    user = models.ForeignKey(CustomUser, related_name='resume_set', on_delete=models.CASCADE)
    resume_name = models.CharField(max_length=100, blank=False, null=False)
    resume_path = models.FileField(blank=False, upload_to="resumes/")
    is_latest = models.BooleanField(default=True)

    def __str__(self):
        return self.resume_name