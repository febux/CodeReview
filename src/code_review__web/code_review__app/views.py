from django.views.generic import TemplateView


class IndexPageView(TemplateView):  # type: ignore
    template_name = 'index.html'
