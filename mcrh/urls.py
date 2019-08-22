"""mcrh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from searches.views import search_view, root_url, MegaChartData #mega_search

from DataAnalysis.views import ChartData, get_data

urlpatterns = [
    path('', root_url),
    path('admin/', admin.site.urls),
    path('api/data_analysis/', ChartData.as_view(), name='ChartData'),
    path('api/data/', get_data, name="get_data"),
    path('Record/', include('Mcrh_Birth_Record.urls')),
    path('search/', search_view),
    # path('mega_search/', mega_search),
    path('mega_search/', MegaChartData.as_view(), name="MegaChartData"),
]
