from django import template
register = template.Library()

@register.filter
def listIndex(List, i):
	return List[int(i)]
	
@register.filter
def convertString(i):
	return str(i)
	
@register.filter
def dbTableData(List, id):
	if id <= 0:
		return None
	else:	
		return List[id - 1]

@register.filter
def multip(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''

@register.filter
def sub(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''