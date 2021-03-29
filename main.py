from tkinter import*
import qrcode
from PIL import Image,ImageTk 
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self, root):
        root.geometry("900x500+200+50")
        root.title("QR CODE GENERATOR !")
        root.resizable(False, False)
        title = Label(root, text="QR CODE GENERATOR !", font=(
            "times new roman", 40), bg='#053246', fg="white").place(x=0, y=0, relwidth=1)

        # ********* Detail Window **********
        # ********* Variables **********
        self.var_emp_id = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_dept = StringVar()
        self.var_emp_designation = StringVar()

        det_Frame = Frame(root, bd=2, relief=RIDGE, bg="white")
        det_Frame.place(x=50, y=100, width=500, height=380)

        det_title = Label(det_Frame, text="Enter Details", font=(
            "goudy old style", 20, "bold"), bg='#043246', fg="white").place(x=0, y=0, relwidth=1)

        lbl_emp_id = Label(det_Frame, text="Employee ID", font=(
            "times new roman", 15, 'bold')).place(x=20, y=60)

        lbl_emp_name = Label(det_Frame, text="Name", font=(
            "times new roman", 15, 'bold')).place(x=20, y=100)

        lbl_emp_dept = Label(det_Frame, text="Department", font=(
            "times new roman", 15, 'bold')).place(x=20, y=140)

        lbl_emp_designation = Label(det_Frame, text="Designation", font=(
            "times new roman", 15, 'bold')).place(x=20, y=180)

        # ***** text field *****

        self.txt_emp_id = Entry(det_Frame, font=(
            "times new roman", 15, 'bold'), textvariable=self.var_emp_id, bg="lightyellow")
        self.txt_emp_id.place(x=200, y=60)

        self.txt_emp_name = Entry(det_Frame, font=(
            "times new roman", 15, 'bold'), textvariable=self.var_emp_name, bg="lightyellow")
        self.txt_emp_name.place(x=200, y=100)

        self.txt_emp_dept = Entry(det_Frame, font=(
            "times new roman", 15, 'bold'), textvariable=self.var_emp_dept, bg="lightyellow")
        self.txt_emp_dept.place(x=200, y=140)

        self.txt_emp_designation = Entry(det_Frame, font=(
            "times new roman", 15, 'bold'), textvariable=self.var_emp_designation, bg="lightyellow")
        self.txt_emp_designation.place(x=200, y=180)

        # ***** Buttons *****

        btn_generate = Button(det_Frame, text="Generate QR", command=self.generate, font=(
            "times new roman", 18, 'bold'), bg="#053246", fg="white").place(x=90, y=240, width="180", height="30")
        btn_clear = Button(det_Frame, text="Clear", command=self.clear, font=(
            "times new roman", 18, 'bold'), bg="#607d8b", fg="white").place(x=282, y=240, width="120", height="30")

        self.msg = ""
        self.lbl_msg = Label(det_Frame, text=self.msg, font=(
            "times new roman", 20), bg="white")
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        # ********* QR Code Window **********
        self.qr_Frame = Frame(root, bd=2, relief=RIDGE, bg="white")
        self.qr_Frame.place(x=600, y=100, width=250, height=380)

        self.qr_title = Label(self.qr_Frame, text="QR Code", font=(
            "goudy old style", 20, "bold"), bg='#043246', fg="white")
        self.qr_title.place(x=0, y=0, relwidth=1)

        # ***** QR Code Image *****

        self.qr_code = Label(self.qr_Frame, text="QR Code \n Not Available", font=(
            "times new roman", 20), bg='#3f51b5', fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_id.set('')
        self.var_emp_name.set('')
        self.var_emp_dept.set('')
        self.var_emp_designation.set('')
        self.qr_code.config(image = '')

        self.msg = ""
        self.lbl_msg.config(text=self.msg)

        self.txt_emp_id.focus()

    def generate(self):
        if self.var_emp_id.get() == '' or self.var_emp_name.get() == '' or self.var_emp_dept.get() == '' or self.var_emp_designation.get() == '':
            self.msg = "Please Enter All Details !!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (f"Employee ID : {self.var_emp_id.get()}\nEmployee Name : {self.var_emp_name.get()}\nEmployee Dept : {self.var_emp_dept.get()}\nEmployee Designation : {self.var_emp_designation.get()}")
            qr_code1 = qrcode.make(qr_data)
            #****** QR Image *****
            qr_code1 = resizeimage.resize_cover(qr_code1,[180,180])
            qr_code1.save("QR_CODES/EMP_"+str(self.var_emp_id.get())+".png")

            self.im = ImageTk.PhotoImage(
                file ="QR_CODES/EMP_"+str(self.var_emp_id.get())+".png")
            self.qr_code.config(image = self.im)

            #***** Notification *****
            self.msg = "QR Code Generated Successfully !!"
            self.lbl_msg.config(text=self.msg, fg="green")


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
