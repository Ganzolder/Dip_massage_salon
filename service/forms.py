from django import forms
from service.models import Masseur, Apppointment, Services


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control form-floating'


class ApppointmentForm(StyleFormMixin, forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    class Meta:
        model = Apppointment
        fields = ('name', 'surname', 'service', 'course', 'phone', 'date')
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ServicesForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Services
        fields = ('title', 'content', 'course', 'price', 'top_service')

