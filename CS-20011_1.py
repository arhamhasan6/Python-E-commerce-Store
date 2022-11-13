import csv
from tkinter import * 
from tkinter import ttk
import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import datetime
from abc import ABC, abstractclassmethod

class FileHandler(ABC):
    @abstractclassmethod
    def writing_to_file(self):
        pass
    def reading_from_file(self):
        pass


class CSVFiling(FileHandler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def setting_fields(self, list_of_fields=['Name', 'Empty', 'Empty', 'Empty']):
        self.fields = list_of_fields

    def setting_rows(self, list_of_rows=[[]]):
        self.rows = list_of_rows

    def writing_to_file(self):
        with open(self.filename, 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.fields)
            csvwriter.writerows(self.rows)

    def reading_from_file(self):
        self.fields = []
        self.rows = []
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.fields = next(csvreader)
            for row in csvreader:
                self.rows.append(row)
        return self.fields, self.rows


class Login_info:
    lst=[]
    count=0
 ################################  login window for uer ###################################################
    def login(self):
        self.main=Toplevel()
        self.main.destroy
        self.main.geometry('550x550+420+150')
        self.main.title('Customer Login') 
        self.main.resizable(FALSE, FALSE)
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.minsize(width=550,height=550)
        self.main.maxsize(width=550,height=550) 
        frame=Frame(self.main,bg='#5D6D7E',bd=5)
        frame.grid(row=0,column=0,sticky=NW)
        # frontp1 = ImageTk.PhotoImage(Image.open('background/final.jpg').resize((550,550), Image.ANTIALIAS))
        self.bg = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/loginback.jpg').resize((550,550), Image.ANTIALIAS))
        self.main.overrideredirect(True)
        self.bg_image = Label(frame, image=self.bg).grid(row=10,column=10 )
        Label1=Label(frame,text='Email',font='Arial 15 bold',fg='maroon1', bg='blue2', padx=10)
        Label1.place(x=100,y=200)
        Label2=Label(frame,text='Password',font='Arial 15 bold',fg='maroon1',bg='blue2', padx=10)
        Label2.place(x=90,y=280)
        self.entry_1=Entry(frame)
        self.entry_1.place(x=220,y=200)
        self.entry_2=Entry(frame,show="*")
        self.entry_2.place(x=220,y=280)
        global photo_1,photo_2,photo_3
        photo_3 = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/user.jpg').resize((150,150), Image.ANTIALIAS))
        Label(frame, image=photo_3, bg='navy blue').place(x=200, y=20)
        photo_1 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/loginb.png').resize((100,50), Image.ANTIALIAS))
        button1 =Button(self.main, command=self.file_login,width=100,height=50,border=0,image=photo_1)
        button1.place(x=240,y=350)
        photo_2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/exit.png').resize((80,30), Image.ANTIALIAS))
        button3=Button(self.main, command=self.main.destroy,width=80,height=30,border=0,image=photo_2)
        button3.place(x=250,y=450)       
 ################################### log out window for user ###################################################################################################
    def log_out_window(self):
        self.main=Toplevel()
        self.main.destroy
        self.main.geometry('400x400+400+120')
        self.main.title('Logout')
        photo = PhotoImage(file = 'C:/CEP Project/images.png')
        self.main.iconphoto(False, photo)
        self.main.minsize(width=400,height=400)
        self.main.maxsize(width=400,height=400)
        frame=Frame(self.main,bg='#5D6D7E',bd=5)
        frame.grid(row=0,column=0,sticky=NW)
        self.bg = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/loginback.jpg').resize((550,550), Image.ANTIALIAS))
        self.bg_image = Label(frame, image=self.bg).grid(row=10,column=10 )
        Label1=Label(frame,text=f'You are logged in as {Login_info.lst[0][0]}',font='Arial 15 bold',fg='maroon1',bg='blue2')
        Label1.place(x=90,y=40)
        global photo_2,photo4
        # photo_2=PhotoImage(file='C:/CEP Project/button/exit.png')
        photo_2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/exit.png').resize((80,30), Image.ANTIALIAS))
        self.photo4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/logout.jpg').resize((100,50), Image.ANTIALIAS))
        self.button1 = Button(self.main, command=self.log_out,width=100,height=50,border=0,image=self.photo4)
        self.button1.place(x=140,y=230)
        button3=Button(self.main, command=self.destroy,width=80,height=30,border=0,image=photo_2)
        button3.place(x=150,y=350)   
 ###########################deletes login information and open main login window exiting the cart window######################################################
    def log_out(self):
        #object2.destroy()
        
        Login_info.lst.clear()
        # self.main.geometry('100x100')
        messagebox.showinfo('Log-out','You are now logged-out')
        object2.destroy()
    #    # if __name__ == "__main__":
       # root = Front_page()
       # root.mainloop()
 ############################### sign up window fo user ##############################################################        
    def sign_up(self):
        self.new=Toplevel()
        self.new.geometry('550x550+420+150')
        self.new.title('Signup page')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.new.iconphoto(False, photo)
        self.new.overrideredirect(True)
        self.new.minsize(width=550,height=550)
        self.new.maxsize(width=550,height=550)
        frame=Frame(self.new,bg='#5D6D7E',bd=5)
        frame.grid(row=0,column=0,sticky=NW)
        self.bg = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/loginback.jpg').resize((550,550), Image.ANTIALIAS))
        self.bg_image = Label(frame, image=self.bg).grid(row=10,column=10 )
        label=Label(frame,text='*Enter password with at least ONE DIGIT and Capital letter',font='Arial 12 bold',fg='black',bg='blue2')
        label.place(x=70,y=310)
        Label1=Label(frame,text='Name',font='Arial 15 bold',fg='maroon1',bg='blue2')
        Label1.place(x=100,y=100)
        Label2=Label(frame,text='Email',font='Arial 15 bold',fg='maroon1',bg='blue2')
        Label2.place(x=100,y=180)
        Label3=Label(frame,text='Password',font='Arial 15 bold',fg='maroon1',bg='blue2')
        Label3.place(x=90,y=270)
        label4=Label(frame,text='Confirm Password',font='Arial 15 bold',fg='maroon1',bg='blue2')
        label4.place(x=30,y=350)
        label5=Label(frame,text='Address',font='Arial 15 bold',fg='maroon1',bg='blue2')
        label5.place(x=100,y=390)
        self.entry1=Entry(frame)
        self.entry1.place(x=220,y=100)
        self.entry2=Entry(frame)
        self.entry2.place(x=220,y=180)
        self.entry3=Entry(frame,show="*")
        self.entry3.place(x=220,y=270)
        self.entry4=Entry(frame,show="*")
        self.entry4.place(x=220,y=350)
        self.entry5=Entry(frame)
        self.entry5.place(x=220,y=400)
        global photo_2,photo_3,photo_4
        photo_4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/user.jpg').resize((80,80), Image.ANTIALIAS))
        Label(frame, image=photo_4, bg='navy blue').place(x=240, y=5)
        photo_2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/exit.png').resize((80,30), Image.ANTIALIAS))
        photo_3= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/register.png').resize((140,50), Image.ANTIALIAS))
        button1=Button(self.new,text='sign-in', command=self.file_signup, border=0,image=photo_3,height=50,width=140)
        button1.place(x=210,y=440)
        button2=Button(self.new,text='Exit', command=self.new.destroy, border=0,image=photo_2,height=30,width=80)
        button2.place(x=240,y=510)
 ############################### data is saved in file of user after verification/validations ############################################################
    def file_signup(self):
        self.list=[]
        self.counter=0
        random_number = random.randint(10000000000, 90000000000)
        if self.entry1.get()!='' and self.entry2.get()!='':
            if self.entry3.get().isalpha()==FALSE and self.entry3.get().isnumeric()==FALSE :
                if self.entry4.get()==self.entry3.get():
                    with open('C:/CEP Project/data.csv', mode ='r')as file: 
                         csvFile = csv.reader(file,dialect='excel') 
                         for lines in csvFile: 
                            self.list.append(lines)
                    self.list = [x for x in self.list if x != []]
                    for i in self.list:
                        if self.entry2.get()==i[1]:
                            self.counter+=1
                            self.new.geometry('100x100')
                            messagebox.showerror('Error','Your account already exist')
                            self.sign_up()
                    if self.counter==0:
                        messagebox.showinfo('Account created',f'Thank you for signing-in,{self.entry1.get()}')
                        self.row=[[self.entry1.get(), self.entry2.get(), self.entry3.get(),random_number,self.entry5.get()]]
                        with open('C:/CEP Project/data.csv', 'a') as self.csvfile: 
                            csvwriter = csv.writer(self.csvfile,dialect='excel')  
                            csvwriter.writerows(self.row)
                else:
                    messagebox.showerror('error','Your password does not match')
                    self.sign_up()
            else:
                messagebox.showerror('Error','Enter correct password with UPPERCASE and digit')
                self.sign_up()
        else:
            messagebox.showerror('Error','Enter correct Name and Email')
            self.sign_up()
 ############# user is logged in after verification that the user acoount exixt or not #####################
    def file_login(self):
        self.list=[]
        self.counter=0
        try:
            if self.entry_1.get()=='' and self.entry_2.get()=='':
                raise ValueError(self.entry_1.get()and self.entry_2.get())
        except ValueError:
            messagebox.showerror("Error", "Enter your account info")
            self.login()
        else:
                with open('C:/CEP Project/data.csv', mode ='r')as file: 
                    csvFile = csv.reader(file,dialect='excel') 
                    for lines in csvFile: 
                        self.list.append(lines)
                self.list = [x for x in self.list if x != []] #for eliminating blank list 
                for i in self.list:
                    if self.entry_1.get()==i[1]:
                        self.counter+=1
                        if self.entry_2.get()==i[2]:
                            Login_info.lst.append(i)
                            Login_info.count+=1
                            self.counter-=1
                if self.counter==1 and Login_info.count==0:
                    messagebox.showerror('Error','Enter correct password for your account')
                    self.login()
                elif Login_info.count==0 and self.counter==0:
                    messagebox.showinfo('Sign-in','Your account doesnt exist please sign-up')
                    self.sign_up()
                elif Login_info.count==1:
                    messagebox.showinfo('Login',f'You are logged in as {Login_info.lst[0][0]}')
                    self.open()
 ############################ a new window is opened after login which includes cart####################################
    def open(self):
        root.destroy()
        global object2
        object2=Cart()
        object2.mainloop()


class Display_products:
    cart_lst=[]
   
    def __init__(self):
        
        self.products = CSVFiling("C:/CEP Project/Products.csv")
        self.content = self.products.reading_from_file()
        
        self.products1 = CSVFiling("C:/CEP Project/Products2.csv")
        self.content2 = self.products1.reading_from_file()
         
    def check(self,slider,number):
        self.slider=slider
        self.item=number
        try:
            if int(self.slider)>int(self.content[1][self.item][2]):
                raise ValueError
        except ValueError :
            self.main.geometry('100x100')
            messagebox.showerror('valueError',f'{self.content[1][self.item][2]} item left')
        else:
            self.content[1][self.item][2]=int(self.content[1][self.item][2])-int(self.slider)   
            self.fields = ['Name', 'Price', 'Quantity', 'Category']
            with open('C:/CEP Project/Products.csv', 'w') as self.csvfile: 
                csvwriter = csv.writer(self.csvfile,dialect='excel')  
                csvwriter.writerow(self.fields)
                for i in range (1,112):
                    try :
                        if len(self.content[1][i])==0:
                            raise IndexError
                    except IndexError:
                        pass
                    else:
                        self.row=[self.content[1][i][0],self.content[1][i][1], self.content[1][i][2],self.content[1][i][3]]
                        csvwriter.writerow(self.row)

   ######################################### to store item for cart ###################################################
    def get_value1(self):
        self.quantity1=self.slider1.get()
        self.check(self.quantity1,1)
        self.price1=(self.quantity1)*float(self.content2[1][1][1])
        Display_products.cart_lst.append([self.content2[1][1][0],self.content2[1][1][1],self.quantity1,self.price1])

    def get_value2(self):
        self.quantity2=self.slider2.get()
        self.check(self.quantity2,3)
        self.price2=self.quantity2*float(self.content2[1][3][1])
        Display_products.cart_lst.append([self.content2[1][3][0],self.content2[1][3][1],self.quantity2,self.price2])

    def get_value3(self):
        self.quantity3=self.slider3.get()
        self.check(self.quantity3,5)
        self.price3=self.quantity3*float(self.content2[1][5][1])
        Display_products.cart_lst.append([self.content2[1][5][0],self.content2[1][5][1],self.quantity3,self.price3])

    def get_value4(self):
        self.quantity4=self.slider4.get()
        self.check(self.quantity4,7)
        self.price4=self.quantity4*float(self.content2[1][7][1])
        Display_products.cart_lst.append([self.content2[1][7][0],self.content2[1][7][1],self.quantity4,self.price4])

    def get_value5(self):
        self.quantity5=self.slider5.get()
        self.check(self.quantity5,9)
        self.price5=self.quantity5*float(self.content2[1][9][1])
        Display_products.cart_lst.append([self.content2[1][9][0],self.content2[1][9][1],self.quantity5,self.price5])

    def get_value6(self):
        self.quantity6=self.slider6.get()
        self.check(self.quantity6,11)
        self.price6=self.quantity6*float(self.content2[1][11][1])
        Display_products.cart_lst.append([self.content2[1][11][0],self.content2[1][11][1],self.quantity6,self.price6])

    def get_value7(self):
        self.quantity7=self.slider7.get()
        self.check(self.quantity7,13)
        self.price7=self.quantity7*float(self.content2[1][13][1])
        Display_products.cart_lst.append([self.content2[1][13][0],self.content2[1][13][1],self.quantity7,self.price7])

    def get_value8(self):
        self.quantity8=self.slider8.get()
        self.check(self.quantity8,15)
        self.price8=self.quantity8*float(self.content2[1][15][1])
        Display_products.cart_lst.append([self.content2[1][15][0],self.content2[1][15][1],self.quantity8,self.price8])

    def get_value9(self):
        self.quantity9=self.slider9.get()
        self.check(self.quantity9,17)
        self.price9=self.quantity9*float(self.content2[1][17][1])
        Display_products.cart_lst.append([self.content2[1][17][0],self.content2[1][17][1],self.quantity9,self.price9])

    def get_value10(self):
        self.quantity10=self.slider10.get()
        self.check(self.quantity10,19)
        self.price10=self.quantity10*float(self.content2[1][19][1])
        Display_products.cart_lst.append([self.content2[1][19][0],self.content2[1][19][1],self.quantity10,self.price10])

    def get_value11(self):
        self.quantity11=self.slider11.get()
        self.check(self.quantity11,21)
        self.price11=self.quantity11*float(self.content2[1][21][1])
        Display_products.cart_lst.append([self.content2[1][21][0],self.content2[1][21][1],self.quantity11,self.price11])

    def get_value12(self):
        self.quantity12=self.slider12.get()
        self.check(self.quantity12,23)
        self.price12=self.quantity12*float(self.content2[1][23][1])
        Display_products.cart_lst.append([self.content2[1][23][0],self.content2[1][23][1],self.quantity12,self.price12])

    def get_value13(self):
        self.quantity13=self.slider13.get()
        self.check(self.quantity13,25)
        self.price13=self.quantity13*float(self.content2[1][25][1])
        Display_products.cart_lst.append([self.content2[1][25][0],self.content2[1][25][1],self.quantity13,self.price13])

    def get_value14(self):
        self.quantity14=self.slider14.get()
        self.check(self.quantity14,27)
        self.price14=self.quantity14*float(self.content2[1][27][1])
        Display_products.cart_lst.append([self.content2[1][27][0],self.content2[1][27][1],self.quantity14,self.price14])

    def get_value15(self):
        self.quantity15=self.slider15.get()
        self.check(self.quantity15,29)
        self.price15=self.quantity15*float(self.content2[1][29][1])
        Display_products.cart_lst.append([self.content2[1][29][0],self.content2[1][29][1],self.quantity15,self.price15])

    def get_value16(self):
        self.quantity16=self.slider16.get()
        self.check(self.quantity16,31)
        self.price16=self.quantity16*float(self.content2[1][31][1])
        Display_products.cart_lst.append([self.content2[1][31][0],self.content2[1][31][1],self.quantity16,self.price16])

    def get_value17(self):
        self.quantity17=self.slider17.get()
        self.check(self.quantity17,33)
        self.price17=self.quantity17*float(self.content2[1][33][1])
        Display_products.cart_lst.append([self.content2[1][33][0],self.content2[1][33][1],self.quantity17,self.price17])

    def get_value18(self):
        self.quantity18=self.slider18.get()
        self.check(self.quantity18,35)
        self.price18=self.quantity18*float(self.content2[1][35][1])
        Display_products.cart_lst.append([self.content2[1][35][0],self.content2[1][35][1],self.quantity18,self.price18])

    def get_value19(self):
        self.quantity19=self.slider19.get()
        self.check(self.quantity19,37)
        self.price19=self.quantity19*float(self.content2[1][37][1])
        Display_products.cart_lst.append([self.content2[1][37][0],self.content2[1][37][1],self.quantity19,self.price19])

    def get_value20(self):
        self.quantity20=self.slider20.get()
        self.check(self.quantity20,39)
        self.price20=self.quantity20*float(self.content2[1][39][1])
        Display_products.cart_lst.append([self.content2[1][39][0],self.content2[1][39][1],self.quantity20,self.price20])

    def get_value21(self):
        self.quantity21=self.slider21.get()
        self.check(self.quantity21,41)
        self.price21=self.quantity21*float(self.content2[1][41][1])
        Display_products.cart_lst.append([self.content2[1][41][0],self.content2[1][41][1],self.quantity21,self.price21])

    def get_value22(self):
        self.quantity22=self.slider22.get()
        self.check(self.quantity22,43)
        self.price22=self.quantity22*float(self.content2[1][43][1])
        Display_products.cart_lst.append([self.content2[1][43][0],self.content2[1][43][1],self.quantity22,self.price22])

    def get_value23(self):
        self.quantity23=self.slider23.get()
        self.check(self.quantity23,45)
        self.price23=self.quantity23*float(self.content2[1][45][1])
        Display_products.cart_lst.append([self.content2[1][45][0],self.content2[1][45][1],self.quantity23,self.price23])

    def get_value24(self):
        self.quantity24=self.slider24.get()
        self.check(self.quantity24,47)
        self.price24=self.quantity24*float(self.content2[1][47][1])
        Display_products.cart_lst.append([self.content2[1][47][0],self.content2[1][47][1],self.quantity24,self.price24])

    def get_value25(self):
        self.quantity25=self.slider25.get()
        self.check(self.quantity25,49)
        self.price25=self.quantity25*float(self.content2[1][49][1])
        Display_products.cart_lst.append([self.content2[1][49][0],self.content2[1][49][1],self.quantity25,self.price25])

    def get_value26(self):
        self.quantity26=self.slider26.get()
        self.check(self.quantity26,51)
        self.price26=self.quantity26*float(self.content2[1][51][1])
        Display_products.cart_lst.append([self.content2[1][51][0],self.content2[1][51][1],self.quantity26,self.price26])

    def get_value27(self):
        self.quantity27=self.slider27.get()
        self.check(self.quantity27,53)
        self.price27=self.quantity27*float(self.content2[1][53][1])
        Display_products.cart_lst.append([self.content2[1][53][0],self.content2[1][53][1],self.quantity27,self.price27])

    def get_value28(self):
        self.quantity28=self.slider28.get()
        self.check(self.quantity28,55)
        self.price28=self.quantity28*float(self.content2[1][55][1])
        Display_products.cart_lst.append([self.content2[1][55][0],self.content2[1][55][1],self.quantity28,self.price28])

    def get_value29(self):
        self.quantity29=self.slider29.get()
        self.check(self.quantity29,57)
        self.price29=self.quantity29*float(self.content2[1][57][1])
        Display_products.cart_lst.append([self.content2[1][57][0],self.content2[1][57][1],self.quantity29,self.price29])

    def get_value30(self):
        self.quantity30=self.slider30.get()
        self.check(self.quantity30,59)
        self.price30=self.quantity30*float(self.content2[1][59][1])
        Display_products.cart_lst.append([self.content2[1][59][0],self.content2[1][59][1],self.quantity30,self.price30])

    def get_value31(self):
        self.quantity31=self.slider31.get()
        self.check(self.quantity31,61)
        self.price31=self.quantity31*float(self.content2[1][61][1])
        Display_products.cart_lst.append([self.content2[1][61][0],self.content2[1][61][1],self.quantity31,self.price31])

    def get_value32(self):
        self.quantity32=self.slider32.get()
        self.check(self.quantity32,63)
        self.price32=self.quantity32*float(self.content2[1][63][1])
        Display_products.cart_lst.append([self.content2[1][63][0],self.content2[1][63][1],self.quantity32,self.price32])

    def get_value33(self):
        self.quantity33=self.slider33.get()
        self.check(self.quantity33,65)
        self.price33=self.quantity33*float(self.content2[1][65][1])
        Display_products.cart_lst.append([self.content2[1][65][0],self.content2[1][65][1],self.quantity33,self.price33])

    def get_value34(self):
        self.quantity34=self.slider34.get()
        self.check(self.quantity34,67)
        self.price34=self.quantity34*float(self.content2[1][67][1])
        Display_products.cart_lst.append([self.content2[1][67][0],self.content2[1][67][1],self.quantity34,self.price34])

    def get_value35(self):
        self.quantity35=self.slider35.get()
        self.check(self.quantity35,69)
        self.price35=self.quantity35*float(self.content2[1][69][1])
        Display_products.cart_lst.append([self.content2[1][69][0],self.content2[1][69][1],self.quantity35,self.price35])

    def get_value36(self):
        self.quantity36=self.slider36.get()
        self.check(self.quantity36,71)
        self.price36=self.quantity36*float(self.content2[1][71][1])
        Display_products.cart_lst.append([self.content2[1][71][0],self.content2[1][71][1],self.quantity36,self.price36])

    def get_value37(self):
        self.quantity37=self.slider37.get()
        self.check(self.quantity37,73)
        self.price37=self.quantity37*float(self.content2[1][73][1])
        Display_products.cart_lst.append([self.content2[1][73][0],self.content2[1][73][1],self.quantity37,self.price37])

    def get_value38(self):
        self.quantity38=self.slider38.get()
        self.check(self.quantity38,75)
        self.price38=self.quantity38*float(self.content2[1][75][1])
        Display_products.cart_lst.append([self.content2[1][75][0],self.content2[1][75][1],self.quantity38,self.price38])

    def get_value39(self):
        self.quantity39=self.slider39.get()
        self.check(self.quantity39,77)
        self.price39=self.quantity39*float(self.content2[1][77][1])
        Display_products.cart_lst.append([self.content2[1][77][0],self.content2[1][77][1],self.quantity39,self.price39])

    def get_value40(self):
        self.quantity40=self.slider40.get()
        self.check(self.quantity40,79)
        self.price40=self.quantity40*float(self.content2[1][79][1])
        Display_products.cart_lst.append([self.content2[1][79][0],self.content2[1][79][1],self.quantity40,self.price40])

    def get_value41(self):
        self.quantity41=self.slider41.get()
        self.check(self.quantity41,81)
        self.price41=self.quantity41*float(self.content2[1][81][1])
        Display_products.cart_lst.append([self.content2[1][81][0],self.content2[1][81][1],self.quantity41,self.price41])

    def get_value42(self):
        self.quantity42=self.slider42.get()
        self.check(self.quantity42,83)
        self.price42=self.quantity42*float(self.content2[1][83][1])
        Display_products.cart_lst.append([self.content2[1][83][0],self.content2[1][83][1],self.quantity42,self.price42])

    def get_value43(self):
        self.quantity43=self.slider43.get()
        self.check(self.quantity43,85)
        self.price43=self.quantity43*float(self.content2[1][85][1])
        Display_products.cart_lst.append([self.content2[1][85][0],self.content2[1][85][1],self.quantity43,self.price43])

    def get_value44(self):
        self.quantity44=self.slider44.get()
        self.check(self.quantity44,87)
        self.price44=self.quantity44*float(self.content2[1][87][1])
        Display_products.cart_lst.append([self.content2[1][87][0],self.content2[1][87][1],self.quantity44,self.price44])

    def get_value45(self):
        self.quantity45=self.slider45.get()
        self.check(self.quantity45,89)
        self.price45=self.quantity45*float(self.content2[1][89][1])
        Display_products.cart_lst.append([self.content2[1][89][0],self.content2[1][89][1],self.quantity45,self.price45])

    def get_value46(self):
        self.quantity46=self.slider46.get()
        self.check(self.quantity46,91)
        self.price46=self.quantity46*float(self.content2[1][91][1])
        Display_products.cart_lst.append([self.content2[1][91][0],self.content2[1][91][1],self.quantity46,self.price46])

    def get_value47(self):
        self.quantity47=self.slider47.get()
        self.check(self.quantity47,93)
        self.price47=self.quantity47*float(self.content2[1][93][1])
        Display_products.cart_lst.append([self.content2[1][93][0],self.content2[1][93][1],self.quantity47,self.price47])

    def get_value48(self):
        self.quantity48=self.slider48.get()
        self.check(self.quantity48,95)
        self.price48=self.quantity48*float(self.content2[1][95][1])
        Display_products.cart_lst.append([self.content2[1][95][0],self.content2[1][95][1],self.quantity48,self.price48])

    def get_value49(self):
        self.quantity49=self.slider49.get()
        self.check(self.quantity49,97)
        self.price49=self.quantity49*float(self.content2[1][97][1])
        Display_products.cart_lst.append([self.content2[1][97][0],self.content2[1][97][1],self.quantity49,self.price49])

    def get_value50(self):
        self.quantity50=self.slider50.get()
        self.check(self.quantity50,99)
        self.price50=self.quantity50*float(self.content2[1][99][1])
        Display_products.cart_lst.append([self.content2[1][99][0],self.content2[1][99][1],self.quantity50,self.price50])

    def get_value51(self):
        self.quantity51=self.slider51.get()
        self.check(self.quantity51,101)
        self.price51=self.quantity51*float(self.content2[1][101][1])
        Display_products.cart_lst.append([self.content2[1][101][0],self.content2[1][101][1],self.quantity51,self.price51])

    def get_value52(self):
        self.quantity52=self.slider52.get()
        self.check(self.quantity52,103)
        self.price52=self.quantity52*float(self.content2[1][103][1])
        Display_products.cart_lst.append([self.content2[1][103][0],self.content2[1][103][1],self.quantity52,self.price52])

    def get_value53(self):
        self.quantity53=self.slider53.get()
        self.check(self.quantity53,105)
        self.price53=self.quantity53*float(self.content2[1][105][1])
        Display_products.cart_lst.append([self.content2[1][105][0],self.content2[1][105][1],self.quantity53,self.price53])

    def get_value54(self):
        self.quantity54=self.slider54.get()
        self.check(self.quantity54,107)
        self.price54=self.quantity54*float(self.content2[1][107][1])
        Display_products.cart_lst.append([self.content2[1][107][0],self.content2[1][107][1],self.quantity54,self.price54])

    def get_value55(self):
        self.quantity55=self.slider55.get()
        self.check(self.quantity55,109)
        self.price55=self.quantity55*float(self.content2[1][109][1])
        Display_products.cart_lst.append([self.content2[1][109][0],self.content2[1][109][1],self.quantity55,self.price55])
   ################################ Product Pages ################################
    
    def elect_access(self):
       
        # CODE FOR PAGE TWO
        def page2():

            def back():
                self.canvas1.destroy()
                self.elect_access()

            self.main.destroy()
            self.main2 = Toplevel()
            self.main2.geometry('1240x695+135+110')
            self.main2.overrideredirect(True)
            self.canvas1 = Canvas(self.main2, height=695, width=1240, bg='sky blue')
            self.canvas1.pack()

            picture4 = Image.open('C:/CEP Project/photos/p4.jpg')
            new_pic4 = picture4.resize((150, 150))
            self.image4 = ImageTk.PhotoImage(new_pic4)
            self.lab4 = Label(self.canvas1, image=self.image4)
            self.lab4.place(x=50, y=70)
            self.canvas1.create_text(410, 95, text=self.content[1][7][0], font='comicsansms 14 ')
            price = str(self.content[1][7][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 140, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider4 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
            self.slider4.config(highlightbackground='sky blue', highlightcolor='sky blue')
            self.slider4.place(x=270, y=150)
            b4_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value4, padx=10, pady=10)
            b4_add_to_cart.place(x=280, y=200)

            picture5 = Image.open('C:/CEP Project/photos/p5.jpg')
            new_pic5 = picture5.resize((150, 150))
            self.image5 = ImageTk.PhotoImage(new_pic5)
            self.lab5 = Label(self.canvas1, image=self.image5)
            self.lab5.place(x=50, y=350)
            self.canvas1.create_text(380, 375, text=self.content[1][9][0], font='comicsansms 14 ')
            price = str(self.content[1][9][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 420, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider5 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
            self.slider5.config(highlightbackground='sky blue', highlightcolor='sky blue')
            self.slider5.place(x=270, y=430)
            b5_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value5, padx=10, pady=10)
            b5_add_to_cart.place(x=280, y=480)

            picture6 = Image.open('C:/CEP Project/photos/p6.jpg')
            new_pic6 = picture6.resize((150, 150))
            self.image6 = ImageTk.PhotoImage(new_pic6)
            self.lab6 = Label(self.canvas1, image=self.image6)
            self.lab6.place(x=640, y=70)
            self.canvas1.create_text(1010, 95, text=self.content[1][11][0], font='comicsansms 14 ')
            price = str(self.content[1][11][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 140, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider6 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
            self.slider6.config(highlightbackground='sky blue', highlightcolor='sky blue')
            self.slider6.place(x=850, y=150)
            b6_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value6, padx=10, pady=10)
            b6_add_to_cart.place(x=860, y=200)

            picture7 = Image.open('C:/CEP Project/photos/p7.jpg')
            new_pic7 = picture7.resize((150, 150))
            self.image7 = ImageTk.PhotoImage(new_pic7)
            self.lab7 = Label(self.canvas1, image=self.image7)
            self.lab7.place(x=640, y=350)
            self.canvas1.create_text(1010, 375, text=self.content[1][13][0], font='comicsansms 14 ')
            price = str(self.content[1][13][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 420, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider7 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
            self.slider7.config(highlightbackground='sky blue', highlightcolor='sky blue')
            self.slider7.place(x=850, y=430)
            b7_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value7, padx=10, pady=10)
            b7_add_to_cart.place(x=860, y=480)

            Button(self.canvas1, text='PREVIOUS PAGE', padx=15, pady=15, command=back).place(x=50, y=550)

        # CODE FOR PAGE ONE
        self.main=Toplevel()
        self.main.geometry('1240x695+135+110')
        self.main.overrideredirect(True)
        self.color = 'sky blue'
        self.canvas = Canvas(self.main, height=695, width=1240, bg=self.color)
        self.canvas.pack()

        self.canvas.create_text(275, 80, text='ELECTRONIC ACCESSORIES', font='ArialRound 24 bold')

        picture1 = Image.open('C:/CEP Project/photos/p1.jpg')
        new_pic1 = picture1.resize((150, 150))
        self.image1 = ImageTk.PhotoImage(new_pic1)
        self.lab1 = Label(self.canvas, image=self.image1)
        self.lab1.place(x=50, y=150)
        self.canvas.create_text(380, 175, text=self.content[1][1][0], font='comicsansms 14 ')
        price = str(self.content[1][1][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]


        self.canvas.create_text(300, 220, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider1 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
        self.slider1.config(highlightbackground='sky blue', highlightcolor='sky blue')
        self.slider1.place(x=250, y=230)
        b1_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value1, padx=10, pady=10)
        b1_add_to_cart.place(x=260, y=280)
        picture2 = Image.open('C:/CEP Project/photos/p2.jpg')
        new_pic2 = picture2.resize((150, 150))
        self.image2 = ImageTk.PhotoImage(new_pic2)
        self.lab2 = Label(self.canvas, image=self.image2)
        self.lab2.place(x=600, y=150)
        self.canvas.create_text(960, 175, text=self.content[1][3][0], font='comicsansms 18 ')
        price = str(self.content[1][3][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(860, 220, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider2 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
        self.slider2.config(highlightbackground='sky blue', highlightcolor='sky blue')
        self.slider2.place(x=810, y=230)
        b2_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value2, padx=10, pady=10)
        b2_add_to_cart.place(x=820, y=280)

        picture3 = Image.open('C:/CEP Project/photos/p3.jpg')
        new_pic3 = picture3.resize((150, 150))
        self.image3 = ImageTk.PhotoImage(new_pic3)
        self.lab3 = Label(self.canvas, image=self.image3)
        self.lab3.place(x=50, y=400)
        self.canvas.create_text(440, 425, text=self.content[1][5][0], font='comicsansms 14 ')
        price = str(self.content[1][5][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 470, text='Rs. ' +up_price, font='comicsansms 16 bold')
        self.slider3 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='sky blue')
        self.slider3.config(highlightbackground='sky blue', highlightcolor='sky blue')
        self.slider3.place(x=250, y=480)
        b3_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value3, padx=10, pady=10)
        b3_add_to_cart.place(x=260, y=530)

        Button(self.canvas, text='NEXT PAGE', padx=15, pady=15, command=page2).place(x=1000, y=550)

    def watches_eyewear(self):

        def page2():

            def back():
                self.canvas1.destroy()
                self.watches_eyewear()

            self.main.destroy()
            self.main2 = Toplevel()
            self.main2.geometry('1240x695+135+110')
            self.main2.overrideredirect(True)
            self.canvas1 = Canvas(self.main2, height=695, width=1240, bg='khaki')
            self.canvas1.pack()

            picture4 = Image.open('C:/CEP Project/photos/p11.jpg')
            new_pic4 = picture4.resize((150, 150))
            self.image4 = ImageTk.PhotoImage(new_pic4)
            self.lab4 = Label(self.canvas1, image=self.image4)
            self.lab4.place(x=50, y=70)
            self.canvas1.create_text(380, 95, text=self.content[1][21][0], font='comicsansms 14 ')
            price = str(self.content[1][21][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 140, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider11 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
            self.slider11.config(highlightbackground='khaki', highlightcolor='khaki')
            self.slider11.place(x=270, y=150)
            b4_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value11, padx=10, pady=10)
            b4_add_to_cart.place(x=280, y=200)

            picture5 = Image.open('C:/CEP Project/photos/p12.jpg')
            new_pic5 = picture5.resize((150, 150))
            self.image5 = ImageTk.PhotoImage(new_pic5)
            self.lab5 = Label(self.canvas1, image=self.image5)
            self.lab5.place(x=50, y=350)
            self.canvas1.create_text(400, 375, text=self.content[1][23][0], font='comicsansms 14 ')
            price = str(self.content[1][23][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 420, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider12 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
            self.slider12.config(highlightbackground='khaki', highlightcolor='khaki')
            self.slider12.place(x=270, y=430)
            b5_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value12, padx=10, pady=10)
            b5_add_to_cart.place(x=280, y=480)

            picture6 = Image.open('C:/CEP Project/photos/p13.jpg')
            new_pic6 = picture6.resize((150, 150))
            self.image6 = ImageTk.PhotoImage(new_pic6)
            self.lab6 = Label(self.canvas1, image=self.image6)
            self.lab6.place(x=640, y=70)
            self.canvas1.create_text(1010, 95, text=self.content[1][25][0], font='comicsansms 14 ')
            price = str(self.content[1][25][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 140, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider13 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
            self.slider13.config(highlightbackground='khaki', highlightcolor='khaki')
            self.slider13.place(x=850, y=150)
            b6_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value13, padx=10, pady=10)
            b6_add_to_cart.place(x=860, y=200)

            picture7 = Image.open('C:/CEP Project/photos/p14.jpg')
            new_pic7 = picture7.resize((150, 150))
            self.image7 = ImageTk.PhotoImage(new_pic7)
            self.lab7 = Label(self.canvas1, image=self.image7)
            self.lab7.place(x=640, y=350)
            self.canvas1.create_text(1010, 375, text=self.content[1][27][0], font='comicsansms 14 ')
            price = str(self.content[1][27][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 420, text='Rs. '+up_price, font='comicsansms 16 bold')
            self.slider14 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
            self.slider14.config(highlightbackground='khaki', highlightcolor='khaki')
            self.slider14.place(x=850, y=430)
            b7_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value14, padx=10, pady=10)
            b7_add_to_cart.place(x=860, y=480)

            Button(self.canvas1, text='PREVIOUS PAGE', padx=15, pady=15, command=back).place(x=50, y=550)


        self.main = Toplevel()
        self.main.geometry('1240x695+135+110')
        self.main.overrideredirect(True)
        self.canvas = Canvas(self.main, height=695, width=1240, bg='khaki')
        self.canvas.pack()

        self.canvas.create_text(275, 80, text='WATCHES AND EYEWEAR', font='ArialRound 24 bold')

        picture1 = Image.open('C:/CEP Project/photos/p8.jpg')
        new_pic1 = picture1.resize((150,150))
        self.image1 = ImageTk.PhotoImage(new_pic1)
        self.lab1 = Label(self.canvas, image=self.image1)
        self.lab1.place(x=50, y=150)
        self.canvas.create_text(390, 175, text=self.content[1][15][0], font='comicsansms 14 ')
        price = str(self.content[1][15][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 220, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider8 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
        self.slider8.config(highlightbackground='khaki', highlightcolor='khaki')
        self.slider8.place(x=250, y=230)
        b1_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value8, padx=10, pady=10)
        b1_add_to_cart.place(x=260, y=280)

        picture2 = Image.open('C:/CEP Project/photos/p9.jpg')
        new_pic2 = picture2.resize((150, 150))
        self.image2 = ImageTk.PhotoImage(new_pic2)
        self.lab2 = Label(self.canvas, image=self.image2)
        self.lab2.place(x=600, y=150)
        self.canvas.create_text(1000, 175, text=self.content[1][17][0], font='comicsansms 14 ')
        price = str(self.content[1][17][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(860, 220, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider9 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
        self.slider9.config(highlightbackground='khaki', highlightcolor='khaki')
        self.slider9.place(x=810, y=230)
        b2_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value9, padx=10, pady=10)
        b2_add_to_cart.place(x=820, y=280)

        picture3 = Image.open('C:/CEP Project/photos/p10.jpg')
        new_pic3 = picture3.resize((150, 150))
        self.image3 = ImageTk.PhotoImage(new_pic3)
        self.lab3 = Label(self.canvas, image=self.image3)
        self.lab3.place(x=50, y=400)
        self.canvas.create_text(360, 425, text=self.content[1][19][0], font='comicsansms 14 ')
        price = str(self.content[1][19][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 470, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider10 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='khaki')
        self.slider10.config(highlightbackground='khaki', highlightcolor='khaki')
        self.slider10.place(x=250, y=480)
        b3_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value10, padx=10, pady=10)
        b3_add_to_cart.place(x=260, y=530)

        Button(self.canvas, text='NEXT PAGE', padx=15, pady=15, command=page2).place(x=1000, y=550)

    def health_fitness(self):

        def page3():
            def back2():
                self.canvas2.destroy()
                page2()

            self.main2.destroy()
            self.main3 = Toplevel()
            self.main3.geometry('1240x695+135+110')
            self.main3.overrideredirect(True)
            self.canvas2 = Canvas(self.main3, height=695, width=1240, bg='orangered3')
            self.canvas2.pack()

            picture8 = Image.open('C:/CEP Project/photos/p22.jpg')
            new_pic8 = picture8.resize((150, 150))
            self.image8 = ImageTk.PhotoImage(new_pic8)
            self.lab4 = Label(self.canvas2, image=self.image8)
            self.lab4.place(x=50, y=70)
            self.canvas2.create_text(395, 95, text=self.content[1][43][0], font='comicsansms 14 ')
            price = str(self.content[1][43][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider22 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider22.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider22.place(x=270, y=150)
            b8_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value22, padx=10, pady=10)
            b8_add_to_cart.place(x=280, y=200)

            picture9 = Image.open('C:/CEP Project/photos/p23.jpg')
            new_pic9 = picture9.resize((150, 150))
            self.image9 = ImageTk.PhotoImage(new_pic9)
            self.lab5 = Label(self.canvas2, image=self.image9)
            self.lab5.place(x=50, y=350)
            self.canvas2.create_text(395, 375, text=self.content[1][45][0], font='comicsansms 14 ')
            price = str(self.content[1][45][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider23 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider23.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider23.place(x=270, y=430)
            b9_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value23, padx=10, pady=10)
            b9_add_to_cart.place(x=280, y=480)

            picture10 = Image.open('C:/CEP Project/photos/p24.jpg')
            new_pic10 = picture10.resize((150, 150))
            self.image10 = ImageTk.PhotoImage(new_pic10)
            self.lab10 = Label(self.canvas2, image=self.image10)
            self.lab10.place(x=660, y=70)
            self.canvas2.create_text(950, 95, text=self.content[1][47][0], font='comicsansms 14 ')
            price = str(self.content[1][47][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider24 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider24.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider24.place(x=850, y=150)
            b10_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value24, padx=10, pady=10)
            b10_add_to_cart.place(x=860, y=200)

            picture11 = Image.open('C:/CEP Project/photos/p25.jpg')
            new_pic11 = picture11.resize((150, 150))
            self.image11 = ImageTk.PhotoImage(new_pic11)
            self.lab11 = Label(self.canvas2, image=self.image11)
            self.lab11.place(x=660, y=350)
            self.canvas2.create_text(940, 375, text=self.content[1][49][0], font='comicsansms 14 ')
            price = str(self.content[1][49][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider25 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider25.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider25.place(x=850, y=430)
            b11_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value25, padx=10, pady=10)
            b11_add_to_cart.place(x=860, y=480)

            Button(self.canvas2, text='PREVIOUS PAGE', padx=15, pady=15, command=back2).place(x=50, y=550)

        def page2():

            def back():
                self.canvas1.destroy()
                self.health_fitness()

            self.main.destroy()
            self.main2 = Toplevel()
            self.main2.geometry('1240x695+135+110')
            self.main2.overrideredirect(True)
            self.canvas1 = Canvas(self.main2, height=695, width=1240, bg='orangered3')
            self.canvas1.pack()

            picture4 = Image.open('C:/CEP Project/photos/p18.jpg')
            new_pic4 = picture4.resize((150, 150))
            self.image4 = ImageTk.PhotoImage(new_pic4)
            self.lab4 = Label(self.canvas1, image=self.image4)
            self.lab4.place(x=50, y=70)
            self.canvas1.create_text(420, 95, text=self.content[1][35][0], font='comicsansms 14 ')
            price = str(self.content[1][35][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider18 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider18.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider18.place(x=270, y=150)
            b4_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value18, padx=10, pady=10)
            b4_add_to_cart.place(x=280, y=200)

            picture5 = Image.open('C:/CEP Project/photos/p19.jpg')
            new_pic5 = picture5.resize((150, 150))
            self.image5 = ImageTk.PhotoImage(new_pic5)
            self.lab5 = Label(self.canvas1, image=self.image5)
            self.lab5.place(x=50, y=350)
            self.canvas1.create_text(410, 375, text=self.content[1][37][0], font='comicsansms 14 ')
            price = str(self.content[1][37][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider19 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider19.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider19.place(x=270, y=430)
            b5_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value19, padx=10, pady=10)
            b5_add_to_cart.place(x=280, y=480)

            picture6 = Image.open('C:/CEP Project/photos/p20.jpg')
            new_pic6 = picture6.resize((150, 150))
            self.image6 = ImageTk.PhotoImage(new_pic6)
            self.lab6 = Label(self.canvas1, image=self.image6)
            self.lab6.place(x=660, y=70)
            self.canvas1.create_text(1010, 95, text=self.content[1][39][0], font='comicsansms 14 ')
            price = str(self.content[1][39][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider20 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider20.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider20.place(x=850, y=150)
            b6_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value20, padx=10, pady=10)
            b6_add_to_cart.place(x=860, y=200)

            picture7 = Image.open('C:/CEP Project/photos/p21.jpg')
            new_pic7 = picture7.resize((150, 150))
            self.image7 = ImageTk.PhotoImage(new_pic7)
            self.lab7 = Label(self.canvas1, image=self.image7)
            self.lab7.place(x=660, y=350)
            self.canvas1.create_text(1010, 375, text=self.content[1][41][0], font='comicsansms 14 ')
            price = str(self.content[1][41][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider21 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
            self.slider21.config(highlightbackground='orangered3', highlightcolor='orangered3')
            self.slider21.place(x=850, y=430)
            b7_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value21, padx=10, pady=10)
            b7_add_to_cart.place(x=860, y=480)

            Button(self.canvas1, text='PREVIOUS PAGE', padx=15, pady=15, command=back).place(x=50, y=550)
            Button(self.canvas1, text='NEXT PAGE', padx=15, pady=15, command=page3).place(x=1000, y=550)

        self.main=Toplevel()
        self.main.geometry('1240x695+135+110')
        self.main.overrideredirect(True)
        self.canvas = Canvas(self.main, height=695, width=1240, bg='orangered3')
        self.canvas.pack()

        self.canvas.create_text(275, 80, text='HEALTH AND FITNESS', font='ArialBlack 24 bold')

        picture1 = Image.open('C:/CEP Project/photos/p15.jpg')
        new_pic1 = picture1.resize((150, 150))
        self.image1 = ImageTk.PhotoImage(new_pic1)
        self.lab1 = Label(self.canvas, image=self.image1)
        self.lab1.place(x=50, y=150)
        self.canvas.create_text(330, 175, text=self.content[1][29][0], font='comicsansms 14 ')
        price = str(self.content[1][29][1])
        if len(price) == 5:
            up_price = price[0]+price[1]+','+price[2]+price[3]+price[4]
        elif len(price) == 4:
            up_price = price[0]+','+price[1]+price[2]+price[3]
        self.canvas.create_text(300, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider15 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
        self.slider15.config(highlightbackground='orangered3', highlightcolor='orangered3')
        self.slider15.place(x=250, y=230)
        b1_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value15, padx=10, pady=10)
        b1_add_to_cart.place(x=260, y=280)

        picture2 = Image.open('C:/CEP Project/photos/p16.jpg')
        new_pic2 = picture2.resize((150, 150))
        self.image2 = ImageTk.PhotoImage(new_pic2)
        self.lab2 = Label(self.canvas, image=self.image2)
        self.lab2.place(x=600, y=150)
        self.canvas.create_text(945, 175, text=self.content[1][31][0], font='comicsansms 14 ')
        price =str(self.content[1][31][1])
        if len(price)==5:
            up_price = price[0]+price[1]+','+price[2]+price[3]+price[4]
        elif len(price)==4:
            up_price = price[0]+','+price[1]+price[2]+price[3]
        self.canvas.create_text(860, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider16 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
        self.slider16.config(highlightbackground='orangered3', highlightcolor='orangered3')
        self.slider16.place(x=810, y=230)
        b2_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value16, padx=10, pady=10)
        b2_add_to_cart.place(x=820, y=280)

        picture3 = Image.open('C:/CEP Project/photos/p17.jpg')
        new_pic3 = picture3.resize((150, 150))
        self.image3 = ImageTk.PhotoImage(new_pic3)
        self.lab3 = Label(self.canvas, image=self.image3)
        self.lab3.place(x=50, y=400)
        self.canvas.create_text(405, 425, text=self.content[1][33][0], font='comicsansms 14 ')
        price = str(self.content[1][33][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 480, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider17 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='orangered3')
        self.slider17.config(highlightbackground='orangered3', highlightcolor='orangered3')
        self.slider17.place(x=250, y=500)
        b3_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value17, padx=10, pady=10)
        b3_add_to_cart.place(x=260, y=550)

        Button(self.canvas, text='NEXT PAGE', padx=15, pady=15, command=page2).place(x=1000, y=550)

    def sports_outdoor(self):
        def page4():
            def back3():
                self.canvas3.destroy()
                page3()

            self.main3.destroy()
            self.main4 = Toplevel()
            self.main4.geometry('1240x695+135+110')
            self.main4.overrideredirect(True)
            self.canvas3 = Canvas(self.main4, height=695, width=1240, bg='darkslategrey')
            self.canvas3.pack()

            picture12 = Image.open('C:/CEP Project/photos/p37.jpg')
            new_pic12 = picture12.resize((150, 150))
            self.image12 = ImageTk.PhotoImage(new_pic12)
            self.lab12 = Label(self.canvas3, image=self.image12)
            self.lab12.place(x=50, y=70)
            self.canvas3.create_text(360, 95, text=self.content[1][73][0], font='comicsansms 14 ')
            price = str(self.content[1][73][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider37 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider37.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider37.place(x=270, y=150)
            b12_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value37, padx=10, pady=10)
            b12_add_to_cart.place(x=280, y=200)

            picture13 = Image.open('C:/CEP Project/photos/p38.jpg')
            new_pic13 = picture13.resize((150, 150))
            self.image13 = ImageTk.PhotoImage(new_pic13)
            self.lab13 = Label(self.canvas3, image=self.image13)
            self.lab13.place(x=50, y=350)
            self.canvas3.create_text(390, 375, text=self.content[1][75][0], font='comicsansms 14 ')
            price = str(self.content[1][75][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider38 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider38.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider38.place(x=270, y=430)
            b13_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value38, padx=10, pady=10)
            b13_add_to_cart.place(x=280, y=480)

            picture14 = Image.open('C:/CEP Project/photos/p39.jpg')
            new_pic14 = picture14.resize((150, 150))
            self.image14 = ImageTk.PhotoImage(new_pic14)
            self.lab14 = Label(self.canvas3, image=self.image14)
            self.lab14.place(x=660, y=70)
            self.canvas3.create_text(960, 95, text=self.content[1][77][0], font='comicsansms 14 ')
            price = str(self.content[1][77][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider39 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider39.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider39.place(x=850, y=150)
            b14_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value39, padx=10, pady=10)
            b14_add_to_cart.place(x=860, y=200)

            picture15 = Image.open('C:/CEP Project/photos/p40.jpg')
            new_pic15 = picture15.resize((150, 150))
            self.image15 = ImageTk.PhotoImage(new_pic15)
            self.lab15 = Label(self.canvas3, image=self.image15)
            self.lab15.place(x=660, y=350)
            self.canvas3.create_text(960, 375, text=self.content[1][79][0], font='comicsansms 14 ')
            price = str(self.content[1][79][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider40 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider40.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider40.place(x=850, y=430)
            b15_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value40, padx=10, pady=10)
            b15_add_to_cart.place(x=860, y=480)

            Button(self.canvas3, text='PREVIOUS PAGE', padx=15, pady=15, command=back3).place(x=50, y=550)

        def page3():
            def back2():
                self.canvas2.destroy()
                page2()

            self.main2.destroy()
            self.main3 = Toplevel()
            self.main3.geometry('1240x695+135+110')
            self.main3.overrideredirect(True)
            self.canvas2 = Canvas(self.main3, height=695, width=1240, bg='darkslategrey')
            self.canvas2.pack()

            picture8 = Image.open('C:/CEP Project/photos/p33.jpg')
            new_pic8 = picture8.resize((150, 150))
            self.image8 = ImageTk.PhotoImage(new_pic8)
            self.lab8 = Label(self.canvas2, image=self.image8)
            self.lab8.place(x=50, y=70)
            self.canvas2.create_text(340, 95, text=self.content[1][65][0], font='comicsansms 14 ')
            price = str(self.content[1][65][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider33 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider33.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider33.place(x=270, y=150)
            b8_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value33, padx=10, pady=10)
            b8_add_to_cart.place(x=280, y=200)

            picture9 = Image.open('C:/CEP Project/photos/p34.jpg')
            new_pic9 = picture9.resize((150, 150))
            self.image9 = ImageTk.PhotoImage(new_pic9)
            self.lab9 = Label(self.canvas2, image=self.image9)
            self.lab9.place(x=50, y=350)
            self.canvas2.create_text(395, 375, text=self.content[1][67][0], font='comicsansms 14 ')
            price = str(self.content[1][67][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider34 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider34.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider34.place(x=270, y=430)
            b9_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value34, padx=10, pady=10)
            b9_add_to_cart.place(x=280, y=480)

            picture10 = Image.open('C:/CEP Project/photos/p35.jpg')
            new_pic10 = picture10.resize((150, 150))
            self.image10 = ImageTk.PhotoImage(new_pic10)
            self.lab10 = Label(self.canvas2, image=self.image10)
            self.lab10.place(x=660, y=70)
            self.canvas2.create_text(970, 95, text=self.content[1][69][0], font='comicsansms 14 ')
            price = str(self.content[1][69][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider35 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider35.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider35.place(x=850, y=150)
            b10_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value35, padx=10, pady=10)
            b10_add_to_cart.place(x=860, y=200)

            picture11 = Image.open('C:/CEP Project/photos/p36.jpg')
            new_pic11 = picture11.resize((150, 150))
            self.image11 = ImageTk.PhotoImage(new_pic11)
            self.lab11 = Label(self.canvas2, image=self.image11)
            self.lab11.place(x=660, y=350)
            self.canvas2.create_text(1010, 375, text=self.content[1][71][0], font='comicsansms 14 ')
            price = str(self.content[1][71][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider36 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider36.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider36.place(x=850, y=430)
            b11_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value36, padx=10, pady=10)
            b11_add_to_cart.place(x=860, y=480)

            Button(self.canvas2, text='PREVIOUS PAGE', padx=15, pady=15, command=back2).place(x=50, y=550)
            Button(self.canvas2, text='NEXT PAGE', padx=15, pady=15, command=page4).place(x=1000, y=550)

        def page2():
            def back():
                self.canvas1.destroy()
                self.sports_outdoor()

            self.main.destroy()
            self.main2 = Toplevel()
            self.main2.geometry('1240x695+135+110')
            self.main2.overrideredirect(True)
            self.canvas1 = Canvas(self.main2, height=695, width=1240, bg='darkslategrey')
            self.canvas1.pack()

            picture4 = Image.open('C:/CEP Project/photos/p29.jpg')
            new_pic4 = picture4.resize((150, 150))
            self.image4 = ImageTk.PhotoImage(new_pic4)
            self.lab4 = Label(self.canvas1, image=self.image4)
            self.lab4.place(x=50, y=70)
            self.canvas1.create_text(370, 95, text=self.content[1][55][0], font='comicsansms 14 ')
            price = str(self.content[1][55][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider29 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider29.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider29.place(x=270, y=150)
            b4_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value29, padx=10, pady=10)
            b4_add_to_cart.place(x=280, y=200)

            picture5 = Image.open('C:/CEP Project/photos/p30.jpg')
            new_pic5 = picture5.resize((150, 150))
            self.image5 = ImageTk.PhotoImage(new_pic5)
            self.lab5 = Label(self.canvas1, image=self.image5)
            self.lab5.place(x=50, y=350)
            self.canvas1.create_text(400, 375, text=self.content[1][59][0], font='comicsansms 14 ')
            price = str(self.content[1][59][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider30 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider30.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider30.place(x=270, y=430)
            b5_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value30, padx=10, pady=10)
            b5_add_to_cart.place(x=280, y=480)

            picture6 = Image.open('C:/CEP Project/photos/p31.jpg')
            new_pic6 = picture6.resize((150, 150))
            self.image6 = ImageTk.PhotoImage(new_pic6)
            self.lab6 = Label(self.canvas1, image=self.image6)
            self.lab6.place(x=660, y=70)
            self.canvas1.create_text(1010, 95, text=self.content[1][61][0], font='comicsansms 14 ')
            price = str(self.content[1][61][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider31 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider31.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider31.place(x=850, y=150)
            b6_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value31, padx=10, pady=10)
            b6_add_to_cart.place(x=860, y=200)

            picture7 = Image.open('C:/CEP Project/photos/p32.jpg')
            new_pic7 = picture7.resize((150, 150))
            self.image7 = ImageTk.PhotoImage(new_pic7)
            self.lab7 = Label(self.canvas1, image=self.image7)
            self.lab7.place(x=660, y=350)
            self.canvas1.create_text(1000, 375, text=self.content[1][63][0], font='comicsansms 14 ')
            price = str(self.content[1][63][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider32 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
            self.slider32.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
            self.slider32.place(x=850, y=430)
            b7_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value32, padx=10, pady=10)
            b7_add_to_cart.place(x=860, y=480)

            Button(self.canvas1, text='PREVIOUS PAGE', padx=15, pady=15, command=back).place(x=50, y=550)
            Button(self.canvas1, text='NEXT PAGE', padx=15, pady=15, command=page3).place(x=1000, y=550)

        self.main=Toplevel()
        self.main.geometry('1240x695+135+110')
        self.main.overrideredirect(True)
        self.canvas = Canvas(self.main,height=695,width=1240,bg='darkslategrey')
        self.canvas.pack()

        self.canvas.create_text(275, 80, text='SPORTS AND OUTDOOR', font='LucidaBright 26 bold')

        picture1 = Image.open('C:/CEP Project/photos/p26.jpg')
        new_pic1 = picture1.resize((150, 150))
        self.image1 = ImageTk.PhotoImage(new_pic1)
        self.lab1 = Label(self.canvas, image=self.image1)
        self.lab1.place(x=50, y=150)
        self.canvas.create_text(375, 175, text=self.content[1][51][0], font='comicsansms 14 ')
        price = str(self.content[1][51][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider26 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
        self.slider26.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
        self.slider26.place(x=250, y=230)
        b1_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value26, padx=10, pady=10)
        b1_add_to_cart.place(x=260, y=280)

        picture2 = Image.open('C:/CEP Project/photos/p27.jpg')
        new_pic2 = picture2.resize((150, 150))
        self.image2 = ImageTk.PhotoImage(new_pic2)
        self.lab2 = Label(self.canvas, image=self.image2)
        self.lab2.place(x=640, y=150)
        self.canvas.create_text(945, 175, text=self.content[1][53][0], font='comicsansms 14 ')
        price = str(self.content[1][53][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(880, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider27 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
        self.slider27.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
        self.slider27.place(x=810, y=230)
        b2_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value27, padx=10, pady=10)
        b2_add_to_cart.place(x=820, y=280)

        picture3 = Image.open('C:/CEP Project/photos/p28.jpg')
        new_pic3 = picture3.resize((150, 200))
        self.image3 = ImageTk.PhotoImage(new_pic3)
        self.lab3 = Label(self.canvas, image=self.image3)
        self.lab3.place(x=50, y=400)
        self.canvas.create_text(370, 425, text=self.content[1][55][0], font='comicsansms 14 ')
        price = str(self.content[1][55][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 480, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider28 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkslategrey')
        self.slider28.config(highlightbackground='darkslategrey', highlightcolor='darkslategrey')
        self.slider28.place(x=250, y=500)
        b3_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value28, padx=10, pady=10)
        b3_add_to_cart.place(x=260, y=550)

        Button(self.canvas, text='NEXT PAGE', padx=15, pady=15, command=page2).place(x=1000, y=550)

    def e_gaming(self):

        def page4():
            def back3():
                self.canvas3.destroy()
                page3()

            self.main3.destroy()
            self.main4 = Toplevel()
            self.main4.geometry('1240x695+135+110')
            self.main4.overrideredirect(True)
            self.canvas3 = Canvas(self.main4, height=695, width=1240, bg='darkorange3')
            self.canvas3.pack()

            picture12 = Image.open('C:/CEP Project/photos/p52.jpg')
            new_pic12 = picture12.resize((150, 150))
            self.image12 = ImageTk.PhotoImage(new_pic12)
            self.lab12 = Label(self.canvas3, image=self.image12)
            self.lab12.place(x=50, y=70)
            self.canvas3.create_text(390, 95, text=self.content[1][103][0], font='comicsansms 14 ')
            price = str(self.content[1][103][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider52 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider52.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider52.place(x=270, y=150)
            b12_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value52, padx=10, pady=10)
            b12_add_to_cart.place(x=280, y=200)

            picture13 = Image.open('C:/CEP Project/photos/p53.jpg')
            new_pic13 = picture13.resize((150, 150))
            self.image13 = ImageTk.PhotoImage(new_pic13)
            self.lab13 = Label(self.canvas3, image=self.image13)
            self.lab13.place(x=50, y=350)
            self.canvas3.create_text(350, 375, text=self.content[1][105][0], font='comicsansms 14 ')
            price = str(self.content[1][105][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider53 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider53.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider53.place(x=270, y=430)
            b13_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value53, padx=10, pady=10)
            b13_add_to_cart.place(x=280, y=480)

            picture14 = Image.open('C:/CEP Project/photos/p54.jpg')
            new_pic14 = picture14.resize((150, 150))
            self.image14 = ImageTk.PhotoImage(new_pic14)
            self.lab14 = Label(self.canvas3, image=self.image14)
            self.lab14.place(x=660, y=70)
            self.canvas3.create_text(1025, 95, text=self.content[1][107][0], font='comicsansms 14 ')
            price = str(self.content[1][107][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider54 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider54.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider54.place(x=850, y=150)
            b14_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value54, padx=10, pady=10)
            b14_add_to_cart.place(x=860, y=200)

            picture15 = Image.open('C:/CEP Project/photos/p55.jpg')
            new_pic15 = picture15.resize((150, 150))
            self.image15 = ImageTk.PhotoImage(new_pic15)
            self.lab15 = Label(self.canvas3, image=self.image15)
            self.lab15.place(x=660, y=350)
            self.canvas3.create_text(960, 375, text=self.content[1][109][0], font='comicsansms 14 ')
            price = str(self.content[1][109][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas3.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider55 = Scale(self.canvas3, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider55.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider55.place(x=850, y=430)
            b15_add_to_cart = Button(self.canvas3, text='Add to cart', command=self.get_value55, padx=10, pady=10)
            b15_add_to_cart.place(x=860, y=480)

            Button(self.canvas3, text='PREVIOUS PAGE', padx=15, pady=15, command=back3).place(x=50, y=550)


        def page3():
            def back2():
                self.canvas2.destroy()
                page2()

            self.main2.destroy()
            self.main3 = Toplevel()
            self.main3.geometry('1240x695+135+110')
            self.main3.overrideredirect(True)
            self.canvas2 = Canvas(self.main3, height=695, width=1240, bg='darkorange3')
            self.canvas2.pack()

            picture8 = Image.open('C:/CEP Project/photos/p48.jpg')
            new_pic8 = picture8.resize((150, 150))
            self.image8 = ImageTk.PhotoImage(new_pic8)
            self.lab8 = Label(self.canvas2, image=self.image8)
            self.lab8.place(x=50, y=70)
            self.canvas2.create_text(410, 95, text=self.content[1][95][0], font='comicsansms 14 ')
            price = str(self.content[1][95][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider48 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider48.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider48.place(x=270, y=150)
            b8_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value48, padx=10, pady=10)
            b8_add_to_cart.place(x=280, y=200)

            picture9 = Image.open('C:/CEP Project/photos/p49.jpg')
            new_pic9 = picture9.resize((150, 150))
            self.image9 = ImageTk.PhotoImage(new_pic9)
            self.lab9 = Label(self.canvas2, image=self.image9)
            self.lab9.place(x=50, y=350)
            self.canvas2.create_text(320, 375, text=self.content[1][97][0], font='comicsansms 14 ')
            price = str(self.content[1][97][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider49 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider49.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider49.place(x=270, y=430)
            b9_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value49, padx=10, pady=10)
            b9_add_to_cart.place(x=280, y=480)

            picture10 = Image.open('C:/CEP Project/photos/p50.jpg')
            new_pic10 = picture10.resize((150, 150))
            self.image10 = ImageTk.PhotoImage(new_pic10)
            self.lab10 = Label(self.canvas2, image=self.image10)
            self.lab10.place(x=660, y=70)
            self.canvas2.create_text(1015, 95, text=self.content[1][99][0], font='comicsansms 14 ')
            price = str(self.content[1][101][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider50 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider50.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider50.place(x=850, y=150)
            b10_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value50, padx=10, pady=10)
            b10_add_to_cart.place(x=860, y=200)

            picture11 = Image.open('C:/CEP Project/photos/p51.jpg')
            new_pic11 = picture11.resize((150, 150))
            self.image11 = ImageTk.PhotoImage(new_pic11)
            self.lab11 = Label(self.canvas2, image=self.image11)
            self.lab11.place(x=660, y=350)
            self.canvas2.create_text(960, 375, text=self.content[1][101][0], font='comicsansms 14 ')
            price = str(self.content[1][101][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas2.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider51 = Scale(self.canvas2, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider51.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider51.place(x=850, y=430)
            b11_add_to_cart = Button(self.canvas2, text='Add to cart', command=self.get_value51, padx=10, pady=10)
            b11_add_to_cart.place(x=860, y=480)

            Button(self.canvas2, text='PREVIOUS PAGE', padx=15, pady=15, command=back2).place(x=50, y=550)
            Button(self.canvas2, text='NEXT PAGE', padx=15, pady=15, command=page4).place(x=1000, y=550)

        def page2():
            def back():
                self.canvas1.destroy()
                self.e_gaming()

            self.main.destroy()
            self.main2 = Toplevel()
            self.main2.geometry('1240x695+135+110')
            self.main2.overrideredirect(True)
            self.canvas1 = Canvas(self.main2, height=695, width=1240, bg='darkorange3')
            self.canvas1.pack()

            picture4 = Image.open('C:/CEP Project/photos/p44.jpg')
            new_pic4 = picture4.resize((150, 150))
            self.image4 = ImageTk.PhotoImage(new_pic4)
            self.lab4 = Label(self.canvas1, image=self.image4)
            self.lab4.place(x=50, y=70)
            self.canvas1.create_text(400, 95, text=self.content[1][87][0], font='comicsansms 14 ')
            price = str(self.content[1][87][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider44 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider44.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider44.place(x=270, y=150)
            b4_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value44, padx=10, pady=10)
            b4_add_to_cart.place(x=280, y=200)

            picture5 = Image.open('C:/CEP Project/photos/p45.jpg')
            new_pic5 = picture5.resize((150, 150))
            self.image5 = ImageTk.PhotoImage(new_pic5)
            self.lab5 = Label(self.canvas1, image=self.image5)
            self.lab5.place(x=50, y=350)
            self.canvas1.create_text(395, 375, text=self.content[1][89][0], font='comicsansms 14 ')
            price = str(self.content[1][89][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(320, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider45 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider45.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider45.place(x=270, y=430)
            b5_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value45, padx=10, pady=10)
            b5_add_to_cart.place(x=280, y=480)

            picture6 = Image.open('C:/CEP Project/photos/p46.jpg')
            new_pic6 = picture6.resize((150, 150))
            self.image6 = ImageTk.PhotoImage(new_pic6)
            self.lab6 = Label(self.canvas1, image=self.image6)
            self.lab6.place(x=650, y=70)
            self.canvas1.create_text(1000, 95, text=self.content[1][91][0], font='comicsansms 14 ')
            price = str(self.content[1][91][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 140, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider46 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider46.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider46.place(x=850, y=150)
            b6_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value46, padx=10, pady=10)
            b6_add_to_cart.place(x=860, y=200)

            picture7 = Image.open('C:/CEP Project/photos/p47.jpg')
            new_pic7 = picture7.resize((150, 150))
            self.image7 = ImageTk.PhotoImage(new_pic7)
            self.lab7 = Label(self.canvas1, image=self.image7)
            self.lab7.place(x=650, y=350)
            self.canvas1.create_text(985, 375, text=self.content[1][93][0], font='comicsansms 14 ')
            price = str(self.content[1][93][1])
            if len(price) == 5:
                up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
            elif len(price) == 4:
                up_price = price[0] + ',' + price[1] + price[2] + price[3]
            self.canvas1.create_text(900, 420, text='Rs. ' + up_price, font='comicsansms 16 bold')
            self.slider47 = Scale(self.canvas1, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
            self.slider47.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
            self.slider47.place(x=850, y=430)
            b7_add_to_cart = Button(self.canvas1, text='Add to cart', command=self.get_value47, padx=10, pady=10)
            b7_add_to_cart.place(x=860, y=480)

            Button(self.canvas1, text='PREVIOUS PAGE', padx=15, pady=15, command=back).place(x=50, y=550)
            Button(self.canvas1, text='NEXT PAGE', padx=15, pady=15, command=page3).place(x=1000, y=550)

        self.main = Toplevel()
        self.main.geometry('1240x695+135+110')
        self.main.overrideredirect(True)
        self.canvas = Canvas(self.main,height=695,width=1240,bg='darkorange3')
        self.canvas.pack()

        self.canvas.create_text(275, 80, text='SPORTS AND OUTDOOR', font='LucidaBright 26 bold')

        picture1 = Image.open('C:/CEP Project/photos/p41.jpg')
        new_pic1 = picture1.resize((150, 150))
        self.image1 = ImageTk.PhotoImage(new_pic1)
        self.lab1 = Label(self.canvas, image=self.image1)
        self.lab1.place(x=50, y=150)
        self.canvas.create_text(325, 175, text=self.content[1][81][0], font='comicsansms 14 ')
        price = str(self.content[1][81][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider41 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
        self.slider41.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
        self.slider41.place(x=250, y=230)
        b1_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value41, padx=10, pady=10)
        b1_add_to_cart.place(x=260, y=280)

        picture2 = Image.open('C:/CEP Project/photos/p42.jpg')
        new_pic2 = picture2.resize((150, 150))
        self.image2 = ImageTk.PhotoImage(new_pic2)
        self.lab2 = Label(self.canvas, image=self.image2)
        self.lab2.place(x=640, y=150)
        self.canvas.create_text(980, 175, text=self.content[1][83][0], font='comicsansms 14 ')
        price = str(self.content[1][83][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(900, 220, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider42 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
        self.slider42.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
        self.slider42.place(x=840, y=230)
        b2_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value42, padx=10, pady=10)
        b2_add_to_cart.place(x=850, y=280)

        picture3 = Image.open('C:/CEP Project/photos/p43.jpg')
        new_pic3 = picture3.resize((150, 150))
        self.image3 = ImageTk.PhotoImage(new_pic3)
        self.lab3 = Label(self.canvas, image=self.image3)
        self.lab3.place(x=50, y=400)
        self.canvas.create_text(380, 425, text=self.content[1][85][0], font='comicsansms 14 ')
        price = str(self.content[1][85][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas.create_text(300, 480, text='Rs. ' + up_price, font='comicsansms 16 bold')
        self.slider43 = Scale(self.canvas, from_=0, to=50, orient=HORIZONTAL, bg='darkorange3')
        self.slider43.config(highlightbackground='darkorange3', highlightcolor='darkorange3')
        self.slider43.place(x=250, y=500)
        b3_add_to_cart = Button(self.canvas, text='Add to cart', command=self.get_value43, padx=10, pady=10)
        b3_add_to_cart.place(x=260, y=550)

        Button(self.canvas, text='NEXT PAGE', padx=15, pady=15, command=page2).place(x=1000, y=550)


class Front_page(Tk,Login_info,Display_products):
    def __init__(self):
        super().__init__()   #method overriding
        self.products = CSVFiling("C:/CEP Project/Products.csv")
        self.content = self.products.reading_from_file()
        self.products1 = CSVFiling("C:/CEP Project/Products2.csv")
        self.content2 = self.products1.reading_from_file()
        self.content[1].extend([['**hot deal**\n>Adidas Mens X \n>Adidas Tango Rosario\n(Manchester United Football)\n>Adidas Real Madrid Football\nsave Rs.3150 now','12600','10','deal']])
        self.content2[1].extend([['*************hot deal*************','12600.0','10','deal']])
        self.content[1].extend([['**Limited Offer**\n>SONY PlayStation 4 Slim 1TB Console\n>Mortal Kombat 11 (PS4)(this product is free)\n>Marvels Spider-Man: Miles Morales\n buy two and get one free\n save upto Rs.3750 ','92700','10','deal']])
        self.content2[1].extend([['***********Limited Offer**********','92700.0','10','deal']])
        self.front()
  
    def get_value56(self):
        self.quantity56=1
        self.price56=self.quantity56*float(self.content2[1][111][1])
        Display_products.cart_lst.append([self.content2[1][111][0],self.content2[1][111][1],self.quantity56,self.price56])
    
    def get_value57(self):
        self.quantity57=1
        self.price57=self.quantity57*float(self.content2[1][112][1])
        Display_products.cart_lst.append([self.content2[1][112][0],self.content2[1][112][1],self.quantity57,self.price57])

    def deal1(self):
        self.main = Toplevel()
        self.main.title('Hot Deal')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p35.jpg')
        new_pic4 = picture4.resize((150, 150))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=13, y=10)
        picture5 = Image.open('C:/CEP Project/photos/p37.jpg')
        new_pic5 = picture5.resize((150, 150))
        self.image5 = ImageTk.PhotoImage(new_pic5)
        self.lab5 = Label(self.canvas_01, image=self.image5)
        self.lab5.place(x=153, y=10)
        picture6 = Image.open('C:/CEP Project/photos/p39.jpg')
        new_pic6 = picture6.resize((150, 150))
        self.image6 = ImageTk.PhotoImage(new_pic6)
        self.lab6 = Label(self.canvas_01, image=self.image6)
        self.lab6.place(x=303, y=10)
        self.canvas_01.create_text(200, 250, text=self.content[1][111][0], font='comicsansms 14 ')
        self.canvas_01.create_text(300, 350, text='Price Before     Rs. 15,770', font='comicsansms 16 bold')
        self.canvas_01.create_text(300, 380, text='Price after deal Rs. 12,600', font='comicsansms 16 bold')
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value56, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=400)
       
    def deal2(self):
        self.main = Toplevel()
        self.main.title('Limited Offer')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p43.jpg')
        new_pic4 = picture4.resize((150, 150))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=13, y=10)
        picture5 = Image.open('C:/CEP Project/photos/p45.jpg')
        new_pic5 = picture5.resize((150, 150))
        self.image5 = ImageTk.PhotoImage(new_pic5)
        self.lab5 = Label(self.canvas_01, image=self.image5)
        self.lab5.place(x=153, y=10)
        picture6 = Image.open('C:/CEP Project/photos/p49.jpg')
        new_pic6 = picture6.resize((150, 150))
        self.image6 = ImageTk.PhotoImage(new_pic6)
        self.lab6 = Label(self.canvas_01, image=self.image6)
        self.lab6.place(x=303, y=10)
        self.canvas_01.create_text(200, 250, text=self.content[1][113][0], font='comicsansms 14 ')
        self.canvas_01.create_text(300, 350, text='Price Before     Rs. 96,450', font='comicsansms 16 bold')
        self.canvas_01.create_text(300, 380, text='Price after deal Rs. 92,700', font='comicsansms 16 bold')
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value57, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=400)
         
    def user_guide(self):
        self.main = Toplevel()
        self.main.title('User Guide')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.geometry('600x600+400+50')
        self.main.resizable(width=False, height=False)
        self.new_pic15= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/guide.jpg').resize((600,600), Image.ANTIALIAS))
        self.l = Label(self.main, image=self.new_pic15).pack()
        self.f1 = Frame(self.main)
        self.f1.place(x=0, y=0, relwidth=1)
        Label(self.main, text='FIVE STEPS FAST CHECKOUT', font='Elephant 22 bold', bg='black', fg='slate blue').place(x=30, y=10)
        Label(self.main, text="1. Create an account using SIGN-UP and then, LOG-IN.\n    (If you already have an account then simply LOG-IN)", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=100)
        Label(self.main, text="2. Open Menu on the top left side and select\nthe CATEGORY you want to browse.", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=100, y=175)
        Label(self.main, text="3. Find the right product for you, Set the quantity using a\n slider and add it to your Cart", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=255)
        Label(self.main, text="4. You can browse around the store. Your CART history\n and current CART can be viewed at all times ", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=335)
        Label(self.main, text="5. CHECKOUT ", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=200, y=415)
    
    def p10(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p10.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][19][0], font='comicsansms 14 ')
        price = str(self.content[1][19][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider10 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider10.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider10.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value10, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)

    def p35(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p35.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][69][0], font='comicsansms 14 ')
        price = str(self.content[1][69][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider35 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider35.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider35.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value35, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
       
    def p45(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p45.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][89][0], font='comicsansms 14 ')
        price = str(self.content[1][89][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider45 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider45.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider45.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value45, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
    
    def p24(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p24.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][47][0], font='comicsansms 14 ')
        price = str(self.content[1][47][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider24 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider24.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider24.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value24, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)     
    
    def p49(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p49.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][97][0], font='comicsansms 14 ')
        price = str(self.content[1][97][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider49 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider49.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider49.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value49, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
       
    def p52(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p52.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][103][0], font='comicsansms 14 ')
        price = str(self.content[1][103][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text( 350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider52 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider52.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider52.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value52, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
   
    def front(self):
        self.geometry('1366x768+0+0')
        self.minsize(width=1366, height=768)
        self.maxsize(width=1600, height=900)
        self.title('shop')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.iconphoto(False, photo)


        def forward():

            def back():
                self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
                self.canvas2.place(x=50, y=450)
                self.new_pic5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=self.new_pic5,command=self.p10).place(x=0,y=0)
                self.new_pic6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=self.new_pic6,command=self.p35).place(x=200,y=0)
                self.new_pic7 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=self.new_pic7,command=self.p45).place(x=400,y=0)
                self.new_pic8 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
                Button(self.canvas2, text='f', image=self.new_pic8, command=forward).place(x=550, y=150)


            self.canvas2.destroy()
            self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
            self.canvas2.place(x=50, y=450)
            self.new_pic5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p24.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='p24', padx=100, pady=100, image=self.new_pic5,command=self.p24).place(x=0,y=0)
            self.new_pic6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p52.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='ME', padx=100, pady=100, image=self.new_pic6,command=self.p52).place(x=200,y=0)
            self.new_pic7 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p49.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='ME', padx=100, pady=100, image=self.new_pic7,command=self.p49).place(x=400,y=0)
            self.new_pic8 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/back.jpg').resize((50,50), Image.ANTIALIAS))
            Button(self.canvas2, text='f', image=self.new_pic8, command=back).place(x=0, y=150)

        self.geometry('1366x768+0+0')
        self.minsize(width=1366, height=768)
        self.maxsize(width=1600, height=900)
        self.title('shop')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.iconphoto(False, photo)
        
        # background image
        self.new_pic4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/front.jpg').resize((1366,768), Image.ANTIALIAS))
        self.l = Label(self, image=self.new_pic4).pack()
        self.f1 = Frame(self)
        self.f1.place(x=0, y=0, relwidth=1)
        
        frame=Frame(self.f1,bg='sandy brown',bd=5)
        frame.grid(row=0,column=0,sticky=EW)
        global photo7,photo1,photo2
        photo7=PhotoImage(file='C:/CEP Project/button/menu.png')
        photo1= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/login.jpg').resize((80,60), Image.ANTIALIAS))
        # photo2=PhotoImage(file='C:/CEP Project/button/signin.png')
        photo2= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/signup.jpg').resize((80,60), Image.ANTIALIAS))
        button=Button(frame,command=self.menu,height=40,width=40,image=photo7,border=0 )
        button.grid(row=0,column=1)
        Label1=Label(frame,text='              CENTERED          ',font='Broadway 26 bold',fg='#4E236F',bg='sandy brown')
        Label1.grid(row=0,column=5,pady=10,padx=330)
        button1=Button(frame,image=photo1,command=self.login,height=60,width=80,border=0)
        button1.grid(row=0,column=25,sticky=NW,padx=10)
        button2=Button(frame,image=photo2,command=Login_info().sign_up,height=60,width=80,border=0)
        button2.grid(row=0,column=35,sticky=NW,padx=10)

        Label(self, text="BUNDLE DEALS" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=100)
        self.canvas1 = Canvas(self, height=200, width=400, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas1.place(x=50, y=150)
        self.new_pic9= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal1.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas1, text='Deal 1', command=self.deal1, padx=80, pady=200, image=self.new_pic9, bg='black').place(x=0, y=0)
        self.new_pic10= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal2.jpeg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas1, text='Deal 2', command=self.deal2, padx=80, pady=200, image=self.new_pic10, bg='black').place(x=205, y=0)
        
        self.new_pic11= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/guide.jpg').resize((100,100), Image.ANTIALIAS))
        Button(self, text='Guide', command=self.user_guide, padx=80, pady=100, bg='black', image=self.new_pic11, relief=SUNKEN).place(x=500, y=200)
        
        Label(self, text="CENTERED'S CHOICE" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=400)
        self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas2.place(x=50, y=450)
        self.new_pic5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p10', padx=100, pady=100, image=self.new_pic5, command=self.p10).place(x=0,y=0)
        self.new_pic6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p35', padx=100, pady=100, image=self.new_pic6,command=self.p35).place(x=200,y=0)
        self.new_pic7 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p45', padx=100, pady=100, image=self.new_pic7,command=self.p45).place(x=400,y=0)
        self.new_pic8 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
        Button(self.canvas2, text='f', image=self.new_pic8, command=forward).place(x=550, y=150)   
        
    def menu(self):
        self.main = Toplevel()
        self.main.geometry('150x768+0+0')
        self.main.overrideredirect(True)
        global photo2,ea,we,hf,so,eg
        self.photo2 = ImageTk.PhotoImage(Image.open('button/exit.png').resize((80,30)), Image.ANTIALIAS)
        button3 = Button(self.main,width=70,height=0,border=0,text='EXIT', command=self.main.destroy, image=self.photo2)  # here
        button3.pack(side=BOTTOM, pady=30)
        canvas1 = Canvas(self.main, height=700, width=130, bg='red')
        canvas1.pack(side=LEFT)
        ea = ImageTk.PhotoImage(Image.open('button/ea.jpg').resize((150,120), Image.ANTIALIAS))
        Button(canvas1, text='Electronic Accessories', bg='black', command=Display_products().elect_access, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=ea).place(x=0, y=10)
        we = ImageTk.PhotoImage(Image.open('button/we.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Watches and Eyewear', bg='black', command=Display_products().watches_eyewear, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=we).place(x=0, y=150)
        hf = ImageTk.PhotoImage(Image.open('button/hf.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Health and Fitness', bg='black', command=Display_products().health_fitness, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=hf).place(x=0, y=290)
        so = ImageTk.PhotoImage(Image.open('button/so.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Sports and Outdoor', bg='black', command=Display_products().sports_outdoor, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=so).place(x=0, y=430)
        eg = ImageTk.PhotoImage(Image.open('button/eg.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='E-Gaming', bg='black', command=Display_products().e_gaming, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=eg).place(x=0, y=570)
    def login(self):
        self.log_in = Login_info()
        self.log_in.login()

class Cart(Tk,Login_info,Display_products):
    cart_list=[]
    counter1= 0
    price=0
    X=datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
 ############# new main window appears after closing the previous main window including the cart option #########################################

    def __init__(self):
        super().__init__()   #method overriding
        self.products = CSVFiling("C:/CEP Project/Products.csv")
        self.content = self.products.reading_from_file()
        self.products1 = CSVFiling("C:/CEP Project/Products2.csv")
        self.content2 = self.products1.reading_from_file()
        self.content[1].extend([['**Hot deal**\n>Adidas Mens X \n>Adidas Tango Rosario\n(Manchester United Football)\n>Adidas Real Madrid Football\nsave Rs.3150 now','12600','10','deal']])
        self.content2[1].extend([['*************Hot deal*************','12600.0','10','deal']])
        self.content[1].extend([['**Limited Offer**\n>SONY PlayStation 4 Slim 1TB Console\n>Mortal Kombat 11 (PS4)(this product is free)\n>Marvels Spider-Man: Miles Morales\n buy two and get one free\n save upto Rs.3750 ','92700','10','deal']])
        self.content2[1].extend([['***********Limited Offer**********','92700.0','10','deal']])
        self.front()
    
    # # def __init__(self):
    # #     super().__init__()
    # #     self.geometry('1366x768+0+0')
    # #     self.minsize(width=1366, height=768)
    # #     self.maxsize(width=1600, height=900)
    # #     self.title('cart')
    # #     photo = PhotoImage(file = "C:/CEP Project/images.png")
    # #     self.iconphoto(False, photo)
        
    # #     def forward(): # FUNCTION FOR NEXT BUTTON

    # #         def back(): # FUNCTION FOR PREVIOUS BUTTON
    # #             self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
    # #             self.canvas2.place(x=50, y=450)
    # #             global frontp1,frontp2,frontp3,next
    # #             frontp1 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
    # #             Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp1, command=self.p10).place(x=0,y=0)
    # #             frontp2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
    # #             Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp2, command=self.p35).place(x=200,y=0)
    # #             frontp3 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
    # #             Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp3, command=self.p45).place(x=400,y=0)
    # #             next = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
    # #             Button(self.canvas2, text='f', image=next, command=forward).place(x=550, y=150)


    # #         self.canvas2.destroy()
    # #         self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
    # #         self.canvas2.place(x=50, y=450)
    # #         global frontp4,frontp5,frontp6
    # #         frontp4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p24.jpg').resize((200,200), Image.ANTIALIAS))
    # #         Button(self.canvas2, text='p24', padx=100, pady=100, image=frontp4, command=self.p24).place(x=0,y=0)
    # #         frontp5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p52.jpg').resize((200,200), Image.ANTIALIAS))
    # #         Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp5, command=self.p52).place(x=200,y=0)
    # #         frontp6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p49.jpg').resize((200,200), Image.ANTIALIAS))
    # #         Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp6, command=self.p49).place(x=400,y=0)
    # #         self.back = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/back.jpg').resize((50,50), Image.ANTIALIAS))
    # #         Button(self.canvas2, text='f', image=self.back, command=back).place(x=0, y=150)


    # #     background image
    # #     self.background_image = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/front.jpg').resize((1366,768), Image.ANTIALIAS))
    # #     self.l = Label(self, image=self.background_image).pack()
    # #     self.f1 = Frame(self)
    # #     self.f1.place(x=0, y=0, relwidth=1)


    # #     frame=Frame(self.f1,bg='sandy brown',bd=5)
    # #     frame.grid(row=0,column=0,sticky=EW)
    # #     global photo5,photo4,photo8,deal_photo1,deal_photo2,guide_picture,frontp1,frontp2,frontp3,next
    # #     photo4=PhotoImage(file='C:/CEP Project/button/logout.png')
    # #     photo8=PhotoImage(file='C:/CEP Project/button/menu.png')
    # #     photo5=PhotoImage(file='C:/CEP Project/button/cart.png')
    # #     button=Button(frame,command=self.menu,image=photo8,height=40,width=40,border=0 )
    # #     button.grid(row=0,column=1)
    # #     Label1=Label(frame,text='        Welcome to shopping cart',font='Arial 25 bold',fg='#4E236F',bg='sandy brown')
    # #     Label1.grid(row=0,column=5,pady=10,padx=270)
    # #     button=Button(frame,command=self.history,image=photo5,border=0, bg='sandy brown')
    # #     button.grid(row=0,column=15,sticky=NW,padx=10)
    # #     button1=Button(frame,command=self.Cart_show,image=photo5,height=35,width=120,border=0, bg='sandy brown')
    # #     button1.grid(row=0,column=25,sticky=NW,padx=10)
    # #     button2=Button(frame,command=login_info().log_out_window,image=photo4,border=0,width=70,height=30, bg='sandy brown')
    # #     button2.grid(row=0,column=35,sticky=NW,padx=10)    
        
    # #     UPPER PART OF FRONT PAGE
    # #     Label(self, text="BUNDLE DEALS" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=100)
    # #     self.canvas1 = Canvas(self, height=200, width=400, bg='goldenrod2', highlightbackground='goldenrod2')
    # #     self.canvas1.place(x=50, y=150)
    # #     deal_photo1= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal1.jpg').resize((200,200), Image.ANTIALIAS))
    # #     Button(self.canvas1, text='Deal 1', command=self.deal1, padx=80, pady=200, image=deal_photo1, bg='black').place(x=0, y=0)
    # #     deal_photo2= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal2.jpeg').resize((200,200), Image.ANTIALIAS))
    # #     Button(self.canvas1, text='Deal 2', command=self.deal2, padx=80, pady=200, image=deal_photo2, bg='black').place(x=205, y=0)
    
    # #     guide_picture= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/guide.jpg').resize((100,100), Image.ANTIALIAS))
    # #     Button(self.master, text='Guide', command=self.user_guide, padx=80, pady=100, bg='black', image=guide_picture, relief=SUNKEN).place(x=500, y=200)
        
    # #     BOTTOM OF THE FRONT PAGE
    # #     Label(self, text="CENTERED'S CHOICE" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=400)
    # #     self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
    # #     self.canvas2.place(x=50, y=450)
    # #     frontp1 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
    # #     Button(self.canvas2, text='p10', padx=100, pady=100, image=frontp1, command=self.p10).place(x=0,y=0)
    # #     frontp2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
    # #     Button(self.canvas2, text='p35', padx=100, pady=100, image=frontp2, command=self.p35).place(x=200,y=0)
    # #     frontp3 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
    # #     Button(self.canvas2, text='p45', padx=100, pady=100, image=frontp3, command=self.p45).place(x=400,y=0)
    # #     self.next = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
    # #     Button(self.canvas2, text='f', image=self.next, command=forward).place(x=550, y=150)
    
    def get_value56(self):
        self.quantity56=1
        self.price56=self.quantity56*float(self.content2[1][111][1])
        Display_products.cart_lst.append([self.content2[1][111][0],self.content2[1][111][1],self.quantity56,self.price56])
    
    def get_value57(self):
        self.quantity57=1
        self.price57=self.quantity57*float(self.content2[1][112][1])
        Display_products.cart_lst.append([self.content2[1][112][0],self.content2[1][112][1],self.quantity57,self.price57])
    
    def deal1(self):
        self.main = Toplevel()
        self.main.title('Hot Deal')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p35.jpg')
        new_pic4 = picture4.resize((150, 150))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=13, y=10)
        picture5 = Image.open('C:/CEP Project/photos/p37.jpg')
        new_pic5 = picture5.resize((150, 150))
        self.image5 = ImageTk.PhotoImage(new_pic5)
        self.lab5 = Label(self.canvas_01, image=self.image5)
        self.lab5.place(x=153, y=10)
        picture6 = Image.open('C:/CEP Project/photos/p39.jpg')
        new_pic6 = picture6.resize((150, 150))
        self.image6 = ImageTk.PhotoImage(new_pic6)
        self.lab6 = Label(self.canvas_01, image=self.image6)
        self.lab6.place(x=303, y=10)
        self.canvas_01.create_text(200, 250, text=self.content[1][111][0], font='comicsansms 14 ')
        self.canvas_01.create_text(300, 350, text='Price Before     Rs. 15,770', font='comicsansms 16 bold')
        self.canvas_01.create_text(300, 380, text='Price after deal Rs. 12,600', font='comicsansms 16 bold')
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value56, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=400)
       
    def deal2(self):
        self.main = Toplevel()
        self.main.title('Limited Offer')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.main.iconphoto(False, photo)
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p43.jpg')
        new_pic4 = picture4.resize((150, 150))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=13, y=10)
        picture5 = Image.open('C:/CEP Project/photos/p45.jpg')
        new_pic5 = picture5.resize((150, 150))
        self.image5 = ImageTk.PhotoImage(new_pic5)
        self.lab5 = Label(self.canvas_01, image=self.image5)
        self.lab5.place(x=153, y=10)
        picture6 = Image.open('C:/CEP Project/photos/p49.jpg')
        new_pic6 = picture6.resize((150, 150))
        self.image6 = ImageTk.PhotoImage(new_pic6)
        self.lab6 = Label(self.canvas_01, image=self.image6)
        self.lab6.place(x=303, y=10)
        self.canvas_01.create_text(200, 250, text=self.content[1][113][0], font='comicsansms 14 ')
        self.canvas_01.create_text(300, 350, text='Price Before     Rs. 96,450', font='comicsansms 16 bold')
        self.canvas_01.create_text(300, 380, text='Price after deal Rs. 92,700', font='comicsansms 16 bold')
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value57, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=400)
            
    def user_guide(self):
        self = Toplevel()
        self.title('User Guide')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.iconphoto(False, photo)
        self.geometry('600x600+400+50')
        self.resizable(width=False, height=False)
        self.guide_picture= ImageTk.PhotoImage(Image.open('button/guide.jpg').resize((600,600), Image.ANTIALIAS))
        self.l = Label(self, image=self.guide_picture).pack()
        self.f1 = Frame(self)
        self.f1.place(x=0, y=0, relwidth=1)
        Label(self, text='FIVE STEPS FAST CHECKOUT', font='Elephant 22 bold', bg='black', fg='slate blue').place(x=30, y=10)
        Label(self, text="1. Create an account using SIGN-UP and then, LOG-IN.\n    (If you already have an account then simply LOG-IN)", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=100)
        Label(self, text="2. Open Menu on the top left side and select\nthe CATEGORY you want to browse.", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=100, y=175)
        Label(self, text="3. Find the right product for you, Set the quantity using a\n slider and add it to your Cart", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=255)
        Label(self, text="4. You can browse around the store. Your CART history\n and current CART can be viewed at all times ", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=50, y=335)
        Label(self, text="5. CHECKOUT ", font='BahnschriftSemiBold 14', bg='black', fg='cyan3').place(x=200, y=415)

    def p10(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p10.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][19][0], font='comicsansms 14 ')
        price = str(self.content[1][19][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider10 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider10.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider10.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value10, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)

    def p35(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p35.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][69][0], font='comicsansms 14 ')
        price = str(self.content[1][69][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider35 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider35.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider35.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value35, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
       
    def p45(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p45.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][89][0], font='comicsansms 14 ')
        price = str(self.content[1][89][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider45 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider45.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider45.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value45, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
    
    def p24(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p24.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][47][0], font='comicsansms 14 ')
        price = str(self.content[1][47][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider24 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider24.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider24.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value24, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)     
    
    def p49(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p49.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][97][0], font='comicsansms 14 ')
        price = str(self.content[1][97][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text(350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider49 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider49.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider49.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value49, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
       
    def p52(self):
        self.main = Toplevel()
        self.main.title("CENTERED'S CHOICE")
        self.main.geometry('500x500+400+50')
        self.main.resizable(width=False, height=False)
        self.canvas_01 = Canvas(self.main, height=500, width=470, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas_01.place(x=13, y=10)
        picture4 = Image.open('C:/CEP Project/photos/p52.jpg')
        new_pic4 = picture4.resize((250, 250))
        self.image4 = ImageTk.PhotoImage(new_pic4)
        self.lab4 = Label(self.canvas_01, image=self.image4)
        self.lab4.place(x=30, y=50)
        self.canvas_01.create_text(200, 350, text=self.content[1][103][0], font='comicsansms 14 ')
        price = str(self.content[1][103][1])
        if len(price) == 5:
            up_price = price[0] + price[1] + ',' + price[2] + price[3] + price[4]
        elif len(price) == 4:
            up_price = price[0] + ',' + price[1] + price[2] + price[3]
        self.canvas_01.create_text( 350, 100, text='Rs. '+up_price, font='comicsansms 16 bold')
        self.slider52 = Scale(self.canvas_01, from_=0, to=50, orient=HORIZONTAL, bg='goldenrod2')
        self.slider52.config(highlightbackground='goldenrod2', highlightcolor='goldenrod2')
        self.slider52.place(x=300, y=150)
        b4_add_to_cart = Button(self.canvas_01, text='Add to cart', command=self.get_value52, padx=10, pady=10)
        b4_add_to_cart.place(x=300, y=210)
    
    def menu(self):
        self.main = Toplevel()
        self.main.geometry('150x768+0+0')
        self.main.overrideredirect(True)
        global photo2,ea,we,hf,so,eg
        self.photo2 = ImageTk.PhotoImage(Image.open('button/exit.png').resize((80,30)), Image.ANTIALIAS)
        button3 = Button(self.main,width=70,height=0,border=0,text='EXIT', command=self.main.destroy, image=self.photo2)  # here
        button3.pack(side=BOTTOM, pady=30)
        canvas1 = Canvas(self.main, height=700, width=130, bg='red')
        canvas1.pack(side=LEFT)
        ea = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/ea.jpg').resize((150,120), Image.ANTIALIAS))
        Button(canvas1, text='Electronic Accessories', bg='black', command=Display_products().elect_access, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=ea).place(x=0, y=10)
        we = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/we.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Watches and Eyewear', bg='black', command=Display_products().watches_eyewear, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=we).place(x=0, y=150)
        hf = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/hf.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Health and Fitness', bg='black', command=Display_products().health_fitness, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=hf).place(x=0, y=290)
        so = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/so.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='Sports and Outdoor', bg='black', command=Display_products().sports_outdoor, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=so).place(x=0, y=430)
        eg = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/eg.jpg').resize((150,120)), Image.ANTIALIAS)
        Button(canvas1, text='E-Gaming', bg='black', command=Display_products().e_gaming, padx=20, pady=30, font="ArialRoundedMTBold 12 bold", image=eg).place(x=0, y=570)
    
    def front(self):
        self.geometry('1366x768+0+0')
        self.minsize(width=1366, height=768)
        self.maxsize(width=1600, height=900)
        self.title('shop')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.iconphoto(False, photo)


        def forward(): # FUNCTION FOR NEXT BUTTON

            def back(): # FUNCTION FOR PREVIOUS BUTTON
                self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
                self.canvas2.place(x=50, y=450)
                global frontp1,frontp2,frontp3,next
                frontp1 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp1, command=self.p10).place(x=0,y=0)
                frontp2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp2, command=self.p35).place(x=200,y=0)
                frontp3 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
                Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp3, command=self.p45).place(x=400,y=0)
                next = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
                Button(self.canvas2, text='f', image=next, command=forward).place(x=550, y=150)


            self.canvas2.destroy()
            self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
            self.canvas2.place(x=50, y=450)
            global frontp4,frontp5,frontp6
            frontp4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p24.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='p24', padx=100, pady=100, image=frontp4, command=self.p24).place(x=0,y=0)
            frontp5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p52.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp5, command=self.p52).place(x=200,y=0)
            frontp6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p49.jpg').resize((200,200), Image.ANTIALIAS))
            Button(self.canvas2, text='ME', padx=100, pady=100, image=frontp6, command=self.p49).place(x=400,y=0)
            self.back = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/back.jpg').resize((50,50), Image.ANTIALIAS))
            Button(self.canvas2, text='f', image=self.back, command=back).place(x=0, y=150)


        # background image
        self.background_image = ImageTk.PhotoImage(Image.open('C:/CEP Project/background/front.jpg').resize((1366,768), Image.ANTIALIAS))
        self.l = Label(self, image=self.background_image).pack()
        self.f1 = Frame(self)
        self.f1.place(x=0, y=0, relwidth=1)


        frame=Frame(self.f1,bg='sandy brown',bd=5)
        frame.grid(row=0,column=0,sticky=EW)
        global photo5,photo4,photo6,photo8,deal_photo1,deal_photo2,guide_picture,frontp1,frontp2,frontp3,next
        self.photo4 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/logout.jpg').resize((70,30), Image.ANTIALIAS))
        photo8 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/menu.png').resize((40,40), Image.ANTIALIAS))
        photo5 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/cart.png').resize((100,40), Image.ANTIALIAS))
        button=Button(frame,command=self.menu,image=photo8,height=40,width=40,border=0 )
        button.grid(row=0,column=1)
        Label1=Label(frame,text='              CENTERED          ',font='Broadway 26 bold',fg='#4E236F',bg='sandy brown')
        Label1.grid(row=0,column=5,pady=10,padx=270)
        photo6 = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/carthistory.jpg').resize((100,70), Image.ANTIALIAS))
        button3=Button(frame,command=self.history,image=photo6,height=70,width=100,border=0, bg='sandy brown')
        button3.grid(row=0,column=15,sticky=NW,padx=10)
        button1=Button(frame,command=self.Cart_show,image=photo5,height=40,width=100,border=0, bg='sandy brown')
        button1.grid(row=0,column=30,sticky=NW,padx=10)
        self.button2=Button(frame,command=lambda : Login_info.log_out_window(self),image=self.photo4,border=0,width=100,height=40, bg='sandy brown')
        self.button2.grid(row=0,column=40,sticky=NW,padx=10)    
        # self.promotion()
        # UPPER PART OF FRONT PAGE
        Label(self, text="BUNDLE DEALS" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=100)
        self.canvas1 = Canvas(self, height=200, width=400, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas1.place(x=50, y=150)
        deal_photo1= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal1.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas1, text='Deal 1', command=self.deal1, padx=80, pady=200, image=deal_photo1, bg='black').place(x=0, y=0)
        deal_photo2= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/deal2.jpeg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas1, text='Deal 2', command=self.deal2, padx=80, pady=200, image=deal_photo2, bg='black').place(x=205, y=0)
    
        guide_picture= ImageTk.PhotoImage(Image.open('C:/CEP Project/button/guide.jpg').resize((100,100), Image.ANTIALIAS))
        Button(self.master, text='Guide', command=self.user_guide, padx=80, pady=100, bg='black', image=guide_picture, relief=SUNKEN).place(x=500, y=200)
        
        # BOTTOM OF THE FRONT PAGE
        Label(self, text="CENTERED'S CHOICE" , font='Broadway 26 bold', bg='Darkgoldenrod1').place(x=50, y=400)
        self.canvas2 = Canvas(self, height=200, width=600, bg='goldenrod2', highlightbackground='goldenrod2')
        self.canvas2.place(x=50, y=450)
        frontp1 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p10.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p10', padx=100, pady=100, image=frontp1, command=self.p10).place(x=0,y=0)
        frontp2 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p35.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p35', padx=100, pady=100, image=frontp2, command=self.p35).place(x=200,y=0)
        frontp3 = ImageTk.PhotoImage(Image.open('C:/CEP Project/photos/p45.jpg').resize((200,200), Image.ANTIALIAS))
        Button(self.canvas2, text='p45', padx=100, pady=100, image=frontp3, command=self.p45).place(x=400,y=0)
        self.next = ImageTk.PhotoImage(Image.open('C:/CEP Project/button/arrow.jpg').resize((50,50), Image.ANTIALIAS))
        Button(self.canvas2, text='f', image=self.next, command=forward).place(x=550, y=150)

            
    def Cart_show(self):
        self.cart= Toplevel()
        self.cart.geometry('800x400+300+120')
        self.cart.minsize(width=800, height=400)
        self.cart.maxsize(width=800, height=400)
        label01=Label(self.cart,text=f'Welcome to your cart {Login_info.lst[0][0]}') 
        label01.pack()
        canvas3 = Canvas(self.cart, height=30, width=750, bg='khaki4')
        canvas3.pack()
        button01=Button(canvas3,text='Select and remove item',command=self.removeItem)
        button01.pack(side=RIGHT)
        button02=Button(canvas3,text='Checkout ',command=self.open1)
        button02.pack(side=LEFT)
        label02=Label(self.cart,text='  Product Name     \t\t\t       Price            Quantity                Total amount  ')
        label02.pack(padx=0,anchor=W)
        #self.cart.overrideredirect(True)
        scrollbar = Scrollbar(self.cart)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listbox = Listbox(self.cart, width=110, height=45,bg='#D0E6D7',fg='#465961',highlightcolor='#8DC6B0',highlightbackground='#B98DC6',highlightthickness=10,selectbackground='#B98DC6' )
        self.listbox.pack()
        l=len(Display_products.cart_lst)
        for i in range(1,l+1):                        
            def check():
                if len(str(Display_products.cart_lst[i-1][2]))==1:
                    return '0'+str(Display_products.cart_lst[i-1][2])
                else:
                    return str(Display_products.cart_lst[i-1][2])
            t=str(Display_products.cart_lst[i-1][0])+'       \t\t\t       '+str(Display_products.cart_lst[i-1][1])+'               '+str(check())+'                     '+str(round(Display_products.cart_lst[i-1][3],0))
            self.listbox.insert(i,t)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
 
    def removeItem(self):
        self.lst_new=Display_products.cart_lst
        y=self.listbox.get(ANCHOR)
        for i, res in enumerate(Display_products.cart_lst): 
            def check():
                if len(str(res[2]))==1:
                    return '0'+str(res[2])
                else:
                    return str(res[2])

            x=str(res[0])+'       \t\t\t       '+str(res[1])+'               '+str(check())+'                     '+str(round(res[3],0))
            if  x==y:
                Cart.counter1+=1
                if res in self.lst_new:
                    self.lst_new.remove(res)
                    self.listbox.delete(ANCHOR)
            else:
                pass 

    def save_to_file(self):
        self.price=0
        if  Cart.counter1==0 :
            with open('C:/CEP Project/cart.csv', 'a') as self.csvfile: 
                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                for j, res in enumerate(Display_products.cart_lst):
                    self.row=[[Login_info.lst[0][0],Login_info.lst[0][3],res[0],res[1],res[2],res[3],Login_info.lst[0][4],str(Cart.X),self.price]]
                    csvwriter.writerows(self.row)

        elif Cart.counter1!=0:
            with open('C:/CEP Project/cart.csv', 'a') as self.csvfile: 
                csvwriter = csv.writer(self.csvfile,dialect='excel') 
                for j, res in enumerate(self.lst_new):
                    self.row=[[Login_info.lst[0][0],Login_info.lst[0][3],res[0],res[1],res[2],res[3],str(Cart.X),self.price]]
                    csvwriter.writerows(self.row)
   
    def last(self):
        self.save_to_file()
        self.list=list
        self.cart= Toplevel()
        self.cart.geometry('400x400+300+120')
        self.cart.minsize(width=800, height=400)
        self.cart.maxsize(width=800, height=400)
        self.cart.title('checkout')
        self.label1=Label(self.cart,text=f'your order will be delivered to the following address\n{Login_info.lst[0][4]}')
        self.label1.pack()
        canvas4 = Canvas(self.cart, height=70, width=750, bg='khaki4')
        canvas4.pack()
        button01=Button(canvas4,text='back to shopping',command=self.cart.destroy)
        button01.pack(side=RIGHT)
        button02=Button(canvas4,text='close',command=root.destroy())
        button02.pack(side=LEFT)
        
    def checkout(self,list):
        self.list=list
        self.cart= Toplevel()
        self.cart.geometry('900x400+300+120')
        self.cart.minsize(width=900, height=400)
        self.cart.maxsize(width=900, height=400)
        self.cart.title('checkout')
        photo = PhotoImage(file = "C:/CEP Project/images.png")
        self.iconphoto(False, photo)
        self.label1=Label(self.cart,text=f'Your order number is {Login_info.lst[0][3]}')
        self.label1.pack()
        canvas4 = Canvas(self.cart, height=70, width=750, bg='khaki4')
        canvas4.pack()
        button01=Button(canvas4,text='Back to cart',command=self.open)
        button01.pack(side=RIGHT)
        button02=Button(canvas4,text='Confirm order',command=self.last)
        button02.pack(side=LEFT)
        self.label1=Label(canvas4,text=f'{Cart.X}')
        self.label1.pack(side=LEFT,padx=200)
        canvas5=Canvas(self.cart, height=70, width=750, bg='khaki4')
        canvas5.pack()
        for k, res in enumerate(self.list):
            self.price+=round(res[3],0)
        self.label3=Label(canvas5,text=(f'Your total amount is PKR.{self.price}'))
        self.label3.pack(padx=0,anchor=E)
        self.label3=Label(self.cart,text='Product Name     \t\t\t       Price         Quantity                Total amount  ')
        self.label3.pack(padx=0,anchor=W)
        scrollbar = Scrollbar(self.cart)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listbox = Listbox(self.cart, width=110, height=45,bg='#D0E6D7',fg='#465961',highlightcolor='#8DC6B0',highlightbackground='#B98DC6',highlightthickness=10,selectbackground='#B98DC6'  )
        self.listbox.pack()
        for k, res in enumerate(self.list):
            x=str(res[0])+'    \t          '+str(res[1])+'               '+str(res[2])+'                     '+str(round(res[3],0))
            self.listbox.insert(k,x)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

    def open1(self):
        Login_info().open
        if Cart.counter1==0:
            self.cart.destroy()
            self.checkout(Display_products.cart_lst)
        if Cart.counter1!=0:
            self.cart.destroy()
            self.checkout(self.lst_new)

    def open(self):
        super().open()
        self.cart.destroy()
        self.Cart_show()
    
    def history(self):
        self.cart= Toplevel()
        self.cart.geometry('900x400+300+120')
        self.cart.minsize(width=900, height=400)
        self.cart.maxsize(width=900, height=400)
        self.cart.title('History')
        self.label1=Label(self.cart,text=f'Your order number is :{Login_info.lst[0][3]}')
        self.label1.pack()
        canvas4 = Canvas(self.cart, height=70, width=750)
        canvas4.pack()
        button01=Button(canvas4,text='Back to order',command=self.cart.destroy)
        button01.pack(side=RIGHT)
        self.label1=Label(canvas4,text=f'By name :{Login_info.lst[0][0]}')
        self.label1.pack(side=LEFT,padx=200)
        canvas5=Canvas(self.cart, height=70, width=750, bg='khaki4')
        canvas5.pack()
        self.products2 = CSVFiling("C:/CEP Project/cart.csv")
        self.content3 = self.products2.reading_from_file()
        self.content3=list(self.content3)
        self.content3.pop(0)
        self.content3[0]= [x for x in self.content3 if x != []]
        self.label3=Label(canvas5,text=(f'Your total amount was PKR.{self.content3[0][0][1][5]}\nYour address {Login_info.lst[0][4]} , date of purchase:{self.content3[0][0][1][7]}'))
        self.label3.pack(padx=0,anchor=E)
        self.label3=Label(self.cart,text='Product Name     \t\t\t       Price          Quantity                Total amount             Date')
        self.label3.pack(padx=0,anchor=W)
        self.yscrollbar = Scrollbar(self.cart)
        self.yscrollbar.pack(side=RIGHT,fill=Y)

        self.listbox = Listbox(self.cart, width=150, height=45,bg='#D0E6D7',fg='#465961',highlightcolor='#8DC6B0',highlightbackground='#B98DC6',highlightthickness=10,selectbackground='#B98DC6'  )
        self.listbox.pack()
        for k, res in enumerate(self.content3[0][0]):
            try:
                if len(res)==0:
                    raise IndexError
            except IndexError:
                pass
            else:
                if res[1]==Login_info.lst[0][3]:
                    x=str(res[2])+'    \t          '+str(res[3])+'               '+str(res[4])+'                     '+str(res[5])+'               '+str(res[7])
                    self.listbox.insert(k,x)
          
        self.listbox.config(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar.config(command=self.listbox.yview)
        
    

        



if __name__ == "__main__":
    root= Front_page()
    root.mainloop()
