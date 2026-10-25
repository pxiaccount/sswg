from rest_framework import viewsets

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Full CRUD: list, create, retrieve, update, partial_update, destroy."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']

    # Uncomment to require auth:
    # permission_classes = [IsAuthenticated]
    #
    # Scope objects to the owner:
    # def get_queryset(self):
    #     return Item.objects.filter(owner=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
