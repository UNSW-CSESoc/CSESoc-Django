from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('helpers/templatetags/generate_pagenumbers.html')
def generate_pagenumbers(paginator, page_obj, extra_pages):
    context = {
        'paginator': paginator,
        'page_obj': page_obj,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'current': page_obj.number,
        'range': [],
    }
    # we add the first and last pages, as well as pages from n - extra to n + extra; False symbolises a redacted page range
    for page in paginator.page_range:
        if (page == paginator.page_range[0]) or (page == paginator.page_range[-1]) or ((page >= page_obj.number - extra_pages) and (page <= page_obj.number + extra_pages)):
            context['range'].append(page)
        elif context['range'][-1] != False:
            context['range'].append(False)
    return context

