from scrapy.utils.project import get_project_settings

SETTINGS = {

    'DOWNLOAD_HANDLERS': {
        'http': 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler',
        'https': 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler',
    },

    'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',

    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',

    'ITEM_PIPELINES': {
        'spiders.pipelines.TgePipeline': 300,  
    }

}


def get_tge_settings() -> dict:
    settings = get_project_settings()
    custom_settings = SETTINGS

    for key, value in custom_settings.items():
        settings.set(key, value)

    return settings