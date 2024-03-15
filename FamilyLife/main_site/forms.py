from django import forms
from .models import Category, Feedback, Post



class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')
    
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        
        
class CommentForm(forms.ModelForm):
  class Meta:
    model = Feedback
    fields = ['text_feed']
    
  # def __init__(self, *args, **kwargs):
  #       super().__init__(*args, **kwargs)
  #       self.fields['post'].queryset = Post.objects.filter(pk=self.kwargs['post_id'])
