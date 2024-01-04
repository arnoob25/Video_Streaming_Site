from django.forms import ModelForm
from . import models

class UploadVideoForm(ModelForm):
    class Meta:
        model = models.Video
        fields = ['title','source', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            'placeholder': 'Enter your comment here...',
        })
        self.fields['comment'].label = ""