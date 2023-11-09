import json

import requests

from fe_app.constants import Services


class CatalogService:
    @staticmethod
    def get_books():
        api = Services.CATALOG_SERVICE + "/books/"
        response = requests.get(api)
        return CatalogService.handle_response(response)

    @staticmethod
    def get_book_by_id(pk):
        api = Services.CATALOG_SERVICE + f"/books/{pk}"
        response = requests.get(api)
        return CatalogService.handle_response(response)

    @staticmethod
    def search_books(term):
        api = Services.CATALOG_SERVICE + f"/search/{term}"
        response = requests.get(api)
        return CatalogService.handle_response(response)

    @staticmethod
    def purchase(item_id, item_number):
        api = Services.ORDER_SERVICE + f"/purchase/{item_id}/"
        response = requests.put(api, data={'item_number': item_number})
        return CatalogService.handle_response(response)

    @staticmethod
    def handle_response(response):
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error happened in catalog server with error code {response.status_code}, message: {response.text}")
            return None
