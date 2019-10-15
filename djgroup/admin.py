from django.contrib import admin
from djgroup.models import *
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('number', 'number2', 'email', 'address', 'website', 'facebook_link',
                    'twitter_link', 'google_link', 'linkedin_link', 'image_tag')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('index_tag', 'about_tag', 'services_tag',
                    'portfolio_tag', 'team_tag', 'contact_tag',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('description', 'mission', 'vision',
                    'strategy', 'goal', 'who_we_are', 'why_choose_us', 'what_we_do', 'how_we_work', 'best_for')


@admin.register(ServiceDesc)
class ServiceDescAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('created',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'description',
                    'facebook_link', 'insta_link', 'linkedin_link')
    ordering = ('name',)
    search_fields = ('name',)
    list_filter = ('created',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'title', 'image_tag')
    ordering = ('title',)
    search_fields = ('title', 'service_type__name')
    list_filter = ('service_type__name', 'created')


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('-created',)
    search_fields = ('name',)
    list_filter = ('created',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    ordering = ('-created',)
    search_fields = ('name', 'email')
    list_filter = ('name', 'created')
