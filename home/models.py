from django.db import models
from django.contrib.auth.models import User

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

class Adl_type(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.TextField(blank = True)
    class Meta:
        verbose_name = "ADL种类"
        verbose_name_plural = verbose_name
        db_table = "Adl_type"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Adl_glossy(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc =  models.TextField(blank = True)
    class Meta:
        verbose_name = "光泽度"
        verbose_name_plural = verbose_name
        db_table = "Glossy"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Adl_region(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.TextField(blank= True)
    class Meta:
        verbose_name = "区域"
        verbose_name_plural = verbose_name
        db_table = "region"
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Adl_Item(models.Model):
    name= models.CharField(max_length=100,unique=True)
    adl_type= models.ForeignKey(Adl_type,on_delete=models.CASCADE)
    adl_region= models.ForeignKey(Adl_region,on_delete=models.CASCADE)
    struct_code= models.CharField(max_length=100)
    glossy_code= models.ForeignKey(Adl_glossy,on_delete=models.CASCADE)
    adl_standard= models.CharField(max_length=100,default="0")
    stock= models.IntegerField(default=0)
    adl_refresh = models.IntegerField(default=0)
    adl_reject = models.BooleanField(default=False)
    createtime= models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to="category")
    due_time= models.DateTimeField(blank=False)
    class Meta:
        verbose_name = "Adl色板"
        verbose_name_plural = verbose_name
        db_table = "Adl_item"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class Adl_borrow(models.Model):
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    counts = models.IntegerField(default=1)
    check_in_time = models.DateTimeField(blank=True)
    check_out_time = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_check_out = models.BooleanField(default=False)
    is_return = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Adl借阅"
        verbose_name_plural = verbose_name
        db_table = "Adl_borrow"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

