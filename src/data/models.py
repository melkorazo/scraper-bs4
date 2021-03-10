from django.db import models


class Catalogue(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catalogue"

class Category(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "category"

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    upc = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "article"
