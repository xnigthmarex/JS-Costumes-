import MySQLdb
import tkinter
from tkinter import ttk
import datetime
import tkinter.messagebox as message
from tkcalendar import Calendar
from pymysql import*
import xlwt
import pandas.io.sql as sql
import tkinter.messagebox as message
root = tkinter.Tk()
root.title("JS COSTUMES")
root.geometry("530x400")

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text="          Add customer           ")
tab_control.pack(expand=1, fill='both')
tab_control.add(tab2, text="          Update Record            ")
tab_control.pack(expand=1, fill='both')
tab_control.add(tab3, text="              Record                     ")
tab_control.pack(expand=1, fill='both')
tab_control.add(tab4, text="              Inventory                   ")
tab_control.pack(expand=1, fill='both')


def inventory():



  db = MySQLdb.connect("localhost", "root", "admin", "jscustomerdetails")
  values = (dress_inv.get(),piece_inv.get(),size_inv.get(),date_inv.get(),year_inv.get(),
             price_inv.get(),rentprice_inv.get())
  cursor = db.cursor()

  sql = """INSERT INTO inventory(dress,piece,size,date,year,price,rent
           )
          VALUES (%s,%s,%s,%s,%s,%s,%s)"""
  cursor.execute(sql, values)
  
  

  dress_inv.delete(0, "end")
  piece_inv.delete(0, "end")
  size_inv.delete(0, "end")
  year_inv.delete(0, "end")
  price_inv.delete(0, "end")
  rentprice_inv.delete(0, "end")
  message.showinfo("JS Costumes","Data Added")
  


  db.commit()
  db.close()
 

def set1():

# connect the mysql with the python
  con=connect(user="root",password="admin",host="localhost",database="JSCustomerdetails")
# read the data
  df=sql.read_sql('select * from inventory',con)
# print the data
  print(df)
# export the data into the excel sheet
  df.to_excel('Inventory.xlsx')
  message.showinfo("JS COSTUMES", "Added to inventory")


def set():
  #exec(open("ViewCustomer.py").read())
  con=connect(user="root",password="admin",host="localhost",database="JSCustomerdetails")
  # read the data
  df=sql.read_sql('select * from jscostumes',con)
  # print the data
  print(df)
# export the data into the excel sheet
  df.to_excel('JSCustomerdetails.xlsx')
  message.showinfo("JS COSTUMES", "Exported successfully")


def update():
    #exec(open("UpdateCustomer.py").read())
    customer_name=customername_update.get()
    customer_address=customeraddress_update.get()
    customer_mobile_number=customermobilenumber_update.get()
    dress=dress_update.get()
    date=date_update.get()
    security_amount=securityamount_update.get()
    amount=amount_update.get()
    status=status_update.get()


    db = MySQLdb.connect("localhost", "root", "admin", "jscustomerdetails")
    cursor = db.cursor()
    cursor.execute("update jscostumes set customer_name='"+ customer_name + "',customer_address='"+ customer_address +"',dress='"+dress+"',security_amount='"+security_amount+"',amount='"+amount+"',status='"+status+"'")




    db.commit()
    customername_update.delete(0, "end")
    customeraddress_update.delete(0, "end")
    customermobilenumber_update.delete(0, "end")
    dress_update.delete(0, "end")
    securityamount_update.delete(0, "end")
    amount_update.delete(0, "end")

    message.showinfo("JS Costumes","Updated Successful")
    db.close()


def get():
    #exec(open("AddCustomer.py").read())
    db = MySQLdb.connect("localhost", "root", "admin", "jscustomerdetails")
    cursor = db.cursor()
    cursor.execute("select * from jscostumes where customer_mobile_number ='"+ selectbox.get() +"'")
    rows=cursor.fetchall()
    for row in rows:

	    customername_update.insert(0,row[1])
	    customeraddress_update.insert(0,row[2])
	    customermobilenumber_update.insert(0,row[3])
	    dress_update.insert(0,row[5])
	    date_update.insert(0,row[4])
	    securityamount_update.insert(0,row[6])
	    amount_update.insert(0,row[7])
	

    db.commit()
    db.close()

#def example2():
 #   def print_sel1():
  #      global stop
   #     stop=tkinter.Entry(tab3,width=15)
    #    stop.insert(0,cal.selection_get())
     #   stop.grid(row=1, column=4)
      #  top2.destroy()

    #top2 = tkinter.Toplevel(root)

    #cal = Calendar(top2,
     #              font="Arial 14", selectmode='day',
      #             cursor="hand1", year=2020, month=5, day=30)
    #cal.pack(fill="both", expand=True)
    #tkinter.Button(top2, text="        ok          ", command=print_sel1).pack()
    
#def example1():
 #   def print_sel():
  #      global start
   #     start=tkinter.Entry(tab3,width=15)
    #    start.insert(0,cal.selection_get())
     #   start.grid(row=1, column=1)
      #  top1.destroy()
    #top1 = tkinter.Toplevel(root)

    #cal = Calendar(top1,
     #              font="Arial 14", selectmode='day',
      #             cursor="hand1", year=2020, month=5, day=30)
    #cal.pack(fill="both", expand=True)
    #tkinter.Button(top1, text="        ok          ", command=print_sel).pack()
    


    


def submit():
    db = MySQLdb.connect("localhost", "root", "admin", "jscustomerdetails")
    values = (customername.get(), customeraddress.get(), customermobilenumber.get(), dress.get(), date.get(),
              securityamount.get(), amount.get(), typehoosen.get(), status.get())
    cursor = db.cursor()

    sql = """INSERT INTO jscostumes(customer_name,customer_address,customer_mobile_number,dress,date,security_amount,amount,type,status
           )
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql, values)
    db.commit()
    message.showinfo("JS COSTUMES", "Added a new customer")

    customername.delete(0, "end")
    customeraddress.delete(0, "end")
    customermobilenumber.delete(0, "end")
    dress.delete(0, "end")
    securityamount.delete(0, "end")
    amount.delete(0, "end")


# creating entery boxes tab1 ////////////////////////////////////////////////////////////////////////////////////////////////////////

# serialnumber= tkinter.Entry(tab1, width=15)

# serialnumber.grid(row=2, column=1)

customername = tkinter.Entry(tab1, width=15)
customername.grid(row=4, column=1)

customeraddress = tkinter.Entry(tab1, width=15)
customeraddress.insert(0, "kompally")
customeraddress.grid(row=5, column=1)

customermobilenumber = tkinter.Entry(tab1, width=15)
customermobilenumber.grid(row=6, column=1)

dress = tkinter.Entry(tab1, width=15)
dress.grid(row=7, column=1)

date = tkinter.Entry(tab1, width=15)
date.insert(0, str(datetime.date.today()))
date.grid(row=4, column=4)

securityamount = tkinter.Entry(tab1, width=15)
# securityamount(0,"disabled")
securityamount.grid(row=6, column=4)

amount = tkinter.Entry(tab1, width=15)
amount.grid(row=5, column=4)

# type= tkinter.Entry(tab1, width=15)
# type.grid(row=6, column=1)

status = tkinter.Entry(tab1, width=15)
status.insert(0, 'Open')
status.grid(row=3, column=4)

# creating labelk for the entery boxes tab1///////////////////////////////////////////////////////////////////////////////////////////////
c_lbl = tkinter.Label(tab1, text=" JS Costumes ", padx=10, pady=10, font=("Times", "25", "bold italic"), fg="red")
c_lbl.grid(row=1, column=0, columnspan=5)

c_lbl = tkinter.Label(tab1, text="Customer Details ", padx=10, pady=10, font=("Times", "20", "bold italic"), fg="blue")
c_lbl.grid(row=2, column=0, columnspan=5)
# c_lbl=tkinter.Label(tab1,text="Serial Number :",padx=10,pady=10, font=("Times", "13", "bold italic"))
# c_lbl.grid(row=2,column=0)

c_lbl = tkinter.Label(tab1, text="Customer Name :", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=4, column=0)

c_lbl = tkinter.Label(tab1, text="Customer Address: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=5, column=0)

c_lbl = tkinter.Label(tab1, text="Mobile Number : ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=6, column=0)

c_lbl = tkinter.Label(tab1, text=" Dress :", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=7, column=0)

c_lbl = tkinter.Label(tab1, text=" Date: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=4, column=3)

c_lbl = tkinter.Label(tab1, text="Security Amount:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=5, column=3)

c_lbl = tkinter.Label(tab1, text=" Amount: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=6, column=3)

c_lbl = tkinter.Label(tab1, text=" Type: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=0)

n = tkinter.StringVar()
typehoosen = ttk.Combobox(tab1, width=13, textvariable=n)
typehoosen['values'] = (' Rent',
                        ' Sale',
                        ' Alteration',
                        )
typehoosen.current(0)
typehoosen.grid(column=1, row=3)
c_lbl = tkinter.Label(tab1, text=" Status", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=3)
# creating a submit button
submit_but = tkinter.Button(tab1, text="Submit", command=submit, padx=50, font=("Times", "13", "bold italic"),
                            fg="blue")
submit_but.grid(row=8, column=0, columnspan=6)

# submit_but=tkinter.Button(tab1,text="Submit",command=select,padx=50, font=("Times", "13", "bold italic"))
# submit_but.grid(row=9,column=0,columnspan=6)

# creating label for enterng the mobile number

c_lbl = tkinter.Label(tab2, text="Enter the  Mobile Number:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=1, column=0, columnspan=2)

# creating a entry box and a button
selectbox = tkinter.Entry(tab2, width=15)
selectbox.grid(row=1, column=3)

submit_but = tkinter.Button(tab2, text="Search", command=get, font=("Times", "11", "bold italic"), fg="blue")
submit_but.grid(row=1, column=4)

# creating label,entry boxesfor tab2///////////////////////////////////////////////////////////////////////////////////////////////////////
customername_update = tkinter.Entry(tab2, width=15)
customername_update.grid(row=4, column=1)

customeraddress_update = tkinter.Entry(tab2, width=15)
customeraddress_update.grid(row=5, column=1)

customermobilenumber_update = tkinter.Entry(tab2, width=15)
customermobilenumber_update.grid(row=6, column=1)

dress_update = tkinter.Entry(tab2, width=15)
dress_update.grid(row=7, column=1)

date_update = tkinter.Entry(tab2, width=15)
date_update.grid(row=4, column=4)

securityamount_update = tkinter.Entry(tab2, width=15)
# securityamount(0,"disabled")
securityamount_update.grid(row=6, column=4)

amount_update = tkinter.Entry(tab2, width=15)
amount_update.grid(row=5, column=4)

# type= tkinter.Entry(tab1, width=15)
# type.grid(row=6, column=1)

status_update = tkinter.Entry(tab2, width=15)
status_update.insert(0, 'Closed')
status_update.grid(row=3, column=4)

# creating labels for tab2
c_lbl = tkinter.Label(tab2, text="Customer Name :", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=4, column=0)

c_lbl = tkinter.Label(tab2, text="Customer Address: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=5, column=0)

c_lbl = tkinter.Label(tab2, text="Mobile Number : ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=6, column=0)

c_lbl = tkinter.Label(tab2, text=" Dress :", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=7, column=0)

c_lbl = tkinter.Label(tab2, text=" Date: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=4, column=3)

c_lbl = tkinter.Label(tab2, text="Security Amount:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=5, column=3)

c_lbl = tkinter.Label(tab2, text=" Amount: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=6, column=3)

c_lbl = tkinter.Label(tab2, text=" Type: ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=0)

n_update = tkinter.StringVar()
typehoosen_update = ttk.Combobox(tab2, width=13, textvariable=n_update)
typehoosen_update['values'] = (' Rent',
                               ' Sale',
                               ' Alteration',
                               )
typehoosen_update.current(0)
typehoosen_update.grid(column=1, row=3)

c_lbl = tkinter.Label(tab2, text=" Status", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=3)

# creating button for update
submit_but = tkinter.Button(tab2, text="Update Record", command=update, padx=50, font=("Times", "13", "bold italic"),
                            fg="red")
submit_but.grid(row=8, column=0, columnspan=6)

# creating tab3
#c_lbl = tkinter.Label(tab3, text="Income Report :", padx=10, pady=10, font=("Times", "13", "bold italic"))
#c_lbl.grid(row=0, column=0)
#n_edit = tkinter.StringVar()
#typehoosen_edit = ttk.Combobox(tab3, width=13, textvariable=n_edit)
#typehoosen_edit['values'] = (' Rent',
 #                            ' Sale',
  #                           ' Alteration',
   #                          )
#typehoosen_edit.current(0)
#typehoosen_edit.grid(column=1, row=0)

# submit_but=tkinter.Button(tab3,text="Update Record", font=("Times", "10", "bold italic"),fg="red")
# submit_but.grid(row=0,column=3)
# date_edit= tkinter.StringVar()
# date_edit = ttk.Combobox(tab3, width = 13, textvariable = n_edit)
# date_edit['values'] = (' Rent',
#                         ' Sale',
#                         ' Alteration',
#                         )
# date_edit.current(0)
# date_edit.grid(column = 1, row = 1)

#t = tkinter.Button(tab3, text='From', command=example1, padx=25)
#t.grid(row=1, column=0)

#t = tkinter.Button(tab3, text='To', command=example2, padx=25)
#t.grid(row=1, column=3)


submit_but = tkinter.Button(tab3, text="Export Records to Excel",padx=40,pady=20, font=("Times", "13", "bold italic"),command=set)
submit_but.place(relx=0.5, rely=0.5, anchor="center")
#creating tad4 for inventory
c_lbl = tkinter.Label(tab4, text="Add Inventory", padx=10, pady=10, font=("Times", "25", "bold italic"), fg="green")
c_lbl.grid(row=0, column=0, columnspan=6)
c_lbl = tkinter.Label(tab4, text="          Dress:          ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=1, column=0)
c_lbl = tkinter.Label(tab4, text="          Piece:          ", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=1, column=3)
c_lbl = tkinter.Label(tab4, text="Size:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=2, column=0)
c_lbl = tkinter.Label(tab4, text="year:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=0)
c_lbl = tkinter.Label(tab4, text="Date:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=2, column=3)
c_lbl = tkinter.Label(tab4, text="Price:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=3, column=3)
c_lbl = tkinter.Label(tab4, text="Rent Price:", padx=10, pady=10, font=("Times", "13", "bold italic"))
c_lbl.grid(row=4, column=0)


#creating entry boxes
dress_inv = tkinter.Entry(tab4, width=15)
dress_inv.grid(row=1, column=1)
piece_inv = tkinter.Entry(tab4, width=15)
piece_inv.grid(row=1, column=4)
size_inv = tkinter.Entry(tab4, width=15)
size_inv.grid(row=2, column=1)
date_inv = tkinter.Entry(tab4, width=15)
date_inv.insert(0, str(datetime.date.today()))
date_inv.grid(row=2, column=4)
price_inv = tkinter.Entry(tab4, width=15)
price_inv .grid(row=3, column=1)
rentprice_inv = tkinter.Entry(tab4, width=15)
rentprice_inv.grid(row=3, column=4)
year_inv = tkinter.Entry(tab4, width=15)
year_inv.grid(row=4, column=1)

submit_but = tkinter.Button(tab4, text="Add to Inventory", font=("Times", "13", "bold italic"),command=inventory)
submit_but.grid(row=6,column=0,columnspan=7)

submit_but = tkinter.Button(tab4, text="Export Records to Excel",font=("Times", "13", "bold italic"),command=set1)
submit_but.grid(row=7,column=0,columnspan=7)

root.mainloop()