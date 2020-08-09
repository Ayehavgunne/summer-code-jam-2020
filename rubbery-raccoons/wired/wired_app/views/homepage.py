from django.utils import timezone
from django.views.generic import ListView, ArchiveIndexView
from wired_app.models import Article


class HomepageView(ListView, ArchiveIndexView):
    model = Article
    date_field = "publication_date"
    make_object_list = True
    paginate_by = 10
    template_name = "wired_app/homepage.html"
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["years"] = set(
            result["publication_date"].year
            for result in Article.objects.order_by().values("publication_date").distinct().all()
        )
        context["categories"] = set(
            result["category"]
            for result in Article.objects.order_by().values("category").distinct().all()
        )
        return context
