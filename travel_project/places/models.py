from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=256)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField('Картинка', upload_to='places/')
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position']

    def __str__(self):
        return f'{self.place.title} - {self.position}'
