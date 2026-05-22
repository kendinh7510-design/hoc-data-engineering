# Bài 3 — Dictionary
# san_pham = [
#     {"ten": "Chuot", "gia": 250000, "so_luong": 5},
#     {"ten": "Ban_phim", "gia": 450000, "so_luong": 3},
#     {"ten": "Man_hinh", "gia": 3500000, "so_luong": 2},
#     {"ten": "Tai_nghe", "gia": 350000, "so_luong": 4}
# ]
# Viết chương trình:

# In tên và giá từng sản phẩm
# Tính tổng tiền từng sản phẩm (giá × số lượng)
# Tính tổng tiền toàn bộ đơn hàng

# Kết quả mong đợi:
# Chuot: 250,000 dong x 5 = 1,250,000 dong
# Ban_phim: 450,000 dong x 3 = 1,350,000 dong
# Man_hinh: 3,500,000 dong x 2 = 7,000,000 dong
# Tai_nghe: 350,000 dong x 4 = 1,400,000 dong
# Tong don hang: 11,000,000 dong

san_pham = [{"ten" : "chuot", "gia" : 250000, "so_luong" : 5},
            {"ten" : "Ban_phim", "gia" : 450000 , "so_luong" : 3},
            {"ten": "Man_hinh", "gia": 3500000, "so_luong": 2},
            {"ten": "Tai_nghe", "gia": 350000, "so_luong": 4}]
tong = 0
for i in range (len(san_pham)):
    print(san_pham[i]["ten"] +  ":" + str(san_pham[i]["gia"]) + " dong x" + str(san_pham[i]["so_luong"])+ " =" + 
          str(san_pham[i]["gia"] * san_pham[i]["so_luong"]) )
    tong += san_pham[i]["gia"] * san_pham[i]["so_luong"]
print("Tong don hang: " + str(tong) + " dong")  
