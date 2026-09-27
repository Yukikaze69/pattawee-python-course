def deposit(money):
    balance = 1000

    print(f"ยอดเงินเริ่มต้น: {balance} บาท")

    try:
        money = float(money)

        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

        balance += money

    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    else:
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")


money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money)