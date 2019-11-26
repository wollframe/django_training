from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length = 50, verbose_name="Товар")
    content = models.TextField(null = True, blank = True, verbose_name="Описание")
    price = models.FloatField(null = True, blank = True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name="Опубликовано")
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Изображение")
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def title_and_price(self):
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.title
    title_and_price.short_description = 'Название и цена'

    class Meta:
        verbose_name_plural="Объявления"
        verbose_name="Объявление"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрика"
        verbose_name = "Рубрика"
        ordering = ['name']
