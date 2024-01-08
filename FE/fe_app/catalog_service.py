import json

import requests

from fe_app.cache_service import CacheService


class ServerPicker:
    servers = []

    def pick_server(self):
        server = self.servers[0]
        self.servers.reverse()
        return server


class CatalogServicePicker(ServerPicker):
    servers = ["http://catalogweb:8003", "http://catalogweb2:8004"]


class OrderServicePicker(ServerPicker):
    servers = ["http://orderweb:8001", "http://orderweb2:8005"]


class CatalogService:
    def __init__(self):
        self.cache_service = CacheService()
    def get_books(self):
        api = CatalogServicePicker().pick_server() + "/books/"
        if not self.cache_service.get_cache(api):
            response = requests.get(api)
            response_content = self.handle_response(response)
            self.cache_service.set_cache(api, response_content)
            return response_content
        return self.cache_service.get_cache(api)

    def get_book_by_id(self, pk):
        api = CatalogServicePicker().pick_server() + f"/books/{pk}"
        if not self.cache_service.get_cache(api):
            response = requests.get(api)
            response_content = self.handle_response(response)
            self.cache_service.set_cache(api, response_content)
            return response_content
        return self.cache_service.get_cache(api)

    def search_books(self, term):
        api = CatalogServicePicker().pick_server() + f"/search/{term}"
        if not self.cache_service.get_cache(api):
            response = requests.get(api)
            response_content = self.handle_response(response)
            self.cache_service.set_cache(api, response_content)
            return response_content
        return self.cache_service.get_cache(api)

    def purchase(self, item_id, item_number):
        api = OrderServicePicker().pick_server() + f"/purchase/{item_id}/"
        response = requests.put(api, data={'item_number': item_number})
        self.cache_service.clear_cache()
        return self.handle_response(response)

    def handle_response(self, response):
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error happened in catalog server with error code {response.status_code}, message: {response.text}")
            return None
