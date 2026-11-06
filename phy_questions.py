from customtkinter import *
import practice_questions as pq
import json 

with open ("c_ans_storage.json","r") as f:
    details = json.load(f)
page_no = 1



def ptasks(ptask, phy, phy_frame, heading, paragrah,questions_data):
    def question_loader(parent,qset,qno=0):
        pra_q = parent
        correct = 0
        corrrect_answer = qset[qno].get("correct")
        themebutton = CTkButton(parent)
        themebutton.grid_forget()
        og_fg_color = themebutton.cget("fg_color")
        og_hover_color= themebutton.cget("hover_color")
        def answer(btn):
            nonlocal qno
            nonlocal correct
            all_opt=[btn.master.grid_slaves(row=1,column=0),btn.master.grid_slaves(row=2,column=0),
                    btn.master.grid_slaves(row=3,column=0),btn.master.grid_slaves(row=4,column=0)]
            for opt in all_opt:
                opt[0].configure(state=DISABLED)
            all_opt.remove(btn.master.grid_slaves(row=corrrect_answer+1,column=0))
            btn.master.grid_slaves(row=corrrect_answer+1,column=0)[0].configure(fg_color="green")
            for wrong_opt in all_opt:
                wrong_opt[0].configure(fg_color="red",hover=FALSE)
            if btn.grid_info().get("row")-1 == corrrect_answer:
                ans_l.configure(text="Your answer is correct ✅")
                btn.configure(fg_color="green",hover = FALSE)
                correct += 1
            elif btn.grid_info().get("row")-1 != corrrect_answer:
                ans_l.configure(text="Your answer is wrong ❌,The correct answer is option no."+str(corrrect_answer)+")" +qset[qno].get("options")[corrrect_answer],wraplength=1000)
                btn.configure(fg_color="red",hover=FALSE)

            def check_procces():
                nonlocal correct
                nonlocal qno
                qno +=1
                nonlocal qset
                nonlocal corrrect_answer
                if qno < len(qset):
                    corrrect_answer = qset[qno].get("correct")
                    label.configure(text=qset[qno].get("question"))
                    b1.configure(text=qset[qno].get("options")[0],hover=TRUE,state=NORMAL,fg_color=og_fg_color,hover_color=og_hover_color)
                    b2.configure(text=qset[qno].get("options")[1],hover=TRUE,state=NORMAL,fg_color=og_fg_color,hover_color=og_hover_color)
                    b3.configure(text=qset[qno].get("options")[2],hover=TRUE,state=NORMAL,fg_color=og_fg_color,hover_color=og_hover_color)
                    b4.configure(text=qset[qno].get("options")[3],hover=TRUE,state=NORMAL,fg_color=og_fg_color,hover_color=og_hover_color)
                    qlimit.configure(text=str(qno+1)+"/15")
                    ans_l.configure(text="")
                else:
                    details["psc"+str(ptask)] = correct
                    for wid in btn.master.winfo_children():
                        wid.destroy()
                    l = CTkLabel(parent,text="You have completed this quiz",font=("Fira Sans Condensed",60))
                    l.grid(sticky="n",column=0,row=1)
                    l2 = CTkLabel(parent,text="Score:"+str(correct)+"/15",font=("Fira Sans Condensed",60))
                    l2.grid(sticky="n",column=0,row=2)
                    if correct == len(qset):
                        l3 = CTkLabel(parent,text="Congrats You have gotten all of it right 🎉",font=("Fira Sans Condensed",60))
                        l3.grid(sticky="n",column=0,row=3)
                    with open ("c_ans_storage.json","w") as f:
                        json.dump(details,f,indent=4)

            pra_q.after(2000,check_procces)


        label = CTkLabel(parent,text=qset[qno].get("question"),font=("Fira Sans Condensed",40))
        label.grid(sticky="n",row=0,column=0,pady=30)
        b1 = CTkButton(parent,text=qset[qno].get("options")[0],font=("Fira Sans Condensed",20),height=50,width=75,command=lambda:answer(b1))
        b1.grid(sticky="n",row=1,column=0,pady=30)
        b2 = CTkButton(parent,text=qset[qno].get("options")[1],font=("Fira Sans Condensed",20),height=50,width=75,command=lambda:answer(b2))
        b2.grid(sticky="n",row=2,column=0,pady=30)
        b3 = CTkButton(parent,text=qset[qno].get("options")[2],font=("Fira Sans Condensed",20),height=50,width=75,command=lambda:answer(b3))
        b3.grid(sticky="n",row=3,column=0,pady=30)
        b4 = CTkButton(parent,text=qset[qno].get("options")[3],font=("Fira Sans Condensed",20),height=50,width=75,command=lambda:answer(b4))
        b4.grid(sticky="n",row=4,column=0,pady=30)
        qlimit = CTkLabel(pra_q,text=str(qno+1)+"/15",font=("Fira Sans Condensed",30),justify="left")
        qlimit.grid(column=0,row=0,sticky ="ne")
        ans_l =CTkLabel(parent,text="",font=("Fira Sans Condensed",40))
        ans_l.grid(sticky="s",row=5,column=0,pady=50)

    page_no = 1
    phy_frame.grid_forget()
    def create_phy_screen(parent, title, core_principle, rule, example_1, example_2, quick_application,questions_data):
        global page_no
        if page_no >3:
            page_no = 0
        def back(button_pressed):
            global page_no
            page_no -=1
            if page_no == 0 :
                button_pressed.master.grid_forget()
                m1_pra.grid_forget()
                phy_frame.grid(sticky="nswe",pady=5,row=0,column=0)
                page_no = 1
            elif page_no == 1 :
                front_b.grid(column=2, row=0, sticky="e", padx=3)
                phy_frame.grid_forget()
                m1_intro.lift()
            

        def front(button_pressed):
            global page_no
            page_no+=1
            if page_no ==2 :
                m1_pra.lift()
                button_pressed.grid_forget()

        phy_sc_1 = CTkFrame(parent)
        phy_sc_1.grid(row=0, column=0, sticky="nswe") 
        phy_sc_1.grid_columnconfigure(0, weight=0)  # Back button column (fixed width)
        phy_sc_1.grid_columnconfigure(1, weight=1)  # Content column (EXPANDS to fill screen)
        phy_sc_1.grid_columnconfigure(2, weight=0)  # Front button column (fixed width)

        back_b = CTkButton(phy_sc_1, text="«", width=60, font=("Nasalization", 40), command=lambda: back(back_b))
        back_b.grid(column=0, row=0, sticky="w", padx=3)

        front_b = CTkButton(phy_sc_1, text="»", font=("Nasalization", 40), width=60, command=lambda: front(front_b))
        front_b.grid(column=2, row=0, sticky="e", padx=3)

        m1_pra = CTkFrame(phy_sc_1)
        m1_pra.columnconfigure(0, weight=1)
        m1_pra.rowconfigure(1, weight=1)
        heading(m1_pra, "Practice Questions", 0, 0)
        
        pra_q = CTkFrame(m1_pra)
        pra_q.columnconfigure(0, weight=1)
        pra_q.grid(row=1, column=0, sticky="nsew", pady=5, padx=3.5)
        m1_pra.grid(column=1, row=0, sticky="nswe")        
        m1_intro = CTkFrame(phy_sc_1)
        m1_intro.columnconfigure(0, weight=1)
        
        heading(m1_intro, title, 0, 0)
        heading(m1_intro, "Core Principle", 1, 1)
        paragrah(m1_intro, core_principle, 2)
        heading(m1_intro, "The Rule", 1, 3)
        paragrah(m1_intro, rule, 4)
        heading(m1_intro, "Examples", 1, 5)
        paragrah(m1_intro, example_1, 6)
        paragrah(m1_intro, example_2, 7)
        heading(m1_intro, "Quick Application", 1, 8)
        paragrah(m1_intro, quick_application, 9)
        
        m1_intro.grid(column=1, row=0, sticky="nswe")    
        phy_sc_1.grid(sticky="nswe", row=0, column=0)
        question_loader(pra_q, questions_data, 0)
    
    if ptask == 1:
        return create_phy_screen(
            parent=phy,
            title="The Power Error Rule",
            core_principle="When calculating maximum percentage error for quantities given in powers, individual errors multiply with their powers and always add up.",
            rule="1. Multiply fractional or percentage errors of individual quantities by their respective powers.\n2. Always add them together (errors never cancel out).",
            example_1="1) Z = A²B / C\nΔZ/Z = 2(ΔA/A) + 1(ΔB/B) + 1(ΔC/C)",
            example_2="2) Error in A is 1% (power 2) and B is 2% (power 1)\nMax error = 2(1%) + 1(2%) = 4%",
            quick_application="Experimental phy error analysis\nCompetitive exam quick calculations\nLab data evaluation",
            questions_data=pq.psc1
        )

    if ptask == 2:
        return create_phy_screen(
            parent=phy,
            title="Projectile Time-Product Rule",
            core_principle="Complementary angles of projection yield the same horizontal range, and the product of their times of flight relates directly to that range.",
            rule="1. Identify complementary angles θ and 90° - θ for the same horizontal range.\n2. Use the product formula: T₁T₂ = 2R/g.",
            example_1="1) Angles 30° and 60° give equal range R.\nT₁T₂ = 2R/g",
            example_2="2) If T₁ = 2s and T₂ = 4s for same range, then 2 × 4 = 8 = 2R/g ⇒ R = 4g",
            quick_application="Projectile motion problems in JEE/NEET\nBallistics and trajectory analysis",
            questions_data=pq.psc2
        )

    if ptask == 3:
        return create_phy_screen(
            parent=phy,
            title="Ball Rebound Height and Total Distance",
            core_principle="Energy loss during inelastic collisions with a floor follows the coefficient of restitution e.",
            rule="1. Height after nth bounce: h_n = e^(2n) * h₀.\n2. Total vertical distance: S_total = h₀ * ((1 + e²) / (1 - e²)).",
            example_1="1) Ball dropped from h₀ = 10m with e = 0.5.\nHeight after 1st bounce: h₁ = (0.5)² × 10 = 2.5m",
            example_2="2) Total vertical distance for h₀ = 10m, e = 0.5:\nS_total = 10 × (1 + 0.25) / (1 - 0.25) = 16.67m",
            quick_application="Drop tests in material science\nMechanical bounce modeling in phy simulations",
            questions_data=pq.psc3
        )

    if ptask == 4:
        return create_phy_screen(
            parent=phy,
            title="String Constraint Trick",
            core_principle="The conservation of total string length in a connected pulley system links the velocities and accelerations of the masses.",
            rule="1. Identify string segments and their tensions.\n2. Apply virtual work principle: sum of the product of tension force and velocity/acceleration equals zero (Σ(T · a) = 0).",
            example_1="1) For blocks connected over a fixed pulley, relate velocities using string length constraints.",
            example_2="2) If a string segment moves downward with acceleration a, connected block moves upward with corresponding constraint ratio.",
            quick_application="Complex pulley systems\nRobotics cable-drive mechanisms",
            questions_data=pq.psc4
        )

    if ptask == 5:
        return create_phy_screen(
            parent=phy,
            title="Spring-Cutting Rule",
            core_principle="Spring constant is inversely proportional to the length of the spring (k ∝ 1/l).",
            rule="1. Note that the product of spring constant and length remains constant.\n2. Use k₁l₁ = k₂l₂ = kL for cut pieces.",
            example_1="1) Spring of constant k cut into 2 equal halves (l/2 each):\nNew spring constant k' = 2k",
            example_2="2) Spring cut into ratio 1:3 lengths:\nConstants become 4k and (4/3)k respectively.",
            quick_application="Mechanical vibration tuning\nDesigning spring-mass isolation systems",
            questions_data=pq.psc5
        )

    if ptask == 6:
        return create_phy_screen(
            parent=phy,
            title="Center of Mass of a Cut-out Body",
            core_principle="A removed portion of a symmetric body can be treated mathematically as negative mass/area in the Center of Mass formula.",
            rule="1. Identify original body area/mass and cut-out area/mass.\n2. Apply negative mass formula: X_cm = (A₁x₁ - A₂x₂) / (A₁ - A₂).",
            example_1="1) Circular disk of radius R with a circular hole of radius R/2 cut out from the edge.",
            example_2="2) Apply area ratio: A₁ = πR², A₂ = π(R/2)² to find shifted X_cm instantly.",
            quick_application="Aerospace structural weight balancing\nMechanical component design with cutouts",
            questions_data=pq.psc6
        )

    if ptask == 7:
        return create_phy_screen(
            parent=phy,
            title="Rolling Acceleration on an Inclined Plane",
            core_principle="Combining torque and translation equations yields a universal acceleration formula for rolling bodies without slipping.",
            rule="1. Identify the geometry factor (k²/R²).\n2. Apply formula: a = (g sinθ) / (1 + k²/R²).",
            example_1="1) Solid cylinder/disk (k²/R² = 1/2):\na = (g sinθ) / (1 + 0.5) = (2/3)g sinθ",
            example_2="2) Solid sphere (k²/R² = 2/5):\na = (g sinθ) / (1 + 0.4) = (5/7)g sinθ",
            quick_application="Conveyor belt system design\nVehicle dynamics on slopes",
            questions_data=pq.psc7
        )

    if ptask == 8:
        return create_phy_screen(
            parent=phy,
            title="Escape Velocity vs. Orbital Speed",
            core_principle="A satellite orbiting very close to a planet's surface has a speed related directly to the planet's escape velocity by a factor of √2.",
            rule="1. Recall orbital speed for a surface-grazing orbit.\n2. Multiply by √2 to get escape velocity: v_escape = √2 × v_orbital.",
            example_1="1) If orbital speed for a low-earth orbit is v₀, escape velocity is v_e = √2 v₀",
            example_2="2) Multiplying low-earth orbital speed (~7.9 km/s) by 1.414 yields escape ve,locity (~11.2 km/s).",
            quick_application="Satellite launch window planning\nOrbital mechanics calculations",
            questions_data=pq.psc8
        )

    if ptask == 9:
        return create_phy_screen(
            parent=phy,
            title="P-V Diagram Isothermal vs Adiabatic Slopes",
            core_principle="An adiabatic process involves temperature changes without heat transfer, making its curve steeper than an isothermal curve by a factor of γ.",
            rule="1. Identify atomicity constant γ (C_p/C_v).\n2. Multiply isothermal slope by γ to get adiabatic slope.",
            example_1="1) For a monoatomic gas (γ = 5/3 = 1.67), adiabatic slope is 1.67 times steeper than isothermal slope.",
            example_2="2) Comparing slopes at the exact same P-V point instantly reveals adiabatic vs isothermal behavior.",
            quick_application="Engine cycle analysis (Carnot, Otto, Diesel cycles)\nAtmospheric thermodynamics",
            questions_data=pq.psc9
        )

    if ptask == 10:
        return create_phy_screen(
            parent=phy,
            title="Tuning Fork Loading and Filing Rules",
            core_principle="Altering the mass or stiffness of a tuning fork prong shifts its resonant frequency systematically.",
            rule="1. Loading with wax lowers frequency (Load = Lower).\n2. Filing or scraping a prong increases frequency (File = Fast).",
            example_1="1) Tuning fork gives 4 beats/sec with 256 Hz fork. When loaded with wax, beat frequency decreases to 2. Frequency is 260 Hz.",
            example_2="2) Filing a prong increases frequency, helping resolve ambiguous beat frequency directions in acoustic problems.",
            quick_application="Musical instrument tuning\nAcoustic calibration",
            questions_data=pq.psc10
        )