from tkinter import *
def Resize():
    height = inp_height.get()
    width = inp_width.get()
    root.geometry(f"{height}x{width}")
root = Tk()
root.title("Resize Me!")
root['bg']='Black'
root.geometry("400x400")
label_height = Label(root , text="Width" ,fg='pink',bg='black',font=("comic sans ms",15)).pack()
inp_height= Entry(root,bg='grey',fg='white',font=("comic sans ms",15))
inp_height.pack()
label_width = Label(root , text="Height" , fg='white',bg='black',font=("comic sans ms",15)).pack()
inp_width = Entry(root,bg='grey',fg='white',font=("comic sans ms",15))
inp_width.pack()
submit = Button(root , text = "Resize" , command = Resize, fg='White',bg='Dark Green',font=("comic sans ms",13))
submit.pack()
exit_but = Button(root , text = " Close " , command = root.destroy, fg='White',bg='Red',font=("comic sans ms",13))
exit_but.pack()
root.mainloop()
