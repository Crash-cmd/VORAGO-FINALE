"""VORAGO Studio — an independent redesign prototype.

Run with: python vorago_redesign.py
The original app.py and its existing modules remain available unchanged.
"""
import ast
import hashlib
import hmac
import json
import os
import secrets
import tkinter.messagebox as messagebox

import customtkinter as ctk
import practice_questions as pq

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "vorago_redesign_data.json")
SUBJECTS = {
    "Mathematics": {"prefix": "msc", "color": "#C5A4FF", "icon": "∑", "module": "math_questions.py", "arg": "mtask"},
    "Physics": {"prefix": "psc", "color": "#75C9E8", "icon": "◉", "module": "phy_questions.py", "arg": "ptask"},
    "Chemistry": {"prefix": "csc", "color": "#8FD6B5", "icon": "⚗", "module": "chem_questions.py", "arg": "ctask"},
}
PALETTE = {
    "bg": "#101116", "sidebar": "#171920", "panel": "#1D2029",
    "panel_alt": "#242834", "line": "#303541", "text": "#F4F1EA",
    "muted": "#A1A7B4", "gold": "#D6B36A", "gold_hover": "#E6C783",
    "danger": "#E17B7B", "success": "#7CC9A1",
}
FONT = "Aptos"

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, dict):
            data.setdefault("users", {})
            data.setdefault("active_user", "")
            return data
    except (OSError, json.JSONDecodeError):
        pass
    return {"users": {}, "active_user": ""}

def save_data(data):
    temp_path = DATA_FILE + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    os.replace(temp_path, DATA_FILE)

def read_lesson_catalog():
    catalog = {name: {} for name in SUBJECTS}
    for subject, config in SUBJECTS.items():
        path = os.path.join(BASE_DIR, config["module"])
        try:
            with open(path, "r", encoding="utf-8") as file:
                tree = ast.parse(file.read(), filename=path)
        except (OSError, SyntaxError):
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.If) or not isinstance(node.test, ast.Compare):
                continue
            test = node.test
            if not (isinstance(test.left, ast.Name) and test.left.id == config["arg"] and len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq)):
                continue
            if len(test.comparators) != 1 or not isinstance(test.comparators[0], ast.Constant):
                continue
            number = test.comparators[0].value
            if not isinstance(number, int) or not 1 <= number <= 10:
                continue
            for child in ast.walk(node):
                if not isinstance(child, ast.Call) or not isinstance(child.func, ast.Name) or not child.func.id.startswith("create_"):
                    continue
                values = {}
                for keyword in child.keywords:
                    if keyword.arg in {"title", "core_principle", "rule", "example_1", "example_2", "quick_application"}:
                        try:
                            values[keyword.arg] = ast.literal_eval(keyword.value)
                        except (ValueError, TypeError):
                            pass
                if values.get("title"):
                    catalog[subject][number] = values
                    break
    return catalog

LESSONS = read_lesson_catalog()
QUESTION_SETS = {
    subject: [getattr(pq, f"{config['prefix']}{number}", []) for number in range(1, 11)]
    for subject, config in SUBJECTS.items()
}

class VoragoStudio(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VORAGO Studio")
        self.geometry("1440x900")
        self.minsize(1050, 700)
        self.configure(fg_color=PALETTE["bg"])
        self.data = load_data()
        self.user = None
        self.page = "home"
        self.quiz_state = None
        self.dark_mode = True
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.show_auth()

    def card(self, parent, **kwargs):
        return ctk.CTkFrame(parent, fg_color=PALETTE["panel"], corner_radius=18,
                            border_width=1, border_color=PALETTE["line"], **kwargs)

    def label(self, parent, text, size=14, color=None, weight="normal", **kwargs):
        return ctk.CTkLabel(parent, text=text, font=(FONT, size, weight),
                            text_color=color or PALETTE["text"], **kwargs)

    def button(self, parent, text, command, primary=False, **kwargs):
        return ctk.CTkButton(
            parent, text=text, command=command, height=42, corner_radius=11,
            fg_color=PALETTE["gold"] if primary else PALETTE["panel_alt"],
            hover_color=PALETTE["gold_hover"] if primary else "#343A49",
            text_color="#171717" if primary else PALETTE["text"],
            font=(FONT, 13, "bold" if primary else "normal"), **kwargs
        )

    def clear(self):
        for child in self.winfo_children():
            child.destroy()

    def show_auth(self):
        self.clear()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        left = ctk.CTkFrame(self, fg_color="#171922", corner_radius=0)
        left.grid(row=0, column=0, sticky="nsew")
        left.grid_columnconfigure(0, weight=1)
        left.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.label(left, "V O R A G O", 17, PALETTE["gold"], "bold").grid(row=0, column=0, sticky="sw", padx=58, pady=(30, 0))
        hero = ctk.CTkFrame(left, fg_color="transparent")
        hero.grid(row=1, column=0, sticky="nsew", padx=58)
        self.label(hero, "Learn smarter.\nSee the pattern.", 42, PALETTE["text"], "bold", justify="left").pack(anchor="w")
        self.label(hero, "A calmer workspace for shortcuts, concepts\nand focused practice across three subjects.", 16, PALETTE["muted"], justify="left").pack(anchor="w", pady=(18, 0))
        self.label(left, "A fresh interface concept · VORAGO Studio", 11, PALETTE["muted"]).grid(row=3, column=0, sticky="sw", padx=58, pady=30)

        right = ctk.CTkFrame(self, fg_color=PALETTE["bg"], corner_radius=0)
        right.grid(row=0, column=1, sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(0, weight=1)
        form = self.card(right, width=440)
        form.grid(row=0, column=0, padx=45, pady=45, sticky="")
        form.grid_columnconfigure(0, weight=1)
        self.label(form, "WELCOME BACK", 11, PALETTE["gold"], "bold").grid(row=0, column=0, sticky="w", padx=34, pady=(34, 8))
        self.label(form, "Your learning space.", 28, PALETTE["text"], "bold").grid(row=1, column=0, sticky="w", padx=34)
        self.label(form, "Create a local profile or sign in to continue.", 13, PALETTE["muted"]).grid(row=2, column=0, sticky="w", padx=34, pady=(7, 26))
        self.auth_mode = ctk.StringVar(value="Sign in" if self.data["users"] else "Create profile")
        tabs = ctk.CTkSegmentedButton(form, values=["Sign in", "Create profile"], variable=self.auth_mode, command=self.refresh_auth_fields)
        tabs.grid(row=3, column=0, sticky="ew", padx=34, pady=(0, 20))
        self.auth_user = ctk.CTkEntry(form, height=46, placeholder_text="Username")
        self.auth_user.grid(row=4, column=0, sticky="ew", padx=34, pady=7)
        self.auth_password = ctk.CTkEntry(form, height=46, placeholder_text="Password", show="•")
        self.auth_password.grid(row=5, column=0, sticky="ew", padx=34, pady=7)
        self.auth_confirm = ctk.CTkEntry(form, height=46, placeholder_text="Confirm password", show="•")
        self.auth_error = self.label(form, "", 12, PALETTE["danger"], wraplength=340)
        self.auth_error.grid(row=7, column=0, padx=34, pady=(4, 8), sticky="w")
        self.button(form, "Continue", self.authenticate, True).grid(row=8, column=0, sticky="ew", padx=34, pady=(8, 14))
        self.label(form, "Local prototype profile. Do not reuse a real password.", 10, PALETTE["muted"], wraplength=340).grid(row=9, column=0, padx=34, pady=(0, 28))
        self.refresh_auth_fields()
        self.bind("<Return>", lambda event: self.authenticate())

    def refresh_auth_fields(self, *_):
        if not hasattr(self, "auth_confirm"):
            return
        if self.auth_mode.get() == "Create profile":
            self.auth_confirm.grid(row=6, column=0, sticky="ew", padx=34, pady=7)
        else:
            self.auth_confirm.grid_forget()
        self.auth_error.configure(text="")

    def authenticate(self):
        username = self.auth_user.get().strip()
        password = self.auth_password.get()
        if len(username) < 2:
            self.auth_error.configure(text="Use a username with at least 2 characters.")
            return
        if len(password) < 6:
            self.auth_error.configure(text="Use at least 6 characters for this local prototype.")
            return
        users = self.data["users"]
        if self.auth_mode.get() == "Create profile":
            if username.lower() in {name.lower() for name in users}:
                self.auth_error.configure(text="That username already exists.")
                return
            if password != self.auth_confirm.get():
                self.auth_error.configure(text="The passwords do not match.")
                return
            salt = secrets.token_bytes(16)
            digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 240000)
            users[username] = {"salt": salt.hex(), "hash": digest.hex(), "scores": {}, "completed": []}
        else:
            record = next((value for name, value in users.items() if name.lower() == username.lower()), None)
            if not record:
                self.auth_error.configure(text="Profile not found. Create a profile first.")
                return
            digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(record["salt"]), 240000)
            if not hmac.compare_digest(digest.hex(), record["hash"]):
                self.auth_error.configure(text="The password doesn't match this profile.")
                return
            username = next(name for name in users if name.lower() == username.lower())
        self.user = username
        self.data["active_user"] = username
        save_data(self.data)
        self.unbind("<Return>")
        self.show_shell()

    def show_shell(self):
        self.clear()
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar = ctk.CTkFrame(self, width=238, fg_color=PALETTE["sidebar"], corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.label(self.sidebar, "VORAGO", 22, PALETTE["gold"], "bold").pack(anchor="w", padx=25, pady=(28, 2))
        self.label(self.sidebar, "STUDIO EDITION", 9, PALETTE["muted"], "bold").pack(anchor="w", padx=27, pady=(0, 30))
        self.nav_button("Overview", self.show_home, "⌂")
        for subject, config in SUBJECTS.items():
            self.nav_button(subject, lambda s=subject: self.show_subject(s), config["icon"])
        self.nav_button("Progress", self.show_progress, "◷")
        self.nav_button("Settings", self.show_settings, "⚙")
        bottom = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        bottom.pack(side="bottom", fill="x", padx=20, pady=22)
        self.label(bottom, self.user, 13, PALETTE["text"], "bold").pack(anchor="w")
        self.button(bottom, "Sign out", self.sign_out).pack(fill="x", pady=(12, 0))
        self.content = ctk.CTkFrame(self, fg_color=PALETTE["bg"], corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)
        self.show_home()

    def nav_button(self, text, command, icon):
        self.button(self.sidebar, f"{icon}    {text}", command, anchor="w", height=46).pack(fill="x", padx=15, pady=4)

    def page_frame(self):
        for child in self.content.winfo_children():
            child.destroy()
        page = ctk.CTkScrollableFrame(self.content, fg_color=PALETTE["bg"], corner_radius=0)
        page.grid(row=0, column=0, sticky="nsew", padx=28, pady=24)
        page.grid_columnconfigure(0, weight=1)
        return page

    def header(self, page, eyebrow, title, subtitle):
        self.label(page, eyebrow.upper(), 10, PALETTE["gold"], "bold").grid(row=0, column=0, sticky="w", pady=(5, 7))
        self.label(page, title, 32, PALETTE["text"], "bold").grid(row=1, column=0, sticky="w")
        self.label(page, subtitle, 13, PALETTE["muted"]).grid(row=2, column=0, sticky="w", pady=(5, 24))

    def user_record(self):
        return self.data["users"][self.user]

    def all_stats(self):
        record = self.user_record()
        completed = len(set(record.get("completed", [])))
        total = 30
        scores = list(record.get("scores", {}).values())
        average = round(sum(scores) / len(scores), 1) if scores else 0
        return completed, total, average

    def show_home(self):
        self.page = "home"
        page = self.page_frame()
        self.header(page, "Your workspace", f"Good to see you, {self.user}.", "Pick up a subject, revisit a shortcut or keep your learning streak moving.")
        hero = self.card(page)
        hero.grid(row=3, column=0, sticky="ew", pady=(0, 18))
        hero.grid_columnconfigure(0, weight=1)
        self.label(hero, "THE VORAGO METHOD", 10, PALETTE["gold"], "bold").grid(row=0, column=0, sticky="w", padx=26, pady=(23, 8))
        self.label(hero, "Understand the idea. Then make it automatic.", 23, PALETTE["text"], "bold").grid(row=1, column=0, sticky="w", padx=26)
        self.label(hero, "Each shortcut opens its principle, rule, worked examples and a focused practice quiz.", 13, PALETTE["muted"], wraplength=760).grid(row=2, column=0, sticky="w", padx=26, pady=(8, 18))
        self.button(hero, "Explore subjects  →", lambda: self.show_subject("Mathematics"), True, width=190).grid(row=3, column=0, sticky="w", padx=26, pady=(0, 24))
        completed, total, average = self.all_stats()
        stats = ctk.CTkFrame(page, fg_color="transparent")
        stats.grid(row=4, column=0, sticky="ew", pady=(0, 20))
        for i, (value, caption) in enumerate([(f"{completed}/{total}", "SHORTCUTS COMPLETED"), (f"{round(completed / total * 100)}%", "OVERALL COVERAGE"), (f"{average}/15", "AVERAGE QUIZ SCORE")]):
            stats.grid_columnconfigure(i, weight=1)
            box = self.card(stats)
            box.grid(row=0, column=i, sticky="ew", padx=(0 if i == 0 else 7, 7 if i < 2 else 0))
            self.label(box, value, 25, PALETTE["gold"], "bold").pack(anchor="w", padx=18, pady=(17, 3))
            self.label(box, caption, 9, PALETTE["muted"], "bold").pack(anchor="w", padx=18, pady=(0, 17))
        self.label(page, "YOUR SUBJECTS", 11, PALETTE["muted"], "bold").grid(row=5, column=0, sticky="w", pady=(8, 12))
        grid = ctk.CTkFrame(page, fg_color="transparent")
        grid.grid(row=6, column=0, sticky="ew")
        for i, (subject, config) in enumerate(SUBJECTS.items()):
            grid.grid_columnconfigure(i, weight=1)
            box = self.card(grid)
            box.grid(row=0, column=i, sticky="nsew", padx=(0 if i == 0 else 7, 7 if i < 2 else 0))
            self.label(box, config["icon"], 26, config["color"], "bold").pack(anchor="w", padx=18, pady=(18, 8))
            self.label(box, subject, 18, PALETTE["text"], "bold").pack(anchor="w", padx=18)
            self.label(box, "10 shortcuts · 15 questions each", 11, PALETTE["muted"]).pack(anchor="w", padx=18, pady=(5, 14))
            self.button(box, "Open subject  →", lambda s=subject: self.show_subject(s)).pack(fill="x", padx=16, pady=(0, 17))

    def show_subject(self, subject):
        self.page = subject
        page = self.page_frame()
        config = SUBJECTS[subject]
        self.header(page, f"{subject} / Learning library", f"{subject} shortcuts", "Choose a topic to study its concept, rule and worked examples before practising.")
        search = ctk.CTkEntry(page, height=44, placeholder_text=f"Search {subject.lower()} shortcuts…")
        search.grid(row=3, column=0, sticky="ew", pady=(0, 16))
        grid = ctk.CTkFrame(page, fg_color="transparent")
        grid.grid(row=4, column=0, sticky="ew")
        grid.grid_columnconfigure((0, 1), weight=1)
        cards = []
        for number in range(1, 11):
            lesson = LESSONS[subject].get(number, {})
            title = lesson.get("title", f"Shortcut {number}")
            question_set = QUESTION_SETS[subject][number - 1]
            completed = f"{config['prefix']}{number}" in self.user_record().get("completed", [])
            box = self.card(grid)
            box.grid(row=(number - 1) // 2, column=(number - 1) % 2, sticky="ew", padx=(0, 8) if number % 2 else (8, 0), pady=7)
            self.label(box, f"{number:02d}  /  SHORTCUT", 9, config["color"], "bold").pack(anchor="w", padx=18, pady=(17, 6))
            self.label(box, title, 17, PALETTE["text"], "bold", wraplength=450, justify="left").pack(anchor="w", padx=18)
            self.label(box, f"{len(question_set)} practice questions  ·  {'Completed' if completed else 'Not completed'}", 11, PALETTE["muted"]).pack(anchor="w", padx=18, pady=(7, 13))
            self.button(box, "Study topic  →", lambda s=subject, n=number: self.show_lesson(s, n), True).pack(anchor="w", padx=16, pady=(0, 16))
            cards.append((box, title.lower(), number))
        def filter_cards(value):
            query = value.strip().lower()
            for box, title, number in cards:
                if query in title or query in str(number):
                    box.grid()
                else:
                    box.grid_remove()
        search.configure(command=filter_cards)
        search.bind("<KeyRelease>", lambda event: filter_cards(search.get()))

    def show_lesson(self, subject, number):
        self.page = "lesson"
        page = self.page_frame()
        lesson = LESSONS[subject].get(number, {})
        config = SUBJECTS[subject]
        title = lesson.get("title", f"Shortcut {number}")
        self.header(page, f"{subject} / Shortcut {number:02d}", title, "Learn the method first. Use the practice set to check your understanding.")
        sections = [
            ("CORE PRINCIPLE", lesson.get("core_principle", "Review the central idea behind this shortcut.")),
            ("THE RULE", lesson.get("rule", "No rule text is currently available for this topic.")),
            ("WORKED EXAMPLE 01", lesson.get("example_1", "Example not provided.")),
            ("WORKED EXAMPLE 02", lesson.get("example_2", "Example not provided.")),
            ("WHERE IT HELPS", lesson.get("quick_application", "Use this method in related problem-solving situations.")),
        ]
        for index, (heading, body) in enumerate(sections):
            box = self.card(page)
            box.grid(row=3 + index, column=0, sticky="ew", pady=6)
            self.label(box, heading, 10, config["color"], "bold").pack(anchor="w", padx=20, pady=(15, 6))
            self.label(box, body, 14, PALETTE["text"], justify="left", wraplength=950).pack(anchor="w", padx=20, pady=(0, 16))
        actions = ctk.CTkFrame(page, fg_color="transparent")
        actions.grid(row=8, column=0, sticky="ew", pady=16)
        self.button(actions, "← Back to topics", lambda: self.show_subject(subject)).pack(side="left")
        self.button(actions, "Start practice  →", lambda: self.start_quiz(subject, number), True).pack(side="right")

    def start_quiz(self, subject, number):
        questions = QUESTION_SETS[subject][number - 1]
        if not questions:
            messagebox.showerror("No questions", "There are no practice questions available for this shortcut.")
            return
        self.quiz_state = {"subject": subject, "number": number, "questions": questions, "index": 0, "score": 0, "answered": False}
        self.show_quiz()

    def show_quiz(self):
        state = self.quiz_state
        page = self.page_frame()
        subject, number = state["subject"], state["number"]
        config = SUBJECTS[subject]
        questions = state["questions"]
        index = state["index"]
        if index >= len(questions):
            self.finish_quiz()
            return
        question = questions[index]
        self.header(page, f"{subject} / Practice", LESSONS[subject].get(number, {}).get("title", f"Shortcut {number}"), f"Question {index + 1} of {len(questions)}")
        progress = ctk.CTkProgressBar(page, height=9, progress_color=config["color"], fg_color=PALETTE["panel_alt"])
        progress.grid(row=3, column=0, sticky="ew", pady=(0, 18))
        progress.set(index / len(questions))
        box = self.card(page)
        box.grid(row=4, column=0, sticky="nsew")
        self.label(box, f"QUESTION {index + 1:02d}", 10, config["color"], "bold").pack(anchor="w", padx=25, pady=(24, 12))
        self.label(box, question.get("question", ""), 20, PALETTE["text"], "bold", wraplength=900, justify="left").pack(anchor="w", padx=25, pady=(0, 20))
        self.quiz_feedback = self.label(box, "", 12, PALETTE["muted"], wraplength=900)
        self.quiz_feedback.pack(anchor="w", padx=25, pady=(8, 0))
        self.quiz_buttons = []
        for option_index, option in enumerate(question.get("options", [])):
            button = self.button(box, f"{chr(65 + option_index)}   {option}", lambda i=option_index: self.answer_question(i))
            button.pack(fill="x", padx=24, pady=5)
            self.quiz_buttons.append(button)
        self.quiz_next = self.button(box, "Next question  →", self.next_question, True, state="disabled")
        self.quiz_next.pack(anchor="e", padx=24, pady=(18, 24))

    def answer_question(self, selected):
        state = self.quiz_state
        if state["answered"]:
            return
        state["answered"] = True
        question = state["questions"][state["index"]]
        correct = int(question.get("correct", -1))
        if selected == correct:
            state["score"] += 1
            self.quiz_feedback.configure(text="Correct. Good work.", text_color=PALETTE["success"])
        else:
            options = question.get("options", [])
            answer = options[correct] if 0 <= correct < len(options) else "Unavailable"
            self.quiz_feedback.configure(text=f"Not quite. Correct answer: {answer}", text_color=PALETTE["danger"])
        for index, button in enumerate(self.quiz_buttons):
            button.configure(state="disabled", fg_color=PALETTE["success"] if index == correct else PALETTE["panel_alt"],
                             text_color="#101116" if index == correct else PALETTE["muted"])
        self.quiz_next.configure(state="normal")

    def next_question(self):
        if not self.quiz_state or not self.quiz_state["answered"]:
            return
        self.quiz_state["index"] += 1
        self.quiz_state["answered"] = False
        self.show_quiz()

    def finish_quiz(self):
        state = self.quiz_state
        subject, number = state["subject"], state["number"]
        config = SUBJECTS[subject]
        key = f"{config['prefix']}{number}"
        record = self.user_record()
        previous = record.setdefault("scores", {}).get(key, 0)
        record["scores"][key] = max(previous, state["score"])
        if key not in record.setdefault("completed", []):
            record["completed"].append(key)
        save_data(self.data)
        page = self.page_frame()
        page.grid_columnconfigure(0, weight=1)
        box = self.card(page)
        box.grid(row=0, column=0, sticky="", pady=80)
        self.label(box, "PRACTICE COMPLETE", 10, PALETTE["gold"], "bold").pack(padx=45, pady=(35, 10))
        self.label(box, f"{state['score']} / {len(state['questions'])}", 44, PALETTE["text"], "bold").pack(padx=45)
        self.label(box, "Your best score has been saved to this local profile.", 12, PALETTE["muted"]).pack(padx=35, pady=(8, 22))
        self.button(box, "Back to topic", lambda: self.show_lesson(subject, number), True).pack(fill="x", padx=30, pady=(0, 12))
        self.button(box, "All subjects", lambda: self.show_subject(subject)).pack(fill="x", padx=30, pady=(0, 30))

    def show_progress(self):
        page = self.page_frame()
        self.header(page, "Your learning record", "Progress overview", "Only completed quizzes count as completed, including a score of zero.")
        record = self.user_record()
        for row, (subject, config) in enumerate(SUBJECTS.items(), start=3):
            keys = [f"{config['prefix']}{n}" for n in range(1, 11)]
            completed = sum(key in record.get("completed", []) for key in keys)
            box = self.card(page)
            box.grid(row=row, column=0, sticky="ew", pady=7)
            self.label(box, subject, 17, config["color"], "bold").pack(anchor="w", padx=20, pady=(16, 5))
            self.label(box, f"{completed} of 10 topics completed", 12, PALETTE["muted"]).pack(anchor="w", padx=20, pady=(0, 10))
            bar = ctk.CTkProgressBar(box, progress_color=config["color"], fg_color=PALETTE["panel_alt"])
            bar.pack(fill="x", padx=20, pady=(0, 18))
            bar.set(completed / 10)

    def show_settings(self):
        page = self.page_frame()
        self.header(page, "Workspace preferences", "Settings", "A small set of controls for your local VORAGO Studio workspace.")
        box = self.card(page)
        box.grid(row=3, column=0, sticky="ew")
        self.label(box, "Appearance", 17, PALETTE["text"], "bold").pack(anchor="w", padx=20, pady=(18, 5))
        self.label(box, "Switch between the dark studio palette and a soft light palette.", 12, PALETTE["muted"]).pack(anchor="w", padx=20, pady=(0, 12))
        self.button(box, "Toggle light / dark mode", self.toggle_theme).pack(anchor="w", padx=20, pady=(0, 20))
        note = self.card(page)
        note.grid(row=4, column=0, sticky="ew", pady=12)
        self.label(note, "About this prototype", 17, PALETTE["text"], "bold").pack(anchor="w", padx=20, pady=(18, 6))
        self.label(note, "This redesign uses a separate local profile and progress file. It reads your existing lesson descriptions and question banks, but does not overwrite credits.json or c_ans_storage.json.", 12, PALETTE["muted"], wraplength=900, justify="left").pack(anchor="w", padx=20, pady=(0, 18))

    def toggle_theme(self):
        global PALETTE
        if self.dark_mode:
            PALETTE = dict(PALETTE, bg="#F3F1EC", sidebar="#E8E5DE", panel="#FFFFFF", panel_alt="#EAE7E0", line="#D8D3C9", text="#252621", muted="#73766F", gold="#A57B32", gold_hover="#C29343")
            self.dark_mode = False
        else:
            PALETTE = dict(PALETTE, bg="#101116", sidebar="#171920", panel="#1D2029", panel_alt="#242834", line="#303541", text="#F4F1EA", muted="#A1A7B4", gold="#D6B36A", gold_hover="#E6C783")
            self.dark_mode = True
        self.show_shell()

    def sign_out(self):
        self.user = None
        self.show_auth()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = VoragoStudio()
    app.mainloop()
