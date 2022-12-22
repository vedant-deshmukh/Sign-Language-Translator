from tkinter import Tk, Label, PhotoImage, Frame, Button
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import LoginFrame 
from functools import partial
import LiveTranslatorFrame
import CaptureImageFrame


# -------------------------------------------------------------------------


	

# -------------------------------------------------------------------


options_image = None
options_frame = None

def add_Options_UI(root):
	root.title("Home - Sign Language Translator")
	
	image = PhotoImage(file= "options.png") 
	
	global options_image
	global options_frame
	
	options_image = Label(root, image=image, border=0, bg="white") 
	options_image.image = image 
	options_image.place(x=20, y=130)
	
	
	options_frame = Frame(root, name= "options", width= 450, height = 520, bg = 'white')
	options_frame.place(x= 520, y=140)		

	head = Label(options_frame, text= "Select a Task", fg = "#57a1f8", bg ="white", font = ("Microsoft Yahei UI Light", 23, 'bold'))
	head.place(x=140, y = 40)

# -----------------------------------------------------------------------------------------------------

	option1 = Button(options_frame, width = 35, pady = 6, text = "Live Translator" ,font = ('Microsoft Yahei UI Light', 12), bg ="#57a1f8", fg = 'white',cursor ='hand2', border = 0, command=partial(goto_livet, root))
	option1.place(x=80, y = 150)

	option2 = Button(options_frame, width = 35, pady = 6, text = "Capture Image" ,font = ('Microsoft Yahei UI Light', 12), bg ="#57a1f8", fg = 'white',cursor ='hand2', border = 0, command=partial(goto_captimg, root))
	option2.place(x=81, y = 260)

	logoutbtn = Button (options_frame, width = 18, text = "Log Out", border = 0, font = ('Microsoft Yahei UI Light', 9), bg = 'white', cursor ='hand2', fg ='#57a1f8', activebackground = "white" , command = partial(final_options,root)).place (x= 175, y = 340)

#------------------------------------------------------------------------------------------------------------------------------------------


def goto_livet(root):
	remove_options_UI()
	LiveTranslatorFrame.add_LiveTranslator_UI(root)

def goto_captimg(root):
	remove_options_UI()
	CaptureImageFrame.add_CaptureImage_UI(root)

def final_options(root):
	remove_options_UI()
	LoginFrame.add_login_UI(root)

def remove_options_UI():
    options_image.place_forget()
    options_frame.place_forget()

#----------------------------------------------------------------------------------------------------------------------------------------
