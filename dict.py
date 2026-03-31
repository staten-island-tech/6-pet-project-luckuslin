""" sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]
def receipt(orders):
    recipets = {}
    for order in orders:
        if order['name'] in recipets:
            recipets[order['name']]['qty'] += 1
        else:
            recipets [order['name']] = {
                'price': order['price'],
                'qty': 1
            }
    for sushi, value in recipets.items():
        price = value['price'] * value['qty']
        print(sushi, value['qty'], f"${price}")



receipt(sushi_orders)
 """




wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}
staff = {}


for wards, staff in wards.items:
    if wards['Cardiology'] in wards:
        staff['Cardiology']


