from django.forms import ModelForm
from django.contrib import admin
from projects.models import Project


class ProjectAdminForm(ModelForm):

    MIN_RESOLUTION = (200, 200)

    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })
        self.fields['image'].help_text = 'Файлы в формате png, jpg. Минимальный размер изображения {} x {}'.format(
            *self.MIN_RESOLUTION)

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    pass


admin.site.register(Project, ProjectAdmin)