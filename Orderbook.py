# from turtle import screensize
# from unittest import result
from pkgutil import get_data
import pygame
import json
import requests
import threading
from class_Request import *
from class_data import *
from drawingfunctions import *

def maxshape(data):
    max = 0
    for  order in data['asks']:
        if float(order[1]) > max:
            max = float(order[1])
    print(max)
    return max


def results(data):
    print('asks')
    print(data['asks'])
    print('bids')
    print(data['bids'])

#================= Main =================
def main():
    symbol = "USDCUSDT_SPBL"
    limit = "2"
    url = 'https://api.bitget.com/api/spot/v1/market/depth?symbol='
    url2 = '&type=step0&limit='
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    # max = 0
    # window_stats = {"screen" : [500, 500], "order_depth": limit*2, "max": max }
    # window_stats["max"] = maxshape(data)

    request = Request(url, url2, symbol, limit)
    data = Data(request.get_data(), limit)
    print(data.data)
    print(data.spread)
    data.maj(request.get_data(), limit)


    running = True
    while running:
        data.maj(request.get_data(), limit)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((0, 0, 0))

        # Draw a solid blue circle in the center

        pygame.draw.rect(screen, (255, 0, 0), (250, 250), ())

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


main()
