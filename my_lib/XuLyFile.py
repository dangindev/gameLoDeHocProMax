def ghi_file(data, ten_file, mode):
    try:
        with open(ten_file, mode) as file:
            for line in data:
                file.write(line + '\n')
        print("Dữ liệu đã được ghi vào file thành công.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def doc_file(duong_dan, mode):
    try:
        with open(duong_dan, mode) as file:
            du_lieu = file.readlines()
        return du_lieu
    except Exception as e:
        print(f"Có lỗi xảy ra khi đọc file: {e}")
        return None