# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = 'bid=qnrg-Om6HSo; gr_user_id=adbd942a-6e95-40c6-be0f-d2fc0114e81b; _vwo_uuid_v2=DEF3C8C1A63D796DBFDC8E1F0895BDADB|026bb6ddc7dfa0977cfd98309e6412c0; ll="118172"; Hm_lvt_6e5dcf7c287704f738c7febc2283cf0c=1555329797,1555424331,1555431024,1555513908; douban-fav-remind=1; _ga=GA1.2.113169978.1553871196; ct=y; __utmc=30149280; __utmc=81379588; viewed="26929955_5375620_26582822_27030507_1767945_24738302_26838557_27168433_1119944_26834485"; dbcl2="146494461:ssWrzbB2DTI"; ck=Uu4j; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1556510481%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fbook.douban.com%252Ftag%252F%2525E7%2525AE%252597%2525E6%2525B3%252595%253Fstart%253D420%2526type%253DT%22%5D; _pk_id.100001.3ac3=7cd6ce805e596b91.1553871196.32.1556510481.1556497709.; _pk_ses.100001.3ac3=*; __utma=30149280.113169978.1553871196.1556497514.1556510481.37; __utmz=30149280.1556510481.37.8.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt_douban=1; __utmb=30149280.1.10.1556510481; __utma=81379588.468017531.1553871196.1556497515.1556510481.31; __utmz=81379588.1556510481.31.6.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmb=81379588.1.10.1556510481; push_doumail_num=0; push_noty_num=3'
    trans = transCookie(cookie)
    print(trans.stringToDict())