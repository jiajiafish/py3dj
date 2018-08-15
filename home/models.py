from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50,unique = True)
    eng_name = models.CharField(max_length=50,unique = True,default="未命名")
    desc = models.TextField(blank = True)
    picture = models.ImageField(upload_to ="category",blank = True)
    site_url = models.URLField(blank=True)
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
        db_table = "类别"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100,unique = True)
    eng_name = models.CharField(max_length=100,unique = True,default="未命名")
    desc = models.TextField(blank = True)
    picture = models.ImageField(upload_to ="category",blank = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    site_url = models.URLField(blank=True)
    # price = models.DecimalField(max_digits=10,decimal_places=4)
    # kucun = models.IntegerField(default=0)
    # onshelf = models.BooleanField(default=True)
    Createtime = models.DateTimeField(auto_now_add=True)
    Modtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "项目列表"
        verbose_name_plural = verbose_name

        db_table = "项目列表"
        ordering = ('Createtime',)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name