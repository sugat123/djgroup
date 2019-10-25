from django.contrib import admin
from djgroup.models import *
from django.contrib.admin.models import LogEntry
from django.utils.safestring import mark_safe

LogEntry.objects.all().delete()


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('number', 'number2', 'email', 'address', 'website', 'facebook_link',
                    'twitter_link', 'google_link', 'linkedin_link', 'image_tag')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('index_tag', 'index_text', 'about_tag', 'about_text', 'services_tag', 'services_text',
                    'portfolio_tag', 'portfolio_text', 'contact_tag', 'contact_text',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('description', 'mission', 'vision',
                    'strategy', 'goal', 'who_we_are', 'why_choose_us', 'best_for')


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
    list_display = ('service_type', 'title', 'image_tag', 'description_safe')
    ordering = ('title',)
    search_fields = ('title', 'service_type__name')
    list_filter = ('service_type__name', 'created')

    def description_safe(self, obj):
        return mark_safe(obj.description)
    description_safe.short_description = 'Description'


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('-created',)
    search_fields = ('name',)
    list_filter = ('created',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image_tag', 'description_safe')
    ordering = ('title',)
    search_fields = ('title', 'date')
    list_filter = ('date',)

    def description_safe(self, obj):
        return mark_safe(obj.description)
    description_safe.short_description = 'Description'


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview_safe', 'description_safe',
                    'requirements_safe', 'skills_safe',)
    ordering = ('title',)
    search_fields = ('title', 'created')
    list_filter = ('created',)

    def overview_safe(self, obj):
        return mark_safe(obj.overview)
    overview_safe.short_description = 'Job Overview'

    def description_safe(self, obj):
        return mark_safe(obj.description)
    description_safe.short_description = 'Job Description'

    def requirements_safe(self, obj):
        return mark_safe(obj.requirements)
    requirements_safe.short_description = 'Job Requirements'

    def skills_safe(self, obj):
        return mark_safe(obj.skills)
    skills_safe.short_description = 'Skills required'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    ordering = ('-created',)
    search_fields = ('name', 'email')
    list_filter = ('name', 'created')
