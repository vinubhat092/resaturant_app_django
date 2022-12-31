from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm  

# Create your views here.

from .models import Articles

@login_required
def article_search_view(request):
    # print(dir(request))
    query_dict = request.GET #This is a dictionery
    # print(query_dict)
    query = query_dict.get("q")
    article_object = None
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    if query is not None:
        article_object = Articles.objects.get(id=query)

    context={
        "object":article_object,
    }
    return render(request,"articles/search.html",context=context)

def article_create_view(request):
    form=ArticleForm(request.POST or None)
    # print(dir(form))
    context ={
        "form":form
    }
    
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # print(title,content)
        # article_object = Articles.objects.create(title=title,content=content)
        # context['object'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html",context=context)
# @csrf_exempt
# def article_create_view(request):
#     form=ArticleForm()
#     # print(dir(form))
#     context ={
#         "form":form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] =form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             print(title,content)
#             article_object = Articles.objects.create(title=title,content=content)
#             context['object'] = article_object
#             context['created'] = True
    
#     return render(request, "articles/create.html",context=context)


def article_detail_view(request,id=None):
    article_obj=None
    if id is not None:
        article_obj = Articles.objects.get(id=id) 
    context ={
        "objects":article_obj, 
        }
    return render(request, "articles/detail.html",context=context)