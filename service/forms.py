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

    class Meta:
        model = Apppointment
        fields = ('name', 'surname', 'course', 'phone', 'date')
        widgets = {
            'course': forms.ChoiceField(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ServicesForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Services
        fields = ('title', 'content', 'course', 'price', 'top_service')

