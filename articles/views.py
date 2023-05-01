from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm 
from django.http import Http404

# Create your views here.

from .models import Articles

@login_required
def article_search_view(request):
    # print("here",dir(request))
    query = request.GET.get('q') 
    qs = Articles.objects.search(query=query) #paasing the keyword argument for models
    context={
        "object_list":qs
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
        # return redirect("article-detail",slug=article_object.slug)
        return redirect(article_object.get_absolute_url())
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


def article_detail_view(request,slug=None):
    article_obj=None
    if slug is not None:
        try:
            article_obj = Articles.objects.get(slug=slug)
            # print("check",article_obj.get("user"))
        except Articles.DoesNotExist:
            raise Http404 
        except Articles.MultipleObjectsReturned:
            article_obj = Articles.objects.filter(slug=slug).first()
        except:
            raise Http404
    context ={
        "object":article_obj, 
        }
    print("context",context)
    return render(request, "articles/detail.html",context=context)