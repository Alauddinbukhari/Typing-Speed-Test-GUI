# Importing necessary modules from the Tkinter library
from tkinter import *
from para_sentence import paragraph_text  # Assuming you have a separate file para_sentence.py with paragraph_text variable

# Creating the main window
window = Tk()
window.config(width=500, height=500)
window.title("Typing Test Speed")

# Initializing variables for time and words per minute (wpm)
second = 0
wpm = 0

def update_sec_label(second):
    seconds_label.config(text=str(second))




# Function to calculate words per minute (wpm)
def calculate_wpm(sec, text_len):
    global wpm
    if sec >= 60:
        to_min = sec / 60
        wpm = (text_len / 5) / to_min  # Assuming an average word length of 5 characters
        print(wpm)
        return wpm

# Function to display the wpm after completing the typing test
def display_after_complete():
    print(f"Your speed per minute is {wpm}")

# Function to detect and increment time, and check for completion
def detect_and_increment(second):
    text_length = len(text_box.get("1.0", "end-1c"))

    # If the text length is greater than or equal to the expected length (298 in this case)
    if text_length >= 298:
        display_after_complete()

    # If there is text in the text box, calculate wpm and increment time
    if text_length > 0:

        calculate_wpm(second, text_length)
        second += 1

        update_sec_label(second)

    # Schedule the function to run after 1000 milliseconds (1 second)
    window.after(1000, lambda: detect_and_increment(second))

# UI Section

# Label to display the given paragraph
paragraph_label = Label(window, text=paragraph_text, justify=LEFT, wraplength=480)
paragraph_label.pack(anchor='center', pady=10)

seconds_label = Label(text="0")
seconds_label.pack(side="right",anchor="n")



# Text box for user input

text_box = Text(window, wrap="word", height=7, width=40)
text_box.pack(anchor='center', pady=10)


# Call the detect_and_increment function to start tracking time and checking for completion
detect_and_increment(second)

# Start the Tkinter event loop
mainloop()
