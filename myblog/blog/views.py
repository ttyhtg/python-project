from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, Category
# Create your views here.
import math
import markdown
# import sys
# print('Python %s on %s' % (sys.version, sys.platform))

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.order_by("-create_time")
        for article in article_list:
            article.pub_date = article.create_time.strftime("%m-%d").replace("-", "月")
            article.length = len(article.text)
            article.read_time = math.ceil(len(article.text)/180) if article.text else 0
            article.categories = article.category_set.values()
            article.tags = article.tag_set.values()
            # cate_list = Category.objects.filter(article_id=article.id)

        context = {
            "article_list": article_list,
        }
        return self.render_to_response(context)


class DetailView(TemplateView):
    template_name = "detail.html"

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(url=request.path)
        content = ""
        for line in article.text.split("\n"):
            content += line.strip("  ") if "```" in line else line
            content += "\n"
        article.content = markdown.markdown(content, extensions=[
            'markdown.extensions.extra',  # 转换标题, 字体等
            'markdown.extensions.codehilite',  # 添加高亮功能
            'markdown.extensions.toc',  # 将表单渲染为html document类型
        ])



        # article.id + 1 是最快的方案, 但是我们不能保证自增键id不会中断.
        # 当前返回的结果不是QuerySet而是RawQuerySet, 当前并没有真正地请求并获取到查询结果.
        raw_query_set = Article.objects.raw(
            f"select * from {Article._meta.db_table} where id < {article.id} order by id desc limit 1")
        raws_query_set = Article.objects.raw(
            f"select * from {Article._meta.db_table} where id > {article.id} order by id asc limit 1")

        try:
            next_article = raw_query_set[0]
            prev_article = raws_query_set[0]
            context = {
                "next_article": next_article,
                "prev_article": prev_article,
                "article": article,
            }
        except IndexError:
            context = {
                "article": article,
            }



        return self.render_to_response(context)
