from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np

room_types = [
    "Normal Standard Room", 
    "Comfort Deluxe Room", 
    "Premium Family Suite", 
    "Executive Business Suite"
]

room_prices = {
    "Normal Standard Room": 1200,
    "Comfort Deluxe Room": 2500,
    "Premium Family Suite": 4500,
    "Executive Business Suite": 7500
}

room_status = {
    "Normal Standard Room": "Not Filled",
    "Comfort Deluxe Room": "Not Filled",
    "Premium Family Suite": "Not Filled",
    "Executive Business Suite": "Not Filled"
}
customer_list = []
total_revenue_tracker = []
def update_status_labels():
    status_label1.config(text=room_status["Normal Standard Room"])
    status_label2.config(text=room_status["Comfort Deluxe Room"])
    status_label3.config(text=room_status["Premium Family Suite"])
    status_label4.config(text=room_status["Executive Business Suite"])

def click_book_button():
    customer = nameentry.get().strip()
    selected_room = room_combo_box.get()
    
    if customer == "":
        messagebox.showerror("Error", "Please enter the customer name.")
        return
        
    if selected_room == "":
        messagebox.showerror("Error", "Please pick a room type from the list.")
        return
        
    if room_status[selected_room] == "Filled":
        messagebox.showerror("Taken", f"Sorry, the '{selected_room}' is already Filled!")
        return
        
    room_status[selected_room] = "Filled"
    customer_list.append(customer)
    
    base_price = room_prices[selected_room]
    cgst = int(base_price * 0.09)
    sgst = int(base_price * 0.09)
    
    money_array = np.array([base_price, cgst, sgst])
    total_bill = np.sum(money_array)
    
    total_revenue_tracker.append(total_bill)
    
    all_prices = np.array(list(room_prices.values()))
    print("\n--- Current Room Status Catalog Update ---")
    print("Live Bookings Track Details:", room_status)
    print("Total Customers Registered:", len(customer_list))
    print("Total Revenue Earned: ₹", np.sum(total_revenue_tracker))
    print("Highest priced baseline room value: ₹", np.max(all_prices))
    print("------------------------------------------\n")
    
    update_status_labels()
    
    invoice_popup = Toplevel(window)
    invoice_popup.title("Hotel Bill")
    invoice_popup.geometry("700x700")
    invoice_popup.configure(bg="white")
    
    invoice_text = f"""
    =========================================
               HOTEL INVOICE & BILL          
    =========================================
    Customer Name : {customer}
    Room Type     : {selected_room}
    Base Price    : ₹{base_price}
    CGST (9%)     : ₹{cgst}
    SGST (9%)     : ₹{sgst}
    -----------------------------------------
    TOTAL PAID    : ₹{total_bill}
    =========================================
    Status        : Paid Successfully
    =========================================
    
     IMPORTANT CHECK-IN INSTRUCTIONS:
    1. Booking successful!
    2. Please bring your aadhar and booking print out with you.
    """
    
    receipt_lbl = Label(invoice_popup, text=invoice_text, font=("Courier", 11), justify="left", bg="white", fg="gray")
    receipt_lbl.pack(pady=20, padx=20)
    
    nameentry.delete(0, END)
    room_combo_box.set("")
    
 
    messagebox.showinfo("Success", "Booking successful!\n\nPlease bring your aadhar and booking print out with you.")

def click_checkout_button():
    selected_room = room_combo_box.get()
    
    if selected_room == "":
        messagebox.showerror("Error", "Please select a room type option from dropdown to check-out.")
        return
        
    if room_status[selected_room] == "Not Filled":
        messagebox.showerror("Error", f"The room type '{selected_room}' is already vacant (Not Filled).")
        return
        
    room_status[selected_room] = "Not Filled"
    update_status_labels()
    room_combo_box.set("")
    messagebox.showinfo("Checked Out", f"The room type '{selected_room}' is now vacant.")

window = Tk()
window.title("Hotel Room Booking System") 
window.geometry("900x650") 
window.configure(bg="beige")

heading = Label(window, text="Grand Royal Hotel Booking Portal", font=("EB Garmond", 24, "bold"), bg="white", fg="black")
heading.place(x=50, y=30)

namelabel = Label(window, text="Customer Full Name:", font=("EB Garmond", 14, "bold"), bg='beige', fg='black')
namelabel.place(x=50, y=150)

nameentry = Entry(window, width=32, font=("EB Garmond", 14), bg="white", fg="black")
nameentry.place(x=50, y=185)

roomlabel = Label(window, text="Select Room Category Type:", font=("EB Garmond", 14, "bold"), bg='beige', fg='black')
roomlabel.place(x=50, y=240)

room_combo_box = ttk.Combobox(window, width=30, font=("EB Garmond", 14), state="readonly")
room_combo_box["values"] = room_types
room_combo_box.place(x=50, y=275)

book_btn = Button(window, text="Process Payment & Book", font=("EB Garmond", 12, "bold"), bg="green", fg="white", width=28, height=2, command=click_book_button)
book_btn.place(x=50, y=340)

checkout_btn = Button(window, text="Check-Out Room Type", font=("EB Garmond", 12, "bold"), bg="darkred", fg="white", width=28, height=2, command=click_checkout_button)
checkout_btn.place(x=50, y=410)

info_lbl_box = Label(window, text="Base Rates Catalog Card:\n----------------------------------------\n• Normal Room      : ₹1,200/N\n• Deluxe Room      : ₹2,500/N\n• Family Suite      : ₹4,500/N\n• Executive Suite      : ₹7,500/N", font=("Courier", 10, "bold"), bg="white", fg="black", justify="left", relief="solid", bd=1, padx=10, pady=10)
info_lbl_box.place(x=50, y=490)

table_heading = Label(window, text="Live Room Allocation Status Panel", font=("EB Garmond", 14, "bold"), bg="beige", fg="black")
table_heading.place(x=450, y=150)

title_col1 = Label(window, text="Room Type Category", font=("EB Garmond", 11, "bold"), bg="white", width=24, padx=5)
title_col1.place(x=450, y=190)

title_col2 = Label(window, text="Price", font=("EB Garmond", 11, "bold"), bg="white", width=8)
title_col2.place(x=670, y=190)

title_col3 = Label(window, text="Current Status", font=("EB Garmond", 11, "bold"), bg="white", width=12)
title_col3.place(x=750, y=190)

r1_name = Label(window, text="Normal Standard Room", font=("EB Garmond", 11), bg="white", width=24, padx=5)
r1_name.place(x=450, y=225)
r1_price = Label(window, text="₹1200", font=("EB Garmond", 11), bg="white", width=8)
r1_price.place(x=670, y=225)
status_label1 = Label(window, text="", font=("EB Garmond", 11, "bold"), fg="blue", bg="white", width=12)
status_label1.place(x=750, y=225)

r2_name = Label(window, text="Comfort Deluxe Room", font=("EB Garmond", 11), bg="white", width=24, padx=5)
r2_name.place(x=450, y=260)
r2_price = Label(window, text="₹2500", font=("EB Garmond", 11), bg="white", width=8)
r2_price.place(x=670, y=260)
status_label2 = Label(window, text="", font=("EB Garmond", 11, "bold"), fg="blue", bg="white", width=12)
status_label2.place(x=750, y=260)

r3_name = Label(window, text="Premium Family Suite", font=("EB Garmond", 11), bg="white", width=24, padx=5)
r3_name.place(x=450, y=295)
r3_price = Label(window, text="₹4500", font=("EB Garmond", 11), bg="white", width=8)
r3_price.place(x=670, y=295)
status_label3 = Label(window, text="", font=("EB Garmond", 11, "bold"), fg="blue", bg="white", width=12)
status_label3.place(x=750, y=295)

r4_name = Label(window, text="Executive Business Suite", font=("EB Garmond", 11), bg="white", width=24, padx=5)
r4_name.place(x=450, y=330)
r4_price = Label(window, text="₹7500", font=("EB Garmond", 11), bg="white", width=8)
r4_price.place(x=670, y=330)
status_label4 = Label(window, text="", font=("EB Garmond", 11, "bold"), fg="blue", bg="white", width=12)
status_label4.place(x=750, y=330)

update_status_labels()
window.mainloop()
