from .models import Comment
from django import forms
from .models import Post



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
class RecipeForm(forms.ModelForm):
    """Add and Update Recipe Form"""
    class Meta:
        """Meta data for add recipe form"""
        model = Post
        fields = ('title', 'slug', 'time',
                  'content', 'featured_image',)
                  