from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length = 225)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 225)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='picures', null= True, blank = True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'id':self.id})

    @property
    def get_comments(self):
        return self.comments.all()

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            result = (300,300)
            img.thumbnail(result)
            img.save(self.image.path)


class comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f'{self.user.username} comment '

    
    @property
    def get_replies(self):
        return self.replies.all()




class Reply(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(comment, related_name = 'replies', on_delete = models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f'{self.user.username} reply '



class Education(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Non_technical_skill(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title

class Technical_skill(models.Model):
    title = models.CharField(max_length = 225)

    def __str__(self):
        return self.title


class Information(models.Model):
    name = models.CharField(max_length = 225)
    email = models.EmailField()
    summary = models.TextField(null= True, blank=True)
    phone = models.CharField(max_length = 225)
    address = models.CharField(max_length = 225, null= True, blank=True)
    city = models.CharField(max_length = 225, null= True, blank=True)
    image = models.ImageField(upload_to = 'pics', null= True, blank=True)
    website = models.URLField(null= True, blank=True)
    description = models.TextField(null= True, blank=True)
    declaration = models.TextField(null= True, blank=True)
    introduction = models.TextField(null= True, blank=True)
    interest = models.ManyToManyField(Interest)
    language = models.ManyToManyField(Language)
    technical_skill =models.ManyToManyField(Technical_skill)
    non_technical_skill = models.ManyToManyField(Non_technical_skill)
    project = models.ManyToManyField(Project)
    certificate = models.ManyToManyField(Certificate)
    education = models.ManyToManyField(Education)

    def __str__(self):
        return self.name


