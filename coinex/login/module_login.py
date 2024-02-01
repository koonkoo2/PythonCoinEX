def login():
    set_pass = int(input("ตั้งรหัสผ่าน: "))
    for i in range(0,3):
        input_pass = int(input("ใส่รหัสผ่าน: "))
        if set_pass == input_pass:
            print("เข้าสู่ระบบสำเร็จ")
            break
        else:
            print("กรุณากรอกรหัสผ่านอีกครั้ง")
