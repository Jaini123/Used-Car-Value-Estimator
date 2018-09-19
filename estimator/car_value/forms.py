from django import forms
from estimator.car_value.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'document','trainingDataset','testingDataset','name','email']
