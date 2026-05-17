"""
Một cấu trúc xử lý lỗi đầy đủ trong Python không chỉ có try và except, nó còn có thể mở rộng thêm 2 khối lệnh nữa là else và finally. Cụ thể vai trò của từng khối:

try: Nơi chứa code có thể gây lỗi.

except: Chạy chỉ khi khối try bị lỗi.

else: Chạy chỉ khi khối try thực hiện thành công và không có lỗi nào xảy ra.

finally: Luôn luôn chạy, bất kể code trong try có lỗi hay không. Thường dùng để dọn dẹp hệ thống (đóng file, ngắt kết nối database...).
"""
def chia_tien ():
    try:
        tong_bill = float(input("nhap so tien tren hoa don"))
        so_nguoi = int(input("nhap so_nguoi"))

        moi_nguoi_tra = tong_bill / so_nguoi

    except ZeroDivisionError as e:
        print(e)
        moi_nguoi_tra = 0

    except ValueError as e:
        print(e)
        moi_nguoi_tra = 0

    print(moi_nguoi_tra)

chia_tien()

