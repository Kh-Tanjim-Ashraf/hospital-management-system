from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from billing.serializers import BillingSerializer
from billing.models import Billing as BillingModel



class Billing(APIView):

    def get(self, request):
        bills = BillingModel.objects.filter(is_deleted=False)
        serializer = BillingSerializer(instance=bills, many=True)
        
        data = {
            'message': 'Bill list',
            'data': serializer.data
        }
        
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BillingSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'message': 'Bill list',
                'data': serializer.data
            }

            return Response(data=data, status=status.HTTP_201_CREATED)



class BillingDetail(APIView):

    def get(self, request, id):
        bill = BillingModel.objects.get(pk=id)
        serializer = BillingSerializer(instance=bill)

        data = {
            'message': 'Billing information',
            'data': serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, id):
        bill = BillingModel.objects.get(pk=id)
        serializer = BillingSerializer(instance=bill, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
            data = {
                'message': 'Billing information updated successfully',
                'data': serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        bill = BillingModel.objects.get(pk=id)
        serializer = BillingSerializer(instance=bill, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
            data = {
                'message': 'Billing information updated successfully',
                'data': serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        bill = BillingModel.objects.get(pk=id)
        bill.is_deleted = True
        bill.save()

        return Response(status=status.HTTP_204_NO_CONTENT)