# Generated by Django 2.2.3 on 2019-10-20 06:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('djgroup', '0009_auto_20191015_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]