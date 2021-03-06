# Generated by Django 2.2.3 on 2019-10-25 03:43

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('strategy', models.TextField()),
                ('goal', models.TextField()),
                ('who_we_are', models.TextField()),
                ('why_choose_us', models.TextField()),
                ('how_we_work', models.ImageField(default=None, upload_to='about')),
                ('best_for', models.TextField()),
                ('bg_image', models.ImageField(default=None, upload_to='about')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.ImageField(upload_to='banners')),
                ('index_text', models.TextField(null=True)),
                ('about', models.ImageField(upload_to='banners')),
                ('about_text', models.TextField(null=True)),
                ('services', models.ImageField(upload_to='banners')),
                ('services_text', models.TextField(null=True)),
                ('team', models.ImageField(upload_to='banners')),
                ('team_text', models.TextField(null=True)),
                ('portfolio', models.ImageField(upload_to='banners')),
                ('portfolio_text', models.TextField(null=True)),
                ('contact', models.ImageField(upload_to='banners')),
                ('contact_text', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Messages submitted from contact form',
            },
        ),
        migrations.CreateModel(
            name='ServiceDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='fa fa-bars', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Description in the first section of service page',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='fa fa-bars', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Types of services',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='sitesetting')),
                ('number', models.IntegerField()),
                ('number2', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('map_link', models.URLField()),
                ('facebook_link', models.URLField(null=True)),
                ('twitter_link', models.URLField(null=True)),
                ('google_link', models.URLField(null=True)),
                ('linkedin_link', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Site Setting',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team')),
                ('post', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('facebook_link', models.URLField()),
                ('insta_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Our Team',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonials of clients',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField(null=True)),
                ('image', models.ImageField(upload_to='portfolio')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djgroup.ServiceType')),
            ],
            options={
                'verbose_name_plural': 'Portfolio of our work',
            },
        ),
    ]
