from django.urls import path
from djgroup import views

app_name = 'djgroup'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('portfolio-detail/<int:id>',
         views.portfolio_detail, name='portfolio-detail'),
    path('events/', views.events, name='events'),
    path('events-detail/<int:id>',
         views.events_detail, name='events-detail'),
    path('career/', views.career, name='career'),
    path('career-detail/<int:id>',
         views.career_detail, name='career-detail'),

]
