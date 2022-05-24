"""Unit Testing for Models"""
from django.test import TestCase
from .models import Post

class TestModels(TestCase):
    """Unit Testing models has featured image"""
    def test_has_featured_image(self):
        self.assertTrue(Post.featured_image)