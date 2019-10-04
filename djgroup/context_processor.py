from django.shortcuts import render, redirect
from djgroup.models import *


def site_setting(request):
    settings = SiteSetting.objects.all().order_by('-created')[0:1]
    abouts = AboutUs.objects.all().order_by('-created')[0:1]
    banners = Banner.objects.all().order_by('-created')[0:1]

    return {'settings': settings, 'abouts': abouts, 'banners': banners}
