#by R.S
#add button image path before running
import csv
import requests
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.font
from tkinter import messagebox

'''
data retrieve and prediction
'''

CSV_URL = 'https://thingspeak.com/channels/357788/feed.csv'

data1=[]
x = np.arange(0,100)
y=[]
z=[]
with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list[1:74]:
       # print(row)
        data1.append(row)
for data in data1:
    y.append(float(data[2]))
    z.append(float(data[3]))
#print(len(y))
#print(len(x))
#print(y)

def interpcurve():
    spl = UnivariateSpline(x,y)
    xs = np.linspace(0, 200, 10)
    plt.plot(xs, spl(xs), 'r')
    plt.xlabel('x points')
    plt.ylabel('temperature')
    plt.show()
def tomtemp():
    spl= UnivariateSpline(x,y)
    t1=spl(120)
    messagebox.showinfo("PREDICTED TEMPERATURE", "The temperature will be approximately\n\n\t %.2fºC"%t1)
def humcurve():
    spl = UnivariateSpline(x,z)
    xs = np.linspace(0, 200, 10)
    plt.plot(xs, spl(xs), 'g')
    plt.xlabel('x points')
    plt.ylabel('humidity')
    plt.show()
def tomhum():
    spl=UnivariateSpline(x,z)
    t1=spl(120)
    messagebox.showinfo("PREDICTED HUMIDITY", "The humidity will be approximately\n\n\t %.2f%%"%t1)


#tomtemp(x,y)
'''
GUI PART
'''

root=Tk()

#frame setup
root.title('NUMERRICAL PROJECT')
root.geometry('350x500')
root.focus_set()
topFrame=Frame(root,bg='#C2C4B9')
topFrame.pack()
bottomFrame=Frame(root,bg='#C2C4B9')
bottomFrame.pack(side='bottom')

#fonts,
helv36 = tkinter.font.Font(family='Helvetica', size=10, weight=tkinter.font.BOLD)
gar=tkinter.font.Font(family='Garamond', size=20, weight=tkinter.font.BOLD)
gar1=tkinter.font.Font(family='Garamond', size=10)
gar2=tkinter.font.Font(family='Garamond', size=8, weight=tkinter.font.BOLD)

#images
img = PhotoImage(file=" ")  #add button image path


#elements
root.configure(background='#C2C4B9')

label=Label(topFrame,text='NUMERICAL\nWEATHER PREDICTOR',font=gar,fg= "#2D42AE",bg='#C2C4B9')
label1=Label(bottomFrame,text="Made by RAKESH SEAL",font=gar1,bg='#C2C4B9')
label2=Label(bottomFrame,text='SELECT DATE FOR GETTING PREVIOUS DATA',font=gar2,bg='#C2C4B9')

button1=Button(topFrame,image=img,text="TEMPERATURE\nGRAPH",command=interpcurve,compound=CENTER)
button1.config( height = '60', width = '120',font=helv36,borderwidth='5')

button4=Button(root,text="TOMORROWS \n HUMIDITY",image=img,compound=CENTER,command=tomhum)
button4.config( height = '60', width = '120',font=helv36,borderwidth='5')

button5=Button(root,text="HUMIDITY\n GPH ",image=img,compound=CENTER,command=humcurve)
button5.config( height = '60', width = '120',font=helv36,borderwidth='5')

button2=Button(topFrame,image=img,text=" TOMMORROWS \nTEMPRETURE",command=tomtemp,compound=CENTER)
button2.config( height = '60', width = '120',font=helv36,borderwidth='5.5')


sp=Spinbox(bottomFrame,from_=0,to=10)
sp.config(width='40',borderwidth='5')

#function for previous datas
def spn():
    spl = UnivariateSpline(x,y)
    spl1=UnivariateSpline(x,z)
    a=sp.get()
    if ((float(a)<=10.0) and (float(a)>=0)):
     b=(spl((10.0)*float(a)))
     c=(spl1((10.0)*float(a)))
     messagebox.showinfo("PAST DATA", "\tRequested  "+str(a)+"\n"+"--------------------------------"+"\n"+"Temperature:"+str(np.round(b,2))+"ºC"+"\n\n"+"Huidity:  "+str(np.round(c,2)))+'%%'
    else:
        messagebox.showinfo("PAST DATA","       INVALID REQUEST")

   
    
   

button3=Button(bottomFrame,text='get previous\ndata',fg='#121C09',font=helv36,borderwidth='5.5',command=spn)

#final packing
button4.place(rely=0.6,relx=0.464, x=0, y=0, anchor=SE)
button5.place(rely=0.6,relx=0.927, x=0, y=0,anchor=SE)

label2.pack(side='top')
label1.pack(side='bottom')
label.pack(side='top')
button1.pack(side='right',padx='10',pady='50')
button2.pack(side='left',padx='10',pady='50')
button3.pack(side='bottom',pady='15')
sp.pack(pady='5',side='bottom')



root.mainloop()

