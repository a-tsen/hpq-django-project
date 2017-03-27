from django.db import models


class About(models.Model):
    paragraph = models.TextField(max_length=1500)

    def __str__(self):
        return "About paragraph"
