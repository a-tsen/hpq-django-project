from bs4 import BeautifulSoup
import requests

from django.db import models

from .validators import *


class Item(models.Model):
    RING = "rings"
    NECKLACE = "necklaces"
    BRACELET = "bracelets"
    EARRING = "earrings"
    MISCELLANEOUS = "miscellaneous"
    ITEM_TYPE_CHOICES = (
        (RING, "Ring"),
        (NECKLACE, "Necklace"),
        (BRACELET, "Bracelet"),
        (EARRING, "Earrings"),
        (MISCELLANEOUS, "Miscellaneous")
    )

    item_name = models.CharField(max_length=70, unique=True)
    link = models.CharField(max_length=200, validators=[isetsyvalidator, validate_link_exists])
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES, default="miscellaneous")

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.item_name

    def get_image_link(self):  # change to add validation for existing link and regex?
        page = requests.get(self.link).text
        soup = BeautifulSoup(page, 'html.parser')
        image_link = soup.find(id="image-0").get('data-large-image-href')
        return image_link

