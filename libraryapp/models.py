import ordering as ordering
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return '{}'.format(self.name)



class books(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}',format(self.name)
