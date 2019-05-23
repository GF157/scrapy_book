# import pymongo
# import jieba
# import jieba.analyse
#
# client = pymongo.MongoClient('localhost',27017)
# book = client['book']
# all = book['4281']
#
# label = ''
# author = ''
# score = 0
# count = 0
#
# for items in all.find():
#     count = count + 1
#     label = label + items['label'][0]
#     author = author + str(items['author'])
#     # score = float(score) + float(items['score'])
#
# print(label)
# # 导入自定义词典
# jieba.load_userdict("D:\project\jieba.txt")
#
# # # 精确模式
# # seg_list = jieba.cut(label, cut_all=False)
# # print (u"分词结果:")
# # print ("/".join(seg_list))
#
# # 提取标签排名前五
# tags = jieba.analyse.extract_tags(label, topK=5)
# print (u"标签TOP5:")
# print (" ".join(tags))
#
# # 作者
# tags = jieba.analyse.extract_tags(author, topK=10)
# print('作者TOP10:')
# print(' '.join(tags))
#
