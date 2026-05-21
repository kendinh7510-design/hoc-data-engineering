

def xep_loai(diem):
    if diem >= 8:
        return "Gioi"
    elif diem >= 6.5:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"
    
def tinh_bmi(can_nang, chieu_cao):
    BMI = can_nang / (chieu_cao **2)
    if BMI < 18.5:
        return "Gay"
    elif BMI < 25:
        return "Binh_thuong"
    else:
        return "Beo_phi"
    
def dem_tu(chuoi):
    return(len(chuoi.split(" ")))

print(xep_loai(8.5))
print(xep_loai(6.0))
print(tinh_bmi(70, 1.75))
print(dem_tu("Data Engineering rat thu vi"))

