BOT_NAME = 'mpscapitalservices'

SPIDER_MODULES = ['mpscapitalservices.spiders']
NEWSPIDER_MODULE = 'mpscapitalservices.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'mpscapitalservices.pipelines.MpscapitalservicesPipeline': 100,

}
