from django import  template
register = template.Library()

@register.filter(name='get')
def get(d, k):
    return d.__dict__.get(k,None)