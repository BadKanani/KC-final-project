products_available = [
{
    "product_number" : 0,
    "product_name" : "gfuel energy drink",
    "product_price" : 1,
},
{
    "product_number" : 1,
    "product_name" : "kitkat",
    "product_price" : 0.150,
},
{
    "product_number" : 2,
    "product_name" : "redbull",
    "product_price" : 0.750,
},
{
    "product_number" : 3,
    "product_name" : "orangesso",
    "product_price" : 1.750,
},
{
    "product_number" : 4,
    "product_name" : "voss water",
    "product_price" : 0.500,
},
{
    "product_number" : 5,
    "product_name" : "jelly beans",
    "product_price" : 0.250,
},
{
    "product_number" : 6,
    "product_name" : "nuka cola",
    "product_price" : 20,
},
{
    "product_number" : 7,
    "product_name" : "winston's peanut butter",
    "product_price" : 1.500,
},
]


the_product = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

run = True

print("------- Vending Machine with Python-------\n\n")
print("----------Products Available Are----------\n\n")

for i in products_available:
    print(f"Product: {i['product_name']} --- Price: {i['product_price']} --- Product number: {i['product_number']}")


def machine(products_available, run, the_product):
    while run:

        buy_product = int(input("\n\nEnter the digit of the product you desire: "))

        if buy_product < len(products_available):
            the_product.append(products_available[buy_product])
        else:
            print("HE DIGIT YOU ENTERED IS WRONG!")

        more_products = str(input("press any key to add more items and press q to quit"))

        if more_products == "q":
            run = False

    rec_bool = int(input(("1. print the reciept? 2. only print the total sum")))
    if rec_bool == 1:
        print(create_reciept(the_product, reciept))
    elif rec_bool == 2:
        print(sum(the_product))
    else:
        print("INVALID ENTRY")


def sum(the_product):
    sum = 0

    for i in the_product:
        sum += i["product_price"]

    return sum

def create_reciept(the_product, reciept):

    for i in the_product:
        reciept += f"""
        \t{i["product_name"]} -- {i['product_price']}
        """

    reciept += f"""
        \tTotal --- {sum(the_product)}
        
        
        """
    return reciept


if __name__ == "__main__":
    machine(products_available, run, the_product)
                            