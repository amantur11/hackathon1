from django.db import models
from ckeditor.fields import RichTextField
import re

class About(models.Model):
    title = models.CharField(max_length=20)
    text = RichTextField()

    @property
    def get_images(self):
        image = AboutImages.objects.filter(about = self)
        return [{'id': i.id, 'image': i.image.url} for i in image]

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
    
    def __str__(self):
        return self.title


class AboutImages(models.Model):
    image = models.ImageField(upload_to='')

    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_image')
    

class Benefits(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'
    
    def __str__(self):
        return self.title


class News(models.Model):
    images = models.ImageField(upload_to='')

    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    def __str__(self):
        return self.title


class HelpImages(models.Model):
    image = models.ImageField(upload_to='')

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()
    help = models.ForeignKey(HelpImages, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'
    
    def __str__(self):
        return self.question


class Offer(models.Model):
    title = models.CharField(max_length=50)
    text = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'
    
    def __str__(self):
        return self.title



class FooterOne(models.Model):
    logo = models.ImageField(upload_to='')
    text = models.TextField()
    number = models.CharField(max_length=30)


NUMBER = 'Number'
MAIL = 'Mail'
INSTAGRAM = 'Instagram'
TELEGRAM = 'Telegram'
WHATSAPP = 'WhatsApp'
FOOTER_CHOICES =[
    ('Number', NUMBER),
    ('Mail', MAIL),
    ('Instagram', INSTAGRAM),
    ('Telegram', TELEGRAM),
    ('WhatsApp', WHATSAPP),
]


class FooterTwo(models.Model):
    type = models.CharField(max_length=100, choices=FOOTER_CHOICES)
    network = models.CharField(max_length=30)
    link = models.CharField(max_length=200, null=True, blank=True)
    footer = models.ForeignKey(FooterOne, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.type == WHATSAPP:
            self.link = 'https://wa.me/'+''.join(re.findall(r'\d' ,self.network))
        super(FooterTwo, self).save(*args, **kwargs)

    def __str__(self):
        return self.type