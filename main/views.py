from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "main/index.html"
