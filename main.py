from coinex.login.module_login import * #นำเข้า login
from coinex.thb_btc.module_btc import * 
from coinex.thb_cny.module_cny import *
from coinex.thb_eth.module_eth import *
from coinex.thb_eur.module_eur import *
from coinex.thb_krw.module_krw import *
from coinex.thb_usd.module_usd import *
from coinex.thb_yen.module_yen import *

print("กรุณาเข้าสู่ระบบ")
login()

print("สกุลเงิน")
print("1.บาทเป็นบิทคอยด์")
print("2.บาทเป็นหยวน")
print("3.บาทเป็นอีทีเรี่ยม")
print("4.บาทเป็นยูโร")
print("5.บาทเป็นวอน")
print("6.บาทเป็นดอลลาร์")
print("7.บาทเป็นเยน")
print("8.จบการทำงาน")

while True:
    select = int(input("เลือกสกุลเงินที่ท่านต้องการแปลง: "))
    
    if select == 1:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_btc(thb)
    elif select ==2:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_cny(thb)
    elif select ==3:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_eth(thb)
    elif select ==4:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_eur(thb)
    elif select ==5:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_krw(thb)
    elif select ==6:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_usd(thb)
    elif select ==7:
        thb = int(input("ใส่จำนวนเงินบาท: "))
        thb_yen(thb)
    else:
        print("จบการทำงาน")
        break
    