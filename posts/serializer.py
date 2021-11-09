# import serializer from rest_framework
from rest_framework import serializers
  
# import model from models.py
from .models import PostsModel
  
# Create a model serializer 
class PostsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = PostsModel
        fields = ('url', 'id', 'title', 'content')