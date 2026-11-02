import os
from customtkinter import *
from PIL import Image, ImageTk  # Ensure ImageTk is imported
import json
with open('credits.json','r') as f:
    credit = json.load(f)



non_alphanumeric = [
    # ASCII Punctuation & Symbols
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    
    # Common Extended Unicode & Math Symbols
    '€', '£', '¥', '₹', '¢', '©', '®', '™', '°', '•', '¶', '§', '…',
    '–', '—', '“', '”', '‘', '’', '«', '»', '±', '×', '÷', '≠', '≤', '≥', '∞', '√',
    
    # Whitespace Characters
    ' ', '\t', '\n', '\r', '\v', '\f'
    ]
def confirmation():
    global non_alphanumeric
    usr_cnt = False
    pas1 =password.get()
    pas2 =password_check.get()
    usr =username.get()


    for axo in usr:
        if axo in non_alphanumeric:
            usr_cnt = True
            
    if usr_cnt == False:
        if len(pas1) > 10:
            error_label.configure(text = "Password should be within 10 characters")            
        elif pas1 !=pas2:
            error_label.configure(text = "You have entered the wrong password") 
        elif usr=="":
            error_label.configure(text = "Enter A valid username") 
        else:
            print("The user proceeds to the next column")
            print("HELLO"+" "+usr)
            credit["entry"] = 1
            credit["username"] = usr
            credit["password"] = pas2
            login.destroy()
    else:
        error_label.configure(text = "The Username should only have numbers and alphabet") 
set_appearance_mode("Dark")
if credit["entry"] == 0:
    login = CTk()
    login.geometry("1000x600")
    login.title("Login Page")

    image_path = os.path.join("images", "logo.png")
    icon_image = Image.open(image_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    login.wm_iconbitmap()
    login.after(200, lambda: login.iconphoto(False, icon_photo))

    main_frame =CTkFrame(login)

    logo_frame = CTkFrame(main_frame)
    logo_image = Image.open("images/logo.png")
    logoimg_label = CTkLabel(logo_frame,image=CTkImage(logo_image,size=(100,100)),text="VORAGO",compound=LEFT,font=("Nasalization",50))
    logoimg_label.grid()
    logo_frame.configure(fg_color="transparent")
    logo_frame.grid(sticky="we",pady=(20,20),padx =30,row =1,column=0)


    login_text = CTkLabel(main_frame,text="LOGIN",font =("Roboto",30) )
    login_text.grid()

    user_frame =CTkFrame(main_frame)
    icon_image =  Image.open("images/icon.png")
    user_label = CTkLabel(user_frame,text="Username",image=CTkImage(icon_image),compound=LEFT)
    username = CTkEntry(user_frame,width=400,height=37,corner_radius=5,border_color="White",border_width=2,bg_color="transparent",fg_color="transparent",placeholder_text="username")
    user_label.grid(sticky = "nw")
    username.grid(pady =(0,20))
    user_frame.grid()
    user_frame.configure(fg_color = "black")

    password_frame  = CTkFrame(main_frame)
    lock = Image.open("images/lock.png")
    pas_label =CTkLabel(password_frame,text="Password",image=CTkImage(lock),compound=LEFT)
    password = CTkEntry(password_frame,width=400,height=37,corner_radius=5,border_color="White",border_width=2,
                        bg_color="transparent",
                        fg_color="transparent",placeholder_text="password")
    pas_label.grid(sticky = "nw")
    password.grid(pady = (0,20))
    password_frame.grid()
    password_frame.configure(fg_color = "black")

    password_check = CTkEntry(main_frame,width=400,height=37,corner_radius=5,
                    border_color="White",border_width=2,bg_color="transparent",
                    fg_color="transparent",placeholder_text="Re-enter your password",show="*")
    password_check.grid(pady = (0,20))

    confirm =CTkButton(main_frame,text="Confirm",command=confirmation,fg_color="Black",corner_radius=10,border_width=3,border_color="white",hover_color="black")
    confirm.grid()

    error_label = CTkLabel(main_frame,text="",bg_color="white")
    error_label.grid()

    main_frame.configure(fg_color="black")
    main_frame.grid(sticky ="ns",column =1,row =0)
    image_frame = CTkFrame(login,fg_color="White")
    bg_img = Image.open("images/blackhole(bg).png")
    bgimg_label = CTkLabel(image_frame,image=CTkImage(bg_img,size=(800,600)),text="")
    bgimg_label.grid()
    image_frame.grid(column=0,row =0,sticky="nswe")
    login.grid_columnconfigure(0,weight =1)
    login.grid_rowconfigure(0,weight =1)
    login.resizable(False,False)
    login.mainloop()
    with open('credits.json','w') as f:
        json.dump(credit,f,indent=4)
