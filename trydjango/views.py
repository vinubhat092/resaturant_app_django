from django.http import HttpResponse
import random
from articles.models import Articles
from django.template.loader import render_to_string

def home_view(request,*args, **kwargs): 
    print("here",kwargs)
    name ="Justin"
    number= random.randint(10,1233123)
    articles_obj = Articles.objects.get(id=3) 
    articles_queryset = Articles.objects.all()
    # mylist_2 = ""
    # for i in mylist:
    # mylist_2 += f"number is {i}\n" 
    context={
    "object_list": articles_queryset, 
    "title": articles_obj.title,
    "id":articles_obj.id, 
    "content":articles_obj.content
}
    HTML_STRING = render_to_string("home-view.html",context=context)
    #
    # <h1>{title}(id:{id})!</h1>
    # HTML_STRING = """
    # # <p>{content} </p>
    # # """.format(**context)
    return HttpResponse(HTML_STRING)