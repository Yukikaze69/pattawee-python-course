prices = []
buy_list = []
total_cost = 0

for i in range(6):
    price = float(input(f"กรอกราคาสินค้ารายการที่ {i + 1}: "))
    prices.append(price)

budget = float(input("กรอกงบประมาณรวม: "))

print("\nผลการพิจารณาการซื้อ")

for i in range(6):
    if total_cost + prices[i] <= budget:
        print(f"สินค้ารายการที่ {i + 1}: {prices[i]} บาท -> buy")
        total_cost += prices[i]
        buy_list.append(prices[i])
    else:
        print(f"สินค้ารายการที่ {i + 1}: {prices[i]} บาท -> cannot buy")

print("\nรายการสินค้าที่ซื้อได้:", buy_list)
print("ยอดใช้จ่ายรวม:", total_cost, "บาท")
print("งบประมาณคงเหลือ:", budget - total_cost, "บาท")