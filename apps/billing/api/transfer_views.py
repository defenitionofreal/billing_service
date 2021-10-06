# core imports
from ..serializers import TransferSerializer
from ..models import Transfer
# rest imports
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (AllowAny,)
