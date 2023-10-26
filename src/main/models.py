from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class About(models.Model):
    photo = models.ImageField(upload_to='about/', verbose_name='Изображения')
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Информация")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "1. О нас"


class AboutLabel(models.Model):
    chooice = models.ForeignKey(About, verbose_name="Seçim", on_delete=models.CASCADE, related_name="labels")
    title = models.CharField(verbose_name="Başlıq", max_length=100)


class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/', verbose_name='Изображения')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')
    description = models.TextField(verbose_name="Информация", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = '2. Слайдеры'

    def __str__(self):
        return self.title

    def get_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="70" height="70" />')

    get_image.short_description = 'Изображения'

    def get_slider_url(self):
        return reverse('slider_detail', args=[self.slug])


class WhyUs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to='whyus/', verbose_name='Изображения')

    class Meta:
        verbose_name = 'Почему мы?'
        verbose_name_plural = '3. Почему мы?'

    def __str__(self):
        return self.title


class WhyUsBlock(models.Model):
    choice = models.ForeignKey(WhyUs, verbose_name="Выбор", on_delete=models.CASCADE, related_name="why_us")
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    icon = models.CharField(
        verbose_name="Икон",
        max_length=100,
        help_text='Misal: fa-cubes | https://fontawesome.com/v4/icons/')
    description = models.CharField(max_length=550, verbose_name='Информация')


class Partners(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    image = models.ImageField(upload_to='partners/', verbose_name='Изображения')
    description = models.TextField(verbose_name='Информация', null=True, blank=True)
    url = models.URLField(verbose_name='URL', blank=True)
    small_photo = models.BooleanField(default=False, verbose_name='Логотип маленький?',
                                      help_text='Для маленького каруселя')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = '4. Партнёры'

    def __str__(self):
        return self.name

    def get_partner_url(self):
        return reverse('partner_detail', args=[self.slug])
