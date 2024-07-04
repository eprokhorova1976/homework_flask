from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, {self.email}, {self.phone}, {self.address}'


class Product(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    adding_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.title}, price: {self.price}, quantity: {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.client}, total amount: {self.order_amount}'


