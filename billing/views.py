from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from billing.serializers import BillingSerializer
from billing.models import Billing as BillingModel



class Billing(APIView):

    def get(self, request):
        bills = BillingModel.objects.all()
        serializer = BillingSerializer(instance=bills, many=True)
        
        data = {
            'message': 'Bill list',
            'data': serializer.data
        }
        
        return Response(data=data, status=status.HTTP_200_OK)