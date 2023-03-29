from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Base, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(Base):
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class Tag(Base):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'



class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blog')
    tags = models.ManyToManyField(Tag)
    view = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
        ordering = ('-created', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title




class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.user.username


