from src.GildedRose import *


def test_gilded_rose():
    items = [NormalItem("Normal Varita sin magia", 10, 10),
             ConjuredItem("Conjured Varita", 5, 20),
             AgedBrie("Aged Brie", 0, 40),
             Sulfuras("Sulfuras", 0, 80),
             Backstage("Backstage", 15, 25)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9
    assert items[0].sell_in == 9
    assert items[1].quality == 18
    assert items[1].sell_in == 4
    assert items[2].quality == 42
    assert items[2].sell_in == -1
    assert items[3].quality == 80
    assert items[3].sell_in == 0
    assert items[4].quality == 26
    assert items[4].sell_in == 14


def test_create_normal_item():
    baston = GildedRose.create_item('Normal Bastón', 10, 10)

    baston.update_quality()
    assert baston.quality == 9
    assert baston.sell_in == 9


def test_create_aged_brie():
    queso = GildedRose.create_item('Aged Brie Asturiano', 10, 10)

    queso.update_quality()
    assert queso.quality == 11
    assert queso.sell_in == 9


def test_create_conjured():
    varita = GildedRose.create_item('Conjured varita', 10, 10)

    varita.update_quality()

    assert varita.quality == 8
    assert varita.sell_in == 9
