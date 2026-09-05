import tkinter as tk
import random

# -----------------------------
# COLORS
# -----------------------------
BG = "#111111"
DISPLAY_BG = "#1C1C1C"
BUTTON_BG = "#2A2A2A"
SPECIAL_BG = "#FF9500"
TEXT = "#FFFFFF"
SECONDARY = "#AAAAAA"


# -----------------------------
# SARCASTIC RESPONSES
# -----------------------------

mild = [
    "Are you sure you need a calculator for this? 😭",
    "You could probably solve this yourself.",
    "Hmm... maybe try using your brain first. 🧠",
    "That's what calculators are for... apparently.",
]

medium = [
    "You REALLY needed a calculator for that? 💀",
    "I know the answer. I'm just not telling you.",
    "Your math teacher is somewhere disappointed.",
    "Congratulations. You have successfully avoided doing math.",
    "I could answer this, but watching you struggle is more fun.",
]

savage = [
    "WOW. You outsourced basic mathematics to a computer. 💀",
    "I'm a calculator, not a substitute for your brain.",
    "At this point, even Google would be concerned.",
    "You had ONE job. ONE.",
    "Maybe mathematics isn't your thing. 😭",
    "I'm beginning to question why I was invented.",
    "The answer is obvious. Your confidence isn't.",
    "Please return to elementary school immediately. 💀",
]

extreme = [
    "I refuse to participate in this academic disaster.",
    "Even my circuits are embarrassed right now.",
    "You don't need a calculator. You need a mathematics intervention. 💀",
    "I'm deleting myself after seeing that equation.",
    "This calculation has caused irreversible damage to my processor.",
    "I'm not answering that. Figure it out yourself, genius. 🤡",
]


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()
root.title("SARCALC — The Useless Calculator")
root.geometry("430x680")
root.resizable(True, True)
root.configure(bg=BG)


# -----------------------------
# VARIABLES
# -----------------------------

attempts = 0
savage_level = 0


# -----------------------------
# FUNCTIONS
# -----------------------------

def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)
    response_label.config(text="Ready to judge your mathematics.")


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    global attempts, savage_level

    expression = display.get().strip()

    if not expression:
        response_label.config(text="You didn't even enter anything. 😭")
        return

    attempts += 1

    # Increase sarcasm
    if attempts <= 2:
        savage_level = 0
    elif attempts <= 4:
        savage_level = 1
    elif attempts <= 7:
        savage_level = 2
    else:
        savage_level = 3

    # Special cases
    if expression.replace(" ", "") in ["0/0", "0÷0"]:
        response_label.config(
            text="Even mathematics has given up on you. 💀"
        )
        return

    if expression.replace(" ", "") in ["2+2", "2+2.0"]:
        response_label.config(
            text="FOUR. YOU KNOW THIS. 😭"
        )
        return

    # Choose response
    if savage_level == 0:
        response = random.choice(mild)

    elif savage_level == 1:
        response = random.choice(medium)

    elif savage_level == 2:
        response = random.choice(savage)

    else:
        response = random.choice(extreme)

    # Fake calculation animation
    response_label.config(text="Calculating... 🤔")
    root.after(
        700,
        lambda: response_label.config(text=response)
    )


def hover_on(button):
    button.config(bg="#3A3A3A")


def hover_off(button):
    button.config(bg=BUTTON_BG)


# -----------------------------
# HEADER
# -----------------------------

title = tk.Label(
    root,
    text="SARCALC",
    font=("Helvetica", 28, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(pady=(25, 2))

subtitle = tk.Label(
    root,
    text="The calculator that refuses to help.",
    font=("Helvetica", 11),
    bg=BG,
    fg=SECONDARY
)
subtitle.pack()


# -----------------------------
# DISPLAY
# -----------------------------

display_frame = tk.Frame(
    root,
    bg=DISPLAY_BG,
    highlightthickness=1,
    highlightbackground="#333333"
)

display_frame.pack(
    padx=25,
    pady=25,
    fill="x"
)

display = tk.Entry(
    display_frame,
    font=("Helvetica", 30),
    bg=DISPLAY_BG,
    fg=TEXT,
    insertbackground=TEXT,
    justify="right",
    bd=0
)

display.pack(
    padx=15,
    pady=20,
    fill="x"
)


# -----------------------------
# BUTTON FRAME
# -----------------------------

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack()


# -----------------------------
# BUTTON CREATOR
# -----------------------------

def create_button(text, row, column, command, special=False):

    color = SPECIAL_BG if special else BUTTON_BG

    button = tk.Button(
        button_frame,
        text=text,
        font=("Helvetica", 17, "bold"),
        fg=TEXT,
        bg=color,
        activebackground="#555555",
        activeforeground=TEXT,
        bd=0,
        width=5,
        height=2,
        command=command,
        cursor="hand2"
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

    if not special:
        button.bind(
            "<Enter>",
            lambda e: hover_on(button)
        )

        button.bind(
            "<Leave>",
            lambda e: hover_off(button)
        )

    return button


# -----------------------------
# CALCULATOR BUTTONS
# -----------------------------

buttons = [
    ("AC", 0, 0, clear_display),
    ("⌫", 0, 1, backspace),
    ("(", 0, 2, lambda: add_to_display("(")),
    (")", 0, 3, lambda: add_to_display(")")),

    ("7", 1, 0, lambda: add_to_display("7")),
    ("8", 1, 1, lambda: add_to_display("8")),
    ("9", 1, 2, lambda: add_to_display("9")),
    ("÷", 1, 3, lambda: add_to_display("/")),

    ("4", 2, 0, lambda: add_to_display("4")),
    ("5", 2, 1, lambda: add_to_display("5")),
    ("6", 2, 2, lambda: add_to_display("6")),
    ("×", 2, 3, lambda: add_to_display("*")),

    ("1", 3, 0, lambda: add_to_display("1")),
    ("2", 3, 1, lambda: add_to_display("2")),
    ("3", 3, 2, lambda: add_to_display("3")),
    ("−", 3, 3, lambda: add_to_display("-")),

    ("0", 4, 0, lambda: add_to_display("0")),
    (".", 4, 1, lambda: add_to_display(".")),
    ("%", 4, 2, lambda: add_to_display("%")),
    ("+", 4, 3, lambda: add_to_display("+")),
]

for text, row, column, command in buttons:
    create_button(
        text,
        row,
        column,
        command
    )


# -----------------------------
# USELESS CALCULATE BUTTON
# -----------------------------

calculate_button = tk.Button(
    root,
    text="CALCULATE  🤡",
    font=("Helvetica", 17, "bold"),
    fg=TEXT,
    bg=SPECIAL_BG,
    activebackground="#FFB340",
    bd=0,
    height=2,
    cursor="hand2",
    command=calculate
)

calculate_button.pack(
    padx=25,
    pady=(15, 10),
    fill="x"
)


# -----------------------------
# RESPONSE AREA
# -----------------------------

response_frame = tk.Frame(
    root,
    bg=DISPLAY_BG
)

response_frame.pack(
    padx=25,
    pady=10,
    fill="both",
    expand=True
)

response_title = tk.Label(
    response_frame,
    text="🤖 CALCULATOR RESPONSE",
    font=("Helvetica", 10, "bold"),
    bg=DISPLAY_BG,
    fg=SECONDARY
)

response_title.pack(
    pady=(15, 5)
)

response_label = tk.Label(
    response_frame,
    text="Ready to judge your mathematics.",
    font=("Helvetica", 15, "bold"),
    bg=DISPLAY_BG,
    fg=TEXT,
    wraplength=330,
    justify="center"
)

response_label.pack(
    padx=20,
    pady=15
)


# -----------------------------
# ATTEMPT COUNTER
# -----------------------------

attempt_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 9),
    bg=BG,
    fg=SECONDARY
)

attempt_label.pack()


def update_attempts():
    attempt_label.config(
        text=f"Calculations attempted: {attempts}"
    )
    root.after(200, update_attempts)


update_attempts()


# -----------------------------
# KEYBOARD SUPPORT
# -----------------------------

root.bind(
    "<Return>",
    lambda event: calculate()
)

root.bind(
    "<Escape>",
    lambda event: clear_display()
)


# -----------------------------
# START
# -----------------------------

root.mainloop()