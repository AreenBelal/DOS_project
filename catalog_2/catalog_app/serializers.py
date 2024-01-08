from rest_framework import serializers

from catalog_app.models import Book, Catalog


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'cost', 'count', 'name', 'catalog']
