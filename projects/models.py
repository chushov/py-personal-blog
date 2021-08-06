from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=76, verbose_name="Заголовок")
    description = models.TextField(max_length=150, verbose_name="Описание")
    technology = models.CharField(max_length=20, verbose_name="Технология")
    image = models.ImageField(upload_to="static/img/", blank=True, null=True, verbose_name="Картинка")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title
