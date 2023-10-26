from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from django.utils.translation import gettext_lazy as _

from config.etc.mail_settings import send_email_feedback
from src.main.forms import ContactForm
from src.main.models import About, Slider, WhyUs, Partners


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['about'] = About.objects.get()
        context['sliders'] = Slider.objects.order_by('id')
        context['why_us'] = list(WhyUs.objects.get().why_us.all())
        context['why'] = WhyUs.objects.get()
        return context


class SliderDetail(DetailView):
    model = Slider
    template_name = 'slider_detail.html'


class AboutUs(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['about'] = About.objects.get()
        return context


class Contact(TemplateView):
    template_name = 'contact.html'


class Partner(TemplateView):
    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super(Partner, self).get_context_data(**kwargs)
        context['partners'] = Partners.objects.order_by('-id')
        return context


class PartnerDetail(DetailView):
    model = Partners
    template_name = 'partner_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerDetail, self).get_context_data(**kwargs)
        context['partners'] = Partners.objects.order_by('?')[:7]

        return context


class SendContactMessage(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        send_email_feedback(form.cleaned_data)
        messages.success(self.request, _('Təşəkkür edirik!'))
        return super().form_valid(form)

    def get_success_url(self):
        redirect_url = self.request.GET.get('redirect_url')
        return redirect_url or super().get_success_url()
