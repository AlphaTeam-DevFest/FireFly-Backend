# peaceApp/urls.py
from django.urls import path
from .views import CharitiesRetrieveUpdateDestroyViewSet, CharitiesViewSet

urlpatterns = [
    path('charities/', CharitiesViewSet.as_view({'get': 'list', 'post': 'create'}), name='charities-list-create'),
    path('charities/<int:pk>/', CharitiesRetrieveUpdateDestroyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='charities-detail'),
]
