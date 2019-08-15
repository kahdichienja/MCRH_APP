from django import forms
from .models import Child, Parent


class SearchForm(forms.Form):
    id_number = forms.CharField(max_length=20, required=False)

# class ChildForm(forms.ModelForm):
#     class Meta:
#         model = Child
#         fields = ('serial_number_b1', 'child_fname', 'child_mname', 'child_lname', 'dob', 'sex', 'type_of_birth','other_type_of_birth','nature_of_birth','place_of_birth','place_of_birth_sub_county')
class ChildForm(forms.Form):
    serial_number_b1 = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'validate', 
                'id': 'icon_prefixb1', 
                'required': "true",
                'name': 'serial_number_b1'
            }
        )
    )
    child_fname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'validate', 
                'id': 'icon_prefixcf', 
                'required': "true",
                'name': 'child_fname'
            }
        )
    )
    child_mname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefix2',
                'class': 'validate', 
                'required': "true",
                'name': 'child_mname'
            }
        )
    )
    child_lname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefix3',
                'class': 'validate', 
                'required': "true",
                'name': 'child_lname'
            }
        )
    )
    dob = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class': 'datepicker', 
                'id': 'icon_prefixdate', 
                'required': "true",
                'name': 'dob'
            }
        )
    )
    sex = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'type': 'radio',
                'class': 'validate with-gap',
                'required': "true",
                'name': 'sex'
            }
        )
    )
    type_of_birth = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'type': 'radio',
                'class': 'validate with-gap', 
                'required': "true",
                'name': 'type_of_birth'
            }
        )
    )
    other_type_of_birth = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefixother',
                'class': '', 
                'placeholder': 'Description...',
                'name': 'other_type_of_birth'
            }
        )
    )
    nature_of_birth = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'type': 'radio',
                'class': 'validate with-gap', 
                'required': "true",
                'name': 'nature_of_birth'
            }
        )
    )
    place_of_birth = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'placeofbirth',
                'class': 'validate', 
                'required': "true",
                'name': 'place_of_birth'
            }
        )
    )
    place_of_birth_sub_county = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'sub-county',
                'class': 'validate', 
                'required': "true",
                'name': 'place_of_birth_sub_county'
            }
        )
    )
    class Meta:
        model = Child
        fields = ('sex', 'type_of_birth','nature_of_birth')


# class ParentForm(forms.ModelForm):
#     class Meta:
#         model = Parent
#         fields = ('mother_fname', 'mother_mname', 'mother_lname', 'notified_name', 'notified_id', 'notified_date')
class ParentForm(forms.Form):
    mother_fname = forms.CharField(widget = forms.TextInput(attrs={'id':'icon_prefixf','class': 'validate','required': "true",'name': 'mother_fname'}))
    mother_mname = forms.CharField(widget = forms.TextInput(attrs={'id': 'icon_prefixf2','class': 'validate','required': "true", 'name': 'mother_mname'}))
    mother_lname = forms.CharField(widget = forms.TextInput(attrs={'id':'icon_prefixf3','class': 'validate','required': "true", 'name': 'mother_lname'}))
    notified_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefixfn',
                'class': 'validate',
                'required': "true",
                'name': 'notified_name'
            }
        )
    )
    notified_id = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefixf2id',
                'class': 'validate',
                'required': "true",
                'name': 'notified_id'
            }
        )
    )
    notified_date = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'icon_prefixdate2',
                'class': 'datepicker',
                'required': "true",
                'name': 'notified_date'
            }
        )
    )
    class Meta:
        model = Parent
        # fields = ('photo')