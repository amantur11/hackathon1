from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

User = get_user_model()

class CallBack(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    callback = models.BooleanField(default=False)

    def __str__(self):
        return str(self.callback)


class CollectionProducts(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Product(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()
    checkbox_hit = models.BooleanField()
    checkbox_new = models.BooleanField(default=True)
    collection = models.ForeignKey(CollectionProducts, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    price = models.IntegerField()

   

    @property
    def get_images(self):
        images = ImageProducts.objects.filter(product=self)
        return [{'id': i.id, 'image': i.image.url, 'color': i.color} for i in images]


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ImageProducts(models.Model):
    # image = models.ImageField(upload_to='')
    # color = ColorField(default='#FF0000')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return f'{self.post.title}'
    

class Slider(models.Model):
    image = models.ImageField(upload_to="")
    link = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Слайдер'



class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'comments')
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} -> {self.post.title}'
    


class Like(models.Model):
    """
    Модель лайков
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
     
    post = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='likes'
    )  
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} liked - {self.post.title}'