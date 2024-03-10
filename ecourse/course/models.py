from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="static/courses/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    tags = models.ManyToManyField('Tag', blank=True, related_name='course')

    def __str__(self):
        return self.subject

class Lesson(BaseModel):
    subject = models.CharField(max_length=100)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="lesson/%Y/%m")

    tags = models.ManyToManyField('Tag', blank=True, related_name='lessons')

    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
