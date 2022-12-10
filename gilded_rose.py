# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        passes_concert = "Backstage passes to a TAFKAL80ETC concert"
        sulfuras = "Sulfuras, Hand of Ragnaros"
        for item in self.items:
            if item.name != "Aged Brie" and item.name != passes_concert:
                self.func_quality(item, sulfuras)
            else:
                self.func_quality2(item, passes_concert)
            if item.name != sulfuras:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self.func_quality3(item, sulfuras, passes_concert)

    @staticmethod
    def func_quality(item, sulfuras):
        if item.quality > 0 and item.name != sulfuras:
            item.quality = item.quality - 1

    @staticmethod
    def func_quality2(item, passes_concert):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == passes_concert:
                if item.sell_in < 11 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality = item.quality + 1

    @staticmethod
    def func_quality3(item, sulfuras, passes_concert):
        if item.name != "Aged Brie":
            if item.name != passes_concert:
                if item.quality > 0 and item.name != sulfuras:
                    item.quality = item.quality - 1
            else:
                item.quality = 0
        else:
            if item.quality < 50:
                item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
