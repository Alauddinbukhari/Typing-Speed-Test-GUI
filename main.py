from tkinter import *
from para_sentence import paragraph

window= Tk()
window.config(width=500,height=500)
window.title("Typing Test Speed")

def catch_input():
    pass



def calculate_wpm():
    pass

##########UI#########

paragraph_label=Label(text= "A paragraph is a series of related sentences developing a central idea, called the topic.\n Try to think about paragraphs in terms of thematic unity:\n" \
                             "                          a paragraph is a sentence or a group of sentences that supports one central, unified idea.\n" \
                             "                                     Paragraphs add one idea at a time to your broder argument " \
)
paragraph_label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_box = Text(window, wrap="word", height=10, width=40)
text_box.place(relx=0.5,rely=0.8, anchor=CENTER)



mainloop()