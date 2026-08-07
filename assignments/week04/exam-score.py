scores = []

# รับคะแนนนักเรียน 5 คน
for i in range(5):
    score = float(input(f"กรอกคะแนนนักเรียนคนที่ {i + 1}: "))
    scores.append(score)

print("\nผลการสอบ")

# ตรวจสอบคะแนน
for i in range(5):
    if scores[i] >= 50:
        print(f"นักเรียนคนที่ {i + 1}: {scores[i]} คะแนน - ผ่าน")
    else:
        print(f"นักเรียนคนที่ {i + 1}: {scores[i]} คะแนน - ไม่ผ่าน")