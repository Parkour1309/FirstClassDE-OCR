from tkinter import *
import asyncio
from tkinter import filedialog
import numpy as num
import cv2
import PIL
from tkinter import *
from tkinter import ttk
from PIL import Image
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title("FirstClassDE")

frame = Frame(root, width=600, height=500)

menu = Menu(frame.master)   #Menu part of frame
frame.master.config(menu=menu)

waitLabel = Label(root, text="Waiting for file selection", bg="black", fg="red")
waitLabel.grid(row=6,column=0)

fileDir = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TIFF Files","*.TIFF"),("all files","*.*")))
fileMenu = Menu(menu)
fileMenu.add_command(label="Import Scan", command=fileDir,) #When import scan button is pressed, assign it to open the file selection dialog
     #Create dropdown to show fileMenu
menu.add_cascade(label='File', menu=fileMenu)





if fileDir != "":
    waitLabel.grid_forget()
    waitLabel = Label(root, text=fileDir, fg="green")
    waitLabel.grid(row=6, column=0)
    print(fileDir)
    frame.grid()

    img = Image.open(fileDir)

    ###FORM READING###
    # FirstName              # Load the image
    crop_Fname = (293, 165, 1758, 230)  # Write crop parameters
    formatted = img.crop(crop_Fname)  # Crop the image
    # formatted.show()     #load cropped image
    FN_Data = image_to_string(formatted, lang='eng')
    print("First Name:", FN_Data)

    # LastName
    crop_Lname = (289, 249, 1751, 309)  # Write crop parameters
    formatted = img.crop(crop_Lname)  # Crop the image
    # formatted.show()     #load cropped image
    LN_Data = image_to_string(formatted, lang='eng')
    print("Last Name:", LN_Data)

    # Address
    crop_Address = (287, 330, 1748, 391)  # Write crop parameters
    formatted = img.crop(crop_Address)  # Crop the image
    # formatted.show()     #load cropped image
    Address_Data = image_to_string(formatted, lang='eng')
    print("Address:", Address_Data)

    # Address2
    crop_Address2 = (446, 410, 1055, 461)  # Write crop parameters
    formatted = img.crop(crop_Address2)  # Crop the image
    # formatted.show()     #load cropped image
    Address2_Data = image_to_string(formatted, lang='eng')
    print("APT/LOT/Bldg:", Address2_Data)

    # City
    crop_City = (182, 493, 913, 554)  # Write crop parameters
    formatted = img.crop(crop_City)  # Crop the image
    # formatted.show()     #load cropped image
    City_Data = image_to_string(formatted, lang='eng')
    print("City:", City_Data)

    # State
    crop_State = (1171, 492, 1292, 554)  # Write crop parameters
    formatted = img.crop(crop_State)  # Crop the image
    # formatted.show()     #load cropped image
    State_Data = image_to_string(formatted, lang='eng')
    print("State:", State_Data)

    # ZIP
    crop_ZIP = (1461, 488, 1766, 549)  # Write crop parameters
    formatted = img.crop(crop_ZIP)  # Crop the image
    # formatted.show()     #load cropped image
    ZIP_Data = image_to_string(formatted, lang='eng')
    print("ZIP:", ZIP_Data)

    # Cellphone
    crop_Cell = (255, 646, 866, 707)  # Write crop parameters
    formatted = img.crop(crop_Cell)  # Crop the image
    # formatted.show()     #load cropped image
    Cell_Data = image_to_string(formatted, lang='eng')
    print("Cellphone:", Cell_Data)

    # Homephone
    crop_Homeph = (1279, 646, 1889, 706)  # Write crop parameters
    formatted = img.crop(crop_Homeph)  # Crop the image
    # formatted.show()     #load cropped image
    Homeph_Data = image_to_string(formatted, lang='eng')
    print("Homephone:", Homeph_Data)

    # Email
    crop_Email = (198, 746, 1659, 807)  # Write crop parameters
    formatted = img.crop(crop_Address)  # Crop the image
    # formatted.show()     #load cropped image
    Email_Data = image_to_string(formatted, lang='eng')
    print("Email:", Email_Data)

    # HS
    crop_School = (372, 856, 1834, 917)  # Write crop parameters
    formatted = img.crop(crop_School)  # Crop the image
    # formatted.show()     #load cropped image
    School_Data = image_to_string(formatted, lang='eng')
    print("High School:", School_Data)

    # Date
    crop_Date = (49, 87, 437, 147)  # Write crop parameters
    formatted = img.crop(crop_Date)  # Crop the image
    # formatted.show()     #load cropped image
    Date_Data = image_to_string(formatted, lang='eng')
    print("Date:", Date_Data)

    # Grad Year
    crop_Grad = (501, 87, 747, 147)  # Write crop parameters
    formatted = img.crop(crop_Grad)  # Crop the image
    # formatted.show()     #load cropped image
    Grad_Data = image_to_string(formatted, lang='eng')
    print("Grad Year:", Grad_Data)

    # BDay
    crop_Bday = (705, 86, 1184, 147)  # Write crop parameters
    formatted = img.crop(crop_Bday)  # Crop the image
    # formatted.show()     #load cropped image
    BDay_Data = image_to_string(formatted, lang='eng')
    print("Birthday:", BDay_Data)

    # RepNumber
    crop_Rep = (1274, 87, 1520, 147)  # Write crop parameters
    formatted = img.crop(crop_Rep)  # Crop the image
    # formatted.show()     #load cropped image
    Rep_Data = image_to_string(formatted, lang='eng')
    print("Rep Number:", Rep_Data)

    # ACCT
    crop_Acct = (1583, 87, 1951, 147)  # Write crop parameters
    formatted = img.crop(crop_Acct)  # Crop the image
    # formatted.show()     #load cropped image
    Acct_Data = image_to_string(formatted, lang='eng')
    print("ACCT Number:", Acct_Data)

      #AUTOFILL ENTRY

    label_First= Label(root,text="First:")
    entry_First= Entry(root)
    entry_First.insert(END, string=FN_Data)
    label_First.grid(row=0, column=0)
    entry_First.grid(row=0, column=1)

    label_First = Label(root, text="Last:")
    entry_First = Entry(root)
    entry_First.insert(END, string=LN_Data)
    label_First.grid(row=1, column=0)
    entry_First.grid(row=1, column=1)

    label_First = Label(root, text="Address:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Address_Data)
    label_First.grid(row=2, column=0)
    entry_First.grid(row=2, column=1)

    label_First = Label(root, text="APT/LOT/BLDG Etc:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Address2_Data)
    label_First.grid(row=3, column=0)
    entry_First.grid(row=3, column=1)

    label_First = Label(root, text="City:")
    entry_First = Entry(root)
    entry_First.insert(END, string=City_Data)
    label_First.grid(row=4, column=0)
    entry_First.grid(row=4, column=1)

    label_First = Label(root, text="State:")
    entry_First = Entry(root)
    entry_First.insert(END, string=State_Data)
    label_First.grid(row=5, column=0)
    entry_First.grid(row=5, column=1)

    label_First = Label(root, text="ZIP:")
    entry_First = Entry(root)
    entry_First.insert(END, string=ZIP_Data)
    label_First.grid(row=0, column=2)
    entry_First.grid(row=0, column=3)

    label_First = Label(root, text="Cellphone:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Cell_Data)
    label_First.grid(row=1, column=2)
    entry_First.grid(row=1, column=3)

    label_First = Label(root, text="Homephone:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Homeph_Data)
    label_First.grid(row=2, column=2)
    entry_First.grid(row=2, column=3)

    label_First = Label(root, text="Email:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Homeph_Data)
    label_First.grid(row=3, column=2)
    entry_First.grid(row=3, column=3)

    label_First = Label(root, text="Highschool:")
    entry_First = Entry(root)
    entry_First.insert(END, string=School_Data)
    label_First.grid(row=4, column=2)
    entry_First.grid(row=4, column=3)

    label_First = Label(root, text="Date:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Date_Data)
    label_First.grid(row=5, column=2)
    entry_First.grid(row=5, column=3)

    label_First = Label(root, text="Grad Year:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Grad_Data)
    label_First.grid(row=0, column=4)
    entry_First.grid(row=0, column=5)

    label_First = Label(root, text="Birthday:")
    entry_First = Entry(root)
    entry_First.insert(END, string=BDay_Data)
    label_First.grid(row=1, column=4)
    entry_First.grid(row=1, column=5)

    label_First = Label(root, text="Rep Number:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Rep_Data)
    label_First.grid(row=2, column=4)
    entry_First.grid(row=2, column=5)

    label_First = Label(root, text="ACCT Number:")
    entry_First = Entry(root)
    entry_First.insert(END, string=Acct_Data)
    label_First.grid(row=3, column=4)
    entry_First.grid(row=3, column=5)




    root.mainloop()

