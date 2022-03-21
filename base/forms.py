from . import models
from django.forms import ModelForm


class SecurityCheck(ModelForm):
    class Meta:
        model = models.Security
        fields = '__all__'


class InformationEdit(ModelForm):
    class Meta:
        model = models.Information
        fields = ['name', 'age', 'agreement']


class InformationCreate(ModelForm):
    class Meta:
        model = models.Information
        fields = ['name', 'age', 'balance', 'agreement']