from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
# Create your views here.
import math


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.order_by("-create_time")
        for article in article_list:
            article.pub_date = article.create_time.strftime("%m-%d").replace("-", "月")
            article.length = len(article.text)
            article.read_time = math.ceil(len(article.text)/180) if article.text else 0

        context = {
            "article_list": article_list
        }
        return self.render_to_response(context)