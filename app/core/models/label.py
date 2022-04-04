from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name
