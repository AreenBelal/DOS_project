from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from catalog_app.models import Book
from catalog_app.serializers import BookSerializer


# Create your views here.

class Checker(ViewSet):
    def list(self, request):
        return JsonResponse({'status': 'Success'}, status=200)


class BookController(ViewSet):

    def list(self, request):
        books = Book.objects.using('default').all()
        return JsonResponse({'data': BookSerializer(books, many=True).data})

    def retrieve(self, request, pk):
        book = Book.objects.filter(id=pk).using('default').first()
        return JsonResponse({'data': BookSerializer(book, many=False).data})

    def update(self, request, pk):
        for db in ['default', 'replica']:

            book = Book.objects.using(db).filter(id=pk).first()
            if not book:
                return JsonResponse({'data': 'Resource Not Found'}, status=422)
            book.count = int(request.data.get('item_number'))
            book.cost = int(request.data.get('item_cost'))
            book.save()
        return JsonResponse({'data': 'Purchase Done'})


class SearchController(ViewSet):
    def retrieve(self, request, pk):
        item_name = pk
        books = Book.objects.using('default').filter(catalog__name__contains=item_name).all()
        return JsonResponse({'data': BookSerializer(books, many=True).data})
