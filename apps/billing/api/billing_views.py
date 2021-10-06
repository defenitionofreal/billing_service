# core imports
from ..serializers import BillingSerializer
from ..models import Billing
# rest imports
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # просто чтобы не париться c jwt авторизацией


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        """
        Переделываю ответ данного метода только
        на идентификатор счета, которым является
        поле id.
        """
        response = super(BillingViewSet, self).create(request, *args, **kwargs)
        response.data = {'id': f'{response.data["id"]}'}
        return response

    @action(detail=False, methods=['get'],
            url_name='get_balance')
    def get_balance(self, request):
        """
        Зарпос баланса счета по входным параметрам
        идентификатора счета, которым является поле
        id.
        
        К основному url добавить ?id=1
        """
        try:
            x = str(request.query_params.get('id'))
            bill = Billing.objects.get(id=x)
            serializer = BillingSerializer(bill)
            return Response({"total": serializer.data["billing"]})
        except Exception as e:
            return Response({"error": f'{e}'})
