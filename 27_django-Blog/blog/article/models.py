from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="YAZAR")
    title = models.CharField(max_length=50, verbose_name="BAŞLIK")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
