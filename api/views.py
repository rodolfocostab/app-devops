from api.models import Post
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

class PostResource(ModelResource):
    class Meta:
        resource_name = 'post'
        queryset = Post.objects.all()
        authorization = Authorization()
