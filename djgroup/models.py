from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


class SiteSetting(models.Model):
    logo = models.ImageField(upload_to='sitesetting')
    number = models.IntegerField()
    number2 = models.IntegerField(null=True)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    website = models.URLField()
    map_link = models.URLField()
    facebook_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    google_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Site Setting'

    def image_tag(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.logo.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Logo'


class Banner(models.Model):
    index = models.ImageField(upload_to='banners', null=True)
    index_text = models.TextField(null=True)
    about = models.ImageField(upload_to='banners', null=True)
    about_text = models.TextField(null=True)
    services = models.ImageField(upload_to='banners', null=True)
    services_text = models.TextField(null=True)
    portfolio = models.ImageField(upload_to='banners', null=True)
    portfolio_text = models.TextField(null=True)
    events = models.ImageField(upload_to='banners', null=True)
    career = models.ImageField(upload_to='banners', null=True)
    contact = models.ImageField(upload_to='banners', null=True)
    contact_text = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Banners'

    def index_tag(self):
        if self.index:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.index.url)
        else:
            return 'No Image Found'
    index_tag.short_description = 'Index Banner'

    def about_tag(self):
        if self.about:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.about.url)
        else:
            return 'No Image Found'
    about_tag.short_description = 'About Banner'

    def services_tag(self):
        if self.services:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.services.url)
        else:
            return 'No Image Found'
    services_tag.short_description = 'Services Banner'

    def portfolio_tag(self):
        if self.portfolio:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.portfolio.url)
        else:
            return 'No Image Found'
    portfolio_tag.short_description = 'Portfolio Banner'

    def contact_tag(self):
        if self.contact:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.contact.url)
        else:
            return 'No Image Found'
    contact_tag.short_description = 'Contact Banner'


class AboutUs(models.Model):
    description = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    strategy = models.TextField()
    goal = models.TextField()
    who_we_are = models.TextField()
    why_choose_us = models.TextField()
    how_we_work = models.ImageField(upload_to='about', default=None)
    best_for = models.TextField()
    bg_image = models.ImageField(upload_to='about', default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About Us'


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team')
    post = models.CharField(max_length=100)
    description = models.TextField()
    facebook_link = models.URLField()
    insta_link = models.URLField()
    linkedin_link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Our Team'


class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='fa fa-bars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Types of services'


class ServiceDesc(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='fa fa-bars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Description in the first section of service page'


class Portfolio(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = HTMLField(null=True)
    image = models.ImageField(upload_to='portfolio')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Portfolio of our work'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Testimonials of clients'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Messages submitted from contact form'


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='events')
    description = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Events'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 80px; height:80px;" />' % self.image.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Events Image'


class Career(models.Model):
    title = models.CharField(max_length=100)
    overview = HTMLField()
    description = HTMLField()
    requirements = HTMLField()
    skills = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Careers'
