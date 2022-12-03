from tkinter import *
#from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time 

root=Tk()
root.geometry("600x450")
image1 = ImageTk.PhotoImage(Image.open("india.jpg"))
image2 = ImageTk.PhotoImage(Image.open("usa.jpg"))
image3 = ImageTk.PhotoImage(Image.open("austrailia.jpg"))
image4 = ImageTk.PhotoImage(Image.open("japan.jpg"))

india_label = Label(root,text="India")
india_label.place(relx=0.2,rely=0.05, anchor = CENTER)

india_clock=Label(root)
#india_clock["image"]=clock_image
india_clock.place(relx=0.2,rely=0.35, anchor = CENTER)


india_time = Label(root)
india_time.place(relx=0.2,rely=0.65, anchor = CENTER)

usa_label = Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.05,anchor = CENTER)

usa_clock=Label(root)
#usa_clock["image"]=clock_image
usa_clock.place(relx=0.7,rely=0.35, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx=0.7,rely=0.65, anchor = CENTER)

australia_label = Label(root, text="australia")
australia_label.place(relx=0.25, rely=0.53, anchor=CENTER)

australia_clock = Label(root)
australia_clock['image'] = image3
australia_clock.place(relx=0.25, rely=0.93, anchor=CENTER)

australia_time = Label(root, bg="green")
australia_time.place(relx=0.25, rely=0.93, anchor=CENTER)

japan_label = Label(root, text="japan")
japan_label.place(relx=0.75, rely=0.53, anchor=CENTER)

japan_clock = Label(root)
japan_clock['image'] = image4
japan_clock.place(relx=0.75, rely=0.73, anchor=CENTER)

japan_time = Label(root, bg="purple")
japan_time.place(relx=0.75, rely=0.93, anchor=CENTER)


class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time :"+ current_time
        usa_time.after(200,self.times)
class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        australia_time["text"]="Time :"+ current_time
        australia_time.after(200,self.times)
class Japan():
    def times(self):
        home=pytz.timezone('Asia/Tokyo')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        japan_time["text"]="Time :"+ current_time
        japan_time.after(200,self.times)

obj_india=India()
obj_usa=USA()
obj_australia = Australia()
obj_japan = Japan()

india_btn=Button(root,text="Show Time",command=obj_india.times)
india_btn.place(relx=0.2,rely=0.8, anchor = CENTER)
usa_btn=Button(root,text="Show Time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8, anchor = CENTER)
australia_btn=Button(root,text="Show Time",command=obj_australia.times)
australia_btn.place(relx=0.7,rely=0.95, anchor = CENTER)
japan_btn=Button(root,text="Show Time",command=obj_japan.times)
japan_btn.place(relx=0.75,rely=0.95, anchor = CENTER)

root.mainloop()
