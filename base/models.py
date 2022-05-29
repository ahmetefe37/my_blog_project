from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Author(models.Model):
    firstname = models.CharField(max_length=200,blank=True,null=True)
    lastname = models.CharField(max_length=200,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    info = models.TextField(max_length=1000,blank=True,null=True)
    date_hired = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    profil_picture = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.firstname

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    frequency = models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    CATEGOIRES = (
    ("daily_news", "Daily News"),
    ("sports","Sports"),
    ("health","Health"),
    ("crypto","Cryptocurrencies"),
    )

    STATUS = (
        ("draft","Draft"),
        ("published","Published")
    )

    title = models.CharField(max_length=200,blank=True,null=True)
    content = RichTextField(max_length=5000,blank=True,null=True)
    status = models.CharField(max_length=200,choices=STATUS,null=True)
    category = models.CharField(max_length=200,null=True,choices = CATEGOIRES)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author,blank=True,null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image_post = models.ImageField(blank=True,null=True)
    slug = models.SlugField(unique=True,editable=False,max_length=210)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail_url', kwargs={"pk_slug_detail":self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug,counter)
            counter +=1
        return unique_slug 

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)    

    class Meta:
        ordering = ('-date_created',)

