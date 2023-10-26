from django.urls import path

from src.main import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('partners/', views.Partner.as_view(), name='partners'),
    path('partners/<slug>', views.PartnerDetail.as_view(), name='partner_detail'),
    path('slider/<slug>', views.SliderDetail.as_view(), name='slider_detail'),
    path('send_messages/', views.SendContactMessage.as_view(), name='send_message')
]