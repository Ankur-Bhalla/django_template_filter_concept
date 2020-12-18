# Create our own custom template filter

from django import template

register = template.Library()


@register.filter
def cutout(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')   # here replace "wor" with spaces from "hello world"

# register.filter("cutout", cutout)
