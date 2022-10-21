import pygame
from class_data import *

def max_calc(data, x):
    max = 0
    for orders in data.asks:
        if float(orders[1]) > max:
            max = float(orders[1])
    for orders in data.bids:
        if float(orders[1]) > max:
            max = float(orders[1])
    return max

# def heigt_rect(x,data, i):
#     max = maxshape(data)
#     coeff = x/max
#     return int(i)*coeff

def cumul_max(data, x):
    cum_asks = 0
    cum_bids = 0
    for orders in data.asks:
        cum_asks += float(orders[1])
    for orders in data.bids:
        cum_bids += float(orders[1])

    if cum_asks >= cum_bids:
        return cum_asks
    else:
        return cum_bids

def reverting(array):
    lenght = len(array) - 1
    array2 = []
    for i in array:
        array2.append(array[lenght])
        lenght -=1
    return array2

def rects_cumulative(x, y, data):
    ask_rect = []
    bid_rect = []
    cpt = 0
    asks_cum = 0
    bids_cum = 0
    max = cumul_max(data, x)
    limit2 = data.limit * 2
    # print("asks")
    cpt2 = data.limit
    for i in range(data.limit):
        ask_rect.append(((x / limit2) * cpt2,
                         (100 + y) - ((float(data.asks[i][1])+ asks_cum)/ max * y),
                         x / limit2, ((float(data.asks[i][1])+ asks_cum) / max) * y))
        asks_cum += float(data.asks[i][1])
        cpt2 -= 1
        cpt += 1

    cpt2 = 0
    # print("bids")
    for i in range(data.limit):
        bid_rect.append(((x / limit2) * cpt,
                         (100 + y) - ((float(data.bids[i][1])+bids_cum) / max * y),
                         x / limit2, ((float(data.bids[i][1])+bids_cum) / max) * y))
        bids_cum += float(data.bids[i][1])
        cpt += 1

    rect_anb = [ask_rect, bid_rect]
    return rect_anb


def rects_separated(x, y, data):
    ask_rect = []
    bid_rect = []
    cpt = 0
    max = max_calc(data, x)
    limit2 = data.limit * 2
    # print("asks")
    for i in range(data.limit):
        ask_rect.append(((x/limit2)*cpt,
                         (100 + y) - (float(data.asks[i][1])/max*y),
                         x/limit2,
                         (float(data.asks[i][1])/max)*y))

        print(float(data.asks[cpt][1]))
        cpt += 1

    cpt2 = 0
    # print("bids")
    for i in range(data.limit):
        bid_rect.append(((x/limit2) * cpt,
                         (100 + y) - (float(data.bids[i][1])/max*y),
                         x/limit2,
                        (float(data.bids[i][1])/max)*y))
        # print(float(data.bids[cpt2][1]))
        cpt2 += 1
        cpt += 1

    rect_anb = [ask_rect, bid_rect]
    return rect_anb
