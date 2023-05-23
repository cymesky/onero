import re
import scrapy
from spiders.items import TGeElectricity


class TGeSpider(scrapy.Spider):
    name = 'tge_spider'

    def start_requests(self):
        url = "https://tge.pl"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = TGeElectricity()

        pattern = r'<script\b[^>]*>(.*?)</script>'
        scripts_data = list(re.findall(
            pattern, response.text, flags=re.DOTALL))

        tge_base_script = next((item for item in scripts_data
                                if "chartdiv-indexes--TGeBase" in item), None)
        tge_peak_script = next((item for item in scripts_data
                                if "chartdiv-indexes--TGePeak" in item), None)
        tge_off_peak_script = next((item for item in scripts_data
                                    if "chartdiv-indexes--TGeOffpeak"
                                    in item), None)
        tge_24_script = next((item for item in scripts_data
                              if "chartdiv-indexes--TGe24" in item), None)
        tge_15_script = next((item for item in scripts_data
                              if "chartdiv-indexes--TGe15" in item), None)
        tge_9_script = next((item for item in scripts_data
                             if "chartdiv-indexes--TGe9" in item), None)

        pattern = r'"date":\s*"(\d{2}-\d{2})",\s*"kurs":\s*\'([\d.]+)\''

        item['tge_base'] = re.findall(pattern, tge_base_script)
        item['tge_peak'] = re.findall(pattern, tge_peak_script)
        item['tge_off_peak'] = re.findall(pattern, tge_off_peak_script)
        item['tge_24'] = re.findall(pattern, tge_24_script)
        item['tge_15'] = re.findall(pattern, tge_15_script)
        item['tge_9'] = re.findall(pattern, tge_9_script)

        yield item
