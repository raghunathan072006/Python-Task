from pymongo import MongoClient
mongoURL=MongoClient("mongodb+srv://raghu07:raghu07@cluster0.kvvxso6.mongodb.net/?appName=Cluster0")
mydata=mongoURL["myproject"]
base=mydata["register"]
# datas={
#     "name":"raghu",
#     "age":20,
#     "mobile":9080991243,
#     "gender":"male",
#     "address":"no:10 alagappa",
#     "isactive":True
# }
# def createData(user):
#     data=base.insert_one(user)
#     print("created suceesful")
# createData(datas)

# std=[
#     {
#         "name":"aa",
#         "std":2,
#         "section":"A",
#         "addres":"no 3 avenue",
#         "district":"cud"
#     },
#     {
        
#         "name":"bb",
#         "std":2,
#         "section":"A",
#         "addres":"no 4 avenue",
#         "district":"cud"
#     },
#     {
        
#         "name":"cc",
#         "std":2,
#         "section":"A",
#         "addres":"no 5 avenue",
#         "district":"cud"
#     }
# ]
# def start(val):
#     value=base.insert_many(val)
#     print("created succesfully")
# start(std)

# from pymongo import MongoClient
# from bson import ObjectId

# mongoURL = MongoClient("mongodb+srv://xavier:xavier123@cluster0.p0p3ape.mongodb.net/?appName=Cluster0")

# myDB = mongoURL["python-project"]

# myCollection = myDB["register"]

# userData = {
#     "name":"durai",
    # "age":10,
    # "mobile":905839453,
    # "address":"no:7,aaa street",
    # "isActive":True
# }

# def createUser(user):
#     data = myCollection.insert_one(user)
#     print("Data created successfully...")

# #createUser(userData)

# studentsData = [
#     {
#         "name":"aaa",
#         "age":7,
#         "mobile":947354395,
#         "address":"no:2,bjhgdfjdg"

#         },
#        {
#         "name":"bbb",
#         "age":3,
#         "mobile":8753845637,
#         "address":"no:69,bjhgdfjdg"

#         }

#     ]

# def createMultipleUser(sData):
#     data = myCollection.insert_many(sData)
#     print("data created successfully....")

# # createMultipleUser(studentsData)


# # get all

# def getAllUserData():
#     userData = myCollection.find()
#     for i in userData:
#         print(i)

# ##getAllUserData()


# def getSpecificUserData(userId):
#     print(userId)
#     singleUser = myCollection.find_one({"_id":ObjectId(userId)})
#     print(singleUser)
    
# ##getSpecificUserData("6aa0f74bb5a8152f8f0ce191")

# def deleteUserData(userId):
#     userrecord = myCollection.find_one_and_delete({"_id":ObjectId(userId)})
#     print("user deleted successfully")

# ##deleteUserData("6aa0f65349a4a1edad86e0ac")

# # updateName = input("Enter your name to update: ")
# # updatedData = {
# #     "name": updateName
# #     }