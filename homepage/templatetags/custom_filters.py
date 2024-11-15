from django import template

register = template.Library()

# Custom filter for subtraction
@register.filter
def subtract(value, arg):
    try:
        return value - arg
    except (TypeError, ValueError):
        return value
