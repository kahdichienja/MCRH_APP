from django.shortcuts import render
from django.http import JsonResponse
from Mcrh_Birth_Record.models import Child, Parent
from .forms import SearchForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
import datetime
import calendar

def get_data(request, *args, **kwargs):

    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):

    authentication_classes = []

    def get(self, request, format=None):
        months_choices = []
        year = datetime.datetime.now()
        for i in range(1, 13):
            months_choices.append((calendar.month_abbr[i]))
        children_count = Child.objects.all().count()
        parent_count = Parent.objects.all().count()
        yester_count = Child.objects.filter(created_at__month = year.month)
        ##############
        Jan = Child.objects.filter(dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(dob__icontains = 'Apr').count()
        May = Child.objects.filter(dob__icontains = 'May').count()
        Jun = Child.objects.filter(dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(dob__icontains = 'Dec').count()
        #############
                            
        
        defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
        
        data = {
            # 'Year': year,
            # 'This Month Records': yester_count,
            # 'labels': labels,
            'labels': months_choices,#x-axis labels
            'default': defaultitems,
            # 'No. Of Parent': parent_count,
            # 'No. Of Children': children_count,
            # 'months_choices': months_choices,
        }
        return Response(data)
