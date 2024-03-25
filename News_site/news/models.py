from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

class News(models.Model):
    """ модель НОВОСТИ и из чего состоит """

    Title = models.CharField(max_length=100, blank=False, help_text = " напишите название новости! ", db_column="Title")
    TheNews = models.TextField(blank=False, help_text = " напишите текст новости! ", db_column="TheNews")
    Author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=False)
    TimePublished = models.DateTimeField(auto_now=True, db_column="published")
    image = models.ImageField(upload_to= "NewsImage", help_text=" добавте картинки! ")

    class Meta:
            db_table = "News"
            verbose_name = "News"

    def __str__(self):
            return self.Title

    def get_absolute_url(self):
        """ метод для показа ИНДИВИДУАЛЬНОЙ новости """
        return reverse('News-detail', args=[str(self.id)])





class Author(models.Model):
    """модель автора и из чего состоит"""
    IdUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, db_column="IdUser")
    FirstName = models.CharField(max_length=50, blank=True, db_column="FirstName" )
    LastName = models.CharField(max_length=50, blank=True, db_column="LastName")
    Nickname = models.CharField(max_length=50, blank=True, db_column="Nickname")
    Email = models.EmailField(blank=False, help_text = "напишите mail!", db_column="Email")
    FaceImage =  models.ImageField(upload_to= "faceImage", db_column="FaceImage")


    class Meta:
          ordering = ['Email']
          db_table = "AuthorNews"
          verbose_name = "author"

    def get_absolute_url(self):
        """ метод для показа ИНДИВИДУАЛЬНОГО автора """
        return reverse('Author-detail, args=[str(self.id)]')
