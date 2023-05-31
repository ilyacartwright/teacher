from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    surname = models.CharField(_("Отчество"), max_length=50, blank=True, null=True)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.surname}'

