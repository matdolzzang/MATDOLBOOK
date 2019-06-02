from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null= True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField()


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
