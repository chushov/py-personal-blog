from typing import Dict, Any

from django.views.generic import TemplateView
from projects.models import Project


class Homepage(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

