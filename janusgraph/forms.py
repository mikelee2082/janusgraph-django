from django import forms
from .models import RelationshipTypeModel

class NodeForm(forms.Form):
    entityName = forms.CharField(label='EntityName', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

class RelationshipForm(forms.Form):
    entityA = forms.CharField(label='EntityA')
    relationship = forms.ChoiceField(choices=set([str(s) for s in RelationshipTypeModel.objects.all()]),label='Relationship')
    entityB = forms.CharField(label='EntityB')

class NodeInfoForm(forms.Form):
    entityName = forms.CharField(label='Entity Name')
