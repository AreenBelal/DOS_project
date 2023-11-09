from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from fe_app.catalog_service import CatalogService


# Create your views here.


class InfoController(ViewSet):
    def list(self, request):
        books = CatalogService.get_books()
        if books is not None:
            return JsonResponse(data={'data': books['data']}, status=200)
        else:
            return JsonResponse(data={'status': 'no books with this name'}, status=200)

    def retrieve(self, request, pk):
        book = CatalogService.get_book_by_id(pk)
        if book is not None:
            return JsonResponse(data={'data': book['data']}, status=200)
        else:
            return JsonResponse(data={'status': 'no books with this name'}, status=200)


class SearchController(ViewSet):
    def retrieve(self, request, pk):
        books = CatalogService.search_books(pk)
        if books is not None:
            return JsonResponse(data={'data': books['data']}, status=200)
        else:
            return JsonResponse(data={'status': 'no books with this name'}, status=200)


class PurchaseController(ViewSet):
    def update(self, request, pk):
        status = CatalogService.purchase(pk, request.data.get('item_number'))
        if status is not None:
            return JsonResponse(data={'data': 'Purchase done'}, status=200)
        else:
            return JsonResponse(data={'data': 'Not allowed to purchase'}, status=200)

