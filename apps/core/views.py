from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tender.models import Item 
from apps.tender.serializers import ItemSerializer

@api_view(['POST'])
def tenderCreate(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def tenderList(request):
    tenders = Item.objects.all()
    serializer = ItemSerializer(tenders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tenderDetail(request, pk):
    tender = Item.objects.get(pk=pk)
    serializer = ItemSerializer(tender, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def tenderUpdate(request, pk):
    tender = Item.objects.get(pk=pk)
    serializer = ItemSerializer(instance=tender, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def tenderDelete(request, pk):
    tender = Item.objects.get(pk=pk)

    # TODO
    # -> on_delete, set following status : is_active=False, is_published=False, deleted_by=request.user etc.
    tender.delete()

    return Response(f"Tender NO: {tender.tender_no} deleted successfully!.")



