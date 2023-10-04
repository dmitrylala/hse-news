from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .forms import ArticlesForm
from .models import News, Page


class NewsDetailView(DetailView):
    model = News
    template_name = "news_navig/details_view.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        menu_items = (
            Page.objects.values("id", "navig", "navig_position")
            .filter(navig_position__gt=0)
            .order_by("-navig_position")
        )

        context["menu_items"] = menu_items

        return context


def create(request):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )

    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_navig:home")

        error = "INCORRECT FORM"

    form = ArticlesForm()

    data = {"form": form, "error": error, "menu_items": menu_items}

    return render(request, "news_navig/create.html", data)


def index(request):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )
    context = {"menu_items": menu_items}
    return render(request, "news_navig/index.html", context)


def moscow(request):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )
    context = {"menu_items": menu_items}
    return render(request, "news_navig/moscow.html", context)


def sasha(request):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )
    context = {"menu_items": menu_items}
    return render(request, "news_navig/sasha.html", context)


def tarkovsky(request):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )
    context = {"menu_items": menu_items}
    return render(request, "news_navig/tarkovsky.html", context)


def news_home(request, context):
    news = News.objects.order_by("-date")[:3]
    context["news"] = news
    return render(request, "news_navig/news_home.html", context)


def price(request, context):
    return render(request, "news_navig/price.html", context)


def sendarequest(request, context):
    return render(request, "news_navig/sendarequest.html", context)


def page(request: HttpRequest, pk: int):
    menu_items = (
        Page.objects.values("id", "navig", "navig_position")
        .filter(navig_position__gt=0)
        .order_by("-navig_position")
    )

    page = Page.objects.filter(id=pk).values()[0]

    context = {
        "pk": pk,
        "menu_items": menu_items,
        "title": page["title"],
        "content": page["content"],
    }

    view_funcs = {
        "PR": price,
        "RE": sendarequest,
        "NE": news_home,
    }

    view_func = view_funcs.get(page["context_type"])
    if view_func:
        return view_func(request, context)

    raise ValueError("Bad page id")
