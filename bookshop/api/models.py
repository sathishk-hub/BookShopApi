from django.db import models

# Create your models here.
class  User(models.Model):
   first_name = models.CharField(max_length=15, help_text="Enter your first name", blank=False)
   second_name = models.CharField(max_length=15, help_text="Enter your second name", blank=True)
   number = models.CharField(max_length=10, help_text="Enter your phone number")
   date = models.DateTimeField(auto_now_add=True)
   


class Book(models.Model):
   book_name = models.CharField(max_length=15, help_text="Enter your book name", blank=False)
   author_name = models.CharField(max_length=15, help_text="Enter your author name", blank=True)
   total_pieces = models.IntegerField(help_text="Enter your total pieces")
   price = models.IntegerField(help_text="Enter the price")
   date = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
   #choices_list =(Book.objects.values_list('book_name',flat=True))
   #res = [(val, val) for val in choices_list] 
   number = models.CharField(max_length=10, help_text="Enter your number", blank=False, null=False)
   book_name = models.CharField(max_length=1000, null=False, help_text="Enter your book name", blank=False, default= "author" )
   total  = models.CharField(max_length=100)
   date = models.DateTimeField(auto_now_add=True)

   

