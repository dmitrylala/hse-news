from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("news_home", views.news_home, name="news_home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news-detail"),
    path("price", views.price, name="price"),
    path("sendarequest", views.sendarequest, name="sendarequest"),
    path("moscow", views.moscow, name="moscow"),
    path("sasha", views.sasha, name="sasha"),
    path("tarkovsky", views.tarkovsky, name="tarkovsky"),
]

# pk - первичный ключ#
