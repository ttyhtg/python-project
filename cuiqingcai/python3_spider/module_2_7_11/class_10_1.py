import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client.test
collections = db.students
collection = db['students']
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collections.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
print("--------------------------------------------------")

result_find = collections.find_one({'name': 'Mike'})
print(type(result))
print(result)