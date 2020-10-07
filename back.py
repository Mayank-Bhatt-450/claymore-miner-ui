import os,threading#,win32com.client
def go():
    print ('start')
    #os.system("text.txt")
    print ('end')
def start(a,b,c,d,e,f):
    s="""setx GPU_FORCE_64BIT_PTR """+str(a)+"""
setx GPU_MAX_HEAP_SIZE """+str(b)+"""
setx GPU_USE_SYNC_OBJECTS """+str(c)+"""
setx GPU_MAX_ALLOC_PERCENT """+str(d)+"""
setx GPU_SINGLE_ALLOC_PERCENT """+str(e)+"""
Edbist.exe """+f
    s1=threading.Thread(target=go)
    s1.start()
    print (s,'should open')
    '''
    a=open('bdist\Ebdist\\000.bat','w')
    a.write(s)
    a.close()
    vbs = win32com.client.Dispatch("ScriptControl")
    vbs.language = "vbscript"
    scode = """Function mul2()
    Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run chr(34) & "bdist\Ebdist\\000.bat" & Chr(34), 0b szvbv
    Set WshShell = Nothing
    End Function
    """
    vbs.addcode(scode)
    vbs.eval("mul2()")
    os.remove("bdist\Ebdist\\000.bat")
#'''


'''
import Tkinter as tk
import ttk
from Tkinter import*
'''
'''
root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

# list the options of the style
# (Argument should be an element of TScrollbar, eg. "thumb", "trough", ...)
print(style.element_options("Vertical.TScrollbar.thumb"))

# configure the style
style.configure("Vertical.TScrollbar", gripcount=0,
                background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="gray", bordercolor="blue", arrowcolor="white")

hs = ttk.Scrollbar(root, orient="vertical",)
hs.place(x=5, y=5, width=150)
hs.set(0.2,0.3)

root.mainloop()
'''
'''
class timetemp:
    def __init__(self,root,image,text,text1):
        self.root=root
        self.text=text
        self.text1=text1
        self.image=image
        self.d = (10 - len(self.text1)) / 2
        self.main()
    def textset(self,n):
        self.a.configure(text=str((" " * self.d) + str(n) + (" " * (10 - self.d-len(n)))), font=('Verdana', '10'))
        #self.a1.configure(text=str((" "*self.d)+str(n)+(" "*(10-self.d))), font=('Verdana', '10'))

        #self.a1.place(x=3, y=23)

    def main(self):
        self.a2 = Label(self.root, image=self.image)
        self.a2.place(x=0, y=0)
        self.a = Label(self.root, width=12,text=self.text,font=('Verdana', '10'),bg='#d0e429')
        self.a.place(x=0, y=0)
        print len((" " * self.d) + str(self.text1) + (" " * (10 - self.d))),'-'
        self.a1 = Label(self.root, width=11,text=self.text1, font=('Verdana', '10'),bg='white')
        self.a1.place(x=3, y=23)




gs=2#gapsize
bx,by=5,5
ex,ey=10,5
ecolor='#F0F0F0'
bfont='Verdana'
bsize='10'
bfontanchor='w'
import time,Tkinter,ImageTk
'''
'''
class meter:
    def __init__(self,root,image,x,y,n=0,total=100,color='#d0e429',text='',text1='',q='%'):
        self.q=q
        self.x=x
        self.y=y
        self.root=root
        self.photoimage=image
        self.n=n
        self.k=total
        self.color=color
        self.text=text
        self.text1 = text1
        self.mainn()
    def per(self,n):
        if n!=self.k:
            #print (360.0 * n / self.k)
            self.c.itemconfig(self.a, start=180, extent=-(360.0 * n / self.k))
            self.lable.configure(text=str((100*n/self.k)).zfill(2) + self.q, font=('Impact', '24'))
            self.lable.place(x=self.x + 31, y=self.y + 29)
        else:
            self.c.lower(self.c.create_oval((2, 2, 121, 121), fill=self.color, outline=self.color))#self.f).lift()
            self.lable.configure(text=str(100)+self.q,font=('Impact', '24'))
            self.place(x=self.x + 29, y=self.y + 30)

    def mainn(self):
        self.c = Canvas(self.root,width=124, height=124)
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((2, 2, 121, 121), fill=self.color, outline=self.color, start=180, extent=-(360.0 * self.n / self.k))
        self.c.create_image(62, 62, image=self.photoimage)
        self.c.lower(self)
        self.lable1 = Label(self.root, text=self.text, font=('Verdana', '11'), bg='white')
        self.lable1.place(x=self.x + 26, y=self.y + 68)
        self.lable2 = Label(self.root, text=self.text1, font=('Verdana', '10'), bg='white')
        self.lable2.place(x=self.x + 50, y=self.y + 86)
        self.lable = Label(self.root, text=str(100*self.n/self.k)+self.q, font=('Impact', '24'), fg='#d0e429', bg='white')#Consolas'
        self.lable.place(x=self.x + 31, y=self.y + 29)
'''
#"""
class pi:
    def __init__(self,root,r,a,x,y,image):
        self.image=image
        self.root=root
        self.r=r
        self.a=a
        self.x=x
        self.y=y
        self.main()
    def pro(self,r= None,a=None):
        if r!=None:
            self.r=r
        else:
            pass
        if a!=None:
            self.a=a
        self.total=self.r+self.a
        self.c.itemconfig(self.d, start=180, extent=-(360.0 * self.a / self.total))


    def main(self):
        self.c = Canvas(self.root, width=124, height=124)
        self.c.place(x=self.x, y=self.y)
        self.c.create_oval((2, 2, 121, 121), fill='#d0e429', outline='#d0e429')
        self.d = self.c.create_arc((2, 2, 121, 121), fill='#F0F0F0', outline='#F0F0F0', start=180,extent=-0)
        self.c.create_image(62, 62, image=self.image)
#"""
"""
class meter:
    def __init__(self,root,image,x,y,n=0,text='',color='#d0e429',text1='',q='MH\\s'):
        self.q=q
        self.x=x
        self.y=y
        self.root=root
        self.photoimage=image
        self.n=n
        self.color=color
        self.text=text
        self.text1 = text1
        self.mainn()
    def per(self,n):
        if n!=1000:
            self.c.itemconfig(self.a, start=210, extent=-(240.0 * n / 1000))
            self.lable.configure(text=str((100*n/self.k)).zfill(2) + self.q, font=('Impact', '24'))
            self.lable.place(x=self.x + 31, y=self.y + 29)
        else:
            pass

    def mainn(self):
        self.c = Canvas(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='blue')
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((0, 0, 120, 120), fill=self.color, outline=self.color, start=210, extent=-(240.0 * self.n / 1000))

        self.c.create_arc((0, 0, 120, 120), fill='white', outline='white', start=210,extent=120.0)
        self.c.create_image(60, 60, image=self.photoimage)
        self.c.lower(self.a)
        self.lable = Label(self.root, text=str((240.0 * self.n / 1000)+760), font=('Verdana', '16'), fg=self.color,bg='white')
        self.lable.place(x=self.x + 21, y=self.y + 48)
        self.lable1 = Label(self.root, text=self.q, font=('Verdana', '13'), bg='white')
        self.lable1.place(x=self.x + 36, y=self.y + 80)
        self.lable2 = Label(self.root, text=self.text1, font=('Verdana', '13','bold'), bg='white',fg='#F0F0F0')
        self.lable2.place(x=self.x + 30, y=self.y + 27)
#"""
class timetemp1:
    def __init__(self,root,x,y,image,text,text1):
        self.root=root
        self.x=x
        self.y=y
        self.text=text
        self.text1=text1
        self.image=image
        self.d = (10 - len(self.text1)) / 2
        self.main()
    def textset(self,n):
        self.a.configure(text=str((" " * self.d) + str(n) + (" " * (10 - self.d-len(n)))), font=('Verdana', '10'))
        #self.a1.configure(text=str((" "*self.d)+str(n)+(" "*(10-self.d))), font=('Verdana', '10'))

        #self.a1.place(x=3, y=23)

    def main(self):
        self.a2 = Label(self.root, image=self.image)
        self.a2.place(x=self.x, y=self.y)
        self.a = Label(self.root, width=12,text=self.text,font=('Verdana', '10'),bg='#d0e429')
        self.a.place(x=self.x, y=self.y)
        print (len((" " * self.d) + str(self.text1) + (" " * (10 - self.d))),'-')
        self.a1 = Label(self.root, width=11,text=self.text1, font=('Verdana', '10'),bg='white')
        self.a1.place(x=self.x+3, y=self.y+23)
class meter1:
    def __init__(self,root,image,x,y,p='1',gr=0,gc=0,n=0,text='',color='#d0e429',text1='',q='MH\\s'):

        self.p=p
        self.q=q
        self.x=x
        self.y=y
        self.gr=gr
        self.gc=gc
        self.root=root
        self.photoimage=image
        self.n=n
        self.color=color
        self.text=text
        self.text1 = text1
        self.mainn()
    def per(self,n):
        if n!=1000:
            self.c.itemconfig(self.a, start=210, extent=-(240.0 * n / 1000))
            self.lable.configure(text=str((100*n/self.k)).zfill(2) + self.q, font=('Impact', '24'))
            self.lable.place(x=self.x + 31, y=self.y + 29)
        else:
            pass

    def mainn(self):
        if self.p=='g':
            print ('in')
            self.root=Frame(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='#F0F0F0')
            self.root.grid(row=self.gr, column=self.gc, sticky=W + E + N + S)
        else:
            pass
        self.c = Canvas(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='#F0F0F0')
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((0, 0, 120, 120), fill=self.color, outline=self.color, start=210, extent=-(240.0 * self.n / 1000))

        self.c.create_arc((0, 0, 120, 120), fill='white', outline='white', start=210,extent=120.0)
        self.c.create_image(60, 60, image=self.photoimage)
        self.c.lower(self.a)
        self.lable2 = Label(self.root, text=self.text,bg='white')
        self.lable2.place(x=self.x + 19, y=self.y + 48)
        self.lable = Label(self.root,width=6, text=self.n, font=('Verdana', '16'), fg=self.color,bg='white')
        self.lable.place(x=self.x + 19, y=self.y + 48)
        self.lable1 = Label(self.root, text=self.q, font=('Verdana', '13'), bg='white')
        self.lable1.place(x=self.x + 36, y=self.y + 80)
        self.lable2 = Label(self.root, text=self.text1, font=('Verdana', '13','bold'), bg='white',fg='#F0F0F0')
        self.lable2.place(x=self.x + 30, y=self.y + 27)
class pi:
    def __init__(self,root,r,a,x,y,image):
        self.image=image
        self.root=root
        self.r=r
        self.a=a
        self.x=x
        self.y=y
        self.main()
    def pro(self,r= None,a=None):
        if r!=None:
            self.r=r
        else:
            pass
        if a!=None:
            self.a=a
        self.total=self.r+self.a
        self.c.itemconfig(self.d, start=180, extent=-(360.0 * self.a / self.total))
class meter:
    def __init__(self,root,image,x,y,p='1',gr=0,gc=0,n=0,text='',color='#d0e429',text1='',q='MH\\s'):

        self.p=p
        self.q=q
        self.x=x
        self.y=y
        self.gr=gr
        self.gc=gc
        self.root=root
        self.photoimage=image
        self.n=n
        self.color=color
        self.text=text
        self.text1 = text1
        self.mainn()
    def per(self,n):
        if n!=1000:
            self.c.itemconfig(self.a, start=210, extent=-(240.0 * n / 1000))
            self.lable.configure(text=str((100*n/self.k)).zfill(2) + self.q, font=('Impact', '24'))
            self.lable.place(x=self.x + 31, y=self.y + 29)
        else:
            pass

    def mainn(self):
        if self.p=='g':
            self.root=Frame(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='white')
            if self.gc%4==0and self.gc!=0:
                self.root.pack(side = BOTTOM)
            else:
                self.root.pack(side=LEFT)
            #self.root.grid(row=self.gr, column=self.gc,padx=0, pady=0,ipadx=0,ipady=0,sticky=E+N)#sticky="nsew")#, sticky=W + E + N + S)
            #self.root.grid_columnconfigure(1, weight=1)
        else:
            pass
        self.c = Canvas(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='#F0F0F0')
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((0, 0, 120, 120), fill=self.color, outline=self.color, start=210, extent=-(240.0 * self.n / 1000))

        self.c.create_arc((0, 0, 120, 120), fill='white', outline='white', start=210,extent=120.0)
        self.c.create_image(60, 60, image=self.photoimage)
        self.c.lower(self.a)
        self.lable2 = Label(self.root, text=self.text,bg='white')
        self.lable2.place(x=self.x + 19, y=self.y + 48)
        self.lable = Label(self.root,width=6, text=self.n, font=('Verdana', '16'), fg=self.color,bg='white')
        self.lable.place(x=self.x + 19, y=self.y + 48)
        self.lable1 = Label(self.root, text=self.q, font=('Verdana', '13'), bg='white')
        self.lable1.place(x=self.x + 36, y=self.y + 80)
        self.lable2 = Label(self.root, text=self.text1, font=('Verdana', '13','bold'), bg='white',fg='#F0F0F0')
        self.lable2.place(x=self.x + 30, y=self.y + 27)
class pidata1:
    def __init__(self,root,x,y,r=0,a=0):
        self.root=root
        self.r=r
        self.a=a
        self.x=x
        self.y=y
        self.main()
    def setpidata(self,r=0,a=0):
        self.xcolor.configure(text=a)
        self.ycolor.configure(text=r)
    def main(self):
        self.a1=Frame(self.root,height=0,width=1000,highlightthickness=0,bd=0,bg='white')
        self.a1.place(x=self.x,y=self.y)
        self.acolor=Label(self.a1,width=2,bd=0,font=('Verdana', '5'),bg='#d0e429')
        self.acolor.grid(row=0, column=0)#,sticky=W + E + N + S)
        self.a1color = Label(self.a1, width=2, bd=0, font=('Verdana', '5'), bg='#F0F0F0')
        self.a1color.grid(row=1, column=0)#,sticky=W + E + N + S)#,pady=10 )
        self.a2color = Label(self.a1,text='Accepted',font=('Verdana', '7'),bg='white',  width=8,bd=0)
        self.a2color.grid(row=0, column=1, pady=5)
        self.a12color = Label(self.a1, text='Rejected',font=('Verdana', '7'),  width=8,bd=0,bg='white')
        self.a12color.grid(row=1, column=1,pady=0, padx=7)
        self.xcolor = Label(self.a1, text='0', font=('Verdana', '7'), bd=0,fg='#F0F0F0',bg='white')
        self.xcolor.grid(row=0, column=2,ipadx=10)
        self.ycolor = Label(self.a1, text='0', font=('Verdana', '7'), width=8,bd=0,fg='#F0F0F0',bg='white')
        self.ycolor.grid(row=1, column=2,ipadx=10)
class pidata:
    def __init__(self,root,x,y,text='',r=0,a=0,r2=None,a2=None):
        self.root=root
        self.r=r
        self.a=a
        self.r2 = r2
        self.a2 = a2
        self.x=x
        self.text=text
        self.y=y
        self.main()
    def setpidata(self,r=0,a=0,r1=None,a1=None):
        self.xcolor.configure(text=a)
        self.ycolor.configure(text=r)
        if r1==None and r2==None:
            self.x1color.configure(text=a1)
            self.y1color.configure(text=r1)
    def main(self):
        self.a1=Frame(self.root,highlightthickness=0,bd=0,bg='white')
        self.a1.place(x=self.x,y=self.y)
        self.acolor=Label(self.a1,width=2,bd=0,font=('Verdana', '5'),bg='#d0e429')
        self.acolor.grid(row=0, column=0)#,sticky=W + E + N + S)
        self.a1color = Label(self.a1, width=2, bd=0, font=('Verdana', '5'), bg='#F0F0F0')
        self.a1color.grid(row=1, column=0)#,sticky=W + E + N + S)#,pady=10 )
        self.a2color = Label(self.a1,text='Accepted',font=('Verdana', '7','bold'),bg='white',  width=8,bd=0)
        self.a2color.grid(row=0, column=1, pady=5)
        self.a12color = Label(self.a1, text='Rejected',font=('Verdana', '7','bold'),  width=8,bd=0,bg='white')
        self.a12color.grid(row=1, column=1,pady=0, padx=7)
        self.xcolor = Label(self.a1, text=self.a, font=('Verdana', '7','bold'), width=9,bd=0,fg='#DBDBDB',bg='white')
        self.xcolor.grid(row=0, column=2,pady=0, padx=1)
        self.ycolor = Label(self.a1, text=self.r, font=('Verdana', '7','bold'), width=9,bd=0,fg='#DBDBDB',bg='white')
        self.ycolor.grid(row=1, column=2,pady=0, padx=1)
        print (self.r2,'=',self.a2,'f')
        if self.r2!=None or self.a2!=None:
            print ('lol')
            self.x1color = Label(self.a1, text=self.a2, font=('Verdana', '7', 'bold'),width=9, bd=0, fg='#DBDBDB', bg='white')
            self.x1color.grid(row=0, column=3,pady=0, padx=1)
            self.y1color = Label(self.a1, text=self.r2, font=('Verdana', '7', 'bold'), width=9, bd=0, fg='#DBDBDB',
                                bg='white')
            self.y1color.grid(row=1, column=3,pady=0, padx=1)


'''
root=Tk()
root.geometry('499x589+100+50')
#root.configure(background='white')
photoimage1 = ImageTk.PhotoImage(file="U.gif")
pidata(root,0,0,r=999999999,a=999999999,r2=999999999,a2=999999999)
#a=timetemp1(root,0,0,photoimage1,text='Total Time',text1='12dsf')
#a=pi(root,6,5,0,0,gc=0,gr=0,image=photoimage1)
#a.pro(a=2)
#a.pro(r=1)
#qa=meter(root,image=photoimage1,x=0,y=0,n=100,total=200,text='GPU FAN')
'''
'''
#b=meter(root,photoimage1,00,0,1000,p='g',gc=0,gr=0,text='100',text1='GPU 1')

#print type(b.a),b.a
#b.c.itemconfig(b.a, start=180, extent = 9)
#a.per(100)

root.mainloop()
#'''
#'''
'''
def prop(n):
    return 360.0 * n / 1000
i=0
def sett(event):
    global i,c
    time.sleep(0.3)
    c.itemconfig(a, start=180, extent = -i)
    i+=1
    print i

c = Tkinter.Canvas(width=124, height=124)
c.pack()
c.bind('<Motion>',sett)
a=c.create_arc((2,2,121,121), fill="#FAF402", outline="#FAF402", start=180, extent = -1)
photoimage = ImageTk.PhotoImage(file="U.gif")
c.create_image(62, 62, image=photoimage)
def sett():
    time.sleep(0.3)
    c.itemconfig(a, start=prop(340+i), extent = prop(360+i))

#canvas.coords(item,0,0,100,100)
#c.create_arc((2,2,152,152), fill="#00AC36", outline="#00AC36", start=prop(200), extent = prop(400))
#c.create_arc((2,2,152,152), fill="#7A0871", outline="#7A0871", start=prop(600), extent = prop(50))
#c.create_arc((2,2,152,152), fill="#E00022", outline="#E00022", start=prop(650), extent = prop(200))
#c.create_arc((2,2,152,152), fill="#294994", outline="#294994",  start=prop(850), extent = prop(150))
root.mainloop()
'''
'''
import Tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()#                 x1   y x  y1
s=120
x,y=100,100
item = canvas.create_rectangle(s+x, y,x,s+y, fill="blue")

def callback():#       x y  x1 y1
    canvas.coords(item,0,0,100,100)
    canvas.itemconfig(item,fill='red')
    #.itemconfigure("highlight", state='hidden')

button = tk.Button(root,text='Push me!',command=callback)
button.pack()


root.mainloop()'''
"""args = {'name': u'Rose Perrone', 'ipAddress': '127.0.0.1', 'email': u'hi@gmail.com'}
class MyClass:
    def __init__(self,
                 name,
                 ipAddress,
                 password=None,
                 email=None,
                 deleted=None,
                 includePromoted=None,
                 explicit=None):
                pass

MyClass(**args)
# <__main__.MyClass instance at blah>#"""
cn=['Pool Name', 'Wallet Address', 'Password', 'Worker', 'Ethereum Stratum mode', 'Ethereum algorithm mode', 'Enables Assembler(asm)', 'Ethereum intensity', 'Eres', 'All Pools', 'All Coins', 'Ethereum Time', 'GPU indexes', 'GPU Serializability', 'Failover Time', 'Fan Min', 'Mode', 'Fan Max', 'Restart Miner', 'No Fee', 'low intensity mode', 'low intensity(DAG)', 'Watch Dog', 'Minimal Speed', 'Retry Delay', 'Job Timeout', 'target GPU temperature', 'Auto Intensity', 'Temprature Stop', 'Ethereum hashrate', 'Ethereum stale', 'GPU Core Clock', 'GPU Memory Clock', 'Power Limit', 'GPU Core Voltage', 'GPU Memory Voltage', 'Alt GPU Index', 'Platform']
ch=['\tEthereum pool address. Only Stratum protocol is supported for pools. Miner supports all pools that are compatible with Dwarfpool proxy and accept Ethereum wallet address directly.\n\tFor solo mining, specify "http://" before address, note that this mode is not intended for proxy or HTTP pools, also "-allpools 1" will be set automatically in this mode.\n\tNote: The miner supports all Stratum versions for Ethereum, HTTP mode is necessary for solo mining only.\n\tUsing any proxies will reduce effective hashrate by at least 1%, so connect miner to Stratum pools directly. Using HTTP pools will reduce effective hashrate by at least 5%.\n ', 'Your Ethereum wallet address. Also worker name and other options if pool supports it.\n\tPools that require "Login.Worker" instead of wallet address are not supported directly currently, but you can use "allpools 1" option to mine there.\n ', 'Password for Ethereum pool, use "x" as password.\n ', 'Worker name, it is required for some pools.\n ', 'Ethereum Stratum mode. 0 - eth-proxy mode (for example, dwarpool.com), 1 - qtminer mode (for example, ethpool.org),\n\t2 - miner-proxy mode (for example, coinotron.com), 3 - nicehash mode. 0 is default.\n', 'Ethereum algorithm mode for AMD cards. 0 - optimized for fast cards, 1 - optimized for slow cards, 2 - for gpu-pro Linux drivers. -1 - autodetect (default, automatically selects between 0 and 1).\n\tYou can also set this option for every card individually, for example "0,1,0".\n ', '(AMD cards only) enables assembler GPU kernels. In this mode some tuning is required even in ETH-only mode,\n\tCurrently ETH-LBRY mode is not supported in assembler.\n\tSpecify "-asm 0" to disable this option. You can also specify values for every card, for example "0,1,0". Default value is "1".\n\tIf ASM mode is enabled, miner must show "GPU #x: algorithm ASM" at startup.\n\tCheck "FINE-TUNING" section below for additional notes.\n\tNEW: added alternative assembler kernels for Tonga and Polaris cards for ETH-only mode.(i.e. you cannot find speed peak), use "2" option to enable this mode.\n ', 'Ethereum intensity. Default value is 8, you can decrease this value if you don\'t want Windows to freeze or if you have problems with stability. The most low GPU load is "0".\n\tnow can set intensity for every card individually, for example "1,8,6".\n\tYou can also specify negative values, for example, "-8192", it exactly means "global work size" parameter which is used in official miner.\n ', 'this setting is related to Ethereum mining stability. Every next Ethereum epoch requires a bit more GPU memory, miner can crash during reallocating GPU buffer for new DAG.\n\tTo avoid it, miner reserves a bit larger GPU buffer at startup, so it can process several epochs without buffer reallocation.\n\tThis setting defines how many epochs miner must foresee when it reserves GPU buffer, i.e. how many epochs will be processed without buffer reallocation. Default value is 2.\n ', 'Specify "1" if miner does not want to mine on specified pool (because it cannot mine devfee on that pool), but you agree to use some default pools for devfee mining.\n\tNote that if devfee mining pools will stop, entire mining will be stopped too.\n ', 'Specify "1" to be able to mine Ethereum forks, in this mode miner will use some default pools for devfee Ethereum mining.\n\tNote that if devfee mining pools will stop, entire mining will be stopped too.\n\tMiner has to use two DAGs in this mode - one for Ethereum and one for Ethereum fork, it can cause crashes because DAGs have different sizes.\n\tTherefore for this mode it is recommended to specify current Ethereum epoch (or a bit larger value),\n\tfor example, "47" means that miner will expect DAG size for epoch #47 and will allocate appropriate GPU buffer at starting, instead of reallocating bigger GPU buffer (may crash) when it starts devfee mining.\n\tAnother option is to specify "-1", in this mode miner will start devfee round immediately after start and therefore will get current epoch for Ethereum, after that it will be able to mine Ethereum fork.\n\tIf you mine Expanse, the best way is to specify "exp", in this mode devfee mining will be on Expanse too and DAG won\'t be recreated at all.\n\tIf you mine ETC on some pool that does not accept wallet address but requires Username.Worker instead, the best way is to specify "etc", in this mode devfee mining will be on ETC pools and DAG won\'t be recreated at all.\n ', 'Time period between Ethereum HTTP requests for new job in solo mode, in milliseconds. Default value is 200ms.\n ', 'GPU indexes, default is all available GPUs. For example, if you have four GPUs "02" will enable only first and third GPUs (#0 and #2).\n\tYou can also turn on/off cards in runtime with "0"..."9" keys and check current statistics with "s" key.\n\tFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ', 'this setting can improve stability on multi-GPU systems if miner hangs during startup. It serializes GPUs initalization routines. Use "1" to serailize some of routines and "2" to serialize all routines.\n\tDefault value is "0" (no serialization, fast initialization).\n ', 'failover main pool switch time, in minutes, see "Failover" section below. Default value is 30 minutes, set zero if there is no main pool.\n ', 'set minimal fan speed, in percents, for example, "50" will set minimal fans speed to 50%. You can also specify values for every card, for example "50,60,70".\n\tThis option works only if miner manages cooling, i.e. when "-tt" option is used to specify target temperature. Default value is "0".\n\tNote: for NVIDIA cards this option is not supported.\n ', 'Select mining mode:\n\t"0" (default) means dual Ethereum + Decred/Siacoin/Lbry mining mode.\n\t"1" means Ethereum-only mining mode. You can set this mode for every card individually, for example, "1-02" will set mode "1" for first and third GPUs (#0 and #2).\n\tFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ', 'set maximal fan speed, in percents, for example, "80" will set maximal fans speed to 80%. You can also specify values for every card, for example "-fanmax 50,60,70".\n\tThis option works only if miner manages cooling, i.e. when "target GPU temperature" option is used to specify target temperature. Default value is "100".\n\tNote: for NVIDIA cards this option is not supported.\n ', 'Restart miner mode. "0" (default) - restart miner if something wrong with GPU. "-1" - disable automatic restarting. restart >20 - restart miner if something\n\twrong with GPU or by timer. For example, "60" - restart miner every hour or when some GPU failed.\n\t"1" closes miner and execute "reboot.bat" file ("reboot.bash" or "reboot.sh" for Linux version) in the miner directory (if exists) if some GPU failed.\n\tSo you can create "reboot.bat" file and perform some actions, for example, reboot system if you put this line there: "shutdown /r /t 5 /f".\n ', 'set "1" to cancel my developer fee at all. In this mode some optimizations are disabled so mining speed will be slower by about 4%.\n\tBy enabling this mode, I will lose 100% of my earnings, you will lose only 2-3% of your earnings.\n\tSo you have a choice: "fastest miner" or "completely free miner but a bit slower".\n\tIf you want both "fastest" and "completely free" you should find some other miner that meets your requirements, just don\'t use this miner instead of claiming that I need\n\tto cancel/reduce developer fee, saying that 1-2% developer fee is too much for this miner and so on.\n ', 'low intensity mode. Reduces mining intensity, useful if your cards are overheated. Note that mining speed is reduced too.\n\tMore value means less heat and mining speed, for example, "10" is less heat and mining speed than "1". You can also specify values for every card, for example "3,10,50".\n\tDefault value is "0" - no low intensity mode.\n ', 'low intensity mode for DAG generation, it can help with OC or weak PSU. Supported values are 0, 1, 2, 3, more value means lower intensity. Example: "1".\n\tYou can also specify values for every card, for example "1,0,3". Default value is "0" (no low intensity for DAG generation).\n ', 'watchdog option. Default value is "1", it enables watchdog, miner will be closed (or restarted, see "restart" option) if any thread is not responding for 1 minute or OpenCL call failed.\n\tSpecify "0" to disable watchdog.\n ', 'minimal speed for ETH, in MH/s. If miner cannot reach this speed for 5 minutes for any reason, miner will be restarted (or "reboot.bat" will be executed if "reastart 1" is set). Default value is 0 (feature disabled).\n ', 'delay, in seconds, between connection attempts. Default values is "20". Specify "-1" if you don\'t need reconnection, in this mode miner will exit if connection is lost.\n ', 'job timeout for ETH, in minutes. If miner does not get new jobs for this time, it will disconnect from pool. Default value is 10.\n ', 'set target GPU temperature. For example, "80" means 80C temperature. You can also specify values for every card, for example "70,80,75".\n\tYou can also set static fan speed if you specify negative values, for example "-50" sets 50% fan speed. Specify zero to disable control and hide GPU statistics.\n\t"1" (default) does not manage fans but shows GPU temperature and fan status every 30 seconds. Specify values 2..5 if it is too often.\n\tNote: for NVIDIA cards only temperature monitoring is supported, temperature management is not supported.\n\tNote: for Linux gpu-pro drivers, miner must have root access to manage fans, otherwise only monitoring will be available.\n ', 'reduce entire mining intensity (for all coins) automatically if GPU temperature is above specified value. For example, "80" reduces mining intensity if GPU temperature is above 80C.\n\tYou can see if intensity was reduced in detailed statistics ("s" key).\n\tYou can also specify values for every card, for example "80,85,80". You also should specify non-zero value for "target GPU temperature" option to enable this option.\n\tIt is a good idea to set "-ttli" value higher than "-tt" value by 3-5C.\n ', 'set stop GPU temperature, miner will stop mining if GPU reaches specified temperature. For example, "-tstop 95" means 95C temperature. You can also specify values for every card, for example "-tstop 95,85,90".\n\tThis feature is disabled by default ("0"). You also should specify non-zero value for "target GPU temperature" option to enable this option.\n\tIf it turned off wrong card, it will close miner in 30 seconds.\n\tYou can also specify negative value to close miner immediately instead of stopping GPU, for example, "-95" will close miner as soon as any GPU reach 95C temperature.\n ', 'send Ethereum hashrate to pool. Default value is "1", set "0" if you don\'t want to send hashrate.\n ', 'send Ethereum stale shares to pool, it can increase effective hashrate a bit. Default value is "1", set "0" if you don\'t want to send stale shares.\n ', 'set target GPU core clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1000,1050,1100,0".\n\tNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\n\tNote: this option changes clocks for all power states, so check voltage for all power states in WattMan or use -cvddc option.\n\tBy default, low power states have low voltage, setting high GPU clock for low power states without increasing voltage can cause driver crash.\n\tNote: for NVIDIA cards this option is not supported.\n ', 'set target GPU memory clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1200,1250,1200,0".\n\tNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\n\tNote: for NVIDIA cards this option is not supported.\n\n ', 'set power limit, from -50 to 50. If not specified, miner will not change power limit. You can also specify values for every card, for example "20,-20,0,10".\n\tNote: for NVIDIA cards this option is not supported.\n ', 'set target GPU core voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\n\tNote: for NVIDIA cards this option is not supported.\n\n ', 'set target GPU memory voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\n\tNote: for NVIDIA cards this option is not supported.\n ', 'alternative GPU indexing. This option does not change GPU order, but just changes GPU indexes that miner displays, it can be useful in some cases. Possible values are:\n\t0: default GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU1".\n\t1: same as "0", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU2".\n\t2: alternative GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU5".\n\t3: same as "2", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU6".\n\tDefault value is "0".\n ', 'selects GPUs manufacturer. 1 - use AMD GPUs only. 2 - use NVIDIA GPUs only. 3 - use both AMD and NVIDIA GPUs. Default value is "3".\n ']
cc=['-epool', '-ewal', '-epsw', '-eworker', '-esm', '-etha', '-asm', '-ethi', '-eres', '-allpools', '-allcoins', '-etht', '-di', '-gser', '-ftime', '-fanmin', '-mode', '-fanmax', '-r', '-nofee', '-li', '-lidag', '-wd', '-minspeed', '-retrydelay', '-ejobtimeout', '-tt', '-ttli', '-tstop', '-erate', '-estale', '-cclock', '-mclock', '-powlim', '-cvddc', '-mvddc', '-altnum', '-platform']

cn.insert(0,'Pool Name')
ch.insert(0,"""Decred/Siacoin/Lbry/Pascal pool address. Use "http://" prefix for HTTP pools, "stratum+tcp://" for Stratum pools. If prefix is missed, Stratum is assumed.\nDecred: both Stratum and HTTP are supported. Siacoin: both Stratum and HTTP are supported, though note that not all Stratum versions are supported currently. Lbry: only Stratum is supported.""")
cc.insert(0,'-dpool')

cn.insert(1,'Wallet Address')
ch.insert(1,"""Your Decred/Siacoin/Lbry/Pascal wallet address or worker name, it depends on pool.""")
cc.insert(1,'-dwal')

cn.insert(2,'Password')
ch.insert(2,"""Password for Decred/Siacoin/Lbry/Pascal pool""")
cc.insert(2,'-dpsw')

cn.insert(7,'Intensity')
ch.insert(7,"""Decred/Siacoin/Lbry/Pascal intensity, or Ethereum fine-tuning value in ETH-only ASM mode. Default value is 30, you can adjust this value to get the best Decred/Siacoin/Lbry mining speed without reducing Ethereum mining speed.\nYou can also specify values for every card, for example "30,100,50".\nYou can change the intensity in runtime with "+" and "-" keys and check current statistics with "s" key.\nFor example, by default (30) 390 card shows 29MH/s for Ethereum and 440MH/s for Decred. Setting 70 causes 24MH/s for Ethereum and 850MH/s for Decred.""")
cc.insert(7,'-dcri')

cn.insert(8,'Second Coin Time Period')
ch.insert(8,"""Time period between Decred/Siacoin HTTP requests for new job, in seconds. Default value is 5 seconds.""")
cc.insert(8,'-dcrt')

cn.insert(15,'Second Autointensity')
ch.insert(15,"""reduce Decred/Siacoin/Lbry/Pascal intensity automatically if GPU temperature is above specified value. For example, "80" reduces Decred intensity if GPU temperature is above 80C. \nYou can see current Decred intensity coefficients in detailed statistics ("s" key). So if you set "-dcri 50" but Decred/Siacoin intensity coefficient is 20% it means that GPU currently mines Decred/Siacoin at "10".\nYou can also specify values for every card, for example "80,85,80". You also should specify non-zero value for  option to enable this option.\nIt is a good idea to set value higher than value by 3-5C.""")
cc.insert(15,'-ttdcr')

cn.insert(18,'Second Coin Timeout')
ch.insert(18,"""job timeout for second coin in dual mode, in minutes. If miner does not get new jobs for this time, it will disconnect from pool. Default value is 30.""")
cc.insert(18,'-djobtimeout')


#print len(ch)
