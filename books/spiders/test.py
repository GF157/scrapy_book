import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))




def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('http://httpbin.org/get', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问

            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None



# 测试web.py
# import web
#
# urls = (
#     '/(.*)', 'hello'
# )
#
# app = web.application(urls, globals())
#
#
# class hello:
#     def GET(self, name):
#         i = web.input(times=1)
#         if not name:
#             name = 'world'
#         for c in range(int(i.times)):
#             print
#             'Hello,', name + '!'
#         return 'Hello, ' + name + '!'
#
#
# if __name__ == "__main__":
#     app.run()