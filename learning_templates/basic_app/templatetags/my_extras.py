from django import template

register = template.Library()

@register.filter(name='mycut')
def mycut(value,arg):
    """
    This cuts out all valur of "aRGS" from the string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
