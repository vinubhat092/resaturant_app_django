from django.test import TestCase
from django.utils.text import slugify
from .utils import slugify_instance_title 
# Create your tests here.
from .models import Articles
class ArticleTestCase(TestCase):
    """
    this is article
    """
    def setUp(self):
        self.number_of_articles = 500
        for i in range(0,self.number_of_articles):
            Articles.objects.create(title='Hello world',content='something else')

    def test_queryset_exists(self):
        qs = Articles.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Articles.objects.all()
        self.assertEqual(qs.count(),self.number_of_articles)

    def test_hello_world_slug(self):
        obj = Articles.objects.all().order_by("id").first() 
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_hello_world_unique_slug(self):
        qs = Articles.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug,slugified_title)

    def test_slugify_instance_title(self):
        obj = Articles.objects.all().last()
        new_slug = []
        for i in range(0,25):
            instance = slugify_instance_title( obj ,save=False)
            new_slug.append(instance)
        unique_slug = list(set(new_slug))
        self.assertTrue(len(new_slug),len(unique_slug))

    def test_slugify_instance_title_redux(self):
        slug_list = Articles.objects.all().values_list('slug',flat=True) #gives the list of actual title in the db
        print("slug_list",slug_list)
        unique_slug_list = list(set(slug_list))  
        self.assertEqual(len(slug_list),len(unique_slug_list))

    def test_user_added_slug_unique(self):
        slug_list = Articles.objects.all().first()
        new_one = Articles.objects.create(title= "hello-world")
        self.assertNotEqual(slug_list,new_one)

    def test_article_search_manager(self):
        qs = Articles.objects.search(query = 'hello world')
        self.assertEqual(qs.count(),self.number_of_articles)

        qs = Articles.objects.search(query = 'hello')
        self.assertEqual(qs.count(),self.number_of_articles)

        qs = Articles.objects.search(query = 'something else')
        self.assertEqual(qs.count(),self.number_of_articles)





