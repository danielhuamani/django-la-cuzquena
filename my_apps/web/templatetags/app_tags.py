from django import template

register = template.Library()


# tags para obtener los grades para cada category #
@register.filter(name='counter_cero')
def counter_cero(num):
    num_cero = format(num, '02d')

    return num_cero
