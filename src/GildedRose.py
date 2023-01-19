class GildedRose():

    def __init__(self, items):
        self.items = items



    def update_quality(self):
        for item in self.items:
            # lo que hacemos aquí es llamar a item, que contendrá una clase con su propio método update_quality
            # lo que significa que cada clase llamará a un método que se llama igual, pero que varía su comportamiento
            # polimorfismo.
            item.update_quality()

    @staticmethod
    def create_item(name, sell_in, quality):
        item_types = {'normal': NormalItem, 'conjured': ConjuredItem, 'aged brie': AgedBrie, 'sulfuras': Sulfuras, 'backstage': Backstage}
        type = name.split()
        item_class = item_types.get(type[0].lower())
        if item_class:
            return item_class(name, sell_in, quality)
        else:
            item_class = item_types.get((type[0] + ' ' + type[1]).lower())
            if item_class:
                return item_class(name, sell_in, quality)
            else:
                raise ValueError(f"Tipo de item inválido {name}")

class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Interfaz():

    def update_quality(self):
        '''Este es el método que introduciremos en todas las clases, aquí lo dejamos vacío
            ya que lo rellenaremos después en las respectivas clases '''
        pass


class NormalItem(Item, Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)  # Utilizamos el constructor de Item.

    def setSell_in(self):  # La caducidad debe reducirse en 1 cada vez que se ejecute
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


class ConjuredItem(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        assert self.quality == 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass


class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()


if __name__ == "__main__":

    def currentItems():
        items = [
            NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
            AgedBrie(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        return items

    def newItems():
        afterItems = [
            NormalItem(name="+5 Dexterity Vest", sell_in=8, quality=18),
            AgedBrie(name="Aged Brie", sell_in=0, quality=3),
            Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-2, quality=80),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-3, quality=80),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=22),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=54),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=55),
            ConjuredItem(name="Conjured Mana Cake", sell_in=2, quality=2),  # <-- :O
        ]
        return afterItems


    def test_gilded_rose(items, afterItems):
        dias = 2
        for dia in range(dias):

            print("-------- día %s --------" % dia)
            print("name, sellIn, quality")
            for item in items:
                print(item)
            print("")
            GildedRose(items).update_quality()

        assert items == afterItems


    test_gilded_rose(currentItems(), newItems())




