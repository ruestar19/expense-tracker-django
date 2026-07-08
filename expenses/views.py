from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses= Expense.objects.all()

    return render(request,'expenses/index.html',{'expenses': expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form= ExpenseForm()
    return render(request,'expenses/add_expense.html', {'form':form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")

    return redirect("expense_list")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm


def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect("expense_list")

    else:
        form = ExpenseForm(instance=expense)

    return render(request, "expenses/edit_expense.html", {
        "form": form
    })