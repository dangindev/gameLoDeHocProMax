def quay_so():
    danh_sach_giai = {}

    ten_giai = ["GIẢI NHẤT", "GIẢI NHÌ", "GIẢI BA", "GIẢI TƯ", "GIẢI NĂM", "GIẢI SÁU", "GIẢI BẢY"]

    for giai in ten_giai:
        so = ""
        for i in range(5):
            so += str(random.randint(0, 9))  # Tạo một chữ số ngẫu nhiên từ 0 đến 9 và thêm vào số
        danh_sach_giai[giai] = so

    return danh_sach_giai


def in_danh_sach_giai(danh_sach_giai):
    print('-' * 20)
    print("---DANH SÁCH GIẢI---")
    for giai, so in danh_sach_giai.items():
        print(f"{giai}: {so}")
    print('-' * 20)

def nhap_so_lo():
    while True:
        so_lo = input("Nhập số lô mà bạn muốn cược (10-99): ")
        if so_lo.isdigit() and 10 <= int(so_lo) <= 99:
            return int(so_lo)
        else:
            print("Nhập sai định dạng, vui lòng nhập lại!")

def nhap_so_lo():
    while True:
        so_lo_input = input("Nhập các số lô bạn muốn chơi, cách nhau bằng dấu phẩy: ")
        danh_sach_so_lo = so_lo_input.split(",")

        so_lo_hop_le = True

        for so_lo in danh_sach_so_lo:
            if len(so_lo) != 2 or not so_lo.isdigit():
                print("Số lô nhập không hợp lệ. Vui lòng nhập lại.")
                so_lo_hop_le = False
                break

        if so_lo_hop_le:
            return danh_sach_so_lo

def nhap_tien_cuoc():
    while True:
        tien_cuoc = input("Nhập tiền cược mà bạn muốn cược (tiền cược < tổng tiền bạn có): ")
        if tien_cuoc.isdigit() and int(tien_cuoc) < tong_tien:
            return int(tien_cuoc)
        else:
            print("Nhập sai định dạng hoặc quá tổng tiền. Nhập lại")

def game_quay_so(danh_sach_so_lo, tien_cuoc):
    global tong_tien

    danh_sach_giai = quay_so()
    
    in_danh_sach_giai(danh_sach_giai)
    dem_so_lo = 0
    so_lo_trung = []  # Danh sách lưu trữ số lô trúng

    print("Các số lô bạn chơi là:", danh_sach_so_lo)
    for giai, so_giai in danh_sach_giai.items():
        for so_lo in danh_sach_so_lo:
            if so_lo == so_giai[-2:]:
                dem_so_lo += 1
                so_lo_trung.append(so_lo)

    if dem_so_lo > 0:
        tien_thang = tien_cuoc * dem_so_lo * 70
        tien_thua = tien_cuoc * (len(danh_sach_so_lo) - len(so_lo_trung))

        tong_tien += tien_thang - tien_thua

        print(f"Bạn đã trúng {dem_so_lo} nháy!")
        print("Các số lô trúng:", ", ".join(so_lo_trung))
        print(f"Số tiền bạn trúng là {tien_thang}")
        print(f"Số tiền bạn thua là {tien_thua}")
        print(f"Tổng tiền bạn có là {tong_tien}")
    else:
        tien_thua = tien_cuoc * len(danh_sach_so_lo)
        tong_tien -= tien_thua

        print("Bạn đã thua lô!")
        print(f"Số tiền bạn thua là {tien_thua}")
        print(f"Tổng tiền bạn còn là {tong_tien}")

def nap_tien():
    global tong_tien
    while True:
        tien_nap = int(input("Nhập số tiền mà bạn muốn nạp: "))
        tong_tien += tien_nap
        print(f"Tổng tiền sau khi bạn nạp là {tong_tien}")
        nap_tiep = int(input("Bạn có muốn nạp tiếp không? (0: không, 1: có)"))
        if nap_tiep == 0:
            break
        else:
            continue

def dang_nhap():
    global dang_nhap_status
    print("---GAME LÔ ĐỀ HỌC---")
    print("Vui lòng đăng nhập để chơi game")
    
    while True:
        username = input("Nhập username: ")
        password = input("Nhập password: ")

        if username == "admin" and password == "admin":
            dang_nhap_status = True
            break
        else:
            print("Sai tên người dùng hoặc mật khẩu, vui lòng thử lại.")
    clear_output()
    menu()