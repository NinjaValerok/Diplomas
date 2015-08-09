from django import template

register = template.Library()

@register.filter(name='get_range')
def get_range(value):
    return range(value)

@register.filter(name='is_new_row')
def is_new_row(value,args=''):
    if args is None or value == 0:
        return False
    arg_list = [arg.strip() for arg in args.split(',')]
    return (value % int(arg_list[0])) == 0
