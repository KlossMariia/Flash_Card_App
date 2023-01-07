from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

# checks if there are words which you have already learned, if there are none,
# program creates new file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# this command flips the card and shows the translation of the current foreign word
def flip_the_card():
    global current_card
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"].capitalize(), fill="white")
    canvas.itemconfig(image_container, image=card_back_img)

# command shows next card with new foreign word on it
# command is in button, it runs after clicking
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(language, text="French", fill="Black")
    canvas.itemconfig(image_container, image=card_front_img)

    current_card = random.choice(to_learn)
    key = current_card["French"]

    canvas.itemconfig(word, text=f"{key.capitalize()}", fill="Black")
    flip_timer = window.after(3000, flip_the_card)


# command removes words which you've already learned from words_to_learn list
def is_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# creating window with tkinter
window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
# setting timer for card to flip after 3 seconds
flip_timer = window.after(3000, flip_the_card)

# importing pictures for canvas
card_back_img = PhotoImage(file="/Users/mariakloss/Desktop/Python programs/Flash Card App/images/card_back.png")
card_front_img = PhotoImage(file="/Users/mariakloss/Desktop/Python programs/Flash Card App/images/card_front.png")
right_img = PhotoImage(file="/Users/mariakloss/Desktop/Python programs/Flash Card App/images/right.png")
wrong_img = PhotoImage(file="/Users/mariakloss/Desktop/Python programs/Flash Card App/images/wrong.png")
# creating canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_container = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
# creating a writing on card
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
# creating buttons
yes_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)

no_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

next_card()
window.mainloop()

