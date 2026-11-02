import os
from customtkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Ensure ImageTk is imported
import json,time
import practice_questions as pq
from math_questions import mtasks
from phy_questions import ptasks
from chem_questions import ctasks

with open('credits.json','r') as f:
    credit = json.load(f)
with open('c_ans_storage.json','r') as c_a:
    details = json.load(c_a)



    


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACTIVE_THEME_FILE = credit["theme"]
ACTIVE_APPEARANCE = "dark"

THEME_FILES = {
    "Default": "app_theme.json",
    "Rich": "app_theme_black_gold.json",
    "Modern Sleek": "app_theme_clean_modern.json",
    "Cosmic Blue": "app_theme_blue_cosmic.json",
    "Aurora": "app_theme_cosmic_aurora.json",
}
def l_d():
    global ACTIVE_APPEARANCE
    if l_dswitch.get() ==1 :
        l_dswitch.configure(text="Switch to Dark Mode")
        set_appearance_mode("light")
        

    elif l_dswitch.get()==0:
        l_dswitch.configure(text="Switch to Light Mode")
        set_appearance_mode("dark")

usr = 1
pas = 1


def taskbar1():
    maths.grid_forget()
    phy.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar2():
    maths.grid(sticky = "nswe",row=0,column=0)
    phy.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar3():
    phy.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar4():
    chem.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    phy.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar5():
    settings.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    phy.grid_forget()
    chem.grid_forget()
    home_page.grid_forget()
def ch_usrname():
    global usr
    
    user_name.configure(state="normal")
    ch_usr.configure(text="Save")
    usr *=-1
    if usr == 1:
        user_name.configure(state="readonly")
        credit["username"]=user_name.get()
        user_name.insert(0,credit["username"])
        ch_usr.configure(text="Change Username")
        with open('credits.json','w') as f:
            json.dump(credit,f,indent=4)

    


def ch_password():
    global pas
    password.configure(state="normal",show="")
    ch_pass.configure(text="Save")
    pas *=-1
    if pas == 1:
        password.configure(state="readonly",show="*")
        credit["password"]=password.get()
        password.insert(0,credit["password"])
        ch_pass.configure(text="Change Password")
        with open('credits.json','w') as f:
            json.dump(credit,f,indent=4)




def font_chk():
    font_tit = tit_var.get()
    l =[info_l,font_l]
    if font_tit =="Liberation Mono":
        for liber in l:
            f_size=liber.cget("font")[1]
            liber.configure(font=("Liberation Mono",f_size))
        info_l.update()
    elif font_tit =="Arial":
        for ari in l:
            f_size=ari.cget("font")[1]
            ari.configure(font=("Arial",f_size))
        info_l.update()
    elif font_tit =="Fira Sans Condensed":
        for fsc in l:
            f_size=fsc.cget("font")[1]
            fsc.configure(font=("Fira Sans Condensed",f_size))
        info_l.update()

def heading(parent,content,p,row):
        
    if p ==0:
            label = CTkLabel(parent,text=content,font=("Nasalization",50),anchor="n",justify="center")
            label.grid(sticky ="n",row=row,column=0)
    if p ==1:
            label = CTkLabel(parent,text=content,font=("Nasalization",50))
            label.grid(sticky="w",row=row,column=0)

def paragrah(parent,content,row):
    label = CTkLabel(parent,text=content,font=("Fira Sans Condensed",30),justify="left",wraplength="1500")
    label.grid(sticky="w",row=row,column=0,padx=60,pady=20)

page_no = 1


def mshortcut_repeater(no):
        sc = CTkLabel(math_frame,text=f"Shortcut {no}",font=("Nasalization",40),fg_color="transparent")
        arrow_button = CTkButton(math_frame,text="➜",font=("arial",40),width=10,bg_color="transparent",
        command=lambda mtask=no: mtasks(mtask, maths, math_frame, heading, paragrah,pq))  
        arrow_button.grid(row=no,column=1,pady=8,padx=8)
        sc.grid(row=no,column=0,pady=8,padx=8)
def pshortcut_repeater(no):
        sc = CTkLabel(phy_frame,text=f"Shortcut {no}",font=("Nasalization",40),fg_color="transparent")
        arrow_button = CTkButton(phy_frame,text="➜",font=("arial",40),width=10,bg_color="transparent",
        command=lambda ptask=no: ptasks(ptask, phy, phy_frame, heading, paragrah,pq))  
        arrow_button.grid(row=no,column=1,pady=8,padx=8)
        sc.grid(row=no,column=0,pady=8,padx=8)
def cshortcut_repeater(no):
        sc = CTkLabel(chem_frame,text=f"Shortcut {no}",font=("Nasalization",40),fg_color="transparent")
        arrow_button = CTkButton(chem_frame,text="➜",font=("arial",40),width=10,bg_color="transparent",
        command=lambda ctask=no: ctasks(ctask, chem, chem_frame, heading, paragrah,pq))  
        arrow_button.grid(row=no,column=1,pady=8,padx=8)
        sc.grid(row=no,column=0,pady=8,padx=8)

def pan_chk():
    pan_mode = pan_var.get()
    if pan_mode == 1:
            app_window.rowconfigure(0, weight=0)
            app_window.rowconfigure(1, weight=0)
            app_window.rowconfigure(2, weight=0)
            app_window.columnconfigure(0, weight=1)
            app_window.columnconfigure(1,weight=0)
            app_window.columnconfigure(2,weight=0)
            logo.grid(column=0, row=0, pady=5, padx=15)
            math.grid(column=1, row=0, padx=10)
            phys.grid(column=2, row=0, padx=10)
            chems.grid(column=3, row=0, padx=10)
            logo5.grid(column=4, row=0, padx=10)
            side_pannel.rowconfigure(0, weight=1)
            for side_i1 in range(5):
                side_pannel.columnconfigure(side_i1, weight=1)
                if side_i1 != 0:
                 side_pannel.rowconfigure(side_i1, weight=1)
                
            side_pannel.grid(row=0, column=0, sticky="ew")
            spacer.grid(row=1, column=0, sticky="ew")
            spacer.configure(app_window, fg_color="transparent", height=0,width=0)
            spacer.grid_forget()
            main_frame.grid(row=2, column=0, sticky="nswe")


    else:
            app_window.columnconfigure(0, weight=0)
            app_window.columnconfigure(1, weight=0)
            app_window.columnconfigure(2, weight=1)
            app_window.rowconfigure(0, weight=1)
            logo.grid(column=0, row=0, pady=15, padx=5)
            math.grid(column=0, row=1, pady=10)
            phys.grid(column=0, row=2, pady=10)
            chems.grid(column=0, row=3, pady=10)
            logo5.grid(column=0, row=4, pady=10)
            side_pannel.columnconfigure(0, weight=1)
            for side_i2 in range(5):
                side_pannel.rowconfigure(side_i2, weight=1)
                if side_i2 != 0:
                 side_pannel.columnconfigure(side_i2, weight=0)
            side_pannel.rowconfigure(0, weight=1)
            side_pannel.grid(row=0, column=0, sticky="ns",pady=40,padx=10)
            spacer.configure(app_window, fg_color="transparent", width=10,height=0)
            spacer.grid(row=0, column=1, sticky="ns")
            main_frame.grid(row=0, column=2, sticky="nswe")

def build_ui():
    global Arial_f, Fsc_f, Theme, accurate, ch_pass, ch_usr, chem,chems, chem_d, chem_frame, chem_l, con_var, content, font_frame, font_l, gear_d, gear_l, home_page, icon, info_l, info_user, l_dswitch, lib_mono, logo, logo5, logo_img, logo_label, main_frame, math, math_d, math_frame, math_l, maths, pan_var, pannel_mode, pannel_normal, pannel_text, pannel_ver, password, phy,phys, phy_d, phy_frame, phy_l, placeholder_badge, settings, side_pannel, spacer, t_switch, text_l, tit_var, title_font, user_name,progress

    set_default_color_theme(os.path.join(BASE_DIR, ACTIVE_THEME_FILE))
    set_appearance_mode(ACTIVE_APPEARANCE)

    # Keep the root window alive and rebuild only its child widgets.
    for widget in app_window.winfo_children():
        widget.destroy()

    #Side Pannel-------------------------------------------
    side_pannel =  CTkFrame(app_window)
    side_pannel.configure(corner_radius=10)



    #Images ____________________________________________________________________
    logo_img = Image.open("images/logo.png")
    math_d = Image.open("images/maths_dark.png")
    math_l = Image.open("images/math_light.png")
    phy_d = Image.open("images/phy_dark.png")
    phy_l = Image.open("images/phy_light.png")
    chem_d= Image.open("images/chem_dark.png")
    chem_l = Image.open("images/chem_light.png")
    gear_d= Image.open("images/gear_dark.png")
    gear_l = Image.open("images/gear_light.png")
    accurate = Image.open("images/badge_accuracte.png")
    placeholder_badge = Image.open("images/place_holder.png")
    #Images ____________________________________________________________________

    #Taskbar ____________________________________________________________________
    
    #Taskbar ____________________________________________________________________
    logo = CTkLabel(
        side_pannel,
        image=CTkImage(logo_img, size=(50, 50)),
        text=""
    )
    logo.grid(column=0, row=0, pady=15, padx=5)

    icon = Image.open("images/icon.png")

    math = CTkButton(
        side_pannel,
        image=CTkImage(light_image=math_d, dark_image=math_l, size=(40, 40)),
        width=50, height=50, text="", bg_color="transparent",
        fg_color="transparent", command=taskbar2
    )
    math.grid(column=0, row=1, pady=10)

    phys= CTkButton(
        side_pannel,
        image=CTkImage(light_image=phy_d, dark_image=phy_l, size=(40, 40)),
        text="", width=50, height=50, bg_color="transparent",
        fg_color="transparent", command=taskbar3
    )
    phys.grid(column=0, row=2, pady=10)

    chems = CTkButton(
        side_pannel,
        image=CTkImage(light_image=chem_d, dark_image=chem_l, size=(40, 40)),
        text="", width=50, height=50, bg_color="transparent",
        fg_color="transparent", command=taskbar4
    )
    chems.grid(column=0, row=3, pady=10)

    logo5 = CTkButton(
        side_pannel,
        image=CTkImage(light_image=gear_d, dark_image=gear_l, size=(40, 40)),
        text="", width=50, height=50, bg_color="transparent",
        fg_color="transparent", command=taskbar5
    )
    logo5.grid(column=0, row=4, pady=10)

    side_pannel.columnconfigure(0, weight=1)
    side_pannel.rowconfigure(0, weight=1)
    side_pannel.rowconfigure(1, weight=1)
    side_pannel.rowconfigure(2, weight=1)
    side_pannel.rowconfigure(3, weight=1)
    side_pannel.rowconfigure(4, weight=1)
    side_pannel.rowconfigure(5, weight=1)

    
    side_pannel.grid(row=0, column=0, sticky="ns",pady=40,padx=10)


    
    # Vertical spacer
    spacer = CTkFrame(app_window, fg_color="transparent", width=10)
    spacer.grid(row=0, column=1, sticky="ns")

    #-------------------------------------------------------------------------------

    #Main frame display ------------------------------------
    
    # Main frame display ------------------------------------
    main_frame = CTkFrame(app_window)
    main_frame.grid(row=0, column=2, sticky="nswe")

    app_window.columnconfigure(0, weight=0)
    app_window.columnconfigure(1, weight=0)
    app_window.columnconfigure(2, weight=1)
    app_window.rowconfigure(0, weight=1)

    
    home_page = CTkFrame(main_frame)
    home_page.rowconfigure(0,weight=1)
    home_page.columnconfigure(0,weight=1)
    home_page.rowconfigure(1,weight=1)
    logo_label = CTkLabel(home_page,text="VORAGO \n HOME",fg_color="transparent",font=("Nasalization",70),compound=BOTTOM,height=10)
    text_l =CTkLabel(home_page,text="Click the icons above to continue",fg_color="transparent",font=("Arial",70),compound=BOTTOM)
    text_l.grid(column = 0, row= 1)
    logo_label.grid(column = 0, row= 0)
    home_page.grid(sticky="nsew")

    maths= CTkFrame(main_frame,corner_radius=25)
    math_frame = CTkFrame(maths,corner_radius=25,width=20)
    heading(math_frame,"Maths Shortcuts",0,0)
    math_frame.grid(sticky="nswe",row=0,column=0,pady=8,padx=8)
    math_frame.columnconfigure(0,weight=1)
    for math_i in range(1,11):
        mshortcut_repeater(math_i)
    
    maths.columnconfigure(0,weight=1)             
    maths.rowconfigure(0,weight=1) 
    maths.grid_forget()

    phy = CTkFrame(main_frame,corner_radius=25)
    phy_frame = CTkFrame(phy,width=20,corner_radius=25)
    phy_frame.columnconfigure(0,weight=1)
    heading(phy_frame,"Physics Shortcuts",0,0)
    for phy_i in range(1,11):
        pshortcut_repeater(phy_i)
    phy_frame.grid(row=0,column=0,sticky="nswe",pady=8,padx=8)
    phy.rowconfigure(0,weight=1)
    phy.columnconfigure(0,weight=1)
    phy.grid_forget()

    chem = CTkFrame(main_frame,corner_radius=25)
    chem_frame = CTkFrame(chem,corner_radius=25,width=20)
    chem_frame.columnconfigure(0,weight=1)
    chem_frame.grid(sticky="nswe",row=0,column=0,pady=8,padx=8)
    heading(chem_frame,"Chemistry Shortcuts",0,0)
    for chem_i in range(1,11):
        cshortcut_repeater(chem_i)
    chem.rowconfigure(0,weight=1)
    chem.columnconfigure(0,weight=1)
    chem.grid_forget()
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    settings = CTkFrame(main_frame)
    Theme = CTkFrame(settings,corner_radius=20,border_width=3)
    l_dswitch = CTkSwitch(
        Theme,
        text="Switch to Dark Mode" if ACTIVE_APPEARANCE == "light" else "Switch to Light Mode",
        command=l_d,
        font=("Fira Sans Condensed", 20),
    )
    l_dswitch.grid(column=0,row=0,sticky="n",padx=8,pady=8)
    if ACTIVE_APPEARANCE == "light":
        l_dswitch.select()
    t_switch = CTkOptionMenu(
        Theme,
        values=list(THEME_FILES.keys()),
        font=("Fira Sans Condensed", 20),
        command=theme_switch,
    )
    t_switch.set(next(
        label for label, filename in THEME_FILES.items()
        if filename == ACTIVE_THEME_FILE
    ))
    t_switch.grid(row=1,column=0,sticky="w",padx=8,pady=8)
    Theme.grid(row=0,column=0,sticky="we")


    tit_var = StringVar(value="Fira Sans Condensed")
    con_var = StringVar(value="Fira Sans Condensed")

    font_frame = CTkFrame(settings,corner_radius=20,border_width=3)
    font_l = CTkLabel(font_frame,text="FONTs",font=("Fira Sans Condensed",40))
    font_l.grid(column=0,row=0,sticky="w",pady=8,padx=8)
    title_font = CTkLabel(font_frame,text="Title",font=("Fira Sans Condensed",30))
    title_font.grid(column=0,row=1,sticky='w',pady=8,padx=8)
    Arial_f = CTkRadioButton(font_frame,variable=tit_var,value="Arial",text="Arial",font=("Arial",20),command=font_chk)
    Arial_f.grid(column = 0,row=2,pady=8,padx=8)
    lib_mono = CTkRadioButton(font_frame,variable=tit_var,value="Liberation Mono",text="Liberation Mono",font=("Liberation Mono",20),command=font_chk)
    lib_mono.grid(column=1,row=2,pady=8,padx=8)
    Fsc_f = CTkRadioButton(font_frame,variable=tit_var,value="Fira Sans Condensed",text="Fira Sans",font=("Fira Sans Condensed",20),command=font_chk)
    Fsc_f.grid(column=2,row=2,pady=8,padx=8)
    content = CTkLabel(font_frame,text="Content",font=("Fira Sans Condensed",30))
    content.grid(column=0,row=3,sticky='w',pady=8,padx=8)
    Arial_f = CTkRadioButton(font_frame,variable=con_var,value="Arial",text="Arial",font=("Arial",20))
    Arial_f.grid(column = 0,row=4,pady=8,padx=8)
    lib_mono = CTkRadioButton(font_frame,variable=con_var,value="Liberation Mono",text="Liberation Mono",font=("Liberation Mono",20))
    lib_mono.grid(column=1,row=4,pady=8,padx=8)
    Fsc_f = CTkRadioButton(font_frame,variable=con_var,value="Fira Sans Condensed",text="Fira Sans",font=("Fira Sans Condensed",20))
    Fsc_f.grid(column=2,row=4,pady=8,padx=8)
    font_frame.grid(column=0,row=1,sticky="ew",pady=10)

    pan_var = IntVar(value=2)
    pannel_mode = CTkFrame(settings,corner_radius=20,border_width=3)
    pannel_text= CTkLabel(pannel_mode,text="Pannel Orientation",font=("Fira Sans Condensed",40),corner_radius=20)
    pannel_text.grid(column=0,row=0,sticky="w",pady=8,padx=8)
    pannel_normal = CTkRadioButton(pannel_mode,text="Horizontal(Default)",font=("Fira Sans Condensed",20),variable=pan_var,value=1,command=pan_chk)
    pannel_normal.grid(column=0,row=1,pady=8,padx=8)
    pannel_ver = CTkRadioButton(pannel_mode,text="Vertical Pannel",font=("Fira Sans Condensed",20),variable=pan_var,value=2,command=pan_chk)
    pannel_ver.grid(column=1,row=1,pady=8,padx=8)
    pannel_mode.grid(column = 0,row=2,sticky = "ew",pady=8,padx=8)

    tit_var = StringVar(value="Fira Sans Condensed")
    info_user = CTkFrame(settings,corner_radius=20,border_width=3)
    info_user.rowconfigure(0,weight=1)
    info_user.rowconfigure(1,weight=1)
    info_user.columnconfigure(0,weight=1)
    user_name = CTkEntry(info_user,state='normal')
    info_l =  CTkLabel(info_user, text="USER INFORMATION",font=(tit_var.get(),30),anchor="center")
    info_l.grid(row=0,column=0,pady=8,padx=8)

    user_name.insert(0,credit["username"])
    user_name.configure(state="readonly")
    ch_usr = CTkButton(info_user,text="Change Username",command=ch_usrname)
    ch_usr.grid(row=1,column=1,pady=8,padx=8)
    user_name.grid(column =0,row=1,sticky="we",pady=8,padx=8)

    password = CTkEntry(info_user,state='normal',show="*")
    password.insert(0,credit["password"])
    password.configure(state="readonly")
    ch_pass = CTkButton(info_user,text="Change password",command=ch_password)
    ch_pass.grid(row=2,column=1,pady=8,padx=8)
    password.grid(column =0,row=2,sticky="we",pady=8,padx=8)
    info_user.grid(column=0,row=3,sticky="nswe")
    settings.columnconfigure(0,weight=1)
    math_progress=0
    phy_progress=0
    chem_progress=0
    for c_ans in details.items():
        if c_ans[0][0:3] == "msc" and c_ans[1] != 0:
            math_progress +=1
        if c_ans[0][0:3] == "psc" and c_ans[1] != 0:
            phy_progress +=1
        if c_ans[0][0:3] == "csc" and c_ans[1] != 0:
            chem_progress +=1
    
    progress = CTkFrame(settings,corner_radius=20,border_width=3)
    progress_l = CTkLabel(progress,text="Progress",font=("Nasalization",40))
    progress_l.grid(column=0,row=0,sticky="n",pady=8,padx=8)
    math_pl = CTkLabel (progress,text="Maths:"+" "+str(math_progress*10)+"%",font=("Nasalization",20))
    math_pl.grid(column=0,row=1,pady=8,padx=8,sticky="w")
    math_percent = CTkFrame(progress,height=40)
    math_percent.columnconfigure(0,weight=1)
    m_done = CTkFrame(math_percent,height=40,width=174.4*math_progress)
    m_done.columnconfigure(0,weight=1)
    m_done.grid(padx=8,pady=8,column=0,row=0,sticky="w")
    math_percent.grid(column=0,row=2,pady=8,padx=8,sticky="nswe")

    phy_pl = CTkLabel (progress,text="Physics:"+" "+str(phy_progress*10)+"%",font=("Nasalization",20))
    phy_pl.grid(column=0,row=3,pady=8,padx=8,sticky="w")
    phy_percent = CTkFrame(progress,height=40)
    phy_percent.columnconfigure(0,weight=1)
    p_done = CTkFrame(phy_percent,height=40,width=174.4*phy_progress)
    p_done.columnconfigure(0,weight=1)
    p_done.grid(padx=8,pady=8,column=0,row=0,sticky="w")
    phy_percent.grid(column=0,row=4,pady=8,padx=8,sticky="nswe")
    

    chem_pl = CTkLabel (progress,text="Chemistry:"+" "+str(chem_progress*10)+"%",font=("Nasalization",20))
    chem_pl.grid(column=0,row=5,padx=8,pady=8,sticky="w")
    chem_percent = CTkFrame(progress,height=40)
    chem_percent.columnconfigure(0,weight=1)
    c_done = CTkFrame(chem_percent,height=40,width=174.4*chem_progress)
    c_done.columnconfigure(0,weight=1)
    c_done.grid(padx=8,pady=8,column=0,row=0,sticky="w")
    chem_percent.grid(column=0,row=6,pady=8,padx=8,sticky="nswe")
    
    progress.columnconfigure(0,weight=1)



    progress.grid(column = 0,row=4,sticky = "ew",pady=8,padx=8)
    for k in range(4):
        settings.rowconfigure(k+1,weight=1)
        font_frame.rowconfigure(k,weight=1)
        font_frame.columnconfigure(k,weight=1)
        pannel_mode.rowconfigure(k,weight=1)
        pannel_mode.columnconfigure(k,weight=1)
        progress.rowconfigure(k,weight=1)
    settings.grid_forget()




    main_frame.rowconfigure(0,weight=1)
    main_frame.columnconfigure(0,weight=1)


def theme_switch(choice=None):
    global ACTIVE_THEME_FILE, ACTIVE_APPEARANCE
    theme_file = THEME_FILES.get(t_switch.get())
    if not theme_file:
        return
    ACTIVE_THEME_FILE = theme_file
    ACTIVE_APPEARANCE = "light" if l_dswitch.get() else "dark"
    credit["theme"] = THEME_FILES[t_switch.get()]
    build_ui()





if __name__ == "__main__":
    app_window = CTk()
    app_window.geometry("1980x1020")
    app_window.title("Vorago:Shortcut Learner")
    logo =PhotoImage(file="images/logo.png")
    app_window.update_idletasks()
    app_window.iconphoto(True,logo)
    build_ui()
    app_window.mainloop()
    with open('credits.json','w') as f:
        json.dump(credit,f,indent=4)