from customtkinter import *
import practice_questions as pq
import json


with open ("c_ans_storage.json","r") as f:
    details = json.load(f)
page_no = 1



def mtasks(mtask, maths, math_frame, heading, paragrah,questions_data):
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
                ans_l.configure(text="Your answer is wrong ❌,The correct answer is option no."+str(corrrect_answer)+")" +qset[qno].get("options")[corrrect_answer],
                                wraplength=1000)
                btn.configure(fg_color="red",hover=FALSE)
            # print(correct)
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
                    details["msc"+str(mtask)] = correct
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
            # print(correct)

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
    math_frame.grid_forget()
    def create_math_screen(parent, title, core_principle, rule, example_1, example_2, quick_application, questions_data):
        global page_no
        if page_no >3:
            page_no = 0
        def back(button_pressed):
            global page_no
            page_no -=1
            if page_no == 0 :
                button_pressed.master.grid_forget()
                m1_pra.grid_forget()
                math_frame.grid(sticky="nswe",pady=5,row=0,column=0)
                page_no = 1
            elif page_no == 1 :
                front_b.grid(column=2, row=0, sticky="e", padx=3)
                math_frame.grid_forget()
                m1_intro.lift()
            

        def front(button_pressed):
            global page_no
            page_no+=1
            if page_no ==2 :
                m1_pra.lift()
                button_pressed.grid_forget()

        math_sc_1 = CTkFrame(parent)
        math_sc_1.grid(row=0, column=0, sticky="nswe") 
        math_sc_1.grid_columnconfigure(0, weight=0) 
        math_sc_1.grid_columnconfigure(1, weight=1)
        math_sc_1.grid_columnconfigure(2, weight=0)
        
        back_b = CTkButton(math_sc_1, text="«", width=60, font=("Nasalization", 40), command=lambda: back(back_b))
        back_b.grid(column=0, row=0, sticky="w", padx=3)

        front_b = CTkButton(math_sc_1, text="»", font=("Nasalization", 40), width=60, command=lambda: front(front_b))
        front_b.grid(column=2, row=0, sticky="e", padx=3)

        m1_pra = CTkFrame(math_sc_1)
        m1_pra.columnconfigure(0, weight=1)
        m1_pra.rowconfigure(1, weight=1)
        heading(m1_pra, "Practice Questions", 0, 0)
        
        pra_q = CTkFrame(m1_pra)
        pra_q.columnconfigure(0, weight=1)
        pra_q.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        m1_pra.grid(column=1, row=0, sticky="nswe")        
        m1_intro = CTkFrame(math_sc_1)
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
        math_sc_1.grid(sticky="nswe", row=0, column=0)
        question_loader(pra_q, questions_data, 0)
    
    if mtask == 1:
        return create_math_screen(
            parent=maths,
            title="Multiplying by 5",
            core_principle="Multiplying by 5 is equivalent to multiplying by 10 and halving (since 5 = 10/2).",
            rule="1. Multiply the number by 10 (shift the decimal one place right / append a zero).\n2. Divide the result by 2.",
            example_1="1) 48 × 5 \n48 × 10= 480\n480 ÷ 2 = 240",
            example_2="2) 79 × 5 \n79 × 10= 790\n790 ÷ 2 = 395",
            quick_application="Financial modeling (quick tip/discount calculations)\nSoftware engineering (cheap integer scaling in embedded systems)\nEveryday estimation (splitting bills, quick unit conversions)",
            questions_data=pq.msc1
        )
    
    
    if mtask ==2:
        return create_math_screen(
        parent=maths,
        title="Multiplying Numbers Near a Common Base",
        core_principle="For numbers close to a base B (like 100), write each as B+x and B+y; then (B+x)(B+y) = B² + B(x+y) + xy, which is fast because B² and B(x+y) are simple base-shifts.",
        rule="1. Choose base B (e.g., 100) and find each number's offset from B (x, y — can be negative).\n2. Compute the 'cross term' B + x + y for the leading part.\n3. Compute x×y for the trailing part and combine (append/add with carry).",
        example_1="1) 97 × 94 (B=100, x=−3, y=−6) → leading: 100−3−6=91 → trailing: (−3)×(−6)=18 → **9118**",
        example_2="2) 798 × 95 (B=100, x=−2, y=−5) → leading: 100−2−5=93 → trailing: (−2)×(−5)=10 → 9310",
        quick_application="-Software engineering: basis for fast multiplication algorithms (Karatsuba-style decomposition).\n- Financial modeling: quick estimates when prices cluster near round figures (e.g., ~$100 items).\n- Everyday estimation: shopping/retail quick math near round price points.",
        questions_data=pq.msc2  
    )
            
    if mtask == 3:  
        return create_math_screen(
            parent=maths,
            title="Compensation Method",
            core_principle="Adding/subtracting a 'round' number is easier than an awkward one; you can adjust one operand to a round number and correct the result afterward, since (a+k)+(b−k) = a+b.",
            rule="1. Round one operand up or down to the nearest 10/100.\n2. Perform the easy addition/subtraction.\n3. Add back or subtract the compensation amount.",
            example_1="297 + 58 → treat 297 as 300 − 3\n300 + 58 = 358\n358 − 3 = 355",
            example_2="",
            quick_application="Everyday estimation: quick grocery/restaurant bill tallying.\nFinancial modeling: rapid mental checks on invoice totals.\nSoftware engineering: sanity-checking loop counters/off-by-one estimates before coding.",
            questions_data=pq.msc3
        )
    if mtask == 4:
        return create_math_screen(
            parent=maths,
            title="Squaring Numbers Ending in 5",
            core_principle="For a number (10a+5)², expanding gives 100a(a+1)+25 — the last two digits are always 25, and the leading digits are a×(a+1).",
            rule="1. Drop the final 5; call the remaining leading digit(s) 'a'.\n2. Compute a × (a+1).\n3. Append '25' to that product.",
            example_1="65² → a=6\n6 × 7 = 42\nAppend 25 → 4225",
            example_2="",
            quick_application="Data analysis: quick variance/area estimates when values cluster around round midpoints.\nEveryday estimation: mental verification of calculator outputs.\nEducation technology: teaching pattern recognition in algebraic identities.",
            questions_data=pq.msc4
        )
    if mtask == 5:
        return create_math_screen(
            parent=maths,
            title="Difference of Squares",
            core_principle="a×b can be rewritten using the midpoint m and half-difference d as (m−d)(m+d) = m² − d², converting an odd multiplication into an easier squaring.",
            rule="1. Find the midpoint m = (a+b)/2 and offset d = (b−a)/2.\n2. Compute m² and d².\n3. Subtract: a×b = m² − d².",
            example_1="23 × 27 → m=25, d=2\n25² − 2² = 625 − 4 = 621",
            example_2="",
            quick_application="Physics: quick estimation in kinematics formulas involving product terms.\nFinancial modeling: fast multiplication of price × quantity pairs near round numbers.\nSoftware engineering: algebraic identity used in optimized squaring-based multiplication algorithms.",
            questions_data=pq.msc5
        )
    if mtask == 6:
        return create_math_screen(
            parent=maths,
            title="Numbers Near a Common Base",
            core_principle="For numbers close to a base B (like 100), write each as B+x and B+y; then (B+x)(B+y) = B² + B(x+y) + xy, which is fast because B² and B(x+y) are simple base-shifts.",
            rule="1. Choose base B (e.g., 100) and find each number's offset from B (x, y — can be negative).\n2. Compute the 'cross term' B + x + y for the leading part.\n3. Compute x×y for the trailing part and combine (append/add with carry).",
            example_1="97 × 94 (B=100, x=−3, y=−6)\nLeading: 100−3−6 = 91\nTrailing: (−3)×(−6) = 18 → 9118",
            example_2="",
            quick_application="Software engineering: basis for fast multiplication algorithms (Karatsuba-style decomposition).\nFinancial modeling: quick estimates when prices cluster near round figures (e.g., ~$100 items).\nEveryday estimation: shopping/retail quick math near round price points.",
            questions_data=pq.msc6
        )
    if mtask == 7:
        return create_math_screen(
            parent=maths,
            title="Vedic Cross-Multiplication",
            core_principle="Standard multiplication (10a+b)(10c+d) = 100ac + 10(ad+bc) + bd; organizing the three partial products (vertical, crosswise, vertical) lets you compute digit-by-digit without writing the full expansion.",
            rule="1. Multiply the units digits (bd) — this is the last digit(s), carry as needed.\n2. Cross-multiply and sum (ad + bc) — add to carry, this is the middle digit(s).\n3. Multiply the tens digits (ac) — add any carry, this is the leading digit(s).",
            example_1="34 × 21\nUnits: 4×1 = 4\nCross: 3×1 + 4×2 = 11 (write 1, carry 1)\nTens: 3×2 + 1(carry) = 7 → 714",
            example_2="",
            quick_application="Software engineering: conceptual basis for schoolbook multiplication algorithms in arbitrary-precision arithmetic libraries.\nEducation technology: speed-math training curricula (Vedic math apps).\nEmbedded systems: manual multiplication logic for microcontrollers lacking hardware multipliers.",
            questions_data=pq.msc7
        )
    if mtask == 8:
        return create_math_screen(
            parent=maths,
            title="Fast Squaring Near a Base",
            core_principle="Any square can be reframed around a nearby easy number: pick a round reference r close to a, let d = a−r, then a² = r² + 2rd + d² (a rearrangement of the binomial expansion).",
            rule="1. Choose a round reference r near a (e.g., nearest multiple of 10).\n2. Compute d = a − r.\n3. Compute r² + 2rd + d².",
            example_1="47² → r=50, d=−3\n2500 + 2(50)(−3) + 9\n= 2500 − 300 + 9 = 2209",
            example_2="",
            quick_application="Physics: quick energy/area calculations (E=mc²-style squared-term estimates).\nData analysis: fast variance calculations (sum of squared deviations).\nEveryday estimation: mental verification of squared measurements (area, speed-squared in kinetic energy).",
            questions_data=pq.msc8
        )
    if mtask == 9:
        return create_math_screen(
            parent=maths,
            title="Rule of 72",
            core_principle="For compound growth at rate r%, the doubling time T satisfies (1+r)^T=2; taking logs and approximating ln(1+r)≈r gives T ≈ ln(2)/r ≈ 0.693/r, conventionally rounded to 72/r for divisibility convenience.",
            rule="1. Take the annual growth/interest rate as a percentage (r).\n2. Divide 72 by r.\n3. The result approximates the number of periods to double.",
            example_1="At 8% annual interest → 72 ÷ 8 = 9 years to double.",
            example_2="",
            quick_application="Financial modeling: investment/loan growth estimation without a calculator.\nData analysis: estimating exponential growth trends (user base, viral spread).\nPhysics/biology: quick half-life/doubling estimates in decay and population models.",
            questions_data=pq.msc9
        )
    if mtask == 10:
        return create_math_screen(
        parent=maths,
        title="Fermat's Little Theorem Shortcut",
        core_principle="For prime p and a not divisible by p, a^(p−1) ≡ 1 (mod p); this lets you reduce huge exponents mod (p−1) before computing, and gives an instant modular inverse as a^(p−2).",
        rule="1. Confirm the modulus p is prime and a is not a multiple of p.\n2. Reduce the exponent n mod (p−1).\n3. Compute a^(n mod (p−1)) mod p using fast exponentiation.",
        example_1="3¹⁰⁰ mod 7 → p−1=6, 100 mod 6=4 → 3⁴=81 mod 7 = **4**",
        example_2="",
        quick_application="- Cryptography: basis of RSA correctness proofs and primality testing (Fermat test).\n- Software engineering: fast modular-inverse computation in prime-modulus fields.\n- Competitive programming: essential for problems involving large factorial/combinatorics mod a prime.",
        questions_data=pq.msc10
    )