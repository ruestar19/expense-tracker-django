from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model= Expense
        fields= ['title', 'amount', 'category', 'date']
        labels = {
            'title': 'Expense Title',
            'amount': 'Amount',
            'category': 'Category',
            'date': 'Date of Expense',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'title': {
                'required': "Please enter a title for the expense.",
                'max_length': "Title is too long.",
            },
            'amount': {
                'required': "Please enter the amount spent.",
                'invalid': "Enter a valid number.",
            },
        }