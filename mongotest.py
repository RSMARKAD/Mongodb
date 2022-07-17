import pymongo

client = pymongo.MongoClient("mongodb+srv://ravikiran:ravikiran1989@cluster0.v1yrg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d= {
    "name":"ravikiran",
    "email":"ravikiranmarkad89@gmail.com",
    "surname": "markad"
}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d)