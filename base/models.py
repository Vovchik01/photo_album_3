from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Photo(models.Model):

    category = models.ForeignKey( Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.description

