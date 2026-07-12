from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Avg, Max, Count
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    search = request.GET.get("search")
    selected_category = request.GET.get("category")
    if selected_category:
        expenses = Expense.objects.filter(category=selected_category)
    else:
        expenses = Expense.objects.all()
    if search:
        expenses = expenses.filter(title__icontains=search)
    stats = Expense.objects.aggregate(
    total=Sum("amount"),
    count=Count("id"),
    highest=Max("amount"),
    average=Avg("amount"),
)
    return render(request,'expenses/index.html',{
        'expenses': expenses,
        'stats': stats,
        'selected_category': selected_category,
        'categories': Expense.CATEGORY_CHOICES,
        })

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