from tkinter import *
#from tkinter.colorchooser import askcolor

tk=Tk()
canvas=Canvas(tk,width=500,height=500)
tk.title("Doraemon")
#D=askcolor()
#M=askcolor()

canvas.create_oval(250,350,195,420,fill='#57dfea')#legL
canvas.create_oval(245,350,300,420,fill='#57dfea')#legR
canvas.create_oval(245,398,185,430,fill='white')#footL
canvas.create_oval(247,398,310,430,fill='white')#footR

canvas.create_oval(150,50,350,250,fill='#57dfea')
canvas.create_arc(247, 245, 347, 350,start=260,extent=230,fill='#57dfea')#arm
canvas.create_arc(150, 245, 250, 350,start=25,extent=230,fill='#57dfea')#arm


canvas.create_oval(165,230,335,400,fill='#57dfea')


canvas.create_oval(180,250,320,399,fill='white')

canvas.create_oval(315,282,365,335,fill='white')#hand

canvas.create_oval(135,282,188,338,fill='white')#hand



canvas.create_arc(194, 240, 306, 360,start=180,extent=180,fill="white")
canvas.create_oval(160,90,340,250,fill="white")
canvas.create_oval(200,55,250,110,fill="white")
canvas.create_oval(250,55,300,110,fill="white")
canvas.create_oval(220,55,240,80,fill="black")
canvas.create_oval(260,55,280,80,fill="black")
canvas.create_oval(240,90,260,110,fill="red")
canvas.create_oval(250,90,255,95,fill="white")
canvas.create_rectangle(250,110,250,170)
canvas.create_arc(180, 80, 320, 220,start=180,extent=180,fill='#ea7500')
canvas.create_line(220,125,190,110)
canvas.create_line(220,130,180,120)
canvas.create_line(220,135,170,130)
canvas.create_line(280,125,310,110)
canvas.create_line(280,130,320,120)
canvas.create_line(280,135,330,130)
canvas.create_oval(300,180,200,210,fill="red")

canvas.create_oval(202,248,298,238,fill="red")
canvas.create_oval(240,260,260,240,fill="yellow")
canvas.create_line(242,245,258,245)
canvas.create_line(240,247,260,247)
canvas.create_oval(248,252,252,247,fill="black")
canvas.create_line(250,247,250,260)




#canvas.create_oval(293,237,320,270,fill='#57dfea')

#canvas.create_oval(300,239,330,280,fill='#57dfea')

#canvas.create_oval(310,250,340,300,fill='#57dfea')



#print(D,M)
canvas.pack()
mainloop()

