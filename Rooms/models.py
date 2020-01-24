from django.db import models
from django import forms

# Create your models here.

class Room(models.Model):
    phone_number = models.CharField(max_length=120)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    pub_date = models.DateField()
    desc = models.CharField(max_length=500)
    file = models.FileField()

    def __str__(self):
        return self.desc

    def TestRoomlocation(self):
        return (self.location == "jorpati") and (self.price > 0.000)

    # def TestProductType(self):
    #     return (self.Product_Type == "wire") or (self.Product_Type == "wireless")
    #
    # def TestProductNameAndType(self):
    #     return (self.Product_Name != self.Product_Type)
    #
    def Test_desc(self):
        return (len (self.desc) > 5)

class Buyer(models.Model):
    B_First_Name = models.CharField(max_length=40)
    B_Last_Name = models.CharField(max_length=40)
    B_Username = models.CharField(max_length=10)
    B_Gender = models.CharField(max_length=25, default="Others")
    B_Phone_number = models.CharField(max_length=10) 
    B_E_mail = models.CharField(max_length=50)
    B_Password = models.CharField(max_length=50)
    # Question = models.CharField(max_length=100)
    # Answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.B_First_Name} {self.B_Last_Name} is the name of the buyer"


class Owner(models.Model):
    O_First_Name = models.CharField(max_length=40)
    O_Last_Name = models.CharField(max_length=40)
    O_Username = models.CharField(max_length=10)
    O_Gender = models.CharField(max_length=25, default="Others")
    O_Phone_number = models.CharField(max_length=10) 
    O_E_mail = models.CharField(max_length=50)
    O_Password = models.CharField(max_length=50)
    # Question = models.CharField(max_length=100)
    # Answer = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.O_First_Name} {self.O_Last_Name} is the name of the owner"
