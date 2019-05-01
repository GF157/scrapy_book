import pymongo


client = pymongo.MongoClient('localhost',27017)
book = client['book']
all = book['all_data']

def get_loan_number():
    for items in all.find():
        print(items)
