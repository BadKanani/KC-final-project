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

print("--- python vending machine ---\n\n")
print("--- the products in stock are --- \n\n")

for i in products_available:
    print(f"Product: {i['Product_name']} --- Price {i['product_price']} --- Product number {i['product_number']}")


def sum(the_product):
    sum = 0
    for i in the_product:
        sum += i["product_price"]
        return sum