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

class Adl_type(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc = models.TextField(blank = True)
    class Meta:
        verbose_name = "ADL种类"
        verbose_name_plural = verbose_name
        db_table = "ADL种类"
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
        db_table = "光泽度"
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
        db_table = "区域"
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
    createtime= models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to="category")
    due_time= models.DateTimeField(blank=False)
    class Meta:
        verbose_name = "Adl色板"
        verbose_name_plural = verbose_name
        db_table = "Adl色板"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



