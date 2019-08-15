from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType

from .models import Parent, Child
from .forms import ParentForm, ChildForm, SearchForm
# Create your views here.

@staff_member_required
def birth_record_home(request):
    children = Child.objects.all().order_by('-id')
    paginator = Paginator(children, 5)
    page = request.GET.get('page')
    children = paginator.get_page(page)


    return render(request, "list_view.html", { 'children': children })
@staff_member_required
def birth_record_add(request):

    form = ParentForm(request.POST or None)
    form2 = ChildForm(request.POST or None)

    if form2.is_valid() & form.is_valid():
        print(form2.cleaned_data)
        print(form.cleaned_data)

        obj = Parent.objects.create(**form.cleaned_data)
        obj2 = obj.child_set.create(**form2.cleaned_data)
        return redirect('/Record/add/')
    return render(request, "add_view.html", {'form': form, 'form2': form2})

def birth_record_detailed(request, serial_number_b1):
    child = Child.objects.get(serial_number_b1 = serial_number_b1)

    context = {
        'child': child,       
    }
    return render(request, "detailed_view.html", context)

@staff_member_required
def search_by_dob(request):
    searchForm = SearchForm(request.POST or None)
    if searchForm.is_valid():
        id_number = searchForm.cleaned_data.get('id_number')
        print(id_number);
        # lookup = (Q(dob__icontains = id_number) | Q(parent__notified_id__icontains = id_number))
        children_searches = Child.objects.filter(dob__icontains = id_number)
        count_children_searches = Child.objects.filter(dob__icontains = id_number).count()
        paginator = Paginator(children_searches, 5)
        page = request.GET.get('page')
        children_searches = paginator.get_page(page)
    context={
        'children_searches': children_searches,
        'count_children_searches': count_children_searches,
        'id_number': id_number,
    }
    return render(request, "search_test_view.html", context)

@staff_member_required
def search_by_id(request):
    searchForm = SearchForm(request.POST or None)
    if searchForm.is_valid():
        id_number = searchForm.cleaned_data.get('id_number')
        count_children_searches = Child.objects.filter(dob__icontains = id_number).count()
        children_searches = Child.objects.filter(parent__notified_id=id_number)
        count_children_searches = Child.objects.filter(parent__notified_id=id_number).count()
        paginator = Paginator(children_searches, 5)
        page = request.GET.get('page')
        children_searches = paginator.get_page(page)
    context={
        'children_searches': children_searches,
        'count_children_searches': count_children_searches,
        'id_number': id_number,
    }
    return render(request, "search_test_view.html", context)