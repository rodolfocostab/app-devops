from app.models import Inicio
from app.models import Fim
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

class InicioResource(ModelResource):
    class Meta:
        resource_name = 'inicio'
        queryset = Inicio.objects.all()
        authorization = Authorization()

class FimResource(ModelResource):
    class Meta:
        resource_name = 'fim'
        queryset = Fim.objects.all()
        authorization = Authorization()
