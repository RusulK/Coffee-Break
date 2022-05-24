"""Unit Testing for Views"""
from django.test import TestCase
from .models import Post


class TestPostListViews(TestCase):
    """Unit Test Index Page View"""
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')



class Add_RecipeViews(TestCase):
    """Unit Test Add Recipe Page View"""
    def test_add_recipe_page(self):
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

class Edit_RecipeViews(TestCase):
    """Unit Test Edit Recipe Page View"""
    def test_edit_recipe_page(self):
        response = self.client.get(f'/edit_recipe/{slug:slug}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')



