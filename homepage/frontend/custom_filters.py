from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    """Subtract the discount from the price."""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return value  # Return the value if there is an error
