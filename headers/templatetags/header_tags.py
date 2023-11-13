from django import template

from ..models import Header

register = template.Library()


@register.simple_tag()
def get_active_header():
    return Header.objects.filter(is_active=True).first()


@register.inclusion_tag("headers/header_item.html", takes_context=True)
def get_header_items(context, parent, calling_page=None):
    header_items = parent.header_items.all()
    return {
        "calling_page": calling_page,
        "header_items": header_items,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag("headers/header_subitem.html", takes_context=True)
def get_header_sub_items(context, parent, calling_page=None):
    return {
        "parent": parent,
        "header_subitems": parent.header_subitems.all(),
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }


@register.inclusion_tag("headers/header_item.html")
def get_header_preview(context, object, calling_page=None):
    header_items = object.header_items.all()
    return {
        "calling_page": calling_page,
        "header_items": header_items,
        # required by the pageurl tag that we want to use within this template
        "request": context["request"],
    }
    
@register.simple_tag()
def get_header_link(context, request, link):
    url = request.build_absolute_uri()
    if link.startswith("/#"):
        return f"{url}{link[1:]}"
    return link
