from django.contrib import admin
from .models import Child,Parent
# Register your models here.

class ChildModelAdmin(admin.ModelAdmin):
    list_display = ["serial_number_b1","child_fname","child_mname","child_lname","dob"]
    list_display_links = ["serial_number_b1"]
    list_filter = ["serial_number_b1", "dob"]
    search_fields = ["serial_number_b1","dob"]
    class Meta:
        model = Child

class ParentModelAdmin(admin.ModelAdmin):
    list_display = ["mother_fname","mother_mname","mother_lname","notified_id"]
    list_display_links = ["notified_id"]
    list_filter = ["notified_id", "notified_date"]
    search_fields = ["notified_id","notified_date"]
    class Meta:
        model = Parent        
admin.site.register(Child, ChildModelAdmin)
admin.site.register(Parent, ParentModelAdmin)