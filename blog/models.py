from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    last_modified = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")
    categories = models.ManyToManyField("Category", related_name="posts", verbose_name="Категория")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60, verbose_name="Автор")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, verbose_name="Пост")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.post
