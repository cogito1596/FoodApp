from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_desc = models.TextField()
    item_img = models.ImageField(upload_to="", default="default_image.png")

    def __str__(self):
        return self.item_name
