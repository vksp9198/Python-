# Store Management System
# Concepts used :
# * Nested Dictionary
# * functions
# * CRUD Operations(Create ,Read , Update , Delete)
# * Loops
# * Conditionals
# * User Input                          .items() --> data traversal 
# * Data structure
store ={
    1 :{
        "name" : "Laptop",
        "price": 50000,
        "stock" : 5
    },
    2 :{
        "name" : "Keybord",
        "price":500,
        "stock" :4
    }
}

def delete_product():
    product_id = int(input("Enter Product id = "))
    if product_id in store:
        product_name = store[product_id]["name"]
        del store[product_id]
        print(f"Product : {product_name} successfully deleted!")
    else:
        print("Product NOT found!!")

def search_product():
    product_id = int(input("Enter Product id = "))
    if product_id in store:
        product_id_details = store[product_id]
        for key , value in product_id_details.items():
            print(f"{key} : {value}")
    else:
        print("Product NOT found!!")
def update_product():
    product_id = int(input("Enter Product id = "))
    if product_id in store:
        new_stock_quantity = int(input("Enter new quantity = "))
        store[product_id]["stock"] += new_stock_quantity
        print("Quantity Updated")
    else:
        print("Product NOT found!!")

def add_product():
    product_id = int(input("Enter Product id = "))
    if product_id in store:
        print("Product already Exists")
        return
    product_name = input("Enter Product Name = ")
    product_price = int(input("Enter Product Price = "))
    product_stock= int(input("Enter Product Quantity = "))
    
    # add data
    store[product_id] = {
        "name" : product_name,
        "price" : product_price,
        "stock" : product_stock
    }
    print("\nProduct Added successfully")
def show_products():
    print("\n------All PRODUCT DETAILS--------")
    for product_id, data in store.items():
        print(f"\nProduct ID : {product_id}")
        print(f"Name : {data["name"]}")
        print(f"Price : {data["price"]}")
        print(f"Stock : {data["stock"]}")
    

def main():
    while True:
        print("_" * 44)
        print("------------Store Data Management System------------")
        print("_" * 44)
        print("""
        1. Show Products
        2. Add Product
        3. Update Quantity
        4. Serch Product
        5. Delete Product
        6. Exit """)

        choice = input("Enter your choice = ")
        match(choice):
            case '1' : show_products()
            case '2' : add_product() 
            case '3' : update_product()
            case '4' : search_product()
            case '5' : delete_product()
            case '6' : 
                print("Programm Ended!!")
                break
            case _:
                print("Invalid choice!! ,Try again")

if __name__ == "__main__":
    main()

