from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplate(TemplateView):
    template_name = 'index.html'


class ShopTemplate(TemplateView):
    template_name = 'shop-page.html'


class AboutTemplate(TemplateView):
    template_name = 'about-us.html'


class ContactTemplate(TemplateView):
    template_name = 'contact.html'


class LoginTemplate(TemplateView):
    template_name = 'login-register.html'


class CartTemplate(TemplateView):
    template_name = 'cart.html'