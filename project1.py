from pymongo import MongoClient
from bson import ObjectId
mongourl=MongoClient("mongodb+srv://raghu07:raghu07@cluster0.kvvxso6.mongodb.net/?appName=Cluster0")
# try:
#     mongourl.admin.command("ping")
#     print("MongoDB Connected Successfully!")
# except Exception as e:
#     print("MongoDB Connection Failed!")
#     print(e)
mydata=mongourl["python_project"]
user=mydata["folder"]
product=mydata["product"]
order=mydata["order"]
# def add_user():
#     print("WELCOME TO MY PROJECT")
#     name=input("enter a name :")
#     email=input("enter a email: ")
#     password=input("enter a password: ")
#     mobile=int(input("enter a mobile: "))
#     address=input("enter a address: ")
#     exixting=user.find_one({"email":email})
#     if exixting:
#         print("all ready exist")
#         return
#     userdata={
#         "name":name,
#         "email":email,
#         "password":password,
#         "mobile":mobile,
#         "addres":address
#         }
#     user.insert_one(userdata)
#     print("user add successfully")
# add_user()

# def get_user():
#     user_id = input("Enter user id: ")

#     result = user.find_one({"_id": ObjectId(user_id)})

#     if result:
#         print(result)
#     else:
#         print("User not found")

# get_user()

# def update_user():
#     user_id = input("Enter user id: ")

#     name = input("Enter new name: ")
#     mobile = int(input("Enter new mobile: "))
#     address = input("Enter new address: ")

#     result = user.update_one(
#         {"_id": ObjectId(user_id)},
#         {
#             "$set": {
#                 "name": name,
#                 "mobile": mobile,
#                 "address": address
#             }
#         }
#     )

#     if result.modified_count > 0:
#         print("User updated successfully")
#     else:
#         print("User not found")
# update_user()

# def delete_user():
#     user_id = input("Enter user id: ")

#     result = user.delete_one({"_id": ObjectId(user_id)})

#     if result.deleted_count > 0:
#         print("User deleted successfully")
#     else:
#         print("User not found")
# delete_user()

# def add_20_products():
#     products = [
#         {"name": "Laptop", "price": 55000, "model": "HP15", "color": "Black", "stock": 20, "discount": 10},
#         {"name": "Mobile", "price": 25000, "model": "S24", "color": "Blue", "stock": 30, "discount": 5},
#         {"name": "Tablet", "price": 18000, "model": "Tab10", "color": "Grey", "stock": 15, "discount": 8},
#         {"name": "Keyboard", "price": 1500, "model": "K100", "color": "Black", "stock": 40, "discount": 5},
#         {"name": "Mouse", "price": 800, "model": "M200", "color": "White", "stock": 50, "discount": 10},
#         {"name": "Monitor", "price": 12000, "model": "LG24", "color": "Black", "stock": 25, "discount": 12},
#         {"name": "Headphone", "price": 2500, "model": "H500", "color": "Black", "stock": 35, "discount": 15},
#         {"name": "Speaker", "price": 3500, "model": "S300", "color": "Red", "stock": 20, "discount": 10},
#         {"name": "Webcam", "price": 2200, "model": "W100", "color": "Black", "stock": 18, "discount": 5},
#         {"name": "Printer", "price": 9000, "model": "P200", "color": "White", "stock": 12, "discount": 7},
#         {"name": "Router", "price": 3000, "model": "R500", "color": "Black", "stock": 25, "discount": 10},
#         {"name": "Power Bank", "price": 1800, "model": "PB10", "color": "Blue", "stock": 30, "discount": 8},
#         {"name": "Smart Watch", "price": 4500, "model": "SW20", "color": "Black", "stock": 22, "discount": 12},
#         {"name": "USB Cable", "price": 500, "model": "UC10", "color": "White", "stock": 60, "discount": 5},
#         {"name": "SSD", "price": 6500, "model": "SSD500", "color": "Black", "stock": 15, "discount": 10},
#         {"name": "Pen Drive", "price": 900, "model": "PD64", "color": "Silver", "stock": 45, "discount": 5},
#         {"name": "Microphone", "price": 4000, "model": "MIC10", "color": "Black", "stock": 16, "discount": 10},
#         {"name": "Projector", "price": 28000, "model": "PJ100", "color": "White", "stock": 8, "discount": 15},
#         {"name": "UPS", "price": 7500, "model": "UPS600", "color": "Black", "stock": 10, "discount": 8},
#         {"name": "Camera", "price": 45000, "model": "C200", "color": "Black", "stock": 7, "discount": 10}
#     ]

#     result = product.insert_many(products)

#     print("20 products added successfully")
#     # print("Inserted IDs:", result.inserted_ids)
# add_20_products()

# def get_all_products():
#     products = product.find()

#     for p in products:
#         print(p)
# get_all_products()

# def get_product():
#     product_id = input("Enter product id: ")

#     result = product.find_one({
#         "_id": ObjectId(product_id)
#     })

#     if result:
#         print(result)
#     else:
#         print("Product not found")
# get_product()

# def update_product():
#     product_id = input("Enter product id: ")

#     name = input("Enter new product name: ")
#     price = float(input("Enter new price: "))
#     stock = int(input("Enter new stock: "))
#     discount = float(input("Enter new discount: "))

#     result = product.update_one(
#         {"_id": ObjectId(product_id)},
#         {
#             "$set": {
#                 "name": name,
#                 "price": price,
#                 "stock": stock,
#                 "discount": discount
#             }
#         }
#     )

#     if result.modified_count > 0:
#         print("Product updated successfully")
#     else:
#         print("Product not found")
# update_product()

# def delete_product():
#     product_id = input("Enter product id: ")

#     result = product.delete_one({
#         "_id": ObjectId(product_id)
#     })

#     if result.deleted_count > 0:
#         print("Product deleted successfully")
#     else:
#         print("Product not found")
# delete_product()

# def create_order():
#     user_id = input("Enter user id: ")
#     product_id = input("Enter product id: ")
#     quantity = int(input("Enter quantity: "))

#     user_data = user.find_one({
#         "_id": ObjectId(user_id)
#     })

#     product_data = product.find_one({
#         "_id": ObjectId(product_id)
#     })

#     if not user_data:
#         print("User not found")
#         return

#     if not product_data:
#         print("Product not found")
#         return

#     if product_data["stock"] < quantity:
#         print("Not enough stock")
#         return

#     amount = product_data["price"] * quantity

#     order_data = {
#         "userId": ObjectId(user_id),
#         "productId": ObjectId(product_id),
#         "amount": amount,
#         "isPaid": False,
#         "quantity": quantity,
#         "isDelivered": False
#     }

#     order.insert_one(order_data)

#     product.update_one(
#         {"_id": ObjectId(product_id)},
#         {"$inc": {"stock": -quantity}}
#     )

#     print("Order created successfully")
#     print("Total amount:", amount)
# create_order()

# def get_order():
#     order_id = input("Enter order id: ")

#     result = order.find_one({
#         "_id": ObjectId(order_id)
#     })

#     if result:
#         print(result)
#     else:
#         print("Order not found")


# get_order()

# def update_order():
#     order_id = input("Enter order id: ")

#     is_paid = input("Is payment done? (yes/no): ")
#     is_delivered = input("Is order delivered? (yes/no): ")

#     result = order.update_one(
#         {"_id": ObjectId(order_id)},
#         {
#             "$set": {
#                 "isPaid": is_paid == "yes",
#                 "isDelivered": is_delivered == "yes"
#             }
#         }
#     )

#     if result.modified_count > 0:
#         print("Order updated successfully")
#     else:
#         print("Order not found")


# update_order()


# def delete_order():
#     order_id = input("Enter order id: ")

#     result = order.delete_one({
#         "_id": ObjectId(order_id)
#     })

#     if result.deleted_count > 0:
#         print("Order deleted successfully")
#     else:
#         print("Order not found")
# delete_order()


# def get_all_orders():
#     orders = order.find()
#     for o in orders:
#         print(o)
# get_all_orders()

# def get_user_orders():
#     user_id = input("Enter user id: ")

#     orders = order.find({
#         "userId": ObjectId(user_id)
#     })

#     found = False

#     for o in orders:
#         print(o)
#         found = True

#     if not found:
#         print("No orders found")
# get_user_orders()

# def check_stock():
#     product_id = input("Enter product id: ")

#     result = product.find_one({
#         "_id": ObjectId(product_id)
#     })

#     if result:
#         print("Product:", result["name"])
#         print("Available stock:", result["stock"])
#     else:
#         print("Product not found")
# check_stock()


# def search_product():
#     name = input("Enter product name: ")

#     results = product.find({
#         "name": {"$regex": name, "$options": "i"}
#     })

#     found = False

#     for p in results:
#         print(p)
#         found = True

#     if not found:
#         print("Product not found")
# search_product()


# def filter_products_by_price():
#     min_price = float(input("Enter minimum price: "))
#     max_price = float(input("Enter maximum price: "))

#     results = product.find({
#         "price": {
#             "$gte": min_price,
#             "$lte": max_price
#         }
#     })

#     found = False

#     for p in results:
#         print(p)
#         found = True

#     if not found:
#         print("No products found")
# filter_products_by_price()


# def get_available_products():
#     results = product.find({
#         "stock": {"$gt": 0}
#     })

#     found = False

#     for p in results:
#         print(p)
#         found = True

#     if not found:
#         print("No products available")
# get_available_products()



# def get_discount_products():
#     results = product.find({
#         "discount": {"$gt": 0}
#     })

#     found = False

#     for p in results:
#         print(p)
#         found = True

#     if not found:
#         print("No discount products found")
# get_discount_products()


# def get_order_amount():
#     order_id = input("Enter order id: ")

#     result = order.find_one({
#         "_id": ObjectId(order_id)
#     })

#     if result:
#         print("Order amount:", result["amount"])
#     else:
#         print("Order not found")
# get_order_amount()


# def get_paid_orders():
#     results = order.find({
#         "isPaid": True
#     })

#     found = False

#     for o in results:
#         print(o)
#         found = True

#     if not found:
#         print("No paid orders found")
# get_paid_orders()

# def get_delivered_orders():
#     results = order.find({
#         "isDelivered": True
#     })

#     found = False

#     for o in results:
#         print(o)
#         found = True

#     if not found:
#         print("No delivered orders found")
# get_delivered_orders()

# def get_pending_orders():
#     results = order.find({
#         "isPaid": False,
#         "isDelivered": False
#     })

#     found = False

#     for o in results:
#         print(o)
#         found = True

#     if not found:
#         print("No pending orders found")


# get_pending_orders()

# def get_all_order_details():
#     result = order.aggregate([
#         {
#             "$lookup": {
#                 "from": "folder",
#                 "localField": "userId",
#                 "foreignField": "_id",
#                 "as": "userDetails"
#             }
#         },
#         {
#             "$lookup": {
#                 "from": "products",
#                 "localField": "productId",
#                 "foreignField": "_id",
#                 "as": "productDetails"
#             }
#         }
#     ])

#     for o in result:
#         print(o)
# get_all_order_details()



# def get_ordered_product_by_user():
#     user_id = input("Enter user id: ")

#     result = order.aggregate([
#         {
#             "$match": {
#                 "userId": ObjectId(user_id)
#             }
#         },
#         {
#             "$lookup": {
#                 "from": "products",
#                 "localField": "productId",
#                 "foreignField": "_id",
#                 "as": "productDetails"
#             }
#         }
#     ])

#     found = False

#     for o in result:
#         print(o)
#         found = True

#     if not found:
#         print("No orders found for this user")
# get_ordered_product_by_user()


def update_delivery_status():
    order_id = input("Enter order id: ")

    result = order.update_one(
        {"_id": ObjectId(order_id)},
        {
            "$set": {
                "isDelivered": True
            }
        }
    )

    if result.modified_count > 0:
        print("Delivery status updated successfully")
    else:
        print("Order not found")


update_delivery_status()