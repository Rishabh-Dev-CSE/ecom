from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
        name = models.CharField(max_length=100)
        choice = (
                
        ('Active', 'Active'),
        ('Disable', 'Disable'),
    )
        status = models.CharField(max_length=100, choices=choice)
        images = models.ImageField(upload_to='category_images', blank= True)

        def __str__(self):
                return self.name
        

class Brand(models.Model):
        name = models.CharField(max_length=100)
        logo = models.ImageField(upload_to='brands', blank=True)
        choice = (
            ('Active','Active'),
            ('Disable', 'Disable')
        )
        status = models.CharField(max_length=100, choices=choice)
        def __str__(self):
                return self.name

class Product(models.Model):
        title = models.CharField(max_length=255, null=True)
        name = models.CharField(max_length=100)
        category = models.ForeignKey(Category, on_delete= models.CASCADE)
        mrp = models.CharField(max_length=100)
        discount = models.IntegerField()
        stock = models.CharField(max_length=255)
        code = models.CharField(max_length=255)
        images = models.ImageField(upload_to='Products')
        description = models.TextField()
        brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
        choice = (
            ('Active','Active'),
            ('Disable', 'Disable')
        )
        trending_choice=(('Y', 'Yes'),('N', "No"))
        trending= models.CharField(max_length=100, choices=trending_choice, null=True)
        status = models.CharField(max_length=100, choices=choice, null=True)

        def __str__(self):
                return self.name

class Cart(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        product= models.ForeignKey(Product, on_delete=models.CASCADE)
        qty= models.IntegerField(default=1)
        cart_date=models.DateField(auto_now_add=True)

        def __str__(self):
                return self.user.first_name
        
class Order(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        product= models.ForeignKey(Product, on_delete=models.CASCADE)
        qty= models.IntegerField()
        orderid=models.CharField(max_length=255)
        choice = (
            ('Success','Success'),
            ('Pending', 'Pending'),
            ('Canceled','Canceled'),
            ('Delivered', 'Delivered'),
            ('Return', 'Return'),
            ('Refund', 'Refund')
        )
        status= models.CharField(choices=choice, max_length=255)
        order_date= models.DateField(auto_now_add=True)

        def __str__(self):
                return self.orderid

class Billing(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)
        orderid=models.ForeignKey(Order, on_delete=models.CASCADE)
        first_name=models.CharField(max_length=255)
        last_name=models.CharField(max_length=255)
        email= models.EmailField()
        contact= models.CharField(max_length=50)
        address=models.TextField()
        state=models.CharField(max_length=255)
        city=models.CharField(max_length=255)
        pincode=models.IntegerField()
        amount=models.CharField(max_length=255)
        payment_mode=models.CharField(max_length=100, choices=(('Online', 'Online'),('COD', 'COD')))
        billing_date=models.DateField(auto_now_add=True)

        def __str__(self):
                return self.first_name

