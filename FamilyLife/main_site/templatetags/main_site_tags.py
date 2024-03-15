

from django import template
import main_site.views as views

register = template.Library()

@register.simple_tag()
def get_menu():
    return views.menu

@register.simple_tag()
def get_category():
    return views.categories