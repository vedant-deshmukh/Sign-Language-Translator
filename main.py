from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from LoginFrame import *
from SignupFrame import *
# -------------------------------------------------

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Translator")
        self.root.geometry('1000x710+180+35')
        self.root.resizable(False, False)
        self.root.configure(bg = "white")
        
        icon = PhotoImage(file="icon.png")
        self.root.iconphoto(False, icon)
        
        self.title = ImageTk.PhotoImage(file = "title.png")
        self.title_image = Label(self.root, image = self.title, border = 0)
        self.title_image.image = self.title
        self.title_image.place(x = 0, y = 10)

        add_login_UI(self.root)
  
#-------------------------------------------------------------- 
       
if __name__ == "__main__":
    root = Tk()
    root.grid_propagate(False)
    UI(root)
    root.mainloop()
    