from django.db import models
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField

DepartmentList=(
    ('Human Resource','Human Resource'),
    ('Sales','Sales'),
     ('Marketing','Marketing'),
)
Role=(
    ('Manager','Manager'),
    ('Cashier','Cashier'),
    ('Admin','Admin'),
)

Resident=(
    ('Dodoma','Dodoma'),
    ('Morogoro','Morogoro'),
    ('Arusha','Arusha'),
    ('Kilimanjaro','Kilimanjaro'),
 
)

ManagementList=(
    ('SALES MANAGER','SALES MANAGER'),
    ('CUSTOMER CARE ASSOCIATE','CUSTOMER CARE ASSOCIATE'),
    ('CALL CENTER AGENT','CALL CENTER AGENT'),
    ('HELP DESK ASSISTANT','HELP DESK ASSISTANT'),

 
)


State=(
    ('Dodoma West','Dodoma West'),
    ('West Kilimanjaro','West Kilimanjaro'),
    ('North Morogoro','North Morogoro'),
    ('East Coast','East Coast'),
    ('West Dar-Es-Salaam','West Dar-Es-Salaam'),
    ('Dodoma Central','Dodoma Central'),
    ('South Arusha','South Arusha'),
    )





class Department(models.Model):
    Department=models.CharField(max_length=200,primary_key=True,choices=DepartmentList)

class Employee(models.Model):
    FUllname=models.CharField(max_length=200)
    Role=models.CharField(max_length=200,choices=Role)
    Email=models.CharField(max_length=200,primary_key=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)

class Announcements(models.Model):
    Logo=models.ImageField(upload_to="Announcements/")
    Heading=models.CharField(max_length=200)
    Document=models.FileField(upload_to="Document/")
    DateRegistered=models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    Fullname=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,primary_key=True)
    Resident=models.CharField(max_length=20,choices=Resident)
    NationalID=models.CharField(max_length=200)
    State=models.CharField(max_length=200,choices=State)
    License=models.FileField(upload_to="License/")
    DateRegistered=models.DateTimeField(auto_now_add=True)
    InsuranceDuration=models.DateTimeField(auto_now_add=False)
    Construction=models.CharField(max_length=100)
    BusinessType=models.CharField(max_length=100)
    Earthquake=models.BooleanField(default=False)
    Flood=models.BooleanField(default=False)
    TINnumber=models.IntegerField(unique=True)
    About=RichTextField(blank=True,null=True)

class compansation(models.Model):
    amount=MoneyField(max_digits=14,decimal_places=2,default_currency='TZS')
    CustomerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    RegisteredDate=models.DateTimeField(auto_now_add=True)
    BankReceipt=models.FileField(upload_to="CompasationReceipt/")

class MonthlyInstallment(models.Model):
    amount=MoneyField(max_digits=14,decimal_places=2,default_currency='TZS')
    CustomerID=models.ForeignKey(Customer,on_delete=models.CASCADE)
    RegisteredDate=models.DateTimeField(auto_now_add=True)
    BankReceipt=models.FileField(upload_to="PaymentReceipt/")

class Administration(models.Model):
    Role=models.CharField(max_length=200,primary_key=True,choices=ManagementList)
    Passport=models.ImageField(upload_to="Management/")
    DateRegistered=models.DateTimeField(auto_now_add=True)
    Message=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
