from django import forms
from .models import  BlogComment


class CommentForm(forms.ModelForm):
	class Meta:
		model = BlogComment
		fields = ('name', 'comment')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'comment': forms.Textarea(attrs={'class': 'form-control'}),			
			
		}