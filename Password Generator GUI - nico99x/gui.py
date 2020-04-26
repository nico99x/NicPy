import tkinter as tk
import random , string


#function generator with exception handling
def psw_generator():
    try:
        if int(lenght_psw.get()) >= 6 :
            #password generator                   
            pwd = ''.join(random.choice(str(random.randint(1,9))+ string.ascii_letters + string.ascii_uppercase
                + string.ascii_lowercase + string.digits + '!@#$%^&*()')for l in range(int(lenght_psw.get())))
            text_response = str(pwd)
        else:
            text_response = "Your password must be at least 6 characters long!"
    except(ValueError): 
         text_response = "Insert a valid number!"
        
    #generating the blank space with the output
    text_space = tk.Text(win , height = 1)
    text_space.insert(tk.END , text_response) 
    text_space.grid(row = 4 , column = 0 , sticky = "S")

#window settings - geometry of the window, not resizable and the title - color background
#and column expansion
win = tk.Tk()
win.geometry("500x300")
win.resizable(False , False)
win.configure(background = "gainsboro")
win.grid_columnconfigure(0 , weight = 1)
win.title("Password Generator - nico99x")

#widget creation
intro = tk.Label(text = "Click the button below to generate a password!" , 
                font = ("Helvetica" , 11))
intro.grid(row = 0 , column = 0 , sticky = "N", padx = 20)

intro2 = tk.Label(text = "--Remember: your password must be at least 6 characters long.--" , 
                font = ("Helvetica" , 11))
intro2.grid(row = 1 , column = 0 , sticky = "N", padx = 30)

lbl = tk.Label(text = "-How many characters should your password have?" ,
                font = ("Helvetica" , 10))
lbl.grid(row = 3 , column = 0 , sticky = "W" , padx = 30 , pady = 10)
 
gen_button = tk.Button(text = "Generate!" , font = "Helvetica" , command = psw_generator)
gen_button.grid(row = 4 , column = 0 , sticky = "WE" , pady = 30 )

lenght_psw = tk.Entry(win , width = "4")
lenght_psw.grid(row = 3 , column = 0 , sticky = "E" , padx = 120 , pady = 10)


#window mainloop
win.mainloop()

