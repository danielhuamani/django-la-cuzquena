from .models import Configuracion


def processors_site(request):
    configuracion = Configuracion.objects.all()
    site = ''
    if configuracion:
        site = configuracion[0]
    dic = {
        'site': site
    }
    return dic
