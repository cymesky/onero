from spiders.items import TGeElectricity


class TgePipeline:
    # def open_spider(self, spider):
    #     self.client = MongoClient('mongodb://mongodb:27017/')
    #     self.db = self.client['db']
    #     self.tge = self.db['tge']
    
    def process_item(self, item, spider):
        tge_electricity = TGeElectricity(item)

        # for primary_key, values in tge_electricity.items():
        #     for date, value in values:
        #         existing_document = self.tge.find_one({'name': primary_key, 'date': date, 'value': value})
                
        #         if existing_document is None:
        #             self.tge.insert_one({
        #                 'name': primary_key,
        #                 'date': date,
        #                 'value': value
        #             })

    def close_spider(self, spider):
        self.client.close()