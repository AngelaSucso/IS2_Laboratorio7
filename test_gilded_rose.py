# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # comprueba para dexterity vest que el nombre del item no cambie en update_quality()
    def test_dexterity_vest_name(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)

    # comprueba para dexterity vest que el numero de dias disminuya tras 1 dia
    def test_dexterity_sell_in_equal(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    # comprueba que el sell in no se mantenga igual tras 1 dia
    def test_dexterity_sell_in_not_equal(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(10, items[0].sell_in)

    # comprueba que el quality no se mantenga igual tras 1 dia
    def test_dexterity_quality(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(20, items[0].quality)


if __name__ == '__main__':
    unittest.main()
