# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import tkcalendar as tcal
import tkinter.filedialog as filedialog
import datetime 
import os
from tkinter import messagebox

root = tk.Tk()

root.title('Delete directory tool')

root.geometry('800x700')

file_gtm = tk.IntVar()
file_gdx = tk.IntVar()
file_sim = tk.IntVar()
file_simt = tk.IntVar()
file_avi = tk.IntVar()
file_csv = tk.IntVar()
file_xb = tk.IntVar()
file_prt = tk.IntVar()
file_xt = tk.IntVar()
file_mpeg = tk.IntVar()
file_png = tk.IntVar()
file_trn = tk.IntVar()
file_xlsx = tk.IntVar()
file_pptx = tk.IntVar()
file_docx = tk.IntVar()

Folder = os.path.join(os.getcwd(),'Misc')

date = datetime.datetime.today()

def browse_folder():
    Entry_folder.delete(0, tk.END)
    global Folder
    Folder = filedialog.askdirectory()
    Entry_folder.insert(0,Folder)
    return None

def del_func(file_gtm,file_gdx,file_sim,file_trn,file_xlsx,file_pptx,file_docx,file_simt,file_csv,file_xb,file_xt, file_prt, file_png, file_avi, file_mpeg, other, Folder,date):
    import Delete_func as Df
    filetype=[file_gtm,file_gdx,file_sim,file_trn,file_xlsx,file_pptx,file_docx,file_simt,file_csv,file_xb,file_xt, file_prt, file_png, file_avi, file_mpeg,other]
   # mylabel2.config(text = str(file_gtm) + str(file_gdx) + str(file_sim)+str(file_trn)+'_'+str(Folder)+'_'+str(date))
    Df.Delete_func(Folder,filetype,date)
    status = messagebox.askyesno(title = 'Question',message = 'Do you want to permanently remove the files from recycle bin?')
    Df.Permanent_del(Folder,status)
    messagebox.showinfo(title = 'Info', message = 'Delete operation completed')
    return None
    
    
l2 = tk.Label(root, text = 'Select destination folder')
l2.place(x=350,y=180)
Entry_folder = tk.Entry(root,width = 50)
#Entry_folder.insert(0,os.path.join(os.getcwd(),'Misc'))
Entry_folder.place(x=350,y=200)

            
              
Browse_folder = tk.Button(root, text ='Browse',command = browse_folder)
Browse_folder.place(x=700, y=200)

l1 = tk.Label(root, text = 'Select which all file formats to delete')
l1.place(x=10,y=10)

c1 = tk.Checkbutton(root, text = 'gtm', variable = file_gtm)
c1.place(x=10,y=50)

c2 = tk.Checkbutton(root, text = 'gdx', variable = file_gdx)
c2.place(x=10,y=80)

c3 = tk.Checkbutton(root, text = 'sim', variable = file_sim)
c3.place(x = 10, y = 110)

c4 = tk.Checkbutton(root,text = 'trn',variable = file_trn)
c4.place(x=10, y=140)

c5 = tk.Checkbutton(root,text = 'xlsx',variable = file_xlsx)
c5.place(x=10, y=170)


c6 = tk.Checkbutton(root,text = 'pptx',variable = file_pptx)
c6.place(x=10, y=200)

c7 = tk.Checkbutton(root,text = 'docx',variable = file_docx)
c7.place(x=10, y=230)


c8 = tk.Checkbutton(root,text = 'sim~', variable = file_simt)
c8.place(x=80,y=50)

c9 = tk.Checkbutton(root,text = 'csv', variable = file_csv)
c9.place(x=80,y=80)

c10 = tk.Checkbutton(root,text = 'x_b', variable = file_xb)
c10.place(x=80,y=110)

c11 = tk.Checkbutton(root,text = 'x_t', variable = file_xt)
c11.place(x=80,y=140)

c12 = tk.Checkbutton(root,text = 'prt',variable = file_prt)
c12.place(x=80,y=170)

c13 = tk.Checkbutton(root,text = 'png', variable = file_png)
c13.place(x=80,y=200)

c14= tk.Checkbutton(root,text = 'avi',variable = file_avi)
c14.place(x=80,y=230)

c15= tk.Checkbutton(root,text = 'mpeg',variable = file_mpeg)
c15.place(x=150,y=50)

l4 = tk.Label(root, text = 'Other')
l4.place(x=150, y=80)

other = tk.Entry(root, width = 10)
other.place(x = 150,y=100)



l3 = tk.Label(root, text = 'Select the cut-off date for file deletion')
l3.place(x=10, y=280)

cal = tcal.Calendar(root, selectmode = "day", year = 2020, month = 4, day = 6)
cal.place(x=10, y=300)

def grab_date():
    global date
    date = datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")
    #date2 = datetime.datetime.today()
    #Days = (date2 - date1).days
    return None

#my_button = tk.Button(root, text = 'Get Date', command = grab_date)
#my_label = tk.Label(root,text = "")
#my_label.place(x=50,y=650)

Delete =tk.Button(root, text = 'Start Delete',command = lambda: del_func(file_gtm.get(),file_gdx.get(),file_sim.get(),file_trn.get(),file_xlsx.get(),file_pptx.get(),file_docx.get(),file_simt.get(),file_csv.get(),file_xb.get(),file_xt.get(), file_prt.get(), file_png.get(), file_avi.get(), file_mpeg.get(), other.get(), Entry_folder.get(),datetime.datetime.strptime(cal.get_date(), "%m/%d/%y")))
Delete.place(x=50, y=600)


#mylabel2 = tk.Label(root, text = "")
#mylabel2.pack(pady = 20)


root.mainloop()





