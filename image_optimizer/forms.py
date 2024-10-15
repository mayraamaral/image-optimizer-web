from django import forms
from django.core.exceptions import ValidationError

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select an image')
    quality = forms.IntegerField(initial=75, min_value=0, max_value=100, label='Quality (0-100)')
    scale = forms.FloatField(initial=0.5, min_value=0.1, max_value=1.0, label='Scale (0.1 to 1.0)')

def clean_image(self):
        image = self.cleaned_data.get('image')

        allowed_extensions = ['jpeg', 'jpg', 'png']
        file_extension = image.name.split('.')[-1].lower()
        
        if file_extension not in allowed_extensions:
            raise ValidationError("Only JPEG, JPG, and PNG files are allowed.")
        
        if image.content_type not in ['image/jpeg', 'image/png']:
            raise ValidationError("File type not supported. Only JPEG, JPG, and PNG files are allowed.")
        
        return image