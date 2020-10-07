from  tkinter import*
import back,os
from threading import Thread,Event,active_count,enumerate
from PIL import ImageTk
import time#ImageTk,time
from multiprocessing import Process
import psutil
import urllib.request
from math import ceil

cn=['Pool Name*', 'Wallet Address*', 'Password*', 'Worker', 'Ethereum Stratum mode', 'Ethereum algorithm mode', 'Enables Assembler(asm)', 'Ethereum intensity', 'Eres', 'All Pools', 'All Coins', 'Ethereum Time', 'GPU indexes', 'GPU Serializability', 'Failover Time', 'Fan Min', 'Mode', 'Fan Max', 'Restart Miner', 'No Fee', 'low intensity mode', 'low intensity(DAG)', 'Watch Dog', 'Minimal Speed', 'Retry Delay', 'Job Timeout', 'target GPU temperature', 'Auto Intensity', 'Temprature Stop', 'Ethereum hashrate', 'Ethereum stale', 'GPU Core Clock', 'GPU Memory Clock', 'Power Limit', 'GPU Core Voltage', 'GPU Memory Voltage', 'Alt GPU Index', 'Platform']
ch=['Ethereum pool address. Only Stratum protocol is supported for pools. Miner supports all pools that are compatible with Dwarfpool proxy and accept Ethereum wallet address directly.\nFor solo mining, specify "http://" before address, note that this mode is not intended for proxy or HTTP pools, also "-allpools 1" will be set automatically in this mode.\nNote: The miner supports all Stratum versions for Ethereum, HTTP mode is necessary for solo mining only.\nUsing any proxies will reduce effective hashrate by at least 1%, so connect miner to Stratum pools directly. Using HTTP pools will reduce effective hashrate by at least 5%.\n ', 'Your Ethereum wallet address. Also worker name and other options if pool supports it.\nPools that require "Login.Worker" instead of wallet address are not supported directly currently, but you can use "allpools 1" option to mine there.\n ', 'Password for Ethereum pool, use "x" as password.\n ', 'Worker name, it is required for some pools.\n ', 'Ethereum Stratum mode. 0 - eth-proxy mode (for example, dwarpool.com), 1 - qtminer mode (for example, ethpool.org),\n2 - miner-proxy mode (for example, coinotron.com), 3 - nicehash mode. 0 is default.\n', 'Ethereum algorithm mode for AMD cards. 0 - optimized for fast cards, 1 - optimized for slow cards, 2 - for gpu-pro Linux drivers. -1 - autodetect (default, automatically selects between 0 and 1).\nYou can also set this option for every card individually, for example "0,1,0".\n ', '(AMD cards only) enables assembler GPU kernels. In this mode some tuning is required even in ETH-only mode,\nCurrently ETH-LBRY mode is not supported in assembler.\nSpecify "-asm 0" to disable this option. You can also specify values for every card, for example "0,1,0". Default value is "1".\nIf ASM mode is enabled, miner must show "GPU #x: algorithm ASM" at startup.\nCheck "FINE-TUNING" section below for additional notes.\nNEW: added alternative assembler kernels for Tonga and Polaris cards for ETH-only mode.(i.e. you cannot find speed peak), use "2" option to enable this mode.\n ', 'Ethereum intensity. Default value is 8, you can decrease this value if you don\'t want Windows to freeze or if you have problems with stability. The most low GPU load is "0".\nnow can set intensity for every card individually, for example "1,8,6".\nYou can also specify negative values, for example, "-8192", it exactly means "global work size" parameter which is used in official miner.\n ', 'this setting is related to Ethereum mining stability. Every next Ethereum epoch requires a bit more GPU memory, miner can crash during reallocating GPU buffer for new DAG.\nTo avoid it, miner reserves a bit larger GPU buffer at startup, so it can process several epochs without buffer reallocation.\nThis setting defines how many epochs miner must foresee when it reserves GPU buffer, i.e. how many epochs will be processed without buffer reallocation. Default value is 2.\n ', 'Specify "1" if miner does not want to mine on specified pool (because it cannot mine devfee on that pool), but you agree to use some default pools for devfee mining.\nNote that if devfee mining pools will stop, entire mining will be stopped too.\n ', 'Specify "1" to be able to mine Ethereum forks, in this mode miner will use some default pools for devfee Ethereum mining.\nNote that if devfee mining pools will stop, entire mining will be stopped too.\nMiner has to use two DAGs in this mode - one for Ethereum and one for Ethereum fork, it can cause crashes because DAGs have different sizes.\nTherefore for this mode it is recommended to specify current Ethereum epoch (or a bit larger value),\nfor example, "47" means that miner will expect DAG size for epoch #47 and will allocate appropriate GPU buffer at starting, instead of reallocating bigger GPU buffer (may crash) when it starts devfee mining.\nAnother option is to specify "-1", in this mode miner will start devfee round immediately after start and therefore will get current epoch for Ethereum, after that it will be able to mine Ethereum fork.\nIf you mine Expanse, the best way is to specify "exp", in this mode devfee mining will be on Expanse too and DAG won\'t be recreated at all.\nIf you mine ETC on some pool that does not accept wallet address but requires Username.Worker instead, the best way is to specify "etc", in this mode devfee mining will be on ETC pools and DAG won\'t be recreated at all.\n ', 'Time period between Ethereum HTTP requests for new job in solo mode, in milliseconds. Default value is 200ms.\n ', 'GPU indexes, default is all available GPUs. For example, if you have four GPUs "02" will enable only first and third GPUs (#0 and #2).\nYou can also turn on/off cards in runtime with "0"..."9" keys and check current statistics with "s" key.\nFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ', 'this setting can improve stability on multi-GPU systems if miner hangs during startup. It serializes GPUs initalization routines. Use "1" to serailize some of routines and "2" to serialize all routines.\nDefault value is "0" (no serialization, fast initialization).\n ', 'failover main pool switch time, in minutes, see "Failover" section below. Default value is 30 minutes, set zero if there is no main pool.\n ', 'set minimal fan speed, in percents, for example, "50" will set minimal fans speed to 50%. You can also specify values for every card, for example "50,60,70".\nThis option works only if miner manages cooling, i.e. when "-tt" option is used to specify target temperature. Default value is "0".\nNote: for NVIDIA cards this option is not supported.\n ', 'Select mining mode:\n"0" (default) means dual Ethereum + Decred/Siacoin/Lbry mining mode.\n"1" means Ethereum-only mining mode. You can set this mode for every card individually, for example, "1-02" will set mode "1" for first and third GPUs (#0 and #2).\nFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ', 'set maximal fan speed, in percents, for example, "80" will set maximal fans speed to 80%. You can also specify values for every card, for example "-fanmax 50,60,70".\nThis option works only if miner manages cooling, i.e. when "target GPU temperature" option is used to specify target temperature. Default value is "100".\nNote: for NVIDIA cards this option is not supported.\n ', 'Restart miner mode. "0" (default) - restart miner if something wrong with GPU. "-1" - disable automatic restarting. restart >20 - restart miner if something\nwrong with GPU or by timer. For example, "60" - restart miner every hour or when some GPU failed.\n"1" closes miner and execute "reboot.bat" file ("reboot.bash" or "reboot.sh" for Linux version) in the miner directory (if exists) if some GPU failed.\nSo you can create "reboot.bat" file and perform some actions, for example, reboot system if you put this line there: "shutdown /r /t 5 /f".\n ', 'set "1" to cancel my developer fee at all. In this mode some optimizations are disabled so mining speed will be slower by about 4%.\nBy enabling this mode, I will lose 100% of my earnings, you will lose only 2-3% of your earnings.\nSo you have a choice: "fastest miner" or "completely free miner but a bit slower".\nIf you want both "fastest" and "completely free" you should find some other miner that meets your requirements, just don\'t use this miner instead of claiming that I need\nto cancel/reduce developer fee, saying that 1-2% developer fee is too much for this miner and so on.\n ', 'low intensity mode. Reduces mining intensity, useful if your cards are overheated. Note that mining speed is reduced too.\nMore value means less heat and mining speed, for example, "10" is less heat and mining speed than "1". You can also specify values for every card, for example "3,10,50".\nDefault value is "0" - no low intensity mode.\n ', 'low intensity mode for DAG generation, it can help with OC or weak PSU. Supported values are 0, 1, 2, 3, more value means lower intensity. Example: "1".\nYou can also specify values for every card, for example "1,0,3". Default value is "0" (no low intensity for DAG generation).\n ', 'watchdog option. Default value is "1", it enables watchdog, miner will be closed (or restarted, see "restart" option) if any thread is not responding for 1 minute or OpenCL call failed.\nSpecify "0" to disable watchdog.\n ', 'minimal speed for ETH, in MH/s. If miner cannot reach this speed for 5 minutes for any reason, miner will be restarted (or "reboot.bat" will be executed if "reastart 1" is set). Default value is 0 (feature disabled).\n ', 'delay, in seconds, between connection attempts. Default values is "20". Specify "-1" if you don\'t need reconnection, in this mode miner will exit if connection is lost.\n ', 'job timeout for ETH, in minutes. If miner does not get new jobs for this time, it will disconnect from pool. Default value is 10.\n ', 'set target GPU temperature. For example, "80" means 80C temperature. You can also specify values for every card, for example "70,80,75".\nYou can also set static fan speed if you specify negative values, for example "-50" sets 50% fan speed. Specify zero to disable control and hide GPU statistics.\n"1" (default) does not manage fans but shows GPU temperature and fan status every 30 seconds. Specify values 2..5 if it is too often.\nNote: for NVIDIA cards only temperature monitoring is supported, temperature management is not supported.\nNote: for Linux gpu-pro drivers, miner must have root access to manage fans, otherwise only monitoring will be available.\n ', 'reduce entire mining intensity (for all coins) automatically if GPU temperature is above specified value. For example, "80" reduces mining intensity if GPU temperature is above 80C.\nYou can see if intensity was reduced in detailed statistics ("s" key).\nYou can also specify values for every card, for example "80,85,80". You also should specify non-zero value for "target GPU temperature" option to enable this option.\nIt is a good idea to set "-ttli" value higher than "-tt" value by 3-5C.\n ', 'set stop GPU temperature, miner will stop mining if GPU reaches specified temperature. For example, "-tstop 95" means 95C temperature. You can also specify values for every card, for example "-tstop 95,85,90".\nThis feature is disabled by default ("0"). You also should specify non-zero value for "target GPU temperature" option to enable this option.\nIf it turned off wrong card, it will close miner in 30 seconds.\nYou can also specify negative value to close miner immediately instead of stopping GPU, for example, "-95" will close miner as soon as any GPU reach 95C temperature.\n ', 'send Ethereum hashrate to pool. Default value is "1", set "0" if you don\'t want to send hashrate.\n ', 'send Ethereum stale shares to pool, it can increase effective hashrate a bit. Default value is "1", set "0" if you don\'t want to send stale shares.\n ', 'set target GPU core clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1000,1050,1100,0".\nNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\nNote: this option changes clocks for all power states, so check voltage for all power states in WattMan or use -cvddc option.\nBy default, low power states have low voltage, setting high GPU clock for low power states without increasing voltage can cause driver crash.\nNote: for NVIDIA cards this option is not supported.\n ', 'set target GPU memory clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1200,1250,1200,0".\nNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\nNote: for NVIDIA cards this option is not supported.\n\n ', 'set power limit, from -50 to 50. If not specified, miner will not change power limit. You can also specify values for every card, for example "20,-20,0,10".\nNote: for NVIDIA cards this option is not supported.\n ', 'set target GPU core voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\nNote: for NVIDIA cards this option is not supported.\n\n ', 'set target GPU memory voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\nNote: for NVIDIA cards this option is not supported.\n ', 'alternative GPU indexing. This option does not change GPU order, but just changes GPU indexes that miner displays, it can be useful in some cases. Possible values are:\n0: default GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU1".\n1: same as "0", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU2".\n2: alternative GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU5".\n3: same as "2", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU6".\nDefault value is "0".\n ', 'selects GPUs manufacturer. 1 - use AMD GPUs only. 2 - use NVIDIA GPUs only. 3 - use both AMD and NVIDIA GPUs. Default value is "3".\n ']
cc=['-epool', '-ewal', '-epsw', '-eworker', '-esm', '-etha', '-asm', '-ethi', '-eres', '-allpools', '-allcoins', '-etht', '-di', '-gser', '-ftime', '-fanmin', '-mode', '-fanmax', '-r', '-nofee', '-li', '-lidag', '-wd', '-minspeed', '-retrydelay', '-ejobtimeout', '-tt', '-ttli', '-tstop', '-erate', '-estale', '-cclock', '-mclock', '-powlim', '-cvddc', '-mvddc', '-altnum', '-platform']
scc = ['-dpool', '-dwal', '-dpsw', '-epool', '-ewal', '-epsw', '-eworker', '-dcri', '-dcrt', '-esm',
           '-etha', '-asm', '-ethi', '-eres', '-allpools', '-ttdcr', '-allcoins', '-etht', '-djobtimeout',
           '-di', '-gser', '-ftime', '-fanmin', '-mode', '-fanmax', '-r', '-nofee', '-li', '-lidag', '-wd',
           '-minspeed', '-retrydelay', '-ejobtimeout', '-tt', '-ttli', '-tstop', '-erate', '-estale', '-cclock',
           '-mclock', '-powlim', '-cvddc', '-mvddc', '-altnum', '-platform']
df=[0,100,1,100,100]
# Def ##############################################################################################################################################################################################
def raisef(f,n):
    f.tkraise()
def hel(a,t=''):
    a1=Toplevel(root)
    a1.title(t)
    a1.wm_attributes("-topmost", "true")
    a1.attributes("-toolwindow",1)
    a1.geometry("%dx%d+%d+%d" % (1260, 70, (root.winfo_screenwidth()-1260)/2, (root.winfo_screenheight()-90)/2))#492
    a1.grab_set()
    t=Text(a1,width=155,height=4)#59
    t.place(x=0,y=0)
    scroll_y = Scrollbar(a1, orient="vertical", command=t.yview)
    scroll_y.place(x=1210, y=0, width=50, height=70)
    t.configure(yscrollcommand=scroll_y.set)
    t.insert(END,a)
    t.configure(state="disabled", relief="flat", bg='white')
    a1.mainloop()
    #print((a)
# End def##############################################################################################################################################################################################
root=Tk()
root.geometry('499x589+100+50')
root.overrideredirect(True)
root.configure(background='black')
root.wm_attributes("-topmost", "true")
def omf(event):
    global xo, yo
    root.geometry('+{0}+{1}'.format(event.x_root-xo, event.y_root-yo))

def smf(event):
    global xo,yo
    xo = event.x
    yo = event.y
def somf(event):
    global xo, yo
    xo = None
    yo = None
f1=Frame(root,width=499,height=25,background='black')
f1.place(x=0,y=0)
f1.bind("<ButtonPress-1>", smf)
f1.bind("<ButtonRelease-1>", somf)
f1.bind("<B1-Motion>", omf)
f=[]
ethb=[]
ethe=[]
###########################################################
photo1 = PhotoImage(file="p.gif")
cane0=PhotoImage(file="can1.gif")
can1=PhotoImage(file="can2.gif")
can2=PhotoImage(file="can3.gif")
can3=PhotoImage(file="can4.gif")
can4=PhotoImage(file="can5.gif")
width1 = photo1.width()
height1 = photo1.height()
###########################################################
f1=Frame(root,width=497,height=563,bg='blue')
f1.place(x=1,y=25)
#f1.grid(row=0, column=0, sticky='news')
f.append(f1)
for i in range(1,10):#FRAME CREATION
    f1=Frame(root,width=497,height=563,bg='#ffffff')
    f1.place(x=1, y=25)
    #f1.grid(row=0, column=0, sticky='news')
    f.append(f1)
f[1].tkraise()###############
#_Home Frame_#############################################################################################################################################################################################
b1=Button(f[0],text="ETH",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0,command=lambda:raisef(f[1],1))
b1.place(x=0,y=0)
"""
b2=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b2.place(x=0,y=0)
b3=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b3.place(x=0,y=0)
b4=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b4.place(x=0,y=0)
b5=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b5.place(x=0,y=0)
b6=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b6.place(x=0,y=0)
b7=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b7.place(x=0,y=0)
b8=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b8.place(x=0,y=0)
b9=Button(f[0],text="UPDATE/DELETE LOG",width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg="light blue",bd=0)
b9.place(x=0,y=0)
#"""
#_End Home Frame_#############################################################################################################################################################################################
#_ETH Only_##############################################################################################################################################################################################
class setx:
    def __init__(self,root,k,image1,image2,x,y):
        self.root=root

        self.k=k
        self.xx=0
        self.yy=0
        self.px=x
        self.py=y
        self.signal=0
        self.photo1=image1
        self.cane=image2
        self.main()
    def pp(self,event):
        x,y=event.x, event.y
        self.xx,self.yy=x,y
    def pai(self,event):
        x, y = event.x, event.y
        if self.xx <= x and self.k > 0:
            self.canvas1.move(self.item, 1, 0)
            self.k -= 1
        else:
            if self.k < (100) and self.xx >= x:
                self.canvas1.move(self.item, -1, 0)
                self.k += 1
                self.signa = self.k
        self.lable_for_pre.configure(text=str(100 - self.k))
    def main(self):
        self.cann = Label(self.root, image=self.cane, bd=0, highlightthickness=0)
        self.cann.place(x=self.px, y=self.py + height1 - 5)
        self.lable_for_pre = Label(self.root, text=str(100 - self.k), bd=0, bg='white', highlightthickness=0)
        self.lable_for_pre.place(x=self.px + 79, y=self.py + height1 + 15)
        self.canvas1 = Canvas(self.root, width=width1, height=height1, bd=0, highlightthickness=0)  # , bg='#d0e429'
        self.canvas1.place(x=self.px, y=self.py)  # <--- Make your canvas expandable.
        self.item = self.canvas1.create_image(-self.k, 0, image=self.photo1, anchor="nw")
        self.canvas1.bind('<Button-1>', self.pai)
        self.canvas1.bind('<B1-Motion>', self.pai)
        self.canvas1.bind('<Motion>', self.pp)
class parameters_set:
    def __init__(self,root, x, y,scoin=''):
        self.fr = root
        self.scoin = scoin
        self.cn = [str(self.scoin) + ' Pool Name*', str(self.scoin) + ' Wallet Address*', str(self.scoin) + ' Password*',
                   'ETH Pool Name*', 'ETH Wallet Address*', 'ETH Password*', 'Worker', str(self.scoin) + ' Intensity',
                   'Second Coin Time Period', 'Ethereum Stratum mode', 'Ethereum algorithm mode',
                   'Enables Assembler(asm)', 'Ethereum intensity', 'Eres', 'All Pools', 'Second Autointensity',
                   'All Coins', 'Ethereum Time', 'Second Coin Timeout', 'GPU indexes', 'GPU Serializability',
                   'Failover Time', 'Fan Min', 'Mode', 'Fan Max', 'Restart Miner', 'No Fee', 'low intensity mode',
                   'low intensity(DAG)', 'Watch Dog', 'Minimal Speed', 'Retry Delay', 'Job Timeout',
                   'target GPU temperature', 'Auto Intensity', 'Temprature Stop', 'Ethereum hashrate', 'Ethereum stale',
                   'GPU Core Clock', 'GPU Memory Clock', 'Power Limit', 'GPU Core Voltage', 'GPU Memory Voltage',
                   'Alt GPU Index', 'Platform']
        self.ch = [
            'Decred/Siacoin/Lbry/Pascal pool address. Use "http://" prefix for HTTP pools, "stratum+tcp://" for Stratum pools. If prefix is missed, Stratum is assumed.\nDecred: both Stratum and HTTP are supported. Siacoin: both Stratum and HTTP are supported, though note that not all Stratum versions are supported currently. Lbry: only Stratum is supported.',
            'Your Decred/Siacoin/Lbry/Pascal wallet address or worker name, it depends on pool.',
            'Password for Decred/Siacoin/Lbry/Pascal pool',
            'Ethereum pool address. Only Stratum protocol is supported for pools. Miner supports all pools that are compatible with Dwarfpool proxy and accept Ethereum wallet address directly.\nFor solo mining, specify "http://" before address, note that this mode is not intended for proxy or HTTP pools, also "-allpools 1" will be set automatically in this mode.\nNote: The miner supports all Stratum versions for Ethereum, HTTP mode is necessary for solo mining only.\nUsing any proxies will reduce effective hashrate by at least 1%, so connect miner to Stratum pools directly. Using HTTP pools will reduce effective hashrate by at least 5%.\n ',
            'Your Ethereum wallet address. Also worker name and other options if pool supports it.\nPools that require "Login.Worker" instead of wallet address are not supported directly currently, but you can use "allpools 1" option to mine there.\n ',
            'Password for Ethereum pool, use "x" as password.\n ', 'Worker name, it is required for some pools.\n ',
            'Decred/Siacoin/Lbry/Pascal intensity, or Ethereum fine-tuning value in ETH-only ASM mode. Default value is 30, you can adjust this value to get the best Decred/Siacoin/Lbry mining speed without reducing Ethereum mining speed.\nYou can also specify values for every card, for example "30,100,50".\nYou can change the intensity in runtime with "+" and "-" keys and check current statistics with "s" key.\nFor example, by default (30) 390 card shows 29MH/s for Ethereum and 440MH/s for Decred. Setting 70 causes 24MH/s for Ethereum and 850MH/s for Decred.',
            'Time period between Decred/Siacoin HTTP requests for new job, in seconds. Default value is 5 seconds.',
            'Ethereum Stratum mode. 0 - eth-proxy mode (for example, dwarpool.com), 1 - qtminer mode (for example, ethpool.org),\n2 - miner-proxy mode (for example, coinotron.com), 3 - nicehash mode. 0 is default.\n',
            'Ethereum algorithm mode for AMD cards. 0 - optimized for fast cards, 1 - optimized for slow cards, 2 - for gpu-pro Linux drivers. -1 - autodetect (default, automatically selects between 0 and 1).\nYou can also set this option for every card individually, for example "0,1,0".\n ',
            '(AMD cards only) enables assembler GPU kernels. In this mode some tuning is required even in ETH-only mode,\nCurrently ETH-LBRY mode is not supported in assembler.\nSpecify "-asm 0" to disable this option. You can also specify values for every card, for example "0,1,0". Default value is "1".\nIf ASM mode is enabled, miner must show "GPU #x: algorithm ASM" at startup.\nCheck "FINE-TUNING" section below for additional notes.\nNEW: added alternative assembler kernels for Tonga and Polaris cards for ETH-only mode.(i.e. you cannot find speed peak), use "2" option to enable this mode.\n ',
            'Ethereum intensity. Default value is 8, you can decrease this value if you don\'t want Windows to freeze or if you have problems with stability. The most low GPU load is "0".\nnow can set intensity for every card individually, for example "1,8,6".\nYou can also specify negative values, for example, "-8192", it exactly means "global work size" parameter which is used in official miner.\n ',
            'this setting is related to Ethereum mining stability. Every next Ethereum epoch requires a bit more GPU memory, miner can crash during reallocating GPU buffer for new DAG.\nTo avoid it, miner reserves a bit larger GPU buffer at startup, so it can process several epochs without buffer reallocation.\nThis setting defines how many epochs miner must foresee when it reserves GPU buffer, i.e. how many epochs will be processed without buffer reallocation. Default value is 2.\n ',
            'Specify "1" if miner does not want to mine on specified pool (because it cannot mine devfee on that pool), but you agree to use some default pools for devfee mining.\nNote that if devfee mining pools will stop, entire mining will be stopped too.\n ',
            'reduce Decred/Siacoin/Lbry/Pascal intensity automatically if GPU temperature is above specified value. For example, "80" reduces Decred intensity if GPU temperature is above 80C. \nYou can see current Decred intensity coefficients in detailed statistics ("s" key). So if you set "-dcri 50" but Decred/Siacoin intensity coefficient is 20% it means that GPU currently mines Decred/Siacoin at "10".\nYou can also specify values for every card, for example "80,85,80". You also should specify non-zero value for  option to enable this option.\nIt is a good idea to set value higher than value by 3-5C.',
            'Specify "1" to be able to mine Ethereum forks, in this mode miner will use some default pools for devfee Ethereum mining.\nNote that if devfee mining pools will stop, entire mining will be stopped too.\nMiner has to use two DAGs in this mode - one for Ethereum and one for Ethereum fork, it can cause crashes because DAGs have different sizes.\nTherefore for this mode it is recommended to specify current Ethereum epoch (or a bit larger value),\nfor example, "47" means that miner will expect DAG size for epoch #47 and will allocate appropriate GPU buffer at starting, instead of reallocating bigger GPU buffer (may crash) when it starts devfee mining.\nAnother option is to specify "-1", in this mode miner will start devfee round immediately after start and therefore will get current epoch for Ethereum, after that it will be able to mine Ethereum fork.\nIf you mine Expanse, the best way is to specify "exp", in this mode devfee mining will be on Expanse too and DAG won\'t be recreated at all.\nIf you mine ETC on some pool that does not accept wallet address but requires Username.Worker instead, the best way is to specify "etc", in this mode devfee mining will be on ETC pools and DAG won\'t be recreated at all.\n ',
            'Time period between Ethereum HTTP requests for new job in solo mode, in milliseconds. Default value is 200ms.\n ',
            'job timeout for second coin in dual mode, in minutes. If miner does not get new jobs for this time, it will disconnect from pool. Default value is 30.',
            'GPU indexes, default is all available GPUs. For example, if you have four GPUs "02" will enable only first and third GPUs (#0 and #2).\nYou can also turn on/off cards in runtime with "0"..."9" keys and check current statistics with "s" key.\nFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ',
            'this setting can improve stability on multi-GPU systems if miner hangs during startup. It serializes GPUs initalization routines. Use "1" to serailize some of routines and "2" to serialize all routines.\nDefault value is "0" (no serialization, fast initialization).\n ',
            'failover main pool switch time, in minutes, see "Failover" section below. Default value is 30 minutes, set zero if there is no main pool.\n ',
            'set minimal fan speed, in percents, for example, "50" will set minimal fans speed to 50%. You can also specify values for every card, for example "50,60,70".\nThis option works only if miner manages cooling, i.e. when "-tt" option is used to specify target temperature. Default value is "0".\nNote: for NVIDIA cards this option is not supported.\n ',
            'Select mining mode:\n"0" (default) means dual Ethereum + Decred/Siacoin/Lbry mining mode.\n"1" means Ethereum-only mining mode. You can set this mode for every card individually, for example, "1-02" will set mode "1" for first and third GPUs (#0 and #2).\nFor systems with more than 10 GPUs: use letters to specify indexes more than 9, for example, "a" means index 10, "b" means index 11, etc.\n ',
            'set maximal fan speed, in percents, for example, "80" will set maximal fans speed to 80%. You can also specify values for every card, for example "-fanmax 50,60,70".\nThis option works only if miner manages cooling, i.e. when "target GPU temperature" option is used to specify target temperature. Default value is "100".\nNote: for NVIDIA cards this option is not supported.\n ',
            'Restart miner mode. "0" (default) - restart miner if something wrong with GPU. "-1" - disable automatic restarting. restart >20 - restart miner if something\nwrong with GPU or by timer. For example, "60" - restart miner every hour or when some GPU failed.\n"1" closes miner and execute "reboot.bat" file ("reboot.bash" or "reboot.sh" for Linux version) in the miner directory (if exists) if some GPU failed.\nSo you can create "reboot.bat" file and perform some actions, for example, reboot system if you put this line there: "shutdown /r /t 5 /f".\n ',
            'set "1" to cancel my developer fee at all. In this mode some optimizations are disabled so mining speed will be slower by about 4%.\nBy enabling this mode, I will lose 100% of my earnings, you will lose only 2-3% of your earnings.\nSo you have a choice: "fastest miner" or "completely free miner but a bit slower".\nIf you want both "fastest" and "completely free" you should find some other miner that meets your requirements, just don\'t use this miner instead of claiming that I need\nto cancel/reduce developer fee, saying that 1-2% developer fee is too much for this miner and so on.\n ',
            'low intensity mode. Reduces mining intensity, useful if your cards are overheated. Note that mining speed is reduced too.\nMore value means less heat and mining speed, for example, "10" is less heat and mining speed than "1". You can also specify values for every card, for example "3,10,50".\nDefault value is "0" - no low intensity mode.\n ',
            'low intensity mode for DAG generation, it can help with OC or weak PSU. Supported values are 0, 1, 2, 3, more value means lower intensity. Example: "1".\nYou can also specify values for every card, for example "1,0,3". Default value is "0" (no low intensity for DAG generation).\n ',
            'watchdog option. Default value is "1", it enables watchdog, miner will be closed (or restarted, see "restart" option) if any thread is not responding for 1 minute or OpenCL call failed.\nSpecify "0" to disable watchdog.\n ',
            'minimal speed for ETH, in MH/s. If miner cannot reach this speed for 5 minutes for any reason, miner will be restarted (or "reboot.bat" will be executed if "reastart 1" is set). Default value is 0 (feature disabled).\n ',
            'delay, in seconds, between connection attempts. Default values is "20". Specify "-1" if you don\'t need reconnection, in this mode miner will exit if connection is lost.\n ',
            'job timeout for ETH, in minutes. If miner does not get new jobs for this time, it will disconnect from pool. Default value is 10.\n ',
            'set target GPU temperature. For example, "80" means 80C temperature. You can also specify values for every card, for example "70,80,75".\nYou can also set static fan speed if you specify negative values, for example "-50" sets 50% fan speed. Specify zero to disable control and hide GPU statistics.\n"1" (default) does not manage fans but shows GPU temperature and fan status every 30 seconds. Specify values 2..5 if it is too often.\nNote: for NVIDIA cards only temperature monitoring is supported, temperature management is not supported.\nNote: for Linux gpu-pro drivers, miner must have root access to manage fans, otherwise only monitoring will be available.\n ',
            'reduce entire mining intensity (for all coins) automatically if GPU temperature is above specified value. For example, "80" reduces mining intensity if GPU temperature is above 80C.\nYou can see if intensity was reduced in detailed statistics ("s" key).\nYou can also specify values for every card, for example "80,85,80". You also should specify non-zero value for "target GPU temperature" option to enable this option.\nIt is a good idea to set "-ttli" value higher than "-tt" value by 3-5C.\n ',
            'set stop GPU temperature, miner will stop mining if GPU reaches specified temperature. For example, "-tstop 95" means 95C temperature. You can also specify values for every card, for example "-tstop 95,85,90".\nThis feature is disabled by default ("0"). You also should specify non-zero value for "target GPU temperature" option to enable this option.\nIf it turned off wrong card, it will close miner in 30 seconds.\nYou can also specify negative value to close miner immediately instead of stopping GPU, for example, "-95" will close miner as soon as any GPU reach 95C temperature.\n ',
            'send Ethereum hashrate to pool. Default value is "1", set "0" if you don\'t want to send hashrate.\n ',
            'send Ethereum stale shares to pool, it can increase effective hashrate a bit. Default value is "1", set "0" if you don\'t want to send stale shares.\n ',
            'set target GPU core clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1000,1050,1100,0".\nNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\nNote: this option changes clocks for all power states, so check voltage for all power states in WattMan or use -cvddc option.\nBy default, low power states have low voltage, setting high GPU clock for low power states without increasing voltage can cause driver crash.\nNote: for NVIDIA cards this option is not supported.\n ',
            'set target GPU memory clock speed, in MHz. If not specified or zero, miner will not change current clock speed. You can also specify values for every card, for example "1200,1250,1200,0".\nNote: for some drivers versions AMD blocked underclocking for some reason, you can overclock only.\nNote: for NVIDIA cards this option is not supported.\n\n ',
            'set power limit, from -50 to 50. If not specified, miner will not change power limit. You can also specify values for every card, for example "20,-20,0,10".\nNote: for NVIDIA cards this option is not supported.\n ',
            'set target GPU core voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\nNote: for NVIDIA cards this option is not supported.\n\n ',
            'set target GPU memory voltage, multiplied by 1000. For example, "1050" means 1.05V. You can also specify values for every card, for example "900,950,1000,970". Supports latest AMD 4xx cards only in Windows.\nNote: for NVIDIA cards this option is not supported.\n ',
            'alternative GPU indexing. This option does not change GPU order, but just changes GPU indexes that miner displays, it can be useful in some cases. Possible values are:\n0: default GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU1".\n1: same as "0", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU2".\n2: alternative GPU indexing. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU0" and "GPU5".\n3: same as "2", but start indexes from one instead of zero. For example, if you specify "-di 05" to select first and last GPUs of six GPUs installed, miner will display these two selected cards as "GPU1" and "GPU6".\nDefault value is "0".\n ',
            'selects GPUs manufacturer. 1 - use AMD GPUs only. 2 - use NVIDIA GPUs only. 3 - use both AMD and NVIDIA GPUs. Default value is "3".\n ']
        self.y=y
        self.x=x
        self.gs = 2
        self.bx, self.by = 5, 5
        self.ex, self.ey = 10, 5
        self.ecolor = '#F0F0F0'
        self.bfont = 'Verdana'
        self.bsize = '10'
        self.bfontanchor = 'w'
        self.bx, self.by = 5, 5
        self.ex, self.ey = 10, 5
        self._main()

        #pass

    def select_all(self,event):
        self.ee.select_range(0, 'end')
        self.ee.icursor('end')

    def _main(self):
        if self.scoin=='':
            self.e = Button(self.fr, anchor='w', text=cn[self.y] , font=(str(self.bfont), str(self.bsize)), bg='#d0e429', bd=0,
                            command=lambda: hel(ch[self.y],cn[self.y]))
            self.e.grid(row=self.x, column=0, sticky=W + E, padx=self.bx, pady=self.by)  # sticky=W+E)
            self.ee = Entry(self.fr, bd=0, bg=self.ecolor)
            self.ee.grid(row=self.x, column=1, sticky=W + E + N + S, padx=self.ex, pady=self.ey, columnspan=3)
            self.ee.bind('<Control-KeyRelease-a>', lambda event: self.select_all(event))
            tempe = Entry(self.fr, bd=0, textvariable=1, font=('Verdana', self.gs), state='disable', disabledbackground='white')
            tempe.grid(row=self.x + 1, column=0, sticky=W + E + N + S, columnspan=4)
        else:
            self.e = Button(self.fr, anchor='w', text=self.cn[self.y] , font=(str(self.bfont), str(self.bsize)),
                            bg='#d0e429', bd=0,
                            command=lambda: hel(self.ch[self.y],self.cn[self.y]))
            self.e.grid(row=self.x, column=0, sticky=W + E, padx=self.bx, pady=self.by)  # sticky=W+E)
            self.ee = Entry(self.fr, bd=0, bg=self.ecolor)
            self.ee.grid(row=self.x, column=1, sticky=W + E + N + S, padx=self.ex, pady=self.ey, columnspan=3)
            self.ee.bind('<Control-KeyRelease-a>', lambda event: self.select_all(event))
            tempe = Entry(self.fr, bd=0, textvariable=1, font=('Verdana', self.gs), state='disable',
                          disabledbackground='white')
            tempe.grid(row=self.x + 1, column=0, sticky=W + E + N + S, columnspan=4)
class para:
    def __init__(self,ma,scoin=''):
        self.f=ma
        self.scoin=scoin
        self.chr=[IntVar(),IntVar()]
        self.buttons=[]
        self.z=[]
        self.main()
    def on_configure(self, event):
        self.can.configure(scrollregion=self.can.bbox('all'))
    def defalt_setx(self, i):
        d = 100 - self.z[i].k
        if d != df[i]:
            if d < df[i]:
                while d < df[i]:
                    self.z[i].canvas1.move(self.z[i].item, 1, 0)
                    d += 1
                    self.z[i].k -= 1
            else:
                while d > df[i]:
                    self.z[i].canvas1.move(self.z[i].item, -1, 0)
                    d -= 1
                    self.z[i].k += 1
        self.z[i].lable_for_pre.configure(text = df[i])
    def thdf(self):
        for i in range(5):
            thd = Thread(target=self.defalt_setx, args = (i,))
            thd.start()
            thd.join()
    def ss(self, i):
        #print( i
        if self.chr[i].get() == 1:
            if i == 0:
                self.setepool1.configure(state="normal")
                epool = open('bdist\Ebdist\epools.txt', 'a+')
                r = epool.read()
                if r == '':
                    epool.write("""POOL: eth-eu2.nanself.opool.org:9999, WALLET: YOUR_WALLET/YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: eth-us-east1.nanself.opool.org:9999, WALLET: YOUR_WALLET/YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: eth-us-west1.nanself.opool.org:9999, WALLET: YOUR_WALLET/YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: eth-asia1.nanself.opool.org:9999, WALLET: YOUR_WALLET/YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0""")
                else:
                    pass
                epool.close()
            else:
                self.setepool0.configure(state="normal")
                epool = open('bdist\Ebdist\dpools.txt', 'a+')
                r = epool.read()
                if r == '':
                    epool.write("""# WARNING! Remove "#" characters to enable lines, with "#" thself.ey are disabled and will be ignored by miner!

POOL: pasc-eu2.nanself.opool.org:15555, WALLET: YOUR_WALLET.YOUR_PAYMENTID.YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: pasc-us-east1.nanself.opool.org:15555, WALLET: YOUR_WALLET.YOUR_PAYMENTID.YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: pasc-us-west1.nanself.opool.org:15555, WALLET: YOUR_WALLET.YOUR_PAYMENTID.YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0
POOL: pasc-asia1.nanself.opool.org:15555, WALLET: YOUR_WALLET.YOUR_PAYMENTID.YOUR_WORKER/YOUR_EMAIL, PSW: x, WORKER: , ESM: 0, ALLPOOLS: 0""")
                else:
                    pass
                epool.close()
        else:
            if i==0:
                self.setepool1.configure(state="disabled")
            else:
                self.setepool0.configure(state="disabled")
    def op(self, i):
        if i == 1:
            os.startfile('bdist\Ebdist\epools.txt')
        else:
            os.startfile('bdist\Ebdist\dpools.txt')
    def start(self,n=''):
        global f,setframe
        f[2].tkraise()
        s = ''

        if n=='':
            for i in range(38):
                ke = self.buttons[i].ee.get()
                if ke != '':
                    s += cc[i] + ' ' + ke.lstrip(' ') + ' '
                else:
                    pass
        else:
            for i in range(45):
                ke = self.buttons[i].ee.get()
                if ke != '':
                    s += scc[i] + ' ' + ke.lstrip(' ') + ' '
                else:
                    pass
        back.start(100 - self.z[0].k, 100 - self.z[1].k, 100 - self.z[2].k, 100 - self.z[3].k, 100 - self.z[4].k, s)
        setframe(f[2])

    def main(self):
        self.tag_1 = Label(self.f, text = 'Parameters  ', font = ('franklin Gothic Medium',13), bg = '#d0e429', bd = 0, highlightthickness = 0)
        self.tag_1.place(x=10, y=130)
        self.z.append(setx(self.f, 100, photo1, cane0, 50, 5))
        self.z.append(setx(self.f, 00, photo1, can1, 190, 5))
        self.z.append(setx(self.f, 99, photo1, can2, 340, 5))
        self.z.append(setx(self.f, 00, photo1, can3, 120, 73))
        self.z.append(setx(self.f, 00, photo1, can4, 260, 73))
        self.dfb = Button(self.f,text = 'Default', bg = '#d0e429', bd = 0, command = lambda: self.thdf())
        self.dfb.place(x=452, y=130)
        self.can = Canvas(self.f, width=470, height=350, bd=0, bg='#ffffff', relief=FLAT,highlightthickness = 0)  #
        self.can.place(x=10, y=150)
        self.srl = Scrollbar(self.f, orient="vertical", elementborderwidth=100, command=self.can.yview)
        self.srl.place(x=447, y=150, width=50, height=350)
        self.can.configure(yscrollcommand=self.srl.set)
        self.can.bind('<Configure>', self.on_configure)
        self.fr = Frame(self.can, width=499, height=350, bd=0, relief=FLAT)  # ,bg='#ffffff')#)#
        self.can.create_window((0, 0), width=499, window=self.fr, anchor='nw')
        k = 0
        if self.scoin=='':
            for i in range(len(cn)):
                a=parameters_set(self.fr, k, i)
                k+=2
                self.buttons.append(a)
        else:
            for i in range(45):
                a=parameters_set(self.fr,k, i,scoin=self.scoin)
                k+=2
                self.buttons.append(a)
        self.fr.grid_columnconfigure(1, weight=1)
        e347 = Button(self.f, width=8, text = 'START', font = ('Verdana','10'), bg = '#d0e429', bd = 0, command = lambda : self.start(self.scoin))
        e347.place(x=400, y=535)
        self.startup_eth = Button(self.f, width=13, text = '''SET TO
STARTUP''', font = ('Verdana', '6'), bg = '#d0e429', bd = 0, command = lambda : start.start(self.scoin))
        self.startup_eth.place(x=400, y=505)
        self.setepool0 = Button(self.f, width=19, text = 'self.open dpools.txt', font = ('Verdana','10'), bg = '#d0e429', bd = 0, state = "disabled", command = lambda: self.op(0))
        self.setepool0.place(x=190, y=505)
        self.setepool1 = Button(self.f, width=19, text = 'self.open epools.txt', font = ('Verdana','10'), bg = '#d0e429', bd = 0, state = "disabled", command = lambda: self.op(1))
        self.setepool1.place(x=190, y=535)
        self.ch1 = Checkbutton(self.f,text = 'Creat epools.txt', activebackground = '#d0e429', bg = '#d0e429', variable = self.chr[0], bd = 0, command = lambda: self.ss(0))
        self.ch1.place(x=20, y=535)
        self.ch2 = Checkbutton(self.f,text = 'Creat dpools.txt', activebackground = '#d0e429', variable = self.chr[1], bd = 0, bg = '#d0e429', command = lambda: self.ss(1))
        self.ch2.place(x=20, y=505)
#End ETH parameters
##############################################################################################################################################################################################
class perin:
    def __init__(self,root,image,x,y,n=0,total=100,color='#d0e429',text='',text1=''):
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
            #print( (360.0 * n//self.k)
            self.c.itemconfig(self.a, start=180, extent=-(360.0 * n//self.k))
            self.lable.configure(text=str((100*n/self.k)).zfill(2) + '%', font=('Impact', '24'))
            self.lable.place(x=self.x + 31, y=self.y + 29)
        else:
            self.c.lower(self.c.create_oval((0, 0, 120, 120), fill=self.color, outline=self.color))#self.f).lift()
            self.lable.configure(text=str(100)+'%',font=('Impact', '24'))
            self.place(x=self.x + 29, y=self.y + 30)

    def mainn(self):
        self.c = Canvas(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='#F0F0F0')
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((0, 0, 120, 120), fill=self.color, outline=self.color, start=180, extent=-(360.0 * self.n//self.k))
        self.c.create_image(60, 60, image=self.photoimage)
        self.c.lower(self)
        self.lable = Label(self.root, text=str(100 * self.n//self.k) + '%', font=('Impact', '24'), fg='#d0e429',
                           bg='white')  # Consolas'
        self.lable.place(x=self.x + 31, y=self.y + 29)
        self.lable1 = Label(self.root,width=5, text=self.text, font=('Verdana', '12','bold'), bg='white',fg='#F0F0F0')
        self.lable1.place(x=self.x + 33, y=self.y + 65)
        self.lable2 = Label(self.root, width=4,text=self.text1, font=('Verdana', '8'), bg='white')
        self.lable2.place(x=self.x + 41, y=self.y + 84)
class meter:
    def __init__(self,root,image,x,y,p='1',gr=0,gc=0,n=0,text='',text2='',color='#d0e429',text1='',q='MH\\s'):

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
        self.text2 = text2
        self.text1 = text1
        self.mainn()
    def per(self,n):

        if n<=1000:
            self.c.itemconfig(self.a, start=210, extent=-(240.0 * n//1000))
        else:
            self.c.itemconfig(self.a, start=210, extent=-(240.0 * n//10000))

        self.lable.configure(text=str(n),width=4,font=('Impact', '23','bold'),bg='white')#width=7,
    def mainn(self):
        self.c = Canvas(self.root,width=120,height=120,highlightthickness=0,bd=0,bg='#F0F0F0')
        self.c.place(x=self.x,y=self.y)
        self.a = self.c.create_arc((0, 0, 120, 120), fill=self.color, outline=self.color, start=210, extent=-(240.0 * self.n//1000))
        self.c.create_arc((0, 0, 120, 120), fill='white', outline='white', start=210,extent=120.0)
        self.c.create_image(60, 60, image=self.photoimage)
        self.c.lower(self.a)
        if self.text=='Total Speed':
            if self.text2!='':
                self.lable2 = Label(self.root,width=8, text="""Total
Speed\n""" + self.text2, font=('Verdana', '5', 'bold'), bg='white', fg='#DBDBDB')
                self.lable2.place(x=self.x + 37, y=self.y + 20)
            else:
                self.lable2 = Label(self.root, text="""Total
Speed""", font=('Verdana', '8', 'bold'), bg='white', fg='#DBDBDB')
                self.lable2.place(x=self.x + 37, y=self.y + 20)
        else:
            self.lable2 = Label(self.root, text=self.text1,width=5, font=('Verdana', '12', 'bold'), bg='white', fg='#F0F0F0')
            self.lable2.place(x=self.x + 30, y=self.y + 27)
        self.lable = Label(self.root, text=self.n, width=4,font=('Impact', '23','bold'), fg=self.color,bg='white')####
        self.lable.place(x=self.x + 26, y=self.y + 48)
        self.lable1 = Label(self.root, text=self.q, font=('Verdana', '13'), bg='white')
        self.lable1.place(x=self.x + 36, y=self.y + 83)
class pi:
    def __init__(self,root,r,a,x,y,image,r1=None,a1=None):
        self.image=image
        self.root=root
        self.r=r
        self.a=a
        self.r1=r1
        self.a1=a1
        self.x=x
        self.y=y
        self.main()
    def pro(self,r= None,a=None):
        if r != None:
            self.r = r
        else:
            pass
        if a != None:
            self.a = a
        self.total = self.r + self.a
        if self.total == 0:
            #print( 'total=', self.total
            self.total += 1
            #print( '\n', self.total
        else:
            pass
        #print( (360.0 * self.r)//self.total,self.a,self.r,self.total
        self.c.itemconfig(self.d, start=180, extent=-round((360.0 * self.r /self.total)))
    def pro1(self,r= None,a=None):
        self.r1 = r
        self.a1 = a
        self.total = self.r + self.a
        if self.total == 0:
            #print( 'total=', self.total
            self.total += 1
            #print( '\n', self.total
        else:
            pass
        self.c.itemconfig(self.d1, start=180, extent=-round((360.0 * self.r1//self.total)))

    def main(self):
        self.c = Canvas(self.root, bd=0,highlightthickness=0,width=200, height=200,bg='white')
        self.c.place(x=self.x, y=self.y)
        self.c.create_oval((0, 0, 200, 200), fill='#d0e429', outline='#d0e429')
        self.d = self.c.create_arc((0, 0, 200, 200), fill='#F0F0F0', outline='#F0F0F0', start=180,extent=-0)
        self.c.create_image(100, 100, image=self.image)
        if self.r1!=None or self.a1!=None:
            self.c.create_oval((40, 40, 160, 160), fill='white', outline='white')
            self.c.create_oval((50, 50, 150, 150), fill='#d0e429', outline='white')
            self.d1 = self.c.create_arc((50, 50, 150, 150), fill='#F0F0F0', outline='#F0F0F0', start=180, extent=-0)
class timetemp:
    def __init__(self,root,x,y,image,text,text1):
        self.root=root
        self.x=x
        self.y=y
        self.text=text
        self.text1=text1
        self.image=image
        self.d = (10 - len(self.text1))//2
        self.main()
    def textset(self,n):
        self.a1.configure(width=11,text=str(n), font=('Verdana', '10'))
        #self.a1.configure(text=str((" "*self.d)+str(n)+(" "*(10-self.d))), font=('Verdana', '10'))

        #self.a1.place(x=3, y=23)

    def main(self):
        self.a2 = Label(self.root, image=self.image)
        self.a2.place(x=self.x, y=self.y)
        self.a = Label(self.root, width=12,text=self.text,font=('Verdana', '10'),bg='#d0e429')
        self.a.place(x=self.x, y=self.y)
        #print( len((" " * self.d) + str(self.text1) + (" " * (10 - self.d))),'-'
        self.a1 = Label(self.root, width=11,text=self.text1, font=('Verdana', '10'),bg='white')
        self.a1.place(x=self.x+3, y=self.y+23)
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
        if r1!=None and a1!=None:
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
        #print( self.r2,'=',self.a2,'f'
        if self.r2!=None or self.a2!=None:
            #print( 'lol'
            self.x1color = Label(self.a1, text=self.a2, font=('Verdana', '7', 'bold'),width=9, bd=0, fg='#DBDBDB', bg='white')
            self.x1color.grid(row=0, column=3,pady=0, padx=1)
            self.y1color = Label(self.a1, text=self.r2, font=('Verdana', '7', 'bold'), width=9, bd=0, fg='#DBDBDB',
                                bg='white')
            self.y1color.grid(row=1, column=3,pady=0, padx=1)
class errr:
    def __init__(self,ma):
        self.err1 = ma  # Tk()#Toplevel()
        self.photoimage = PhotoImage(file="pp.gif")
        self.line=1
        self.main()
    def set(self,s,c):
        self.text.configure(state="normal", relief="flat")
        self.text.insert(END,s+'\n')
        self.text.tag_add("s", str(self.line)+'.0',END)
        self.text.tag_config("s", background="black", foreground=c)
        self.text.configure(state="disabled", relief="flat")
        #print( s.count('\n'),'--'
        self.line+=1+s.count('\n')
    def main(self):
        self.err1.geometry("640x300")
        self.err1.wm_attributes("-alpha", 0.85)
        self.err1.wm_attributes("-topmost", "true")
        self.text=Text(self.err1,bg='black')#,bg='white')
        self.text.place(x=0,y=0)
        self.text.configure(state="disabled", relief="flat")
        #self.err1.mainloop()
class setframe:
    def __init__(self,f2):

        self.f2=f2
        self.t_eth = []
        self.sc=[]
        self.no=None
        self.ki=0
        self.txt=''
        self.event1=Event()
        self.event1.set()
        self.photoimage = ImageTk.PhotoImage(file="Upi.gif")
        self.photoimage1 = ImageTk.PhotoImage(file="U.gif")
        self.photoimage2 = ImageTk.PhotoImage(file="can11.gif")
        self.s=None
        self.main()
    def stopit(self):
        try:
            os.popen("TASKKILL /F /IM " + 'notepad.exe')
            #subprocess.call("TASKKILL /F /IM " + 'notepad.exe')
            #os.system("TASKKILL /F /IM " + 'notepad.exe')
        except (Exception, e):
            pass
    def on_configure1(self,event):
        self.can11.configure(scrollregion=self.can11.bbox('all'))
    def setgui(self):
        l = self.threadt('cxv')
        #print( l
        #input(l)
        #l=[['#00ffff', 'ETH:', 'GPU1', '29.259', 'Mh/s', 'GPU2', '29.392', 'Mh/s', 'GPU3', '29.278', 'Mh/s', 'GPU4', '29.394', 'Mh/s', 'GPU5', '29.179', 'Mh/s', 'GPU6', '29.383', 'Mh/s', 'GPU7', '29.261', 'Mh/s'], ['#00ffff', 'ETH-', 'TotalSpeed:', '205.146', 'Mh/s', 'TotalShares:', '387', 'Rejected:', '0', 'Time:', '05:38'], None, None, None, None, None, ['#ffff00', 'PASC:', 'GPU1', '341.353', 'Mh/s', 'GPU2', '342.901', 'Mh/s', 'GPU3', '341.580', 'Mh/s', 'GPU4', '342.935', 'Mh/s', 'GPU5', '340.421', 'Mh/s', 'GPU6', '342.799', 'Mh/s', 'GPU7', '341.373', 'Mh/s'], ['#ffff00', 'PASC-', 'TotalSpeed:', '2393.362', 'Mh/s', 'TotalShares:', '701', 'Rejected:', '9']]
        r = 1
        self.fm = Frame(self.fr1, width=497, height=281, bg='#ffffff')
        self.fm.grid(row=0, column=0, sticky=W + E + N + S, padx=1, pady=1)
        self.stop=Button(self.fm,text='Stop Miner',font=('Verdana', '10'),bg="#d0e429",relief=GROOVE,command=lambda:self.stopit())
        self.stop.place(x=1,y=0)
        if l[1] != None  :#['ETH:', 'ETH-', 'GPU0','SC:','SC-', 'DCR:','DCR-','PASC:','PASC-']
            self.q = Label(self.fm, text='Share Chart', font=('Verdana', '8', 'bold'), bg='white', fg='#DBDBDB')
            self.q.place(x=274, y=10)
            self.q = Label(self.fm, text='ETH', font=('Verdana', '8'), bg='white')
            self.q.place(x=355, y=10)  # fg='#F0F0F0'
            if l[4]==None and l[6]==None and l[8]==None:
                t = pi(self.fm, int(l[1][8]), int(l[1][6]), 274, 30, image=self.photoimage)
                t.pro(a=int(l[1][8]), r=int(l[1][6]))
                self.t_eth.append(t)
                t = pidata(self.fm, 290, 240, r=12, a=100)
                self.t_eth.append(t)
                t = meter(self.fm, self.photoimage1, 63, 34, n=int(round(float(l[1][3]))), text1='', q=l[1][4], text='Total Speed')
                self.t_eth.append(t)
            else:
                for i in range(len(l)):
                    if l[i]!=None and l[i][1]not in ['ETH:','ETH-']:
                        self.no=i
                        self.ki=1
                        self.txt=l[i][1][:-1]
                self.q.configure(text='ETH , '+self.txt)
                t = pi(self.fm, int(l[1][8]), int(l[1][6]), 274, 30, image=self.photoimage,a1=int(l[self.no][6]), r1=int(l[self.no][8]))
                t.pro(r=int(l[1][8]), a=int(l[1][6]))
                t.pro1(r=int(l[self.no][8]), a=int(l[self.no][6]))
                self.t_eth.append(t)
                self.sc.append(t)
                t = pidata(self.fm, 274, 240,r=int(l[1][8]), a=int(l[1][6]),r2=int(l[self.no][8]), a2=int(l[self.no][6]))
                self.q = Label(self.fm, text='ETH             ' + str(self.txt), font=('Verdana', '6','bold'), bg='white')
                self.q.place(x=370, y=232)
                self.t_eth.append(t)
                t = meter(self.fm, self.photoimage1, 0, 50, n=int(round(float(l[1][3]))), text1='', q=l[1][4],
                          text='Total Speed')
                self.t_eth.append(t)
                t = meter(self.fm, self.photoimage1, 120, 50, n=int(round(float(l[self.no][3]))), text1='', q=l[self.no][4],
                          text='Total Speed',text2=self.txt)
                self.sc.append(t)
            t = timetemp(self.fm, 10, 200, self.photoimage2, text='Start At', text1=str(time.ctime()[10:-5]))#time.strftime("%H:%M:%S", time.gmtime())))
            self.t_eth.append(t)
            t = timetemp(self.fm, 130, 200, self.photoimage2, text='Minner Time', text1=l[1][10])
            self.t_eth.append(t)
        s = []
        if l[0] != None:
            k = 0
            t = Frame(self.fr1, width=497, height=120, bd=0, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[0]) - 2) // 3)):
                if (i + 1) % 5 == 0:
                    k = 0
                    r += 1
                    t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0, sticky=W + E + N + S)
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[0][3 + (i * 3)]))),
                            'text': '100', 'text1': l[0][2 + (i * 3)]}
                    # g = meter(**args)

                    k += 120
                else:
                    # print( l[0][3 + (i * 3)]
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[0][3 + (i * 3)]))),
                            'text': '100', 'text1': l[0][2 + (i * 3)]}
                    # g = meter(**args)
                    k += 120
                s.append(meter(**args))
            else:
                print('for end')
            self.t_eth.append(s)
            r += 1
            s = []
        if self.no!=None and l[self.no-1] != None:
            #print( l[self.no-1],'\n\n',int(round(float(l[self.no-1][3 + (i * 3)])))
            k = 0
            t = Frame(self.fr1, width=497, height=120, bd=0, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[self.no-1]) - 2) // 3)):
                if (i + 1) % 5 == 0:
                    k = 0
                    r += 1
                    t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0, sticky=W + E + N + S)
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[self.no-1][3 + (i * 3)]))),
                            'text': '100', 'text1': l[self.no-1][2 + (i * 3)]}
                    # g = meter(**args)

                    k += 120
                else:
                    # print( l[0][3 + (i * 3)]
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[self.no-1][3 + (i * 3)]))),
                            'text': '100', 'text1': l[self.no-1][2 + (i * 3)]}
                    # g = meter(**args)
                    k += 120
                s.append(meter(**args))
            self.sc.append(s)
            r += 1
            s = []
        if l[2] != None:
            k = 7
            t = Frame(self.fr1, width=497, height=60, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[2]) - 1) // 3)):
                if (i + 1) % 5 == 0:
                    k = 7
                    r += 1
                    t = Frame(self.fr1, width=497, height=60, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0, sticky=W + E + N + S)  # root,x,y,image,text,text1
                    args = {'root': t, 'image': self.photoimage2, 'x': k, 'y': 7, 'text1': (l[2][2 + (i * 3)][2:]),
                            'text': l[2][1 + (i * 3)]}

                    k += 120
                else:
                    args = {'root': t, 'image': self.photoimage2, 'x': k, 'y': 7, 'text1': (l[2][2 + (i * 3)][2:]),
                            'text': l[2][1 + (i * 3)]}
                    k += 120
                s.append(timetemp(**args))
            self.t_eth.append(s)
            r += 1
            s = []
        else:
            k = 7
            t = Frame(self.fr1, width=497, height=60, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[0]) - 2) // 3)):
                if (i + 1) % 5 == 0:
                    k = 7
                    r += 1
                    t = Frame(self.fr1, width=497, height=60, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0, sticky=W + E + N + S)  # root,x,y,image,text,text1
                    args = {'root': t, 'image': self.photoimage2, 'x': k, 'y': 7, 'text1': '',
                            'text': l[0][2 + (i * 3)]}

                    k += 120
                else:
                    args = {'root': t, 'image': self.photoimage2, 'x': k, 'y': 7, 'text1': '',
                            'text':l[0][2 + (i * 3)]}
                    k += 120
                s.append(timetemp(**args))
            self.t_eth.append(s)
            r += 1
            s = []
        if l[2] != None:
            k = 0
            t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[2]) - 1) // 3)):
                # print( int(round(float(l[0][3 + (i * 3)])), l[0][2 + (i * 3)]
                if (i + 1) % 5 == 0:
                    k = 0
                    r += 1
                    t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0,
                           sticky=W + E + N + S)  # root,image,x,y,n=0,total=100,color='#d0e429',text='',text1=''
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[2][3 + (i * 3)][4:-1].replace("%","")))),
                            'text': 'Fan%', 'text1': l[2][1 + (i * 3)], 'total': 100}
                    # g = meter(**args)

                    k += 120
                else:
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': int(round(float(l[2][3 + (i * 3)][4:-1].replace("%","")))),
                            'text': 'Fan%', 'text1': l[2][1 + (i * 3)], 'total': 100}
                    # g = meter(**args)
                    k += 120
                s.append(perin(**args))
            self.t_eth.append(s)
            r += 1
            s = []
        else:
            k = 0
            t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
            t.grid(row=r, column=0, sticky=W + E + N + S)
            for i in range(((len(l[0]) - 2) // 3)):
                # print( int(round(float(l[0][3 + (i * 3)])), l[0][2 + (i * 3)]
                if (i + 1) % 5 == 0:
                    k = 0
                    r += 1
                    t = Frame(self.fr1, width=497, height=120, bg='white')  # ,highlightthickness=0,bd=0
                    t.grid(row=r, column=0,
                           sticky=W + E + N + S)  # root,image,x,y,n=0,total=100,color='#d0e429',text='',text1=''
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': 0,
                            'text': 'Fan%', 'text1': '', 'total': 100}
                    # g = meter(**args)

                    k += 120
                else:
                    args = {'root': t, 'image': self.photoimage1, 'x': k, 'y': 0, 'n': 0,
                            'text': 'Fan%', 'text1': '', 'total': 100}
                    # g = meter(**args)
                    k += 120
                s.append(perin(**args))
            self.t_eth.append(s)
            r += 1
            s = []
        #print( (ceil((((len(l[0])-2)/3)/4.0)))*3*120
        self.fr1.config(height=128+((ceil((((len(l[0])-2)/3)/4.0)))*(3+self.ki)*120)+50)
    def setgu(self,l):
        #print( l
        #print( self.t_eth
        if l[1] != None:
            self.t_eth[0].pro(r=int(l[1][8]), a=int(l[1][6]))
            self.t_eth[1].setpidata(a=int(l[1][6]), r=int(l[1][8]))
            self.t_eth[2].per(n=int(round(float(l[1][3]))))
            #self.t_eth[3].textset(time.ctime)
            self.t_eth[4].textset(l[1][10])
        if self.no!=None and l[self.no] != None:
            self.sc[0].pro1(r=int(l[self.no][8]), a=int(l[self.no][6]))
            self.sc[1].per(n=int(round(float(l[self.no][3]))))
        if self.no!=None and l[l[self.no-1] != None]:
            #print( self.no,'0000',l
            for i in range(((len(l[self.no-1]) - 2) // 3)):
                self.sc[2][i].per(int(round(float(l[self.no-1][3 + (i * 3)]))))
        if l[0] != None:
            for i in range(((len(l[0]) - 2)//3)):
                self.t_eth[5][i].per(int(round(float(l[0][3 + (i * 3)]))))
        if l[2] != None:
            for i in range(((len(l[2]) - 1)//3)):
                self.t_eth[6][i].textset((l[2][2 + (i * 3)][2:]))
        if l[2] != None:
            for i in range(((len(l[2]) - 1)//3)):
                self.t_eth[7][i].per(int(round(float((l[2][3 + (i * 3)][4:]).replace('%','')))))
    def er(self):
        a = Toplevel()
        self.s = errr(a)
        #a.mainloop()
    def threadt(self,h=''):
        print( 'lol t')
        st = []
        t1=0
        while "notepad.exe" in (p.name() for p in psutil.process_iter()):
            se = ''
            se1=''
            if self.event1.is_set()==True or h!='':
                time.sleep(1)
                #print( 1
                #quotes = urllib.request.urlopen("http://175.127.140.36:9001/")#"http://1.53.110.4:3001/")#"http://106.244.93.179:9001/")#"http://95.85.85.53:4443/")
                #print( quotes.read(), 'hgjghj')
                
                
                quotes="""
<html><body bgcolor="#000000" style="font-family: monospace;">
{"result": ["10.0 - ETH", "7249", "105717;24296;249", "29340;23489;29328;23559", "2642936;15529;275", "733502;587234;733219;588981", "68;58;68;64;69;61;69;63", "eth-ru2.dwarfpool.com:8008;dcr.coinmine.pl:2222", "177;13;0;1"]}<br><br>&nbsp;<font color="#00ff00"> DCR: Share accepted (83 ms)!
</font><br>&nbsp;<font color="#00ff00"> DCR: 01/16/18-14:42:30 - SHARE FOUND - (GPU 0)
</font><br>&nbsp;<font color="#00ff00"> DCR: Share accepted (83 ms)!
</font><br><font color="#ffffff">ETH: 01/16/18-14:42:34 - New job from eth-ru2.dwarfpool.com:8008
</font><br><font color="#00ffff">ETH - Total Speed: 111.560 Mh/s, Total Shares: 24294, Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.329 Mh/s, GPU1 29.366 Mh/s, GPU2 29.328 Mh/s, GPU3 23.536 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2788.993 Mh/s, Total Shares: 15527, Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.219 Mh/s, GPU1 734.159 Mh/s, GPU2 733.210 Mh/s, GPU3 588.405 Mh/s
</font><br><font color="#ffffff">ETH: 01/16/18-14:42:39 - New job from eth-ru2.dwarfpool.com:8008
</font><br><font color="#00ffff">ETH - Total Speed: 111.486 Mh/s, Total Shares: 24294, Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.308 Mh/s, GPU1 29.327 Mh/s, GPU2 29.350 Mh/s, GPU3 23.502 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2787.157 Mh/s, Total Shares: 15527, Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 732.700 Mh/s, GPU1 733.165 Mh/s, GPU2 733.748 Mh/s, GPU3 587.544 Mh/s
</font><br><font color="#ffffff">ETH: 01/16/18-14:42:45 - New job from eth-ru2.dwarfpool.com:8008
</font><br><font color="#00ffff">ETH - Total Speed: 105.854 Mh/s, Total Shares: 24294, Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.334 Mh/s, GPU1 29.408 Mh/s, GPU2 23.585 Mh/s, GPU3 23.526 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2646.356 Mh/s, Total Shares: 15527, Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.356 Mh/s, GPU1 735.212 Mh/s, GPU2 589.635 Mh/s, GPU3 588.153 Mh/s
</font><br><font color="#ff00ff">GPU0 t=68C fan=55%, GPU1 t=69C fan=64%, GPU2 t=69C fan=61%, GPU3 t=69C fan=63%
</font><br><font color="#ffffff">
</font><br><font color="#00ff00">GPU #0: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #1: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #2: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #3: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ffff">ETH - Total Speed: 111.668 Mh/s, Total Shares: 24294(6349+6297+6240+5893), Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.379 Mh/s, GPU1 29.388 Mh/s, GPU2 29.347 Mh/s, GPU3 23.553 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2791.687 Mh/s, Total Shares: 15527(3942+3825+3913+3855), Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 734.479 Mh/s, GPU1 734.708 Mh/s, GPU2 733.666 Mh/s, GPU3 588.834 Mh/s
</font><br><font color="#00ffff">Incorrect ETH shares: GPU0 34, GPU1 48, GPU2 48, GPU3 47
</font><br>&nbsp;<font color="#00ffff">1 minute average ETH total speed: 111.260 Mh/s
</font><br><font color="#ffffff">Pool switches: ETH - 13, DCR - 1
</font><br><font color="#ffffff">Current ETH share target: 0x0000000225c17d04 (diff: 2000MH), epoch 163(2.27GB)
Current DCR share target: 0x00000000117580fe (diff: 62GH), block #204331
</font><br><font color="#ff00ff">GPU0 t=68C fan=55%, GPU1 t=69C fan=64%, GPU2 t=69C fan=62%, GPU3 t=68C fan=63%
</font><br><font color="#ffffff">
</font><br><font color="#ffffff">ETH: 01/16/18-14:42:51 - New job from eth-ru2.dwarfpool.com:8008
</font><br><font color="#00ffff">ETH - Total Speed: 117.332 Mh/s, Total Shares: 24294, Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.330 Mh/s, GPU1 29.317 Mh/s, GPU2 29.339 Mh/s, GPU3 29.345 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2933.298 Mh/s, Total Shares: 15527, Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.247 Mh/s, GPU1 732.937 Mh/s, GPU2 733.484 Mh/s, GPU3 733.630 Mh/s
</font><br><font color="#ffffff">
</font><br><font color="#00ff00">GPU #0: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #1: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #2: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #3: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ffff">ETH - Total Speed: 117.348 Mh/s, Total Shares: 24294(6349+6297+6240+5893), Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.330 Mh/s, GPU1 29.317 Mh/s, GPU2 29.339 Mh/s, GPU3 29.362 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2933.709 Mh/s, Total Shares: 15527(3942+3825+3913+3855), Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.247 Mh/s, GPU1 732.937 Mh/s, GPU2 733.484 Mh/s, GPU3 734.041 Mh/s
</font><br><font color="#00ffff">Incorrect ETH shares: GPU0 34, GPU1 48, GPU2 48, GPU3 47
</font><br>&nbsp;<font color="#00ffff">1 minute average ETH total speed: 111.352 Mh/s
</font><br><font color="#ffffff">Pool switches: ETH - 13, DCR - 1
</font><br><font color="#ffffff">Current ETH share target: 0x0000000225c17d04 (diff: 2000MH), epoch 163(2.27GB)
Current DCR share target: 0x00000000117580fe (diff: 62GH), block #204331
</font><br><font color="#ff00ff">GPU0 t=68C fan=55%, GPU1 t=69C fan=64%, GPU2 t=69C fan=62%, GPU3 t=69C fan=63%
</font><br><font color="#ffffff">
</font><br><font color="#ffffff">
</font><br><font color="#00ff00">GPU #0: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #1: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #2: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #3: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ffff">ETH - Total Speed: 105.642 Mh/s, Total Shares: 24294(6349+6297+6240+5893), Rejected: 249, Time: 120:47
</font><br><font color="#00ffff">ETH: GPU0 29.396 Mh/s, GPU1 23.580 Mh/s, GPU2 29.186 Mh/s, GPU3 23.479 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2641.037 Mh/s, Total Shares: 15527(3942+3825+3913+3855), Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 734.900 Mh/s, GPU1 589.511 Mh/s, GPU2 729.655 Mh/s, GPU3 586.971 Mh/s
</font><br><font color="#00ffff">Incorrect ETH shares: GPU0 34, GPU1 48, GPU2 48, GPU3 47
</font><br>&nbsp;<font color="#00ffff">1 minute average ETH total speed: 111.275 Mh/s
</font><br><font color="#ffffff">Pool switches: ETH - 13, DCR - 1
</font><br><font color="#ffffff">Current ETH share target: 0x0000000225c17d04 (diff: 2000MH), epoch 163(2.27GB)
Current DCR share target: 0x00000000117580fe (diff: 62GH), block #204331
</font><br><font color="#ff00ff">GPU0 t=68C fan=55%, GPU1 t=68C fan=64%, GPU2 t=69C fan=62%, GPU3 t=68C fan=62%
</font><br><font color="#ffffff">
</font><br>&nbsp;<font color="#00ff00"> DCR: 01/16/18-14:43:00 - SHARE FOUND - (GPU 0)
</font><br>&nbsp;<font color="#00ff00"> DCR: Share accepted (83 ms)!
</font><br><font color="#00ff00">ETH: 01/16/18-14:43:02 - SHARE FOUND - (GPU 0)
</font><br><font color="#00ff00">ETH: Share accepted (27 ms)!
</font><br><font color="#ffffff">ETH: 01/16/18-14:43:11 - New job from eth-ru2.dwarfpool.com:8008
</font><br><font color="#00ffff">ETH - Total Speed: 105.757 Mh/s, Total Shares: 24295, Rejected: 249, Time: 120:48
</font><br><font color="#00ffff">ETH: GPU0 29.346 Mh/s, GPU1 23.553 Mh/s, GPU2 29.345 Mh/s, GPU3 23.513 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2643.923 Mh/s, Total Shares: 15528, Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.639 Mh/s, GPU1 588.823 Mh/s, GPU2 733.630 Mh/s, GPU3 587.831 Mh/s
</font><br><font color="#00ff00">ETH: 01/16/18-14:43:12 - SHARE FOUND - (GPU 0)
</font><br><font color="#00ff00">ETH: Share accepted (44 ms)!
</font><br>&nbsp;<font color="#ffffff"> DCR: 01/16/18-14:43:18 - New job from dcr.coinmine.pl:2222
</font><br><font color="#ff00ff">GPU0 t=68C fan=56%, GPU1 t=69C fan=63%, GPU2 t=69C fan=61%, GPU3 t=69C fan=62%
</font><br>&nbsp;<font color="#00ff00"> DCR: 01/16/18-14:43:25 - SHARE FOUND - (GPU 2)
</font><br>&nbsp;<font color="#00ff00"> DCR: Share accepted (83 ms)!
</font><br><font color="#ff00ff">GPU0 t=68C fan=53%, GPU1 t=69C fan=64%, GPU2 t=69C fan=61%, GPU3 t=68C fan=62%
</font><br><font color="#ffffff">
</font><br><font color="#00ff00">GPU #0: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #1: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #2: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ff00">GPU #3: Ellesmere, 4085 MB available, 36 compute units
</font><br><font color="#00ffff">ETH - Total Speed: 105.718 Mh/s, Total Shares: 24296(6351+6297+6240+5893), Rejected: 249, Time: 120:49
</font><br><font color="#00ffff">ETH: GPU0 29.340 Mh/s, GPU1 23.489 Mh/s, GPU2 29.329 Mh/s, GPU3 23.559 Mh/s
</font><br>&nbsp;<font color="#ffff00"> DCR - Total Speed: 2642.936 Mh/s, Total Shares: 15529(3943+3825+3914+3855), Rejected: 275
</font><br>&nbsp;<font color="#ffff00"> DCR: GPU0 733.502 Mh/s, GPU1 587.234 Mh/s, GPU2 733.219 Mh/s, GPU3 588.981 Mh/s
</font><br><font color="#00ffff">Incorrect ETH shares: GPU0 34, GPU1 48, GPU2 48, GPU3 47
</font><br>&nbsp;<font color="#00ffff">1 minute average ETH total speed: 111.882 Mh/s
</font><br><font color="#ffffff">Pool switches: ETH - 13, DCR - 1
</font><br><font color="#ffffff">Current ETH share target: 0x0000000225c17d04 (diff: 2000MH), epoch 163(2.27GB)
Current DCR share target: 0x00000000117580fe (diff: 62GH), block #204331
</font><br><font color="#ff00ff">GPU0 t=68C fan=58%, GPU1 t=68C fan=64%, GPU2 t=69C fan=61%, GPU3 t=69C fan=63%
</font><br><font color="#ffffff">
</font><br></body></html>

"""
                getj = (str(quotes).replace('<br><br>&nbsp;', '\n').replace('<br><br>', '\n').replace('big\n','big').split('\n')[2:-2]
                        )
                '''
                getj = (str(quotes.read()).replace('<br><br>&nbsp;', '\n').replace('<br><br>', '\n').replace('big\n','big').split('\n')#[2:-2]
                        )'''
                print('getj==',getj)
                #print( 2

                l = ['ETH:', 'ETH-', 'GPU0','SC:','SC-', 'DCR:','DCR-','PASC:','PASC-']
                l1 = [None, None, None, None, None, None, None, None, None]
                for i in range(len(getj)):



                    if "#ff0000" in getj[i]and getj[i] not in st:
                        #print( getj[i]
                        if "#ff0000" not in getj[i-1]:
                            se=str(getj[i]).replace('<fontcolor="#ff0000">','').replace('<font color="#ff0000">','').replace('</font><br>','').replace(' ','').replace('&nbsp;','').replace('<br>','').replace('</font>','')
                        else:
                            se += '\n' + str(getj[i]).replace('<fontcolor="#ff0000">','').replace('<font color="#ff0000">','').replace('</font><br>','').replace(' ','').replace('&nbsp;','').replace('<br>','').replace('</font>','')#
                    if ("#ffffff"in getj[i]) and (l[0] not in getj[i])   and(l[3] not in getj[i])   and(l[5] not in getj[i])   and(l[7] not in getj[i])and ((getj[i] not in st)and('</font><br>'+getj[i]not in st))and 'Dev' not in getj[i] :
                        if "#ffffff"not in getj[i-1]and str(getj[i])[33:]!=' ':
                            se1 = str(getj[i]).replace('<font color="#ffffff">','').replace('</font><br>','').replace('&nbsp;','').replace('<br>','').replace('</font>','')
                        else:
                            if str(getj[i]).replace('<font color="#ffffff">','').replace('</font><br>','')!=' ':
                                se1 += '\n'+(str(getj[i]).replace('<font color="#ffffff">','').replace('</font><br>','').replace('&nbsp;','').replace('<br>','').replace('</font>',''))







                    if getj[i] not in st and "#ff0000" not in getj[i]:
                        p = getj[i].replace('</font><br><font color=', '').replace('</font><br>&nbsp;<font color=',
                                                                                   '').replace('<font color=',
                                                                                               '').replace(
                            '"', '').replace('>', ' ').replace('  ', ' ').replace(' -', '-').replace(',', '').replace(
                            'Total ', 'Total').split(' ')
                        #print( p
                        try:  #            0       1       2       3     4     5       6       7       8
                            if ('GPU' in p[1] and "#ff00ff" in p[0] )or p[1] in ['ETH:', 'ETH-', 'GPU0', 'SC:', 'SC-', 'DCR:', 'DCR-', 'PASC:', 'PASC-']:
                                if p[1] == l[0] and 'GPU' in p[2]:
                                    l1[0] = p
                                if p[1] == l[3] and 'GPU' in p[2]:
                                    l1[3] = p
                                if p[1] == l[5] and 'GPU' in p[2]:
                                    l1[5] = p
                                if p[1] == l[7] and 'GPU' in p[2]:
                                    l1[7] = p
                                if p[1] == l[1]:
                                    s12 = ''
                                    for i in p[6]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[6] = s12
                                    s12 = ''
                                    for i in p[8]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[8] = s12
                                    l1[1] = p
                                if p[1] == l[4]:
                                    s12 = ''
                                    for i in p[6]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[6] = s12
                                    s12 = ''
                                    for i in p[8]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[8] = s12
                                    l1[4] = p
                                if p[1] == l[6]:
                                    s12 = ''
                                    for i in p[6]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[6] = s12
                                    s12 = ''
                                    for i in p[8]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[8] = s12
                                    l1[6] = p
                                if p[1] == l[8]:
                                    s12 = ''
                                    for i in p[6]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[6] = s12
                                    s12 = ''
                                    for i in p[8]:
                                        if i != "(":
                                            s12 += i
                                        else:
                                            break
                                    p[8] = s12
                                    l1[8] = p
                                #print( p

                                if 'GPU' in p[1] or p[1] == l[2]:
                                    #print( 'yes'
                                    l1[2] = p
                            else:
                                pass
                        except:
                            pass
                try:
                    if se!='' and h == '':
                        self.s.set('error:'+se, "red")
                    if se1!='' and h == '':
                        self.s.set(se1, "white")
                except:
                    pass

                if st == [] and h != '':
                    a = Toplevel()
                    self.s = errr(a)
                    return l1
                else:
                    self.setgu(l1)
                st = getj
            else:
                time.sleep(2)
        else:
            if h!='':
                time.sleep(5)
                return(self.threadt(h='k'))
    def StartMove(self,event):
        #print( 'clear'
        self.event1.clear()
    def StopMove(self,event):
        #print( 'set'
        self.event1.set()
    def main(self):
        #print( active_count(),'0000000000000',enumerate()
        self.can11=Canvas(self.f2,width=497,height=563 ,bd=0,bg='#ffffff', relief=FLAT,highlightthickness=0)#
        self.can11.place(x=0,y=0)
        self.srl1=Scrollbar(self.f2, command=self.can11.yview)
        self.srl1.place(x=447,y=0,width=50, height=563)
        self.can11.configure(yscrollcommand = self.srl1.set)
        self.can11.bind('<Configure>', self.on_configure1)
        self.srl1.bind("<ButtonPress-1>", self.StartMove)
        self.srl1.bind("<ButtonRelease-1>", self.StopMove)
        self.fr1= Frame(self.can11,width=497,height=563, bd=0,relief=FLAT)#change hight and every thing gosr nice
        self.can11.create_window((0,0),width=499,window=self.fr1,anchor='nw')
        self.plzwait=Label(self.fr1,text='Please wait miner is starting.....')
        self.plzwait.grid(row=0, column=0, sticky=W + E + N + S, padx=1, pady=1)
        self.setgui()
        #'''
        self.thd= Thread(target=self.threadt,args=())
        self.thd.start()
        #'''
#zx=setframe(f[2])
zx=para(f[1])
root.mainloop()
