from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget(), required=False)  # Remove required

    class Meta:
        model = FAQ
        fields = ['question', 'answer']
{
            'answer': CKEditorWidget(),
        }
