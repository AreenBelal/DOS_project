import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from order_app.catalog_service import CatalogServer


# Create your views here.

class PurchaseController(ViewSet):

    def update(self, request, pk):
        book = CatalogServer.get_book_data(pk)
        if book['data']['count'] >= int(request.data.get('item_number')) and book['data']['count'] != 0:
            CatalogServer.purchase_book(
                int(pk),
                int(book['data']['count']) - int(request.data.get('item_number')),
                int(book['data']['cost'])
            )
            return JsonResponse(data={'data': 'successful'}, status=200)
        else:
            return JsonResponse({'data': 'Not Allowed to purchase more than existing'}, status=403)
