from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Post
#'gravity':'auto', 'crop': 'lfill',
#'crop': 'thumb',    'width': 200,'height': 200,

class ImageForm(forms.ModelForm):

    image = CloudinaryFileField(
        options = {
            'aspect_ratio': '1.0',
            'width': 320,
            'crop': 'limit',
            'folder': 'MesSnaps'
            }
    )

    class Meta:
        model = Post
        fields= '__all__'