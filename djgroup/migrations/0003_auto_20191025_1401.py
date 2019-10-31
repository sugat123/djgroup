# Generated by Django 2.2.3 on 2019-10-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djgroup', '0002_auto_20191025_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='team',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='team_text',
        ),
        migrations.AlterField(
            model_name='banner',
            name='about',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='contact',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='portfolio',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='services',
            field=models.ImageField(null=True, upload_to='banners'),
        ),
    ]