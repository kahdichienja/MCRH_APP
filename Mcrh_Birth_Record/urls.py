from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .import views

urlpatterns = [
    path('', views.birth_record_home, name = 'birth_record_home'),
    path('add/', views.birth_record_add, name = 'birth_record_add'),
    path('detailed/<serial_number_b1>', views.birth_record_detailed, name = 'birth_record_detailed'),
    path('searchlisttest/', views.search_by_dob, name = 'search_by_dob'),
    path('searchlist/', views.search_by_id, name = 'search_by_id'),
    path('AnalysisBirth/', views.record_data_analysis, name="record_data_analysis"),
]