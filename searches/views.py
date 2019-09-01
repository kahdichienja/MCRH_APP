from django.shortcuts import render
from django.http import JsonResponse
from Mcrh_Birth_Record.models import ChildModelManager, ChildQuerySet, Child
from .models import SearchQuery

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication

import datetime
import calendar

def root_url(request):
    return render(request, 'index_home_view.html')
class MegaChartData(APIView):

    authentication_classes = []

    def get(self, request, format=None):
        # query = request.GET.get('q', None)
        query = 2019

        # data = {}
        months_choices = []
        yearitems = []
        # if query is not None:

        # months_choices = []
        for i in range(1, 13):
            months_choices.append((calendar.month_abbr[i]))
        # child_list = Child.objects.filter(sex__icontains = query)
        # child_list = Child.objects.filter(created_at__year=query, dob__icontains='Aug').count()
        # Year search
        Jan = Child.objects.filter(created_at__year=query, dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(created_at__year=query, dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(created_at__year=query, dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(created_at__year=query, dob__icontains = 'Apr').count()
        May = Child.objects.filter(created_at__year=query, dob__icontains = 'May').count()
        Jun = Child.objects.filter(created_at__year=query, dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(created_at__year=query, dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(created_at__year=query, dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(created_at__year=query, dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(created_at__year=query, dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(created_at__year=query, dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(created_at__year=query, dob__icontains = 'Dec').count()
        # end year search
        defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
        # quota search
        quota_defaultitems = defaultitems[:3]
        quota_labels = months_choices[:3]
        # end quota search
        # semi anual search
        semi_defaultitems = defaultitems[:6]
        semi_labels = months_choices[:6]
        # end anul search
        # Sex Male Analysis
        Jan = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Apr').count()
        May = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'May').count()
        Jun = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(created_at__year=query, sex__icontains = 'Male', dob__icontains = 'Dec').count()
        # end sex male search
        male_defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
        # quota search
        quota_male_defaultitems = male_defaultitems[:3]
        quota_male_labels = months_choices[:3]
        # end quota search
        # semi anual search
        semi_male_defaultitems = male_defaultitems[:6]
        semi_male_labels = months_choices[:6]
        # end anul search
        # Sex Female Analysis
        Jan = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Apr').count()
        May = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'May').count()
        Jun = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(created_at__year=query, sex__icontains = 'Female', dob__icontains = 'Dec').count()
        # end sex Female search   
    
        female_defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]

        # quota search
        quota_female_defaultitems = female_defaultitems[:3]
        quota_female_labels = months_choices[:3]
        # end quota search
        # semi anual search
        semi_female_defaultitems = female_defaultitems[:6]
        semi_female_labels = months_choices[:6]
        # end anul search
        # start type of birth
        # single birth
        Jan = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Apr').count()
        May = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'May').count()
        Jun = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Single', dob__icontains = 'Dec').count()
                
        single_defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]

        # quota search
        quota_single_defaultitems = single_defaultitems[:3]
        quota_single_labels = months_choices[:3]
        # end quota search
        # semi anual search
        semi_single_defaultitems = single_defaultitems[:6]
        semi_single_labels = months_choices[:6]
        # end anul search
        # end single birth.
        # Twin
        Jan = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Jan').count()
        Feb = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Feb').count()
        Mar = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Mar').count()
        Apr = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Apr').count()
        May = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'May').count()
        Jun = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Jun').count()
        Jul = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Jul').count()
        Aug = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Aug').count()
        Sep = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Sep').count()
        Oct = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Oct').count()
        Nov = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Nov').count()
        Dec = Child.objects.filter(created_at__year=query, type_of_birth__icontains = 'Twin', dob__icontains = 'Dec').count()
                
        twin_defaultitems = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]

        # quota search
        quota_twin_defaultitems = twin_defaultitems[:3]
        quota_twin_labels = months_choices[:3]
        # end quota search
        # semi anual search
        semi_twin_defaultitems = twin_defaultitems[:6]
        semi_twin_labels = months_choices[:6]
        # end twin
        # end type of birth



        data = {
            "labels": months_choices,
            "default": defaultitems,
            "quota_labels": months_choices[:3],
            "quota_defaultitems": defaultitems[:3],
            "semi_labels": months_choices[:6],
            "semi_defaultitems": defaultitems[:6],
            # male_analysis
            "male_defaultitems": male_defaultitems,
            "quota_male_labels": quota_male_labels,
            "quota_male_defaultitems": quota_male_defaultitems,
            "semi_male_defaultitems": semi_male_defaultitems,
            "semi_male_labels": semi_male_labels,
            # female_analysis
            "female_defaultitems": female_defaultitems,
            "quota_female_labels": quota_female_labels,
            "quota_female_defaultitems": quota_female_defaultitems,
            "semi_female_defaultitems": semi_female_defaultitems,
            "semi_female_labels": semi_female_labels,
            # single birth
            "single_defaultitems": single_defaultitems,
            "quota_single_labels": quota_single_labels,
            "quota_single_defaultitems": quota_single_defaultitems,
            "semi_single_defaultitems": semi_single_defaultitems,
            "semi_single_labels": semi_single_labels,
            # twin birth
            "twin_defaultitems": twin_defaultitems,
            "quota_twin_labels": quota_twin_labels,
            "quota_twin_defaultitems": quota_twin_defaultitems,
            "semi_twin_defaultitems": semi_twin_defaultitems,
            "semi_twin_labels": semi_twin_labels,


        }
        return Response(data)


def search_view(request):
    query = request.GET.get('q', None)

    context = {
        'query': query,
    }

    if query is not None:
        months_choices = []
        for i in range(1, 13):
            months_choices.append((calendar.month_abbr[i]))
        child_list = Child.objects.filter(sex__icontains = query)
        # permonth for 12 months

        context['child_list'] = child_list
    return render(request, 'searches/view.html', context)
