# -*- coding: utf-8 -*-

# Scrapy settings for books project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'
# IMAGES_STORE = "D:\\book\\images"
# FEED_EXPORT_ENCODING='UTF8' # 输出json为中文
FEED_EXPORT_ENCODING ='gb18030'# 输出csv为中文

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = [		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#                     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#                     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#                     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#              ]


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOG_LEVEL='WARNING'

# JOBDIR = 'shop'
# ITEM_PIPELINES	=	{'scrapy.pipelines.files.FilesPipeline':	1}

# PROXIES = ['https://125.123.141.252:9000', 'https://125.123.139.228:9000', 'https://116.238.152.116:9797', 'https://59.32.103.182:808', 'https://119.90.126.106:7777', 'https://210.77.23.197:1080', 'https://125.123.126.133:9000', 'https://171.36.40.195:9797', 'https://163.125.157.97:8888', 'https://113.116.147.125:9000', 'https://180.213.169.75:8118', 'https://223.199.158.84:9797', 'https://123.161.18.174:9797', 'https://182.88.191.254:9797', 'https://124.16.85.80:8123', 'https://49.83.46.89:8118', 'https://58.58.48.138:53281', 'https://211.101.136.86:8080', 'https://14.115.104.138:808', 'https://14.115.107.87:808', 'https://114.249.112.40:9000', 'https://203.110.164.139:52144', 'https://114.249.115.9:9000', 'https://163.125.18.182:8888', 'https://183.47.46.238:1080', 'https://59.38.62.173:9797', 'https://114.240.192.171:9797', 'https://113.87.161.64:1080', 'https://113.118.191.2:9000', 'https://183.172.15.10:1080', 'https://113.118.159.56:9000', 'https://124.16.112.74:1080', 'https://119.123.175.200:9797', 'https://182.61.170.45:3128', 'https://59.32.103.66:808', 'https://14.115.104.49:808', 'https://101.5.214.182:8123', 'https://112.95.18.123:8088', 'https://119.145.2.100:44129', 'https://119.131.89.134:9797', 'https://123.138.89.132:9999', 'https://113.78.255.107:9000', 'https://111.225.11.87:9999', 'https://124.204.78.12:8123', 'https://120.92.136.251:8088', 'https://61.164.39.67:53281', 'https://14.115.105.222:808', 'https://101.6.68.190:1080', 'https://59.32.103.248:808', 'https://58.240.220.86:53281', 'https://223.199.157.41:9797', 'https://117.62.94.128:8118', 'https://115.171.203.68:9000', 'https://182.134.149.170:8118', 'https://101.5.111.32:8123', 'https://59.34.115.158:1080', 'https://119.176.80.220:9999', 'https://114.234.81.143:8118', 'https://119.29.21.113:808', 'https://124.205.143.213:32612', 'https://59.38.60.206:9797', 'https://113.78.67.64:9797', 'https://120.7.245.80:9000', 'https://111.230.31.213:808', 'https://112.67.187.155:9797', 'https://113.116.180.119:9000', 'https://171.37.158.242:9797', 'https://106.14.17.74:8123', 'https://125.123.126.227:9000', 'https://163.125.156.227:8888', 'https://113.251.173.117:8123', 'https://163.125.156.222:8888', 'https://14.115.105.243:808', 'https://163.125.17.164:8888', 'https://14.115.106.246:808', 'https://203.93.209.163:53281', 'https://163.125.156.230:8888', 'https://182.40.55.198:8118', 'https://223.199.152.200:9797', 'https://183.172.200.252:1080', 'https://125.123.139.170:9000', 'https://113.78.254.156:9000', 'https://124.127.70.48:1080', 'https://112.95.189.117:9797', 'https://36.110.14.68:48443', 'https://171.36.165.99:9797', 'https://111.230.211.23:1080', 'https://218.20.54.211:9999', 'https://119.123.125.137:9797', 'https://101.76.244.152:1080', 'https://113.78.66.203:9797', 'https://123.58.10.49:8080', 'https://221.11.105.69:56120', 'https://183.33.131.176:9797', 'https://125.123.140.175:9000', 'https://111.177.174.141:9999', 'https://111.177.166.225:9999', 'https://222.128.9.235:59593', 'https://111.177.178.158:9999', 'https://119.101.115.71:9999', 'https://111.179.20.57:9999', 'https://223.244.252.58:45744', 'http://119.101.115.87:9999', 'https://119.101.115.120:9999', 'https://119.101.112.158:9999', 'https://119.101.116.50:9999', 'https://119.101.114.80:9999', 'https://119.101.114.225:9999', 'https://223.241.118.246:8010', 'http://119.101.113.111:9999', 'https://61.183.176.122:53281', 'https://119.101.112.110:9999', 'https://119.101.116.250:9999', 'https://111.177.178.124:9999', 'https://111.177.178.26:9999', 'https://115.223.93.199:8010', 'https://119.101.113.161:9999', 'https://60.168.86.45:42078', 'https://114.230.41.235:3128', 'https://119.101.115.38:9999', 'https://119.101.114.7:9999', 'https://119.101.117.7:9999', 'https://218.76.253.201:61408', 'https://119.101.115.82:9999', 'https://119.101.117.15:9999', 'https://119.101.114.77:9999', 'https://119.101.115.46:9999', 'https://119.101.113.57:9999', 'https://111.179.20.53:9999', 'https://111.177.174.137:9999', 'https://119.101.113.178:9999', 'https://119.101.117.112:9999', 'https://119.101.115.140:9999', 'https://119.101.115.147:9999', 'http://119.101.115.83:9999', 'https://119.101.113.191:9999', 'https://119.101.112.57:9999', 'https://119.101.112.242:9999', 'https://119.101.112.200:9999', 'https://113.120.61.62:9999', 'https://119.101.115.90:9999', 'https://119.101.112.81:9999', 'https://119.101.117.27:9999', 'https://219.145.170.23:34186', 'https://119.101.116.207:9999', 'https://119.101.116.30:9999', 'http://119.101.112.175:9999', 'https://119.101.116.145:9999', 'https://119.101.115.112:9999', 'https://119.101.113.155:9999', 'https://111.177.174.245:9999', 'https://223.241.118.37:8010', 'https://119.101.114.243:9999', 'https://119.101.116.146:9999', 'https://113.121.242.69:25564', 'https://183.15.122.107:3128', 'https://119.101.112.88:9999', 'https://119.101.113.242:9999', 'http://119.101.115.106:9999', 'https://115.46.76.89:8123', 'https://119.101.112.186:9999', 'http://124.112.237.66:8118', 'https://119.101.113.39:9999', 'https://61.170.179.89:50799', 'https://111.177.168.172:9999', 'https://119.101.112.218:9999', 'https://119.101.114.241:9999', 'https://111.177.168.89:9999', 'https://211.154.140.221:58175', 'https://119.101.112.4:9999', 'http://124.235.135.87:80', 'https://1.192.241.146:9999', 'https://119.101.112.171:9999', 'http://119.101.115.158:9999', 'https://119.101.112.187:9999', 'https://119.101.113.101:9999', 'https://110.52.234.32:9999', 'https://119.101.114.171:9999', 'https://119.101.114.217:9999', 'https://119.101.112.219:9999', 'https://111.177.168.15:9999', 'http://119.101.116.195:9999', 'https://60.205.213.172:8118', 'https://119.101.112.167:9999', 'https://119.101.113.116:9999', 'https://119.101.113.224:9999', 'https://119.101.113.70:9999', 'https://119.101.112.235:9999', 'http://119.101.112.89:9999', 'https://101.236.42.63:8866', 'https://119.101.116.67:9999', 'https://113.120.61.95:9999', 'http://119.101.113.216:9999', 'https://119.101.113.235:9999', 'https://119.101.112.251:9999', 'https://119.167.153.50:8118', 'https://116.7.176.60:8118', 'https://119.101.114.187:9999', 'https://119.101.113.244:9999', 'https://119.101.113.92:9999', 'http://119.101.112.149:9999', 'https://202.104.113.35:53281', 'https://110.52.234.132:9999', 'https://119.101.113.145:9999', 'https://119.101.113.189:9999', 'https://111.177.168.135:9999', 'http://119.101.112.122:9999', 'https://111.177.174.177:9999', 'http://119.101.116.249:9999', 'http://119.101.112.231:9999', 'https://110.52.234.37:9999', 'https://119.101.112.178:9999', 'https://119.101.112.180:9999', 'https://119.101.112.194:9999', 'https://117.114.149.66:53281']
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = round(random.uniform(1, 4), 2)  # 随机生成浮点数 最后一位代表保留2位小数

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'books.middlewares.ProxyMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # # 'books.middlewares.ProxyMiddleware': 543,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
    # 'books.middlewares.ProxyMiddleWare':125,
    # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
    'books.middlewares.IPProxyMiddleWare': None, # IP代理池1
    'books.middlewares.IPProxySelfMiddleWare': None, # IP代理池2
    'books.middlewares.IPProxyPoolMiddleWare': None, # IP代理池3
    'books.middlewares.SeleniumMiddleware': None, # selenuim
    'books.middlewares.RotateUserAgentMiddleware': 125, #User_Agent
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#      'books.pipelines.BooksPipeline': 300,
#      # 'books.pipelines.files.BooksPipeline': 1,
# }
# FILES_STORE = '/Download/scrapy'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
