import pygame
import json
import requests
import threading

class Data:

    def __init__(self, data, limit):
        self.data = data
        self.asks = data["asks"]
        self.bids = data["bids"]
        self.limit = limit
        self.spread = float(self.asks[0][0]) - float(self.bids[0][0])

    def maj(self, data, limit):
        self.data = data
        self.asks = data["asks"]
        self.bids = data["bids"]
        self.limit = limit
        self.spread = float(self.asks[0][0]) - float(self.bids[0][0])
        print("updated data")
