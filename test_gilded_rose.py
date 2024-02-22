# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_results = [(0, 1), (8, 18), (3, 5)]
        
        for item, (expected_sell_in, expected_quality) in zip(items, expected_results):
            self.assertEqual(item.sell_in, expected_sell_in)
            self.assertEqual(item.quality, expected_quality)

    def test_conjured_item_degrades_twice_as_fast(self):
        conjured_item = "Conjured Mana Cake"
        items = [Item(conjured_item, 3, 6)]
        gr = GildedRose(items)

        gr.update_quality()
        
        expected_quality = 4
        self.assertEqual(items[0].quality, expected_quality)
    
    def test_aged_brie_increases_in_quality_over_time(self):
        items = [Item("Aged Brie", 2, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_backstage_passes_increases_in_quality_as_sell_in_approaches(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_sulfuras_never_decreases_in_quality_or_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in) 
        self.assertEqual(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
