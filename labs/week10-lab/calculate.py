try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+,-,*,/): ")
    result = 0 
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
    else:
        raise ValueError

    print("ผลลัพธ์:", result)
except ValueError:
    print("กรุณาป้อนตัวเลขหรือเครื่องหมายให้ถูกต้อง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")    