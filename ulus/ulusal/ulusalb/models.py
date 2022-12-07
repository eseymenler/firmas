from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.title)

    """ def get_absolute_url(self):
        return reverse('home')  """

class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    """ def get_absolute_url(self):
        return reverse('home')  """







