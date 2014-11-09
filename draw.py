# -*- coding: utf-8 -*-
#import time
from math import *
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFont
from Object import Object

step=0.0005

sleep_time = 1.0/24

screen_size_x=1600
screen_size_y=900

image1 = "ball.png"

distance=1000

o1 = (70.0,70.0,70.0)
o2 = (-70.0,-70.0,-70.0)
o3 = (70.0,0.0,-70.0)


arc1=pi/8
arc2=pi/8

lines=[]

sarc1=sin(arc1)
carc1=cos(arc1)

sarc2=sin(arc2)
carc2=cos(arc2)

for i in range(-1,2):
    for j in range(-1,2):
        for k in [-1,1]:
            lines.append((300*k,300*i,300*j))
            
for i in range(-1,2):
    for j in range(-1,2):
        for k in [-1,1]:
            lines.append((300*i,300*k,300*j))
        
for i in range(-1,2):
    for j in range(-1,2):
        for k in [-1,1]:
            lines.append((300*i,300*j,300*k))
        


 

id1=0
id2=0
id3=0
 

def f3t2(x,y,z):
    
    
    
    ax=x*carc2-z*sarc2
    az=z*carc2+x*sarc2
    ay=y*carc1+az*sarc1
    tz=y*sarc1-az*carc1
    
    ax=(ax*250*log(distance))/(tz+distance)
    ay=(ay*250*log(distance))/(tz+distance)
    

    ax+=screen_size_x/2
    ay+=screen_size_y/2
   
    return ax,ay





tx=0
ty=0

def press(event):
    global tx,ty
    tx,ty=event.x,event.y

def rota(aa,dd):

    global arc2,arc1,sarc2,carc2,sarc1,carc1
    arc1+=dd/100.0
    arc2-=aa/100.0
    
    sarc1=sin(arc1)
    carc1=cos(arc1)
    
    sarc2=sin(arc2)
    carc2=cos(arc2)
    
    for i in range(0,9):
        redraw('red', i, chr(97+i)+'x')
    
    for i in range(0,9):
        redraw('blue', i+9, chr(97+i)+'y')
          
    for i in range(0,9):
        redraw('green', i+18, chr(97+i)+'z')
    
def redraw(color,index,Tag):
    canvas.delete(Tag)
    canvas.create_line(
        (f3t2(*lines[2*index]),f3t2(*lines[2*index+1])),   
        fill=color,                                  
        tag=Tag
        )
    

def motion(event):
    global tx,ty
    rota(event.x-tx,event.y-ty)
    tx,ty=event.x,event.y
     

def Row(event):
    global distance
    if event.num == 4 or event.delta == 120:
    
        if(distance>600):
            distance -= 100
    if event.num == 5 or event.delta == -120:
        if(distance<40000):
            distance += 100
            
    for i in range(0,9):
        redraw('red', i, chr(97+i)+'x')
    
    for i in range(0,9):
        redraw('blue', i+9, chr(97+i)+'y')
          
    for i in range(0,9):
        redraw('green', i+18, chr(97+i)+'z')
    


def reflesh():
    root.after(int(sleep_time*1000), reflesh)
    global ax1,ax2,ax3,ay1,ay2,ay3
    canvas.coords(id1,ax1,ay1)
    canvas.coords(id2,ax2,ay2)
    canvas.coords(id3,ax3,ay3)
  #  canvas.coords(id4,ax4,ay4)
  #  canvas.coords(id5,ax5,ay5)
  #  canvas.coords(id6,ax6,ay6)
    
  
    ax1,ay1=f3t2(object1.pos._get_x(),object1.pos._get_y(),object1.pos._get_z())
    ax2,ay2=f3t2(object2.pos._get_x(),object2.pos._get_y(),object2.pos._get_z())
    ax3,ay3=f3t2(object3.pos._get_x(),object3.pos._get_y(),object3.pos._get_z())
   # ax4,ay4=f3t2(object4.pos._get_x(),object4.pos._get_y(),object4.pos._get_z())
   # ax5,ay5=f3t2(object5.pos._get_x(),object5.pos._get_y(),object5.pos._get_z())
   # ax6,ay6=f3t2(object6.pos._get_x(),object6.pos._get_y(),object6.pos._get_z())
    
    
    
    
    i=0.0
    while(i<sleep_time):
        object1.alterspd(Objects)
        object1.move(step)
        object2.alterspd(Objects)
        object2.move(step)
        object3.alterspd(Objects)
        object3.move(step)
 #       object4.alterspd(Objects)
 #       object4.move(step)
 #       object5.alterspd(Objects)
 #       object5.move(step)
 #       object6.alterspd(Objects)
 #       object6.move(step)
        i+=step
 
    

Objects=[]
object1=Object(1,o1,(130,54,28),1.2)
object2=Object(2,o2,(-120,-24,28),1.3)
object3=Object(3,o3,(0,-24,-50),1.4)
#object4=Object(3,o4,(0,0,42),1.5)
#object5=Object(3,o5,(0,51,0),1.6)
#object6=Object(3,o6,(0,-48,0),1.7)

Objects.append(object1)
Objects.append(object2)
Objects.append(object3)
#Objects.append(object4)
#Objects.append(object5)
#Objects.append(object6)

ax1,ay1=f3t2(object1.pos._get_x(),object1.pos._get_y(),object1.pos._get_z())
ax2,ay2=f3t2(object2.pos._get_x(),object2.pos._get_y(),object2.pos._get_z())
ax3,ay3=f3t2(object3.pos._get_x(),object3.pos._get_y(),object3.pos._get_z())

root = Tk()

root.title('三体')
screen_size_x=root.winfo_screenwidth()
screen_size_y=root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(
            screen_size_x, screen_size_y))

canvas = Canvas(width=screen_size_x, height=screen_size_y, bg='black')

canvas.pack()
ft = tkFont.Font(family = 'Fixdsys',size = 20)
label = Label(canvas,text = '鼠标控制视角，滚轮控制视野',font=ft,fg='white',bg='black')
label.place(x=5,y=5)

      

root.bind("<B1-Motion>", motion)
root.bind("<ButtonPress-1>", press)
root.bind("<MouseWheel>",Row)
root.bind("<Button-4>",Row)
root.bind("<Button-5>",Row)
photo1 = ImageTk.PhotoImage(Image.open(image1).resize((24,24),Image.ANTIALIAS))


id1=canvas.create_image(f3t2(*o1), image = photo1) 
id2=canvas.create_image(f3t2(*o2), image = photo1) 
id3=canvas.create_image(f3t2(*o3), image = photo1) 
#id4=canvas.create_image(f3t2(*o4), image = photo1) 
#id5=canvas.create_image(f3t2(*o5), image = photo1) 
#id6=canvas.create_image(f3t2(*o6), image = photo1) 

for i in range(0,9):
    redraw('red', i, chr(97+i)+'x')
    
for i in range(0,9):
    redraw('blue', i+9, chr(97+i)+'y')
          
for i in range(0,9):
    redraw('green', i+18, chr(97+i)+'z')
    
root.after(int(sleep_time*1000), reflesh)



root.mainloop()
