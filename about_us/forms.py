from django_svg_image_form_field import SvgAndImageFormField
from .models import Benefits
from django.forms import ModelForm


class SvgImageForm(ModelForm):
    class Meta:
        model = Benefits
        exclude = []
        field_classes = {
            'icon': SvgAndImageFormField,
        }
