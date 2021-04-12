from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.CharField(max_length=200)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "article"

    def __str__(self):
        return f"<Article {self.title}>"
