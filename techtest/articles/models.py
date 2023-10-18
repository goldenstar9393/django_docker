from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )
    authors = models.ManyToManyField(
        'authors.Author', related_name='articles', blank=True
    )

    def __str__(self) -> str:
        return f"{self.title} {self.content} {self.regions} {self.authors}"
