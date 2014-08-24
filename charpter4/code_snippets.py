# -*- coding: utf-8 -*-
__author__ = 'dongdaqing'

import json
import pymongo
conn = pymongo.Connection("localhost", 27017)

# example1
#连接数据库
# db = conn.widgets
#得到表
# widget = db.widgets
#向表中插入文档
# widget.insert({"foo":"bar"})

#打印数据库中表的个数
# print db.collection_names()
# db.widgets.insert({"name":"flibnip","description":"grade-A industrial flibnip","quantity":3})

#查找集合中某个文档
# print widget.find_one({"name":"flibnip"})

#文档的查找和替换
# doc = widget.find_one({"name":"flibnip"})
# print type(doc)
# print doc['name']
# print doc['quantity']
# doc['quantity'] = 4
# widget.save(doc)
# print widget.find_one({"name":"flibnip"})

#插入更多的文档
# widget.insert({"name": "smorkeg", "description": "for external use only", "quantity": 4})
# widget.insert({"name": "clobbasker", "description": "properties available on request", "quantity": 2})

#遍历文档
# for doc in widget.find():
#     print doc

#获得文档子集
# for doc in widget.find({"quantity":4}):
#     print doc

#删除文档
# widget.remove({"foo": "bar"})

#json转换
# doc = widget.find_one({"foo":"bar"})
# del doc["_id"]
# print json.dumps(doc)


#example2
db = conn.example
# db.words.insert({"word": "oarlock", "definition": "A device attached to a rowboat to hold the oars in place"})
# db.words.insert({"word": "seminomadic", "definition": "Only partially nomadic"})
# db.words.insert({"word": "perturb", "definition": "Bother, unsettle, modify"})

#数据库共有多少个表
# print db.collection_names()

for doc in db.words.find():
    print doc
