from django.urls import path

from . import views

app_name = "news_navig"
urlpatterns = [
    path("", views.index, name="home"),
    path("create", views.create, name="create"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news"),
    path("moscow", views.moscow, name="moscow"),
    path("sasha", views.sasha, name="sasha"),
    path("tarkovsky", views.tarkovsky, name="tarkovsky"),
    path("page/<int:pk>", views.page, name="page"),
]
