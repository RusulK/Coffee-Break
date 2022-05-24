from django.test import TestCase
from .forms import CommentForm, RecipeForm



class TestRecipeForm(TestCase):
    """Unit Test for Recipe Form"""
    def test_post_title_is_required(self):
        form = RecipeForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = RecipeForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RecipeForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'slug', 'time', 'ingredients', 
            'content', 'featured_image',)
            )

class TestCommentForm(TestCase):
    """Unit Test for Comments Form"""
    def test_post_title_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
