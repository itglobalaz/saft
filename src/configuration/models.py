from django.db import models


class Config(models.Model):
    logo = models.ImageField(upload_to='siteLogo/', verbose_name='Логотип')
    phone = models.CharField(max_length=255, verbose_name="Контакт")
    email = models.EmailField(verbose_name="Почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    map = models.CharField(max_length=1000, verbose_name="Ссылка карты", null=True)

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "1. Контакты & Лого"

    def __str__(self):
        return self.phone


class Seo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name="Информация")
    keywords = models.TextField(max_length=255, verbose_name="Ключевые слова",
                                help_text="Пример: Разработка сайта, разработка сайтов в баку")

    class Meta:
        verbose_name = "Сео"
        verbose_name_plural = "2. Сео"

    def __str__(self):
        return self.title


class Social(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя", help_text="fb, tw, ins")
    url = models.CharField(max_length=255, verbose_name="Ссылка", help_text="facebook.com, +994504996588")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Социальную сеть"
        verbose_name_plural = "3. Социальная сеть"
