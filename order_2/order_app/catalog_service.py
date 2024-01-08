import json

import requests


class CatalogServer:
    @staticmethod
    def get_book_data(item_id):
        api = "http://catalogweb2:8004/books/{id}/".format(id=item_id)
        response = requests.get(api)
        return CatalogServer.handle_response(response)

    @staticmethod
    def handle_response(response):
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error happened in catalog server with error code {response.status_code}, message: {response.text}")
            return None

    @staticmethod
    def purchase_book(item_id, item_number, item_cost):
        api = "http://catalogweb2:8004/books/{id}/".format(id=item_id)
        response = requests.put(api, data={'item_number': item_number, 'item_cost': item_cost})
        return CatalogServer.handle_response(response)
