from django.conf.urls import url
from django.urls import path

from .views import index, topic, AddArticleView, ArticleView

app_name = "web"

urlpatterns = [
    url(r"^$", index, name="index"),
    path(r'topics/<int:topic_id>', topic, name="topic"),
    path(r'topics/<int:topic_id>/add_article', AddArticleView.as_view(), name="add_article"),
    path(r'articles/<int:article_id>', ArticleView.as_view(), name="article")
]
