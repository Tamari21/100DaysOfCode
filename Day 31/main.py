
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
WORD_LIST = "Day 31\\data\\french_words.csv"
WORDS_TO_LEARN = "Day 31\\data\\words_to_learn.csv"

word_list = {}
word = ""
# ----- DICTIONARY -----


def make_word_list():
    global word_list, word
    try:
        a = pd.read_csv(WORD_LIST)
        b = pd.read_csv(WORDS_TO_LEARN)
        c = pd.concat([a,b], axis=0)

        c.drop_duplicates(keep='first', inplace=True) # Set keep to False if you don't want any
                                                    # of the duplicates at all
        c.reset_index(drop=True, inplace=True)

        word_list = c.to_dict(orient='records')

        word = rd.choice(word_list)

    except FileNotFoundError:
        print("Data files are missing!")

    

def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = rd.choice(word_list)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=word["French"], fill="black")
    flash_card.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global word
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=word["English"], fill="white")
    flash_card.itemconfig(card_background, image=back_card)

def save_card():
    global word
    try:
        with open("Day 31\\data\\words_to_learn.csv", "a") as data_file:
            data_file.write(f"{word["French"]},{word["English"]}\n")
    except FileNotFoundError:
        with open("Day 31\\data\\words_to_learn.csv", "w") as data_file:
            data_file.write(f"French,English\n")
            data_file.write(f"{word["French"]},{word["English"]}\n")
    finally:
        next_card()

# ----- UI SETUP -----
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# ----- IMAGE SETUP -----
right_image = PhotoImage(file="Day 31\\images\\right.png")
wrong_image = PhotoImage(file="Day 31\\images\\wrong.png")
front_card = PhotoImage(file="Day 31\\images\\card_front.png")
back_card = PhotoImage(file="Day 31\\images\\card_back.png")
cards = {front_card,back_card}

# ----- FLASH CARD -----
make_word_list()
flash_card = Canvas(height=526, width=800,
                    highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = flash_card.create_image(400, 263, image=front_card)
card_title = flash_card.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(
    400, 263, text=word["French"], font=("Ariel", 60, "bold"))

flash_card.grid(row=0, column=0, columnspan=2)

# ----- BUTTONS -----
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=save_card)
wrong_button.grid(row=1, column=0)

right_button = Button(
    image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

# ----- LABELS -----
# website = Label(text="Website")
# website.grid(row=1, column=0)

window.mainloop()
