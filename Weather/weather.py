from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geopiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,2)} °N,{round(location.longitude,2)}")
   
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)               

    #weather
    api='http://api.weatherapi.com/v1/current.json?key=03a371335425453aa2b125403231904&q={}&aqi=no'.format(city)
    json_data = requests.get(api).json()
        
    #current
    temp = json_data['current']['temp_c'] #celsius
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure_mb'] # in millibar(mb)
    wind = json_data['current']['wind_kph'] #kph
    Description = (json_data['current']['condition']['text'])
    
    t.config(text=(temp,"°C"))
    (t.place(x=50,y=380))
    h.config(text=(humidity,"%"))
    (h.place(x=230,y=380))
    p.config(text=(pressure,"mb"))
    (p.place(x=370,y=380))
    w.config(text=(wind,"kph"))
    (w.place(x=510,y=380))
    d.config(text=Description)
    (d.place(x=700,y=380))

  
##icon
image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)


#label
label1=Label(root,text="Temperature",font=('Helvetica',18),fg="white",bg="#203243")
label1.place(x=50,y=250)

label2=Label(root,text="Humidity",font=('Helvetica',18),fg="white",bg="#203243")
label2.place(x=230,y=250)

label3=Label(root,text="Pressure",font=('Helvetica',18),fg="white",bg="#203243")
label3.place(x=370,y=250)

label4=Label(root,text="Wind Speed",font=('Helvetica',18),fg="white",bg="#203243")
label4.place(x=510,y=250)

label5=Label(root,text="Description",font=('Helvetica',18),fg="white",bg="#203243")
label5.place(x=700,y=250)


##Serach Box
Search_image=PhotoImage(file="images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="images/Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)


textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()


Search_icon=PhotoImage(file="images/Layer 6.png")
myimage_icon=Button(image=Search_icon,border=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

wIcon=PhotoImage(file="images/weather.png")
Label(root,image=wIcon,bg="#57adff").place(x=60,y=80)

##Bottom Box
frame=Frame(root,width=980,height=150,bg="#212120")
frame.pack(side=BOTTOM)


#clock (here we will palce time)
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)


#timzone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)


long_lat=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)


#thpwd
t=Label(root,font=("Helvetica",20),fg="white",bg="#203243")
t.place(x=150,y=120)
h=Label(root,font=("Helvetica",20),fg="white",bg="#203243")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",20),fg="white",bg="#203243")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",20),fg="white",bg="#203243")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",20),fg="white",bg="#203243")
d.place(x=150,y=200)

root.mainloop()