inventory = []
sales_records = []

def add_snack():
    snack = {}
    snack['id'] = input("Enter snack ID: ")
    snack['name'] = input("Enter snack name: ")
    snack['price'] = float(input("Enter snack price: "))
    snack['availability'] = True
    for item in inventory:
        if item['id'] == snack['id']:
            print("Snack with the same ID already exists!")
            return
    inventory.append(snack)
    print("Snack added successfully!")

def remove_snack():
    snack_id = input("Enter snack ID to remove: ")
    found_snack = None
    for snack in inventory:
        if snack['id'] == snack_id:
            found_snack = snack
            break
    if found_snack:
        inventory.remove(found_snack)
        print("Snack removed successfully!")
    else:
        print("Snack not found!")

def update_availability():
    snack_id = input("Enter snack ID to update availability: ")
    found_snack = None
    for snack in inventory:
        if snack['id'] == snack_id:
            found_snack = snack
            break
    if found_snack:
        new_availability = input("Enter new availability (yes/no): ")
        if new_availability.lower() == "yes":
            found_snack['availability'] = True
        elif new_availability.lower() == "no":
            found_snack['availability'] = False
        else:
            print("Invalid input! Availability not updated.")
            return
        print("Availability updated successfully!")
    else:
        print("Snack not found!")

def record_sale():
    snack_id = input("Enter snack ID sold: ")
    found_snack = None
    for snack in inventory:
        if snack['id'] == snack_id:
            found_snack = snack
            break
    if found_snack:
        if found_snack['availability']:
            sales_records.append(snack_id)
            found_snack['availability'] = False
            print("Sale recorded successfully!")
        else:
            print("Snack is already sold!")
    else:
        print("Snack not found!")

# Testing the functions
add_snack()
add_snack()
print(inventory)

remove_snack()
print(inventory)

update_availability()
print(inventory)

record_sale()
print(inventory)
print(sales_records)
