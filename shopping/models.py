from django.db import models

# Create your models here.

class 商品类别表(models.Model):
    商品名 = models.CharField(max_length=50,unique = True)
    描述 = models.TextField()
    图片 = models.ImageField(upload_to ="category",blank = True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
