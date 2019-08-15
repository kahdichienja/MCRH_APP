from django.shortcuts import render
from Mcrh_Birth_Record.models import ChildModelManager, ChildQuerySet, Child
from .models import SearchQuery
# Create your views here.


def search_view(request):

    query = request.GET.get('q', None)
    child = None
    if request.user.is_authenticated:
        child = child

    context = {
        'query': query,
    }

    if query is not None:
        SearchQuery.objects.create(child = child, query = query)
        child_list = Child.objects.search(query = query)  
        context['child_list'] = child_list
    return render(request, 'searches/view.html', context)
