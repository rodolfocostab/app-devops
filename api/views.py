from api.models import Post
from tastypie.resources import ModelResource

class PostResource(ModelResource):
    class Meta:
        resource_name = 'post'
        queryset = Post.objects.all()
