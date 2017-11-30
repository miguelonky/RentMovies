from rest_framework import serializers
from . models import movies
from . models import rentmovie

class moviesSerializer(serializers.ModelSerializer):
    class Meta :
        model = movies
     #   fields = ('Name','Descripction','QuantityAvaliable','Price')
        fields = '__all__'

class rentmoviesSerializer(serializers.ModelSerializer):
    class Meta :
        model = rentmovie
        movie = moviesSerializer()
     #   fields = ('Name','Descripction','QuantityAvaliable','Price','Image')
        fields = '__all__'


