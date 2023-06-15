# Generated by Django 4.2.1 on 2023-05-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='description',
            field=models.TextField(blank=True, db_column='description', null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, db_column='title', max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(db_column='image', upload_to='banners', verbose_name='Banner Image'),
        ),
    ]
