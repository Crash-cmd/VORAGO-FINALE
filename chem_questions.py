from customtkinter import *
import practice_questions as pq
import json

with open ("c_ans_storage.json","r") as f:
    details = json.load(f)
page_no = 1



def ctasks(ctask, chem, chem_frame, heading, paragrah,questions_data):
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
            print(correct)
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
                    details["csc"+str(ctask)] = correct
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
    chem_frame.grid_forget()
    def create_chem_screen(parent, title, core_principle, rule, example_1, example_2, quick_application, questions_data):
        def back(button_pressed):
            global page_no
            page_no-=1
            if page_no == 0:
                button_pressed.master.grid_forget()
                m1_pra.grid_forget()
                chem_frame.grid(sticky="nswe",pady=5,row=0,column=0)
                page_no = 1
            elif page_no == 1 :
                chem_frame.grid_forget()
                m1_intro.lift()
            elif page_no == 2 :
                chem_frame.grid_forget()
                m1_pra.lift()

        def front(button_pressed):
            global page_no
            page_no+=1
            if page_no == 2 :
                chem_frame.grid_forget()
                m1_pra.lift()
        chem_sc_1 = CTkFrame(parent)
        chem_sc_1.grid(row=0, column=0, sticky="nswe") 
        chem_sc_1.grid_columnconfigure(0, weight=0)  # Back button column (fixed width)
        chem_sc_1.grid_columnconfigure(1, weight=1)  # Content column (EXPANDS to fill screen)
        chem_sc_1.grid_columnconfigure(2, weight=0)  # Front button column (fixed width)

        back_b = CTkButton(chem_sc_1, text="«", width=60, font=("Nasalization", 40), command=lambda: back(back_b))
        back_b.grid(column=0, row=0, sticky="w", padx=3)

        front_b = CTkButton(chem_sc_1, text="»", font=("Nasalization", 40), width=60, command=lambda: front(front_b))
        front_b.grid(column=2, row=0, sticky="e", padx=3)

        m1_pra = CTkFrame(chem_sc_1)
        m1_pra.columnconfigure(0, weight=1)
        m1_pra.rowconfigure(1, weight=1)
        heading(m1_pra, "Practice Questions", 0, 0)
        
        pra_q = CTkFrame(m1_pra)
        pra_q.columnconfigure(0, weight=1)
        pra_q.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        m1_pra.grid(column=1, row=0, sticky="nswe")        
        m1_intro = CTkFrame(chem_sc_1)
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
        chem_sc_1.grid(sticky="nswe", row=0, column=0)
        question_loader(pra_q, questions_data, 0)
    
    if ctask == 1:
        return create_chem_screen(
            parent=chem,
            title="Hybridization Number Formula (H)",
            core_principle="The state of hybridization can be found rapidly by calculating the steric number using valence electrons and surrounding atoms.",
            rule="1. Calculate H = ½ (V + M - C + A), where V = valence electrons of central atom, M = monovalent atoms, C = positive charge, A = negative charge.\n2. Match H value: 2=sp, 3=sp², 4=sp³, 5=sp³d, 6=sp³d².",
            example_1="1) For CH₄:\nH = ½(4 + 4 - 0 + 0) = 4 ⇒ sp³ hybridization",
            example_2="2) For NH₄⁺:\nH = ½(5 + 4 - 1 + 0) = 4 ⇒ sp³ hybridization",
            quick_application="Molecular geometry prediction\nVSEPR theory quick problem solving",
            questions_data=pq.csc1
        )

    if ctask == 2:
        return create_chem_screen(
            parent=chem,
            title="Degree of Unsaturation (DBE) Formula",
            core_principle="The number of rings and/or pi bonds in an organic molecule can be calculated directly from its molecular formula without drawing structures.",
            rule="1. Use formula: DBE = C + 1 - (H/2) + (N/2) - (X/2), where C=carbons, H=hydrogens, N=nitrogens, X=halogens.\n2. Ignore oxygen and sulfur entirely.",
            example_1="1) For C₆H₆ (Benzene):\nDBE = 6 + 1 - (6/2) + 0 - 0 = 7 - 3 = 4 (4 rings/pi bonds)",
            example_2="2) For C₃H₅Cl:\nDBE = 3 + 1 - (5/2) + 0 - (1/2) = 4 - 3 = 1 (1 ring or double bond)",
            quick_application="Determining organic compound isomers\nStructure elucidation in organic synthesis",
            questions_data=pq.csc2
        )

    if ctask == 3:
        return create_chem_screen(
            parent=chem,
            title="Total Spectral Lines Formula",
            core_principle="When an electron de-excites from an excited state level n to the ground state, multiple transition lines are emitted.",
            rule="1. Use the combination formula for transitions from level n to n=1: Total lines = n(n-1)/2.\n2. For transitions between any higher level n₂ to n₁, use: (n₂ - n₁)(n₂ - n₁ + 1)/2.",
            example_1="1) Electron falls from n = 4 to ground state:\nLines = 4(4-1)/2 = 6 spectral lines",
            example_2="2) Electron falls from n = 5 to n = 2:\nLines = (5 - 2)(5 - 2 + 1)/2 = (3 × 4)/2 = 6 lines",
            quick_application="Atomic emission spectroscopy analysis\nAstrochem stellar spectrum evaluation",
            questions_data=pq.csc3
        )

    if ctask == 4:
        return create_chem_screen(
            parent=chem,
            title="Kp and Kc Conversion Rule",
            core_principle="The equilibrium constants in terms of pressure (Kp) and concentration (Kc) are linked by the change in moles of gas (Δn_g).",
            rule="1. Calculate Δn_g = (Moles of gaseous products) - (Moles of gaseous reactants).\n2. Apply relation: K_p = K_c(RT)^(Δn_g).",
            example_1="1) For N₂ + 3H₂ ⇌ 2NH₃:\nΔn_g = 2 - (1 + 3) = -2 ⇒ K_p = K_c(RT)⁻²",
            example_2="2) For H₂ + I₂ ⇌ 2HI:\nΔn_g = 2 - (1 + 1) = 0 ⇒ K_p = K_c",
            quick_application="Industrial gas-phase synthesis (Haber process)\nThermodynamic equilibrium calculations",
            questions_data=pq.csc4
        )

    if ctask == 5:
        return create_chem_screen(
            parent=chem,
            title="Limiting Reagent Ratio Test",
            core_principle="The reactant that yields the least amount of product limits the reaction and is consumed completely.",
            rule="1. Divide the given moles of each reactant by its stoichiometric coefficient in the balanced equation.\n2. The reactant with the lowest numerical ratio is the limiting reagent.",
            example_1="1) For 2A + 3B → C, given 4 moles of A and 6 moles of B:\nA ratio = 4/2 = 2; B ratio = 6/3 = 2 (Both are stoichiometric equivalents).",
            example_2="2) If ratios are 2 (for A) and 1.5 (for B), B is the limiting reagent since 1.5 < 2.",
            quick_application="Chemical manufacturing yield optimization\nAnalytical chem titrations",
            questions_data=pq.csc5
        )

    if ctask == 6:
        return create_chem_screen(
            parent=chem,
            title="Atomic Number Position Mapping Rule",
            core_principle="Noble gas atomic numbers (2, 10, 18, 36, 54, 86) act as reference milestones for locating an element in the periodic table.",
            rule="1. Find the nearest noble gas with atomic number just below Z.\n2. Period = Noble gas period + 1.\n3. Group/Block determined by excess electrons beyond the noble gas core.",
            example_1="1) For Element Z = 15 (Phosphorus):\nNearest noble gas below is Neon (Z=10, Period 2).\nPeriod = 2 + 1 = 3. Excess electrons = 15 - 10 = 5 ⇒ Group 15 (p-block).",
            example_2="2) For Z = 19 (Potassium): Nearest noble gas Argon (Z=18) ⇒ Period 4, Group 1 (s-block).",
            quick_application="Quick periodic property estimation\nInorganic chem trend analysis",
            questions_data=pq.csc6
        )

    if ctask == 7:
        return create_chem_screen(
            parent=chem,
            title="Enthalpy vs Internal Energy Rule",
            core_principle="Enthalpy change accounts for both internal energy change and pressure-volume work done by gaseous species.",
            rule="1. Calculate change in gaseous moles: Δn_g = n_products(gas) - n_reactants(gas).\n2. Use relation: ΔH = ΔU + Δn_g RT.",
            example_1="1) Combustion of 1 mole of CH₄ at T:\nCH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)\nΔn_g = 1 - 3 = -2 ⇒ ΔH = ΔU - 2RT",
            example_2="2) If all reactants and products are liquids or solids, Δn_g = 0 ⇒ ΔH = ΔU.",
            quick_application="Thermochemical calculations\nCalorimetry energy balance",
            questions_data=pq.csc7
        )

    if ctask == 8:
        return create_chem_screen(
            parent=chem,
            title="Solution Dilution and Mixing Rule",
            core_principle="The total number of moles of solute remains conserved before and after dilution or mixing of non-reacting solutions.",
            rule="1. For dilution: M₁V₁ = M₂V₂.\n2. For mixing two solutions of same solute: M_mix = (M₁V₁ + M₂V₂) / (V₁ + V₂).",
            example_1="1) Diluting 100 mL of 2M HCl to 500 mL:\n2 × 100 = M₂ × 500 ⇒ M₂ = 0.4M",
            example_2="2) Mixing 100 mL of 1M HCl and 400 mL of 2M HCl:\nM_mix = (1×100 + 2×400) / (100 + 400) = 900/500 = 1.8M",
            quick_application="Preparing lab standard solutions\nBiochemical assay buffer preparation",
            questions_data=pq.csc8
        )

    if ctask == 9:
        return create_chem_screen(
            parent=chem,
            title="Valence Factor (n-factor) Shortcut",
            core_principle="The n-factor represents the molar exchange capacity of an acid (basicity), base (acidity), or redox agent.",
            rule="1. For acids: n-factor = number of replaceable H⁺ ions.\n2. For bases: n-factor = number of replaceable OH⁻ ions.\n3. For salts: total positive or negative charge of constituent ions.",
            example_1="1) For H₂SO₄:\nn-factor = 2 (two replaceable hydrogens)",
            example_2="2) For Ca(OH)₂:\nn-factor = 2 (two hydroxide ions)",
            quick_application="Normality calculations in volumetric analysis\nAcid-base titration stoichiometry",
            questions_data=pq.csc9
        )

    if ctask == 10:
        return create_chem_screen(
            parent=chem,
            title="Gas Density and Molar Mass Relation",
            core_principle="Ideal gas law can be rearranged to relate gas density directly to pressure, molar mass, and temperature.",
            rule="1. Use PM = dRT, where P = pressure, M = molar mass, d = density, R = gas constant, T = temperature in Kelvin.\n2. Rearrange to find density: d = PM / RT.",
            example_1="1) Find density of O₂ gas at STP (P = 1 atm, T = 273K, M = 32 g/mol):\nd = (1 × 32) / (0.0821 × 273) ≈ 1.43 g/L",
            example_2="2) Density is directly proportional to pressure and molar mass, and inversely proportional to temperature.",
            quick_application="Atmospheric chemistry gas profiling\nWeather balloon gas buoyancy calculations",
            questions_data=pq.csc10
        )