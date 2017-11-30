from django.utils.six import BytesIO
from django.shortcuts        import render
from django.http             import HttpResponse
from django.shortcuts        import get_object_or_404
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework          import status
from . models                import movies
from . models                import rentmovie
from . Serializers           import moviesSerializer
from . Serializers           import rentmoviesSerializer

# Create your views here.
def index(request):
   return  render(request,'Index.html')

class MoviesList(APIView):

  def get(self , request):

    # if  self.kwargs['rented']:
    #   is_rented = self.kwargs['rented']
    #   _movies = movies.object.filter(movie__)
    moviesl    = movies.objects.all()
    serializer = moviesSerializer(moviesl , many=True)
    return Response(serializer.data)

  def post(self):
    return Response('!')

class RentMoviesList(APIView):

  def put(self):
    pass

  def get(self , request):
    rentmoviesl    = rentmovie.objects.all()
    serializer     = rentmoviesSerializer(rentmoviesl , many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = rentmoviesSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnMovie(APIView):

  def get(self, request):
    all_rented_movies  = rentmovie.objects.all()
    # rented_movies = movies.objects.filter(Id__in=all_rented_movies)
    serialized_movies = rentmoviesSerializer(all_rented_movies, many=True)

    return Response(serialized_movies.data)