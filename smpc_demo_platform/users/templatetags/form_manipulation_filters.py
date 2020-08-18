from django.conf import settings
from django import template

# https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

