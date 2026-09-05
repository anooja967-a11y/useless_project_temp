import tkinter as tk
import random
import winsound

# =========================================================
# SARCALC
# The Calculator That Refuses To Calculate
# =========================================================

# -------------------------
# COLORS
# -------------------------

BG = "#101010"
DISPLAY_BG = "#1B1B1B"
BUTTON_BG = "#292929"
BUTTON_HOVER = "#3A3A3A"
ORANGE = "#FF9500"
ORANGE_HOVER = "#FFAD32"
WHITE = "#FFFFFF"
GRAY = "#999999"
GREEN = "#5BE37D"


# -------------------------
# VARIABLES
# -------------------------

attempts = 0
sound_on = True


# =========================================================
# SARCASTIC RESPONSES
# =========================================================

mild = [
    "Are you sure you need a calculator for this? 😭",
    "You could probably solve this yourself.",
    "Try using your brain first. 🧠",
    "That's a pretty easy one...",
    "Hmm... interesting choice of question."
]

medium = [
    "You REALLY needed a calculator for that? 💀",
    "I know the answer. I'm just not telling you.",
    "Your math teacher is disappointed.",
    "Congratulations. You avoided doing math.",
    "I could answer this, but why should I?",
    "This is why calculators were invented, apparently."
]

savage = [
    "WOW. You outsourced basic mathematics to a computer. 💀",
    "I'm a calculator, not your brain.",
    "At this point, even Google is concerned.",
    "You had ONE job. ONE.",
    "Maybe mathematics isn't your thing. 😭",
    "I'm beginning to question why I was invented.",
    "The answer is obvious. Your confidence isn't.",
    "Please reconsider your life choices."
]

extreme = [
    "I refuse to participate in this academic disaster. 💀",
    "Even my circuits are embarrassed right now.",
    "You need a mathematics intervention.",
    "I'm deleting myself after seeing that equation.",
    "This calculation has caused irreversible damage to my processor.",
    "I'm not answering that. Figure it out yourself. 🤡",
    "STOP PRESSING EQUALS. 😭",
    "At this point, YOU are the useless project."
]


# =========================================================
# SOUND EFFECTS
# =========================================================

def play_sound(sound_type="click"):

    if not sound_on:
        return

    try:

        if sound_type == "click":
            winsound.Beep(700, 40)

        elif sound_type == "error":
            winsound.Beep(350, 100)
            winsound.Beep(220, 120)

    except:
        pass


# =========================================================
# DISPLAY FUNCTIONS
# =========================================================

def add_to_display(value):

    play_sound("click")

    display.insert(tk.END, value)


def clear_display():

    play_sound("click")

    display.delete(0, tk.END)

    response_label.config(
        text="Ready to judge your mathematics.",
        fg=WHITE
    )


def backspace():

    play_sound("click")

    current = display.get()

    display.delete(0, tk.END)

    display.insert(0, current[:-1])


# =========================================================
# CALCULATE / ROAST
# =========================================================

def calculate():

    global attempts

    expression = display.get().strip()

    if expression == "":

        play_sound("error")

        response_label.config(
            text="You didn't even enter anything. 😭",
            fg=WHITE
        )

        return

    attempts += 1

    play_sound("error")

    clean = expression.replace(" ", "")

    # -------------------------
    # SPECIAL CALCULATIONS
    # -------------------------

    if clean in ["2+2", "2+2.0"]:

        response = "FOUR. YOU KNOW THIS. 😭"

    elif clean in ["0/0", "0÷0"]:

        response = "Even mathematics has given up on you. 💀"

    # -------------------------
    # INCREASING SARCASM
    # -------------------------

    elif attempts <= 2:

        response = random.choice(mild)

    elif attempts <= 4:

        response = random.choice(medium)

    elif attempts <= 7:

        response = random.choice(savage)

    else:

        response = random.choice(extreme)

    # -------------------------
    # FAKE CALCULATION
    # -------------------------

    response_label.config(
        text="Calculating... 🤔",
        fg=ORANGE
    )

    # Display animation

    display_frame.config(
        highlightbackground=ORANGE
    )

    root.after(
        250,
        lambda: display_frame.config(
            highlightbackground="#333333"
        )
    )

    root.after(
        700,
        lambda: show_roast(response)
    )


def show_roast(response):

    response_label.config(
        text=response,
        fg=WHITE
    )


# =========================================================
# SOUND ON / OFF
# =========================================================

def toggle_sound():

    global sound_on

    sound_on = not sound_on

    if sound_on:

        sound_button.config(
            text="🔊",
            fg=GREEN
        )

        play_sound("click")

    else:

        sound_button.config(
            text="🔇",
            fg=GRAY
        )


# =========================================================
# HOVER ANIMATION
# =========================================================

def hover_on(button, special=False):

    if special:

        button.config(
            bg=ORANGE_HOVER
        )

    else:

        button.config(
            bg=BUTTON_HOVER
        )


def hover_off(button, special=False):

    if special:

        button.config(
            bg=ORANGE
        )

    else:

        button.config(
            bg=BUTTON_BG
        )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("SARCALC 🤡")

root.geometry("350x590")

root.resizable(False, False)

root.configure(
    bg=BG
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg=BG
)

header.pack(
    fill="x",
    padx=20,
    pady=(16, 0)
)


title = tk.Label(
    header,
    text="SARCALC",
    font=("Helvetica", 21, "bold"),
    bg=BG,
    fg=WHITE
)

title.pack(
    side="left"
)


# -------------------------
# SOUND BUTTON
# -------------------------

sound_button = tk.Button(
    header,
    text="🔊",
    font=("Helvetica", 13),
    bg=BG,
    fg=GREEN,
    activebackground=BG,
    activeforeground=GREEN,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=toggle_sound
)

sound_button.pack(
    side="right"
)


# -------------------------
# SUBTITLE
# -------------------------

subtitle = tk.Label(
    root,
    text="The calculator that refuses to help.",
    font=("Helvetica", 9),
    bg=BG,
    fg=GRAY
)

subtitle.pack(
    pady=(1, 12)
)


# =========================================================
# DISPLAY
# =========================================================

display_frame = tk.Frame(
    root,
    bg=DISPLAY_BG,
    highlightthickness=1,
    highlightbackground="#333333"
)

display_frame.pack(
    padx=20,
    pady=(0, 13),
    fill="x"
)


display = tk.Entry(
    display_frame,
    font=("Helvetica", 22),
    bg=DISPLAY_BG,
    fg=WHITE,
    insertbackground=WHITE,
    selectbackground=ORANGE,
    selectforeground=WHITE,
    justify="right",
    bd=0
)

display.pack(
    padx=10,
    pady=12,
    fill="x"
)


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack()


# =========================================================
# BUTTON CREATOR
# =========================================================

def create_button(
    text,
    row,
    column,
    command,
    special=False
):

    color = ORANGE if special else BUTTON_BG

    button = tk.Button(
        button_frame,
        text=text,
        font=("Helvetica", 13, "bold"),
        fg=WHITE,
        bg=color,
        activebackground=(
            ORANGE_HOVER if special
            else "#505050"
        ),
        activeforeground=WHITE,
        bd=0,
        relief="flat",
        width=4,
        height=1,
        cursor="hand2",
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=3,
        pady=3,
        ipadx=2,
        ipady=3
    )

    # Hover effect

    button.bind(
        "<Enter>",
        lambda event: hover_on(
            button,
            special
        )
    )

    button.bind(
        "<Leave>",
        lambda event: hover_off(
            button,
            special
        )
    )

    return button


# =========================================================
# CALCULATOR BUTTONS
# =========================================================

buttons = [

    # Row 1
    ("AC", 0, 0, clear_display),
    ("(", 0, 1, lambda: add_to_display("(")),
    (")", 0, 2, lambda: add_to_display(")")),
    ("+", 0, 3, lambda: add_to_display("+")),

    # Row 2
    ("7", 1, 0, lambda: add_to_display("7")),
    ("8", 1, 1, lambda: add_to_display("8")),
    ("9", 1, 2, lambda: add_to_display("9")),
    ("÷", 1, 3, lambda: add_to_display("/")),

    # Row 3
    ("4", 2, 0, lambda: add_to_display("4")),
    ("5", 2, 1, lambda: add_to_display("5")),
    ("6", 2, 2, lambda: add_to_display("6")),
    ("×", 2, 3, lambda: add_to_display("*")),

    # Row 4
    ("1", 3, 0, lambda: add_to_display("1")),
    ("2", 3, 1, lambda: add_to_display("2")),
    ("3", 3, 2, lambda: add_to_display("3")),
    ("−", 3, 3, lambda: add_to_display("-")),

    # Row 5
    ("0", 4, 0, lambda: add_to_display("0")),
    (".", 4, 1, lambda: add_to_display(".")),
    ("%", 4, 2, lambda: add_to_display("%")),
    ("+", 4, 3, lambda: add_to_display("+"))
]


# Create buttons

for text, row, column, command in buttons:

    create_button(
        text,
        row,
        column,
        command
    )


# =========================================================
# EQUAL BUTTON
# =========================================================

equal_button = tk.Button(
    button_frame,
    text="=",
    font=("Helvetica", 14, "bold"),
    fg=WHITE,
    bg=ORANGE,
    activebackground=ORANGE_HOVER,
    activeforeground=WHITE,
    bd=0,
    relief="flat",
    width=4,
    height=1,
    cursor="hand2",
    command=calculate
)

equal_button.grid(
    row=4,
    column=3,
    padx=3,
    pady=3,
    ipadx=2,
    ipady=3
)


equal_button.bind(
    "<Enter>",
    lambda event: hover_on(
        equal_button,
        True
    )
)


equal_button.bind(
    "<Leave>",
    lambda event: hover_off(
        equal_button,
        True
    )
)


# =========================================================
# RESPONSE AREA
# =========================================================

response_frame = tk.Frame(
    root,
    bg=DISPLAY_BG
)

response_frame.pack(
    padx=20,
    pady=12,
    fill="both",
    expand=True
)


response_title = tk.Label(
    response_frame,
    text="🤖 CALCULATOR RESPONSE",
    font=("Helvetica", 9, "bold"),
    bg=DISPLAY_BG,
    fg=GRAY
)

response_title.pack(
    pady=(10, 3)
)


response_label = tk.Label(
    response_frame,
    text="Ready to judge your mathematics.",
    font=("Helvetica", 12, "bold"),
    bg=DISPLAY_BG,
    fg=WHITE,
    wraplength=280,
    justify="center"
)

response_label.pack(
    padx=10,
    pady=8
)


# =========================================================
# ROAST COUNTER
# =========================================================

attempt_label = tk.Label(
    root,
    text="Roasts delivered: 0",
    font=("Helvetica", 8),
    bg=BG,
    fg=GRAY
)

attempt_label.pack(
    pady=(0, 7)
)


def update_counter():

    attempt_label.config(
        text=f"Roasts delivered: {attempts}"
    )

    root.after(
        200,
        update_counter
    )


update_counter()


# =========================================================
# KEYBOARD SUPPORT
# =========================================================

root.bind(
    "<Return>",
    lambda event: calculate()
)

root.bind(
    "<Escape>",
    lambda event: clear_display()
)


# =========================================================
# START
# =========================================================

root.mainloop()