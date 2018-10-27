from django.urls import path
import newsapp.views as newsapp

urlpatterns = [
    path('', newsapp.index, name="news_index"),
    path('<int:id>', newsapp.read, name="news_read")
]