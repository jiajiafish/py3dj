from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique = True)
    desc = models.TextField()
    picture = models.ImageField(upload_to ="category",blank = True)
    class Meta:
        verbose_name = "商品类别表"
        verbose_name_plural = verbose_name
        db_table = "商品类别表"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100,unique = True)
    desc = models.TextField()
    picture = models.ImageField(upload_to ="category",blank = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=4)
    kucun = models.IntegerField(default=0)
    onshelf = models.BooleanField(default=True)
    Createtime = models.DateTimeField(auto_now_add=True)
    Modtime = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "商品列表"
        verbose_name_plural = verbose_name

        db_table = "商品列表"
        ordering = ('Createtime',)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name