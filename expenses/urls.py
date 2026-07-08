from django.urls import path
from .views import expense_list, add_expense, delete_expense, edit_expense

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('add/', add_expense, name='add_expense'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
]