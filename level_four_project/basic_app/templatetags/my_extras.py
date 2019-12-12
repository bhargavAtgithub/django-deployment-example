from django import template


register = template.Library()

@register.filter(name = 'snipe')
def snipe(value, arg):
    """This cuts out all the values from the string"""
    return value.replace(arg,'Hello')

