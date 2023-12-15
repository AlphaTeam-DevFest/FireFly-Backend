from rest_framework.viewsets import ModelViewSet
from .models import Charities
from .serializers import CharitiesSerializer

class CharitiesViewSet(ModelViewSet):
    queryset = Charities.objects.all()
    serializer_class = CharitiesSerializer
   

class CharitiesRetrieveUpdateDestroyViewSet(ModelViewSet):
    queryset = Charities.objects.all()
    serializer_class = CharitiesSerializer
