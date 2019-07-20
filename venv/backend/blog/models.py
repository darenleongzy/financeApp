from django.db import models
    # Create your models here.

    # add this
class Blog(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title


class Bank(models.Model):
    title = models.CharField(max_length=120)

class BankAccount(models.Model):
    name =  models.CharField(max_length=120)
    type =  models.CharField(max_length=120)
    amount =  models.CharField(max_length=120)

class User(models.Model):
    name =  models.CharField(max_length=120)
    bankAccount = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
