from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save,post_save
from .utils import slugify_instance_title
from django.urls import reverse
from django.db.models import Q
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL   #now we can use User instead of "auth.User" in Articles class

class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query =="":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using = self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)


class Articles(models.Model):
    user = models.ForeignKey("auth.User", blank=True, null=True, on_delete = models.SET_NULL)   #auth is the default django user model
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=False,auto_now=False,null=True,blank=True)

    objects = ArticleManager()


    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse("article-detail",kwargs={"slug":self.slug})


    def save(self, *args, **kwargs):
        # obj = Article.obbjects.get(id=1)
        # obj.save()
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

#django pre_save and post_save signals


def article_pre_save(sender,instance,*args,**kwargs):   
    # print("pre_save")
    if instance.slug is None:
        slugify_instance_title(instance,save=False)

pre_save.connect(article_pre_save, sender=Articles)

def article_post_save(sender,instance,created,*args,**kwargs):
    # print("post_save")
    if created:
        slugify_instance_title(instance,save=True)
        # slug = slugify(instance.title)
        # instance.slug = slug
        # instance.save()

post_save.connect(article_post_save,sender=Articles)





