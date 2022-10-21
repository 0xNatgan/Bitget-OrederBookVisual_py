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
import time

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
    symbol = "BTCUSDT_SPBL"
    limit = 40
    url = 'https://api.bitget.com/api/spot/v1/market/depth?symbol='
    url2 = '&type=step0&limit='
    pygame.init()
    screen = pygame.display.set_mode()
    x, y = screen.get_size()
    font = pygame.font.SysFont(None, 24)
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
        # rect_anb = rects_separated(x, y, data)
        rect_anb = rects_cumulative(x, y, data)
        ask_rect = rect_anb[0]
        bid_rect = rect_anb[1]

        # img = font.render('hello', True, BLUE)
        # screen.blit(img, (20, 20))
        # Draw a solid blue circle in the center
        for i in range(limit):
            pygame.draw.rect(screen, (0, 255, 0), ask_rect[i])

        for i in range(limit):
            pygame.draw.rect(screen, (255, 0, 0), bid_rect[i])

        # Flip the display
        pygame.display.flip()
        # print("=============================")
        time.sleep(0.05)

    # Done! Time to quit.
    pygame.quit()


main()
