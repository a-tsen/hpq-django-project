from bs4 import BeautifulSoup
import requests

from django.urls import reverse
from django.test import TestCase

from .models import Item


class ItemMethodTests(TestCase):

    def test_set_image_link_with_etsy_link_listing_number_only(self):
        pass

    def test_set_image_link_with_etsy_link_number_and_name(self):
        pass

    def test_set_image_link_with_non_etsy_link(self):
        pass

    def test_set_image_link_with_non_link(self):
        pass


class ItemViewTests(TestCase):

    def test_index_view_with_no_items(self):
        response = self.client.get(reverse('collection:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This page does not exist")  # placeholder - will be different later
        self.assertQuerysetEqual(response.context['item_list'], [])

    def test_index_view_with_single_item(self):
        item = Item(item_name="Item")
        response = self.client.get(reverse('collection:index'))
        self.assertQuerysetEqual(
            response.context['item_list'],
            ['<Item: Item>']
        )

    def test_index_view_with_two_items(self):
        item_one = Item(item_name="Item 1")
        item_two = Item(item_name="Item 2")
        response = self.client.get(reverse('collection:index'))
        self.assertQuerysetEqual(
            response.context['item_list'],
            ['<Item: Item 2>', '<Item: Item 1>']
        )

    def test_all_numbered_view_with_no_items(self):
        pass

    def test_all_numbered_view_with_single_item(self):
        pass
