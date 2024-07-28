from pymongo import MongoClient

uri = "mongodb://localhost:27017" # enter your uri

client = MongoClient(uri, connectTimeoutMS=60000)

database = client["test"] # 'test' is name of DataBase

collection = database["intro"] # 'intro' is name of collection

#Put objects in collection
document_list = [
   { "Name" : "Muaaz", "Age" : 21 },
   { "University":"FAST", "Semester":7}
]
result = collection.insert_many(document_list)

# Fetch data from DB
results = collection.find({ "Name": "Muaaz" }) # it return object which contain Name 'Muaaz'
for result in results:
    print(result)

