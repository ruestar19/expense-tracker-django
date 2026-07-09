from django.db import models

class Expense(models.Model):

    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Shopping", "Shopping"),
        ("Bills", "Bills"),
        ("Entertainment", "Entertainment"),
        ("Healthcare", "Healthcare"),
        ("Education", "Education"),
        ("Other", "Other"),
    ]

    title= models.CharField(max_length=100)

    amount= models.DecimalField(max_digits=10, decimal_places=2)

    category= models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    date= models.DateField()

    def __str__(self):
        return self.title