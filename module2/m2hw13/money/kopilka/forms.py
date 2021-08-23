from django import forms
from .models import Money

class DateInput(forms.DateInput):
    input_type = 'date'
    
class MyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['earnings', 'pub_date', 'category', 'note_text']
        labels = {'earnings' : '+-money', 'pub_date' : 'Date', 'category': 'Category', 'note_text' : 'Note'}
        widgets = {'pub_date' : DateInput()}
        
class DateForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_for = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))