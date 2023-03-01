from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30, null=True ,blank=True)
    phoneno = models.CharField(max_length=10, null=True ,blank=True)
    address = models.CharField(max_length=50, null=True ,blank=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('delivered','delivered'), ('Out for delivery','Out for delivery'), ('Pending', 'Pending'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, null=True, blank=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
