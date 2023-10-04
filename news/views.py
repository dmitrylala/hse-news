from django.shortcuts import redirect, render
from django.views.generic import DetailView

from .forms import ArticlesForm
from .models import News


def news_home(request):
    news = News.objects.order_by("-date")[:3]
    return render(request, "news/news_home.html", {"news": news})


class NewsDetailView(DetailView):
    model = News
    template_name = "news/details_view.html"
    context_object_name = "article"


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

        error = "INCORRECT FORM"

    form = ArticlesForm()

    data = {"form": form, "error": error}

    return render(request, "news/create.html", data)


def index(request):
    return render(request, "news/index.html")


def price(request):
    return render(request, "news/price.html")


def sendarequest(request):
    return render(request, "news/sendarequest.html")


def moscow(request):
    return render(request, "news/moscow.html")


def sasha(request):
    return render(request, "news/sasha.html")


def tarkovsky(request):
    return render(request, "news/tarkovsky.html")
