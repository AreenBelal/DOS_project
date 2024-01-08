

class CacheService:
    def __init__(self):
        self.cache = {}

    def clear_cache(self):
        self.cache = {}
        return True

    def get_cache(self, api):
        return self.cache.get(api, {}).get('value')

    def set_cache(self, api, value):
        self.cache[api] = {'value': value, 'editied': False}
        return True

    def delete_cache(self, api):
        del self.cache[api]
