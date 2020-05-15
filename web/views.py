from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import View

from web.forms import ArticleForm
from web.models import Topic, Article


def index(request):
    topics = Topic.objects.all()
    slide_one = topics[:3]
    slide_two = topics[3:6]

    context = {}

    if slide_one:
        context["slide_one"] = slide_one
    if slide_two:
        context["slide_two"] = slide_two

    return render(request, "web/index.html", context=context)


def topic(request, topic_id):
    current_topic = Topic.objects.get(id=topic_id)
    articles = current_topic.article_set.all()
    return render(request, "web/topic.html", context={"topic": current_topic, "articles": articles})


class ArticleView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        return render(
            request,
            "web/article/article.html",
            context={"article": article},
        )


class AddArticleView(View):
    def get(self, request, topic_id):
        topics = Topic.objects.all()
        current_topic = Topic.objects.get(id=topic_id)

        return render(
            request,
            "web/article/add.html",
            context={"topics": topics, "topic": current_topic},
        )

    def post(self, request, topic_id):
        form = ArticleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            article = Article.objects.create(
                title=form.clean().get("title"),
                content=form.clean().get("content"),
                description=form.clean().get("description")
            )
            Topic.objects.get(id=topic_id).article_set.add(article)
            return HttpResponseRedirect(
                redirect_to=reverse("web:topic", kwargs={"topic_id": topic_id})
            )
