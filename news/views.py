from django.shortcuts import render, HttpResponse
from news.models import categories, articles
from news.form import RegisterationForm

# Create your views here.
def main(request):
    context={
        # 'categories':categories.objects.all(),        //since we are using context processor we need not specify the categories everytime, by default the context processor will pass to all the HTML file present inside the project.
        'articles':articles.objects.all().filter(status="Published", is_trending=True).order_by("updated_at"),
        'articles_not_trending':articles.objects.all().filter(status="Published", is_trending=False).order_by("updated_at")

    }

    return render(request,"main.html",context)

def post_by_category(request, cname):
    category=categories.objects.get(category=cname)
    context={
        'category':cname, #for displaying purpose
        'articles':articles.objects.all().filter(status="Published", category=category.id)
    }
    return render(request, 'post_by_category.html', context)


def single_article(request, slug):
    context={
        'article':articles.objects.get(slug=slug)
    }
    return render(request, "article.html",context)

def register(request):
    if request.method=='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('registeration done...')
    else:
        form=RegisterationForm()
    context={
        'form':form
    }
    return render(request, "register.html", context)