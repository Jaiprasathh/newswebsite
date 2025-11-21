from news.models import categories

def get_categories(request):
    d={
        'categories':categories.objects.all()
    }
    return d


#since we are using context processor we need not specify the categories everytime, by default the context processor will pass the categories to all the HTML file present inside the project.