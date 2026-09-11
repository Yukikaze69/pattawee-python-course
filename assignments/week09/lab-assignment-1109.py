def calculate_electricity_cost(units):
    if unit < 0:
        return None

    if unit <= 50:
        cost1 = unit * 2.50
        cost2 = 0
        cost3 = 0

    elif unit <= 100:
        cost1 = 50 * 2.50
        cost2 = (unit - 50) * 3.00
        cost3 = 0

    else:
        cost1 = 50 * 2.50
        cost2 = 50 * 3.00
        cost3 = (unit - 100) * 3.50

    electricity_cost = cost1 + cost2 + cost3
    service_charge = 25
    total = electricity_cost + service_charge

    return cost1, cost2, cost3, service_charge, total


def show_result(unit):
    result = calculate_electricity_cost(units)

    if result is None:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
        return

    cost1, cost2, cost3, service_charge, total = result

    print("\nรายละเอียดค่าไฟ:")
    print(f"1-50 หน่วย: {cost1:.2f} บาท")
    print(f"51-100 หน่วย: {cost2:.2f} บาท")
    print(f"101-{unit:g} หน่วย: {cost3:.2f} บาท")
    print(f"ค่าบริการ: {service_charge:.2f} บาท")
    print(f"ยอดรวมสุทธิ: {total:.2f} บาท")


# โปรแกรมหลัก
while True:
    print("\n===== โปรแกรมคำนวณค่าไฟฟ้า =====")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")

    menu = input("เลือกเมนู: ")

    if menu == "1":
        unit = float(input("กรอกจำนวนหน่วยไฟฟ้า: "))
        show_result(unit)

    elif menu == "2":
        print("ออกจากโปรแกรม")
        break

    else:
        print("เลือกเมนูไม่ถูกต้อง กรุณาเลือกใหม่")