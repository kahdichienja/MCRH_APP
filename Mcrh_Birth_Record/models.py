from django.db import models
from datetime import datetime
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class ChildQuerySet(models.Manager):
    def search(self, query):
        return self.filter(dob__iexact = query)

        
class ChildModelManager(models.Manager):

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Parent(models.Model):
    mother_fname = models.CharField(max_length = 100)
    mother_mname = models.CharField(max_length = 100)
    mother_lname = models.CharField(max_length = 100)
    notified_name = models.CharField(max_length=50)
    notified_id = models.CharField(max_length = 100)
    notified_date = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.notified_id
        

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type
class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    # child = models.ForeignKey("Mcrh_Birth_Record.Parent", null=True, verbose_name="notified_id", on_delete=models.SET_NULL)
    serial_number_b1 = models.CharField(max_length = 100)
    child_fname = models.CharField(max_length = 100)
    child_mname = models.CharField(max_length = 100)
    child_lname = models.CharField(max_length=50)
    dob = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 100)
    type_of_birth = models.CharField(max_length = 100)
    other_type_of_birth = models.CharField(max_length = 191, null = True, blank = True)
    nature_of_birth = models.CharField(max_length = 100)
    place_of_birth = models.CharField(max_length = 100)
    place_of_birth_sub_county = models.CharField(max_length=50)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.serial_number_b1
        

    def clean_dob(self, *args, **kwargs):
        dob = self.cleaned_data.get('dob')
        if dob > datetime.now:
            raise forms.ValidationError("Date cannot be more than today")
        return dob
          
    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

# p2 = Parent(mother_fname='Jane', mother_mname='Smith', mother_lname='Teresa',notified_name='Teresa', notified_id='344573943', notified_date='Aug 26, 2019')
# c = p2.child_set.create(serial_number_b1='422243212', child_fname='ascmaskj', child_mname='jxak', child_lname='djlknjsd', dob='Jan 21, 2019', sex='Male', type_of_birth='Single', other_type_of_birth='',nature_of_birth='Born Dead', place_of_birth='MCRH', place_of_birth_sub_county='Suna East', created_at=datetime.now())