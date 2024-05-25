from django.db import models
from django_quill.fields import QuillField


class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="laptops/%Y/%m/", null=True)
    content = QuillField()
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title