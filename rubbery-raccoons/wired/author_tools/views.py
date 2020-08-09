from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views.generic.list import ListView

from .forms import ArticleForm
from wired_app.models import Article


@login_required
def compose(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.publication_date = date.today()
            art.slug = "-".join(
                (slugify(x) for x in [art.author.username, art.title, art.publication_date])
            )
            art.save()
            messages.success(request, "Article submitted!")
            form = ArticleForm()
        else:
            messages.error(request, "Form input was invalid.")

    else:
        form = ArticleForm()

    return render(request, "author_tools/compose.html", {"form": form})


@login_required
def update(request, slug):
    art = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            art.update(title=form.cleaned_data.get("title"))
            art.update(headline=form.cleaned_data.get("headline"))
            art.update(body=form.cleaned_data.get("body"))
            messages.success(request, "Article updated!")
    else:
        form = ArticleForm(instance=art)
    return render(request, "author_tools/update.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class AuthorsArticleView(ListView):
    template_name = "author_tools/authors_article_view.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by("-created")