from .models import *

def category_list(request):
    return {
        'category_list':Category.objects.all()
    }