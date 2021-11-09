from rest_framework import viewsets
  
# import local data
from .serializer import PostsSerializer
from .models import PostsModel
  
# create a viewset
class PostsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = PostsModel.objects.all()
      
    # specify serializer to be used
    serializer_class = PostsSerializer
