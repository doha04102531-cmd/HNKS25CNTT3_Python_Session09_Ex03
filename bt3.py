order_list = ["GE001", "GE002", "GE003"]

while True:
    print("""
    ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
            1. Hiển thị danh sách đơn hàng
            2. Thêm đơn hàng mới
            3. Xóa đơn hàng theo mã
            4. Thoát chương trình
""")
    choice = int(input('Nhập lựa chọn của bạn(1 - 4): '))

    if choice == 1:
        if len(order_list) == 0:
            print('Danh sách đơn hàng hiện đang trống')
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                list = order_list[i]
                print(f'{i+1}. {list}')

    elif choice == 2:
        new_order = input('Nhập mã đơn hàng mới: ').strip().upper()

        order_list.append(new_order)
        print('===  Thêm thành công  ===')

    elif choice == 3:
        del_order = input('Nhập mã đơn hàng cần xóa: ').strip().upper()

        if del_order in order_list :
            order_list.remove(del_order)
        else :
            print('Không tìm thấy mã đơn hàng cần xóa!')
    elif choice == 4:
        print('Thoát chương trình')
        break
    else :
        print('Lựa chọn không hợp lệ, vui lòng nhập lại!')
