import pygame
import json
import requests
import threading

class Request:

    def __init__(self, url, url2, symbol, limit):
        self.url=  url
        self.url2 = url2
        self.symbol = symbol
        self.limit = limit
        self.max_order = 0

    def get_data(self):
        r = requests.get(self.url + self.symbol + self.url2 + self.limit)
        r.status_code
        result = r.json()
        # print(result)
        data = result['data']
        return data
