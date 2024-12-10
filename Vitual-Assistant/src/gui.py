from tkinter import*
from PIL import Image, ImageTk
import action
import speech_to_text

root = Tk()
root.title("AI Assistant")
root.geometry("600x675")
root.resizable(False,False)
root.config(bg = "#233142")

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "USER --> "+user_val+"\n")
    if bot_val != None:
        text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
          root.destroy()  


def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "USER --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()


def del_text():
     text.delete("1.0", "end")
     entry.delete(0, Tk.END)


frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg = "#233142")
frame.grid(row= 0, column = 1, padx = 55, pady = 10)

textLabel =  Label(frame, text="Ai Assistant", font=("comic Sans ms", 14, "bold"), bg = "#fff" )
textLabel.grid(row= 0, column = 0, padx = 20, pady = 10)

image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame, image = image)
image_label.grid(row = 1, column = 0, pady = 20)

text = Text(root, font=('courier 10'), bg = "#e3e3e3")
text.grid(row = 2, column = 0)
text.place(x = 100, y = 375,width = 375, height = 100 )

entry = Entry(root, justify=CENTER)
entry.place(x = 100, y = 500 ,width = 375, height = 30 )

Button1 = Button(root, text = "Ask", bg = "#e3e3e3", pady = 16, padx = 40, borderwidth= 3, relief= SOLID, command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text = "Send", bg = "#e3e3e3", pady = 16, padx = 40, borderwidth= 3, relief= SOLID, command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text = "Delete", bg = "#e3e3e3", pady = 16, padx = 40, borderwidth= 3, relief= SOLID, command=del_text)
Button3.place(x=230, y=575)



root.mainloop()