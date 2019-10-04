from django.shortcuts import render, redirect
from djgroup.models import *
from djgroup.forms import ContactForm
from django.contrib import messages


def index(request):
    service_type = ServiceType.objects.all().order_by('-created')
    portfolio = Portfolio.objects.all().order_by('-created')
    testimonial = Testimonials.objects.all().order_by('-created')
    context = {'portfolios': portfolio,
               'service_types': service_type,
               'testimonials': testimonial}

    return render(request, 'djgroup/index.html', context)


def about(request):
    abouts = AboutUs.objects.all().order_by('-created')[0:1]
    context = {'abouts': abouts}

    return render(request, 'djgroup/about.html', context)


def service(request):
    service_desc = ServiceDesc.objects.all().order_by('-created')
    service_type = ServiceType.objects.all().order_by('-created')
    context = {'service_descs': service_desc,
               'service_types': service_type}

    return render(request, 'djgroup/service.html', context)


def team(request):
    teams = Team.objects.all().order_by('-created')
    context = {'teams': teams}

    return render(request, 'djgroup/team.html', context)


def portfolio(request):
    portfolio = Portfolio.objects.all().order_by('-created')
    context = {'portfolios': portfolio}
    return render(request, 'djgroup/portfolio.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Successfully Submitted')

            return redirect('djgroup:contact')
    else:
        form = ContactForm()

    return render(request, 'djgroup/contact.html', {'form': form})


def handler404(request, exception):
    
    return render(request, 'djgroup/404.html', {})
