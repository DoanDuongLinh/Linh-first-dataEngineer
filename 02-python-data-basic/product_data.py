products = [
    {"id": "P001", "name": "Ca phe sua", "price": 25000},
    {"id": "P002", "name": "Tra dao", "price": 30000},
    {"id": "P003", "name": "Bac xiu", "price": 28000}
]

print("Danh sach san pham:")

for product in products:
    print(product["id"], "-", product["name"], "-", product["price"])