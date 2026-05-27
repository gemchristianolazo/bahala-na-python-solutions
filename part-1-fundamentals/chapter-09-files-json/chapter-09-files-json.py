import json

inventory = {
    "sardines": {"qty": 12, "price": 26},
    "candy": {"qty": 60, "price": 2},
    "instant noodles": {"qty": 15, "price": 17},
    "bread": {"qty": 0, "price": 8},
    "zesto": {"qty": 4, "price": 12},
    "softdrinks": {"qty": 3, "price": 15}
}

def save_data(filename, inventory):
    with open(filename, 'w') as file:
        json.dump(inventory, file, indent=4)

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

save_data("inventory.json", inventory)

loaded_inventory = load_data("inventory.json")
for item, details in loaded_inventory.items():
    print(f"""
        Item: {item}
        Quantity: {details['qty']}
        Price: {details['price']}
        """)