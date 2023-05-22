from scrapy.item import Item, Field

class TGeElectricity(Item):
    tge_base = Field()
    tge_peak = Field()
    tge_off_peak = Field()
    tge_24 = Field()
    tge_15 = Field()
    tge_9 = Field()
