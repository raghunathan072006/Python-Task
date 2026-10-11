from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime


MongoURL = MongoClient(
    "mongodb+srv://xavier:xavier123@cluster0.p0p3ape.mongodb.net/?appName=Cluster0"
)

db = MongoURL["ecommerce_db"]

users = db["users"]
products = db["products"]
orders = db["orders"]

print("MongoDB Connected!")


# USER COLLECTION


# 1. ADD USER

def add_user():

    print("\n========== ADD USER ==========")

    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    mobile = input("Mobile: ")
    address = input("Address: ")

    # Check email

    if users.find_one({"email": email}):

        print("Email already exists!")
        return

    data = {
        "name": name,
        "email": email,
        "password": password,
        "createdAt": datetime.now(),
        "mobile": mobile,
        "address": address
    }

    users.insert_one(data)

    print("User added successfully!")


# 2. LOGIN

def login():

    print("\n========== LOGIN ==========")

    email = input("Email: ")
    password = input("Password: ")

    user = users.find_one({
        "email": email,
        "password": password
    })

    if user:

        print("Login successful!")
        print("Welcome", user["name"])

    else:

        print("Invalid email or password!")


# 3. GET ALL USERS

def get_users():

    print("\n========== ALL USERS ==========")

    for user in users.find():

        print("\nID:", user["_id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Mobile:", user["mobile"])
        print("Address:", user["address"])


# 4. GET SPECIFIC USER

def get_user():

    print("\n========== GET USER ==========")

    user_id = input("Enter User ID: ")

    user = users.find_one({
        "_id": ObjectId(user_id)
    })

    if user:

        print("\nID:", user["_id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Mobile:", user["mobile"])
        print("Address:", user["address"])

    else:

        print("User not found!")


# 5. UPDATE USER

def update_user():

    print("\n========== UPDATE USER ==========")

    user_id = input("Enter User ID: ").strip()

    name = input("New Name: ")
    mobile = input("New Mobile: ")
    address = input("New Address: ")
    email = input("New Email: ")

    update_data = {}

    if name != "":
        update_data["name"] = name

    if mobile != "":
        update_data["mobile"] = mobile

    if address != "":
        update_data["address"] = address

    if email != "":
        update_data["email"] = email

    users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    print("User updated!")





# 6. DELETE USER

def delete_user():

    print("\n========== DELETE USER ==========")

    user_id = input("Enter User ID: ")

    users.delete_one({
        "_id": ObjectId(user_id)
    })

    print("User deleted!")


# USER MENU

def user_menu():

    while True:

        print("\n==============================")
        print("       USER COLLECTION")
        print("==============================")

        print("1. Add User")
        print("2. Login")
        print("3. Get All Users")
        print("4. Get Specific User")
        print("5. Update User")
        print("6. Delete User")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            add_user()

        elif choice == "2":

            login()

        elif choice == "3":

            get_users()

        elif choice == "4":

            get_user()

        elif choice == "5":

            update_user()

        elif choice == "6":

            delete_user()

        elif choice == "7":

            break

        else:

            print("Invalid choice!")

# PRODUCT COLLECTION


# 7. ADD PRODUCT

def add_product():

    print("\n========== ADD PRODUCT ==========")

    name = input("Product Name: ")
    price = float(input("Price: "))
    model = input("Model: ")
    color = input("Color: ")
    stock = int(input("Stock: "))
    discount = float(input("Discount: "))

    product = {
        "name": name,
        "price": price,
        "model": model,
        "color": color,
        "stock": stock,
        "discount": discount
    }

    products.insert_one(product)

    print("Product added!")


# 8. GET ALL PRODUCTS

def get_products():

    print("\n========== ALL PRODUCTS ==========")

    for product in products.find():

        print("\nID:", product["_id"])
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Model:", product["model"])
        print("Color:", product["color"])
        print("Stock:", product["stock"])
        print("Discount:", product["discount"], "%")


# 9. GET SPECIFIC PRODUCT

def get_product():

    print("\n========== GET PRODUCT ==========")

    product_id = input("Enter Product ID: ")

    product = products.find_one({
        "_id": ObjectId(product_id)
    })

    if product:

        print("\nID:", product["_id"])
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Model:", product["model"])
        print("Color:", product["color"])
        print("Stock:", product["stock"])
        print("Discount:", product["discount"], "%")

    else:

        print("Product not found!")


# 10. UPDATE PRODUCT

def update_product():

    print("\n========== UPDATE PRODUCT ==========")

    product_id = input("Enter Product ID: ")

    price = float(input("New Price: "))
    stock = int(input("New Stock: "))

    if price != "":
       update_product["price"]=price

    if stock !="":
      update_product ["stock"]=stock
    

    products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": {update_product}}
    )

    print("Product updated!")


# 11. DELETE PRODUCT

def delete_product():

    print("\n========== DELETE PRODUCT ==========")

    product_id = input("Enter Product ID: ")

    products.delete_one({
        "_id": ObjectId(product_id)
    })

    print("Product deleted!")


# PRODUCT MENU

def product_menu():

    while True:

        print("\n==============================")
        print("      PRODUCT COLLECTION")
        print("==============================")

        print("1. Add Product")
        print("2. Get All Products")
        print("3. Get Specific Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            add_product()

        elif choice == "2":

            get_products()

        elif choice == "3":

            get_product()

        elif choice == "4":

            update_product()

        elif choice == "5":

            delete_product()

        elif choice == "6":

            break

        else:

            print("Invalid choice!")


# ORDER COLLECTION

# 12. CREATE ORDER

def create_order():

    print("\n========== PLACE ORDER ==========")

    user_id = input("Enter User ID: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Quantity: "))


    # Find user

    user = users.find_one({
        "_id": ObjectId(user_id)
    })


    # Find product

    product = products.find_one({
        "_id": ObjectId(product_id)
    })


    if not user:

        print("User not found!")
        return


    if not product:

        print("Product not found!")
        return


    # Check stock

    if product["stock"] < quantity:

        print("Not enough stock!")
        return


    # Calculate amount

    price = product["price"]

    discount = product["discount"]

    final_price = price - (
        price * discount / 100
    )

    amount = final_price * quantity


    # Order details

    print("\n==============================")
    print("       ORDER DETAILS")
    print("==============================")

    print("Product:", product["name"])
    print("Price:", price)
    print("Discount:", discount, "%")
    print("Price after discount:", final_price)
    print("Quantity:", quantity)
    print("Total Amount:", amount)


    confirm = input("\nPlace Order? (yes/no): ")


    if confirm.lower() != "yes":

        print("Order cancelled!")
        return


    # Create order

    order = {

        "userId": ObjectId(user_id),

        "productId": ObjectId(product_id),

        "amount": amount,

        "isPaid": False,

        "quantity": quantity,

        "orderedDate": datetime.now(),

        "isDelivered": False
    }


    orders.insert_one(order)


    # Decrease stock

    products.update_one(

        {
            "_id": ObjectId(product_id)
        },

        {
            "$inc": {
                "stock": -quantity
            }
        }
    )


    print("\nOrder successful!")

    print("Product:", product["name"])

    print("Quantity:", quantity)

    print("Amount:", amount)

    print(
        "Remaining Stock:",
        product["stock"] - quantity
    )


# 13. GET ALL ORDERS

def get_all_orders():

    print("\n========== ALL ORDERS ==========")

    for order in orders.find():

        user = users.find_one({
            "_id": order["userId"]
        })

        product = products.find_one({
            "_id": order["productId"]
        })


        print("\n====================")

        print("Order ID:", order["_id"])

        print("User:", user["name"])

        print("Product:", product["name"])

        print("Quantity:", order["quantity"])

        print("Amount:", order["amount"])

        print("Paid:", order["isPaid"])

        print("Delivered:",
              order["isDelivered"])


# 14. GET ORDERS BY USER

def get_user_orders():

    print("\n========== USER ORDERS ==========")

    user_id = input("Enter User ID: ")


    for order in orders.find({

        "userId": ObjectId(user_id)

    }):

        product = products.find_one({

            "_id": order["productId"]

        })


        print("\n====================")

        print("Order ID:",
              order["_id"])

        print("Product:",
              product["name"])

        print("Quantity:",
              order["quantity"])

        print("Amount:",
              order["amount"])

        print("Delivered:",
              order["isDelivered"])


# 15. UPDATE DELIVERY STATUS

def delivery():

    print("\n========== UPDATE DELIVERY ==========")

    order_id = input("Enter Order ID: ")


    orders.update_one(

        {
            "_id": ObjectId(order_id)
        },

        {
            "$set": {
                "isDelivered": True
            }
        }
    )


    print("Delivery status updated!")

# ORDER MENU

def order_menu():

    while True:

        print("\n==============================")
        print("       ORDER COLLECTION")
        print("==============================")

        print("1. Place Order")
        print("2. Get All Orders")
        print("3. Get Orders By User")
        print("4. Update Delivery")
        print("5. Exit")

        choice = input("\nEnter choice: ")


        if choice == "1":

            create_order()

        elif choice == "2":

            get_all_orders()

        elif choice == "3":

            get_user_orders()

        elif choice == "4":

            delivery()

        elif choice == "5":

            break

        else:

            print("Invalid choice!")

# MAIN MENU

while True:

    print("\n")
    print("==============================")
    print("          WELCOME😊")
    print("==============================")

    print("1. Add User")
    print("2. View Product🎁")
    print("3. Place Order")
    print("4. Exit👋")


    choice = input("\nEnter choice: ")


    if choice == "1":

        user_menu()


    elif choice == "2":

        product_menu()


    elif choice == "3":

        order_menu()


    elif choice == "4":

        print("\nThank you!")
        break


    else:

        print("Invalid choice!")