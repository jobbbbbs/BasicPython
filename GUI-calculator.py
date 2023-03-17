#GUI-calculator.py

from tkinter import * # import * คือ import ทั้งหมดของแพ็คเกจ
from tkinter import ttk ,messagebox # messagebox = ป๊อปอัพ

GUI = Tk() # ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณปลารถพุ่มพวง') # กำหนดชื่อโปรแกรม
GUI.geometry('700x600') # กำหนดขนาดหน้าต่างโปรแกรม

#วิธีใส่รูปภาพ * ไฟล์ .png
bg = PhotoImage(file='car.png') 

BG = Label(GUI, image=bg)
BG.pack() #เป็นการเอาเข้ามูลที่สร้างขึ้นแปะใน GUI

L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=('Angsana New','20'))# ใส่ข้อความ/font/ขนาดอักษร
L.pack() # เอา Label ใส่โปรแกรม

# เพิ่มช่องกรอกข้อมูล
v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=('Angsana New','20')) # textvariable= ตัวแปรพิเศษใช้เพื่อเก็บข้อมูล
E1.pack()


# สร้างป๊อปอัพ
def Cal():
    try: #ดักจับ error
        quan = float(v_quantity.get()) #รับค่าตัวแปร และแปลงเป็นประเภทจุดทศนิยม
        calc = quan * 39 # กำหนดให้กิโลละ 39 บาท * จำนวนปลา
        messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc)) # ชื่อกล่องข้อความ, ไตเติ้ลที่จะโชว์
        v_quantity.set('1') #เคลียร์ข้อความ เป็นค่าเริ่มต้น คือ 1
        E1.focus() #เมื่อกรอกเสร็จให้ cersor ไปอยู่ที่ช่องกรอกเลย เพื่อกรอกข้อมูลถัดไป
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น') #ดักจับ error ชื่อกล่องข้อความ, ไตเติ้ลที่จะโชว์
        v_quantity.set('1') #เคลียร์ข้อความ เป็นค่าเริ่มต้น คือ 1
        E1.focus()

#สร้างปุ่ม
B = ttk.Button(GUI, text='คำนวณ',command=Cal) #เปลี่ยน font ด้วยวิธีทั่วไปไม่ได้
B.pack(ipadx=30,ipady=20,pady=20) # ipadx/y = กำหนดขนาดปุ่ม ความกว้างยาว x/y // pady = เว้นระยะช่องว่าง


GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา