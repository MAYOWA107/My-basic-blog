from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Share your thought...',
                    'class': 'form-control',
                }
            ),
        }
        labels = {
            'body': 'Thought',
        }

    def clean_body(self):
        body = self.cleaned_data.get('body', '')
        if not body.strip():
            raise forms.ValidationError('Post content cannot be empty.')
        return body
