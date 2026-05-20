# Bài 2 — List và vòng lặp 
# diem = [8, 6, 9, 5, 7, 10, 4, 8, 6, 9]
# Viết chương trình:

# In ra tổng số học sinh
# Tính điểm trung bình
# Đếm bao nhiêu học sinh đạt (điểm >= 5)
# Đếm bao nhiêu học sinh rớt (điểm < 5)

# Kết quả mong đợi:
# Tong so hoc sinh: 10
# Diem trung binh: 7.2
# So hoc sinh dat: 9
# So hoc sinh rot: 1

from itertools import count


diem = [8, 6, 9, 5, 7, 10, 4, 8, 6, 9]

print("Tong so hoc sinh:", len(diem))
total = 0
passed =0
failed = 0
for i in range(len(diem)):
    total += diem[i]
    if diem[i] >= 5:
        passed += 1
    else:
        failed += 1

print("Diem trung binh:", total / len(diem))

print("So hoc sinh dat:", passed)
print("So hoc sinh rot:", failed)
