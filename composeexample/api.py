from tastypie.resources import ModelResource
from webserver.rest_app.models import Post
from tastypie.authorization import Authorization
from django.contrib.auth.models import Name
from tastypie import fields

class NameResource(ModelResource):
    class Meta:
        queryset = Name.objects.all()
        resource_name = 'name'
        authorization = Authorization()


class PostResource(ModelResource):
    user = fields.ForeignKey(NameResource, 'name')

    class Meta:
        resource_name = 'post'
        queryset = Post.objects.all()
        authorization = Authorization()
