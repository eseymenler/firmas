from django.db import models

# Create your models here.



class FirmaCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Firma Kategorileri'

    def __str__(self):
        return str(self.title)



class Firma(models.Model):
    category = models.ForeignKey(FirmaCategory, related_name="firma", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Firmalar'

    def __str__(self):
        return str(self.title)