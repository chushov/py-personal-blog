from django.forms import ModelForm, ValidationError
from django.contrib import admin
from projects.models import Project

from PIL import Image


class ProjectAdminForm(ModelForm):

    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Формат картинок: png, jpg.<br>Минимальный размер изображения {} x {}'.format(
            *self.MIN_RESOLUTION)
        self.fields['title'].help_text = 'Самодостаточный заголовок, от 3 символов и более.<br>' \
                                         '<a target="_blank" href="https://bureau.ru/bb/soviet/20150201/">Правила ' \
                                         'заголовков Бюро</a> '

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Картинка слишком маленькая :-(')
        return image

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('Заголовок должен быть самодостаточным')
        return title


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    pass


admin.site.register(Project, ProjectAdmin)
