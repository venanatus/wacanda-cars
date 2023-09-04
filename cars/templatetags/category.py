from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('categories.html')
def categories():
    category_list = Category.objects.all()
    return {'category_list': category_list}
