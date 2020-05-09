import time
import os 
import tkinter as tk 
import re

#----WINDOWS SETTINGS---->
win = tk.Tk()
win.resizable(False , False)
win.title("TXTer - nico99x")
win.geometry("400x300")
win.configure(background = "whitesmoke")
win.columnconfigure(0 , weight = 1)



#----Button Function---->
def generator_button():
    #get text input in entry widget
    n_i = name_entry.get()
    s_i = surname_entry.get()
    d_i = date_entry.get()
    e_i = email_entry.get()
    #check if the entry widgets are correctly filled
    #all fields are required

    #regex for the control of the correct format of the e-mail
    if not re.match(r"[^@]+@[^@+]\.^@+" , e_i):
        email_entry.delete(0 , 30)
        email_entry.insert(0 , "Invalid e-mail format! ")


    if str(n_i and s_i) == "":
        while True:
            name_entry.delete(0,30) 
            name_entry.insert(0 , "Required")
            surname_entry.delete(0,30)
            surname_entry.insert(0 , "Required")
            break
            continue
            
        
    #this check if the date in input match with the correct format 
    try:
        d_i != time.strptime(d_i , '%d/%m/%Y')
    except(ValueError):
        date_entry.delete(0 , 30)
        date_entry.insert(0, "This is not a valid date!") 
    else: 
        try:
            dir_name = n_i
            os.mkdir(n_i)
            file_name = os.path.join(n_i , n_i+".txt")
            with open(file_name , 'wt') as f:
                f.write('\n---->Name : ' + str(n_i))
                f.write('\n---->Surname : ' + str(s_i))
                f.write('\n---->Date : ' + str(d_i))
                f.write('\n---->E-mail : ' + str(e_i))
                process_label = tk.Label(win , text = "Your TXT file is Ready!" , bg = "green" , font = ("Ubuntu" , 12))
                process_label.grid(row = 6 , column = 0 , columnspan = 3 , pady = 15)
                process_label.after(1500 , process_label.destroy)
        except(FileExistsError):
            process_label = tk.Label(win , text = "The directory with the name '"+dir_name+"' already exists!" , bg = "red" , font = ("Ubuntu" , 12))
            process_label.grid(row = 6 , column = 0 , columnspan = 3 , pady = 15)
            process_label.after(1500 , process_label.destroy)






#----WIDGETS---->

"""
--------------
Name Section
--------------
"""

name = tk.Label(win , text = "Your name : " ,  bg = "whitesmoke",  font=("Ubuntu" , 11))
name.grid(row = 0 , column = 0 , pady = 5 , padx = 10)

name_entry = tk.Entry(win , width = 30  , font = ("Ubuntu" , 11))
name_entry.grid(row = 0 , column = 1 , padx = 4)


"""
------------------
First Name Section
------------------
"""

surname = tk.Label(win , text = "Your Surname : " , bg = "whitesmoke",  font=("Ubuntu" , 11))
surname.grid(row = 1 , column = 0 , pady = 5 , padx = 10)

surname_entry = tk.Entry(win , width = 30 , font = ("Ubuntu" , 11))
surname_entry.grid(row = 1 , column = 1 , padx = 4)



"""
------------
Date Section
------------
"""

date = tk.Label(win , text = "Your Birth Date: " , bg = "whitesmoke" ,  font=("Ubuntu" , 11))
date.grid(row = 2 , column = 0 , pady = 5 , padx = 10)

date_entry = tk.Entry(win , width = 30 , font = ("Ubuntu" , 11))
date_entry.grid(row = 2 , column = 1 , padx = 4)


"""
--------------
E-Mail Section
--------------
"""

email = tk.Label(win , text = "Your e-mail: " , bg = "whitesmoke" ,   font=("Ubuntu" , 11))
email.grid(row = 3 , column = 0 , pady = 5 , padx = 10)

email_entry = tk.Entry(win , width = 30 , font = ("Ubuntu" , 11))
email_entry.grid(row = 3 , column = 1 , padx = 4)

    
"""
------------------------------
Generate file creation button
------------------------------
"""

generate_button = tk.Button(win , text = "Generate new file!" , command = generator_button , font = ("Ubuntu" , 11))
generate_button.grid(row = 5 , column = 0 , columnspan = 3 , pady = 30 , sticky = "")






#windows mainloop
win.mainloop()