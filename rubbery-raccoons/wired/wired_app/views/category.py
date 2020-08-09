from django.views.generic.list import ListView

from wired_app.models import Article


class Category(ListView):
    model = Article
    date_field = "publication_date"
    make_object_list = True
    context_object_name = "articles"
    template_name = "wired_app/category.html"

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs['category']).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = self.kwargs['category']
        return context
