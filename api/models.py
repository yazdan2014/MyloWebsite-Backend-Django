from django.db import models


class Commands(models.Model):
    class Fields(models.TextChoices):
        Everyone = "Everyone", "Everyone"
        DJ = "DJ", "DJ"
        Premium = "Premium", "Premium"
        Admin = "Admin", "Admin"

    name = models.CharField(primary_key=True, max_length=46)
    description = models.TextField(max_length=100)
    aliases = models.CharField(max_length=45)
    field = models.CharField(
        choices=Fields.choices,
        default=Fields.Everyone,
        max_length=50
    )

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.JSONField()
    tags = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title
