from django import template

register = template.Library()


# tags para obtener los grades para cada category #
@register.filter(name='counter_cero')
def counter_cero(num):
    num_cero = format(num, '02d')

    return num_cero


@register.filter(name='tags_telefono_header')
def tags_telefono_header(list_telefono):
    telefonos = list_telefono.split("|")

    return telefonos[0]


@register.filter(name='tags_telefono_footer')
def tags_telefono_footer(list_telefono):
    telefonos = list_telefono.split("|")

    return telefonos
