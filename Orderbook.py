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
    symbol = "USDCUSDT_SPBL"
    limit = 10
    url = 'https://api.bitget.com/api/spot/v1/market/depth?symbol='
    url2 = '&type=step0&limit='



    pygame.init()
    screen = pygame.display.set_mode()
    x, y = screen.get_size()
    y = y - 80
    font = pygame.font.SysFont(None, 20)



    # max = 0
    # window_stats = {"screen" : [500, 500], "order_depth": limit*2, "max": max }
    # window_stats["max"] = maxshape(data)
    request = Request(url, url2, symbol, limit)
    data = Data(request.get_data(), limit)

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
        ask_rect, bid_rect = rects_cumulative(x, y, data)
        # ask_rect = rect_anb[0]
        # bid_rect = rect_anb[1]

        # img = font.render('hello', True, BLUE)
        # screen.blit(img, (20, 20))
        # Draw a solid blue circle in the center
        for i in range(limit):
            pygame.draw.rect(screen, (150, 255, 0), ask_rect[i])
            a = (round(ask_rect[i][0], 2), round(ask_rect[i][1], 2),
                 round(ask_rect[i][2], 2), round(ask_rect[i][3], 2))
            print(a, "  ", data.asks[i][0], "    size :", data.asks[i][1])
            img_asks = font.render(str(data.asks[i][0]), True, (255,255,255))
            screen.blit(img_asks,(ask_rect[i][0] + 5, y))

        print("end")

        for i in range(limit):
            pygame.draw.rect(screen, (230, 50, 0), bid_rect[i])
            b = (round(bid_rect[i][0], 2), round(bid_rect[i][1], 2),
                 round(bid_rect[i][2], 2), round(bid_rect[i][3], 2))
            print(b, "   ",data.bids[i][0], "    size :", data.bids[i][1])
            img_bid = font.render(str(data.bids[i][0]), True, (255, 255, 255))
            screen.blit(img_bid, (bid_rect[i][0] + 5, y))

        # Flip the display
        pygame.display.flip()
        print("========================================================")
        time.sleep(0.05)

    # Done! Time to quit.
    pygame.quit()


main()
