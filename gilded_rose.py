# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                if "Conjured" in item.name:  # 检查商品是否是Conjured类型
                    degrade_rate = 2  # Conjured商品的质量下降速度是普通商品的两倍
                else:
                    degrade_rate = 1  # 普通商品的质量下降速度
                if item.quality > 0:
                    item.quality = item.quality - degrade_rate
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if "Conjured" in item.name:  # 检查商品是否过期且是Conjured类型
                        degrade_rate = 2  # Conjured商品过期后的质量下降速度加倍
                    else:
                        degrade_rate = 1  # 普通商品过期后的质量下降速度
                    if item.quality > 0:
                        item.quality = item.quality - degrade_rate
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
