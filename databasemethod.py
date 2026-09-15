from pymongo import MongoClient
from bson import ObjectId
mongoURL=MongoClient("mongodb+srv://raghu07:raghu07@cluster0.kvvxso6.mongodb.net/?appName=Cluster0")
mydata=mongoURL["myproject"]
base=mydata["register"]
userdata={
    "name":"raj",
    "age":10,
    "mobile":905839453,
    "address":"no:7,aaa street",
    "isActive":True
}
# get find()
def auto():
    userdata=base.find()
    for i in userdata:
        print(i)
# auto()

#find_one()
def specifuser(userId):
    single=base.find_one({"_id":ObjectId(userId)})
    print(single)
# specifuser('6aa39c37b5e10de55341ecef')

#delete()
def deleteuser(userid):
    dele=base.find_one_and_delete({"_id":ObjectId(userid)})
    print(dele)
    print("delete successfully")
# deleteuser("6aa39c9ae2c7515768a4136f")

#update
def updatedata (userid):
    updatename=input("update the value  ")
    get={"name":updatename}
    up=base.find_one_and_update({"_id":ObjectId(userid)},{"$set":get})
    print("updated successfully") 
# updatedata("6aa39c37b5e10de55341ecef")