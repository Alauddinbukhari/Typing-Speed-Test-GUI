from tkinter import *
from para_sentence import paragraph

window= Tk()
window.config(width=500,height=500)
window.title("Typing Test Speed")
second =0
def calcualte_wpm(second): # add a functionality to call this function for each second , if only  user start typing

    if second>=60:
        to_min=second/60

        #call a function for a fetchiing text data adn caluculatiing wpm
        #to calculate wpa fetch all data then divide by 5 then by total minutes

    #add a functionality for checking if all pragraph words are typed



def detect_and_increment(second):
    text_data= len(text_box.get("1.0", "end-1c"))
    if text_data>0:
        calculate_wpm(second)
        second += 1
    window.after(1000, lambda:detect_and_increment(second))

def catch_input():
    pass



def calculate_wpm():
    pass

##########UI#########
paragraph_text = (
    "A paragraph is a series of related sentences developing a central idea, called the topic.\n"
    "Try to think about paragraphs in terms of thematic unity:\n"
    "a paragraph is a sentence or a group of sentences that supports one central, unified idea.\n"
    "Paragraphs add one idea at a time to your broader argument."
)

# Create a Label widget to display the paragraph
paragraph_label = Label(window, text=paragraph_text, justify=LEFT, wraplength=480)
paragraph_label.place(relx=0.5,rely=0.1, anchor=CENTER)



text_box = Text(window, wrap="word", height=10, width=40)
text_box.place(relx=0.5,rely=0.8, anchor=CENTER)



detect_and_increment(second)

mainloop()