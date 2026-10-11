from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# MONGODB CONNECTION

mongourl = MongoClient("mongodb+srv://raghu07:raghu07@cluster0.kvvxso6.mongodb.net/?appName=Cluster0")
try:
    mongourl.admin.command("ping")
    print("MongoDB Connected Successfully!")
except Exception as e:
    print("MongoDB Connection Failed!")
    print(e)
mydata = mongourl["python_project"]
user = mydata["userid"]
product = mydata["product"]
order = mydata["order"]


# USER FUNCTIONS
def add_user():

    print("\nCome on! Let's create an account")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    mobile = int(input("Enter your mobile: "))
    address = input("Enter your address: ")
    if not name.strip():
        print("plz enter name")
        return
    existing = user.find_one({"email": email})

    if existing:
        print("Email already exists")
        return

    userdata = {
        "name": name,
        "email": email,
        "password": password,
        "mobile": mobile,
        "address": address,
        "date":datetime.now()
    }

    user.insert_one(userdata)

    print("User added successfully!")


def login_user():

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    result = user.find_one({
        "email": email,
        "password": password
    })

    if result:
        print("Login successful!")
    else:
        print("Invalid email or password")


def get_all_users():

    users = user.find()

    for u in users:
        print("ID:",u["_id"])
        print("name:",u["name"])
        print("email:",u["email"])
        print("password:",u["password"])
        print("mobile:",u["mobile"])
        print("address:",u["address"])
        print("date:",u["date"])


def get_user():

    user_id = input("Enter user id: ")

    result = user.find_one({
        "_id": ObjectId(user_id)
    })

    if result:
        print("ID:",result["_id"])
        print("name:",result["name"])
        print("email:",result["email"])
        print("mobile:",result["mobile"])
        print("address:",result["address"])
    else:
        print("User not found")


def update_user():
    email=input("enter new email:")
    users=user.find_one({"email":email})

    if users:
        name=input("enter new name:")
        mobile=input("enter new mobile:")
        address=input("enter new address:")
        updata={}
        if name.strip():
            updata["name"]=name
        if mobile.strip():
            updata["mobile"]=mobile
        if address.strip():
            updata["address"]=address
        if updata:
            user.update_one(
                {"email":email},
                {"$set":updata})
            print("User updated successfully")
    else:
        print("User not found")


def delete_user():

    user_id = input("Enter user id: ")

    result = user.delete_one({
        "_id": ObjectId(user_id)
    })

    if result.deleted_count > 0:
        print("User deleted successfully")
    else:
        print("User not found")


# USER MENU

def user_menu():

    while True:

        print("\nWELCOME TO USER COLLECTION")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Get All Users")
        print("4. Get One User")
        print("5. Update User")
        print("6. Delete User")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()

        elif choice == "2":
            login_user()

        elif choice == "3":
            get_all_users()

        elif choice == "4":
            get_user()

        elif choice == "5":
            update_user()

        elif choice == "6":
            delete_user()

        elif choice == "7":
            print("Thank you")
            break

        else:
            print("Invalid choice")


# PRODUCT FUNCTIONS

def add_product():

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    model = input("Enter product model: ")
    color = input("Enter product color: ")
    stock = int(input("Enter product stock: "))
    discount = float(input("Enter product discount: "))

    product_data = {
        "name": name,
        "price": price,
        "model": model,
        "color": color,
        "stock": stock,
        "discount": discount
    }

    product.insert_one(product_data)

    print("Product added successfully!")


def get_all_products():

    print("\n all product")
    for i in product.find():
        print("\nID:",i["_id"])
        print("name:",i["name"])
        print("price:",i["price"])
        print("model:",i["model"])
        print("color:",i["color"])
        print("stock:",i["stock"])
        print("discount:",i["discount"],"%")


def get_product():

    product_id = input("Enter product id: ")
    try:
        result = product.find_one({
             "_id": ObjectId(product_id)
    })

        if result:
            print("ID:", product["_id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Model:", product["model"])
            print("Color:", product["color"])
            print("Stock:", product["stock"])
            print("Discount:", product["discount"], "%")
        else:
            print("product not found")
    except:
        print("invalid product id")

def update_product():

    product_id = input("Enter product id: ")
    if product_id:
        name = input("Enter new product name: ")
        price = input("Enter new price: ")
        stock = input("Enter new stock: ")
        discount = input("Enter new discount: ")
        updata={}
        if name.strip():
            updata["name"]=name
        if price.strip():
            updata["price"]=float(price)
        if stock.strip():
            updata["stock"]=int(stock)
        if discount.strip():
            updata["discount"]=float(discount)
        if updata:
            product.update_one(
                {"-id":ObjectId(product_id)},
                {"$set":updata}
            )
        print("product update succesfully")
    else:
        print("Product not found")


def delete_product():

    product_id = input("Enter product id: ")

    result = product.delete_one({
        "_id": ObjectId(product_id)
    })

    if result.deleted_count > 0:
        print("Product deleted successfully")
    else:
        print("Product not found")


# PRODUCT MENU

def product_menu():

    while True:

        print("\nWELCOME TO PRODUCT COLLECTION")
        print("1. Add Product")
        print("2. Order Product")
        print("3. Get All Products")
        print("4. Get One Product")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            create_order()

        elif choice == "3":
            get_all_products()

        elif choice == "4":
            get_product()

        elif choice == "5":
            update_product()

        elif choice == "6":
            delete_product()

        elif choice == "7":
            break

        else:
            print("Invalid choice")


# ORDER FUNCTION

def create_order():

    print("\nCome on! Let's place our order")

    user_id = input("Enter User ID: ")
    product_id = input("Enter Product ID: ")
    quantity = int(input("Enter your quantity: "))
    date=datetime.now()

    user_data = user.find_one({
        "_id": ObjectId(user_id)
    })

    product_data = product.find_one({
        "_id": ObjectId(product_id)
    })

    if not user_data:
        print("User not found")
        return

    if not product_data:
        print("Product not found")
        return

    if product_data["stock"] < quantity:
        print("Not enough stock")
        return

    price = product_data["price"]
    discount = product_data["discount"]

    discount_amount = price * discount / 100

    price_after_discount = price - discount_amount

    total_amount = price_after_discount * quantity

    order_data = {
        "userId": ObjectId(user_id),
        "productId": ObjectId(product_id),
        "amount": total_amount,
        "isPaid": False,
        "quantity": quantity,
        "isDelivered": False
    }

    result = order.insert_one(order_data)

    product.update_one(
        {"_id": ObjectId(product_id)},
        {
            "$inc": {
                "stock": -quantity
            }
        }
    )

    print("\n==============================")
    print("        ORDER SUMMARY")
    print("==============================")

    print("Product:", product_data["name"])
    print("M.R.P: ₹", price)
    print("Discount: ₹", discount_amount)
    print("Discount Percentage:", discount, "%")
    print("Price after discount: ₹", price_after_discount)
    print("Quantity:", quantity)

    print("------------------------------")
    print("TOTAL AMOUNT: ₹", total_amount)
    print("==============================")

    print("\nOrder placed successfully!")
    print("Order ID:", result.inserted_id)

def get_all_orders():
    print("\n========== ALL ORDERS ==========")

    for orders in order.find():

        users = user.find_one({
            "_id": orders["userId"]
        })

        products = product.find_one({
            "_id": orders["productId"]
        })

        print("\n====================")
        print("Order ID:", orders["_id"])

        if users:
            print("User:", users["name"])
        else:
            print("User: User not found")

        if products:
            print("Product:", products["name"])
        else:
            print("Product: Product not found")

        print("Quantity:", orders["quantity"])
        print("Amount:", orders["amount"])
        print("Paid:", orders["isPaid"])
        print("Delivered:", orders["isDelivered"])


#  GET ORDERS BY USER

def get_user_orders():

    print("\n========== USER ORDERS ==========")

    user_id = input("Enter User ID: ")

    for orders in order.find({
        "userId": ObjectId(user_id)
    }):

        products = product.find_one({
            "_id": orders["productId"]
        })

        print("\n====================")
        print("Order ID:", orders["_id"])

        if products:
            print("Product:", products["name"])
        else:
            print("Product: Product not found")

        print("Quantity:", orders["quantity"])
        print("Amount:", orders["amount"])
        print("Delivered:", orders["isDelivered"])


# UPDATE DELIVERY STATUS

def delivery():

    print("\n========== UPDATE DELIVERY ==========")

    order_id = input("Enter Order ID: ")


    order.update_one(

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

    print("\nWELCOME 😊")
    print("1. Add User")
    print("2. View Products")
    print("3. Place Order")
    print("4. Exit")

    choice = input("What do you want to do?: ")

    if choice == "1":

        user_menu()

    elif choice == "2":

        product_menu()

    elif choice == "3":

        order_menu()

    elif choice == "":

        print("Thank you!")
        print("Bye 👋")
        break

    else:

        print("Invalid choice")