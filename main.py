from tkinter import *
from para_sentence import paragraph_text




window= Tk()
window.config(width=500,height=500)
window.title("Typing Test Speed")
second =0
wpm=0


def calculate_wpm(sec, text_len):
    if sec >= 60:
        to_min = sec / 60
        wpm = (text_len / 5) / to_min
        print(wpm)
        return wpm

        # Call a function for fetching text data and calculating WPM
        # To calculate WPM, fetch all data, then divide by 5, then by total minutes

# Add a functionality for checking if all paragraph words are typed
def display_after_complete():
    print(f"your speed per minute is {wpm}")

def detect_and_increment(second):
    text_length = len(text_box.get("1.0", "end-1c"))
    if text_length>=298:
        display_after_complete()
    if text_length > 0:
        print(text_length)
        calculate_wpm(second,text_length)
        second += 1
    window.after(1000, lambda: detect_and_increment(second))




##########UI#########



# Create a Label widget to display the paragraph
paragraph_label = Label(window, text=paragraph_text, justify=LEFT, wraplength=480)
paragraph_label.place(relx=0.5,rely=0.1, anchor=CENTER)



text_box = Text(window, wrap="word", height=7, width=40)
text_box.place(relx=0.5,rely=0.8, anchor=CENTER)



detect_and_increment(second)

mainloop()