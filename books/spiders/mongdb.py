import pymongo


client = pymongo.MongoClient('localhost',27017)
book = client['book']
all = book['all_data']

def get_loan_number(file):
    fp = open(file, "w+")
    for items in all.find():
        print(items)
        fp.write(items[0])
    fp.close()

if __name__ == "__main__":
    file = r"D:\loanNUmber.txt"
    get_loan_number(file)