# Game Lô Đề Học ProMax

Các tính năng

**Chức năng đăng nhập:**
- Nếu là tài khoản admin sẽ có menu riêng gồm quản lý tài khoản, nạp tiền tài khoản, thống kê và đăng xuất. 
- Nếu là tài khoản thường thì hiển thị menu thường gồm: chơi lô, đổi mật khẩu, thống kê và đăng xuất.
  
**Chức năng admin:**
- Quản lý tài khoản: tạo tài khoản (không được phép tạo trùng username) và xóa tài khoản (không được phép xóa tài khoản admin). Thông tin tài khoản gồm username, password, tổng tiền và được lưu vào trong file taikhoan.txt, mỗi tài khoản 1 dòng. 
- Nạp tiền: Chức năng nạp tiền sẽ cập nhật số tiền tài khoản trong file taikhoan.txt. 
- Thống kê: Chức năng thống kê sẽ thống kê có bao nhiêu tài khoản, số lượt chơi lô là bao nhiêu, tỷ lệ kèo thắng/thua.

**Chức năng người dùng:**
- Chức năng đổi  mật khẩu: Người chơi có thể đổi mật khẩu của họ
- Chức năng chơi lô: Mỗi lần chơi lô, thông tin sẽ tự được lưu vào file choilo.txt các thông tin: thời gian chơi, username, số lô cược, tiền cược, kết quả quay số, kết quả trúng lô, mỗi lần chơi là 1 dòng.
- Chức năng thống kê: Cho phép người dùng xem thống kê số lần chơi lô, tổng tiền chơi lô thắng, tổng tiền chơi lô thua, tỉ lệ chơi lô thắng/thua.
