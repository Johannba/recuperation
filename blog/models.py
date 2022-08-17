from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()
    class Meta:
        verbose_name = "Catégorie"


    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "Arcticle"
        ordering = ["date"]

    def __str__(self):
        return self.title

    def publish_string(self):
        if self.published:
            return "L'arcticle est publié"
        return "L'arcticle est inaccessible"



