from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return "link-dark"


@register.simple_tag
def status_label(status):
    if status ==  'WAITING':
        return "bg-info"
    elif  status ==  'APPROVED' :
        return "bg-primary"
    elif status ==  'IN PROGRESS' :
        return "bg-warning"
    elif status ==  'BLOCKED' :
        return "bg-danger"
    elif status ==  'DONE' :
        return "bg-success"
    else:
        return "bg-success"
        