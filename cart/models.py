from django.db import models
from product.models import ImageProducts, Product
from colorfield.fields import ColorField
from django.utils.html import mark_safe 


CHOISES_ORDER = [
    ('New', 'New'),
    ('Decorated', 'Decorated'),
    ('Сanceled', 'Сanceled')
]
class Order(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    data = models.DateField(auto_now_add=True)

    status =models.CharField(max_length=20, choices=CHOISES_ORDER, default='New')

    def __str__(self):
        return self.name + ' ' + self.second_name


class OrderProduct(models.Model):
    quantity = models.IntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ForeignKey(ImageProducts, on_delete=models.PROTECT)

    
    def image_tag(self):
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.image.url))

    image_tag.short_description = 'Image'
    
    @property
    def price(self):
        return self.products.price

    @property
    def new_price(self):
        return self.products.new_price
    
    @property
    def size_range(self):
        return self.products.size_range
    
    @property
    def color(self):
        return self.image.color 



class OrderInfo(models.Model):
    quantity = models.IntegerField()
    quantity_in_line = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()
    total_price = models.IntegerField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
