from django.db import models
import datetime

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    catagory = models.ForeignKey(Catagory , on_delete=models.CASCADE, default=1)
    image =models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in =ids)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    
    def get_customer(email):
        return Customer.objects.get(email = email)   


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField() 
    address= models.CharField(max_length=200 , default='', blank=True)
    phone= models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False) 

    @staticmethod

    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone= models.CharField(max_length=10, default='', blank=True)
    content= models.CharField(max_length=100)
  



    
