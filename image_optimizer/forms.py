from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select an image')
    quality = forms.IntegerField(initial=75, min_value=0, max_value=100, label='Quality (0-100)')
    scale = forms.FloatField(initial=0.5, min_value=0.1, max_value=1.0, label='Scale (0.1 to 1.0)')
