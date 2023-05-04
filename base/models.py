from django.db import models
from django.urls import reverse

class GroupModel(models.Model):
    group_name = models.CharField(max_length=20, unique=True)
    group_image = models.ImageField(upload_to="images", null=True)
    
    def __str__(self):
        return self.group_name
    
    def get_absolute_url(self):
        return reverse("lores:lore_list", kwargs={"pk": self.pk})
    

class Lore(models.Model):
    name = models.CharField(max_length=50)
    belongs_to = models.ForeignKey(GroupModel, on_delete=models.CASCADE, to_field='group_name')
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("lores:loreitems", kwargs={"pk": self.pk})
    


class LoreItem(models.Model):
    item_type = models.ManyToManyField(Lore) ### MANYTOMANY
    item_title = models.CharField(max_length=70, null=True)
    item_description = models.TextField()

    def __str__(self):
        return f"{self.item_title}"

    class Meta:
        ordering = ['-id']
    