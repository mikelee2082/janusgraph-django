from django.db import models

class RelationshipTypeModel(models.Model):
    REL_TYPES = [
            ('parent', 'parent'),
            ('child', 'child'),
            ('married', 'married'),
            ('sibling', 'sibling'),
            ('employer', 'employer'),
            ('employee', 'employee'),
            ('associate', 'associate')
    ]
    name = models.CharField(choices=REL_TYPES, max_length=50)
    reverse = models.CharField(choices=REL_TYPES, max_length=50)

    def __str__(self):
        return self.name
