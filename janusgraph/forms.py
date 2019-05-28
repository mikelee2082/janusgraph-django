from django import forms

class NodeForm(forms.Form):
    entityName = forms.CharField(label='EntityName', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

class RelationshipForm(forms.Form):
    entityA = forms.CharField(label='EntityA')
    relationship = forms.CharField(label='Relationship')
    entityB = forms.CharField(label='EntityB')
