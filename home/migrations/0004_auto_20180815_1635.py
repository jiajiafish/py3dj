# Generated by Django 2.1 on 2018-08-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_site_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='site_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]