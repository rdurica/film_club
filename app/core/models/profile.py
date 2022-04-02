from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"

    def __repr__(self) -> str:
        return f"--id: {self.id} --name: {self.user.username}"
