from tkinter import *
from tkinter import ttk,messagebox
import requests
from ctypes import windll
import webbrowser
from threading import*


root=Tk()
root.title("Bdix Tester") 
root.overrideredirect(True)
root.geometry('800x390+250+120')
root.iconbitmap("resource/title_icon.ico")


im1="resource/a5.gif"
background_1=PhotoImage(file="resource/background_1.png")
button1=PhotoImage(file="resource/b1.png")
button2=PhotoImage(file="resource/b2.png")
button3=PhotoImage(file="resource/b3.png")
button4=PhotoImage(file="resource/b4.png")
b1=PhotoImage(file="resource/b5.png")
b2=PhotoImage(file="resource/b6.png")
b3=PhotoImage(file="resource/back.png")
b_nextwindowall=PhotoImage(file="resource/all.png")
b_nextwindowmovie=PhotoImage(file="resource/movie.png")
b_nextwindowftp=PhotoImage(file="resource/ftp.png")
b_nextwindowtv=PhotoImage(file="resource/tv.png")
b_nextwindowfamous=PhotoImage(file="resource/famous.png")
b_nextwindowcopy=PhotoImage(file="resource/copy.png")
background_2=PhotoImage(file="resource/background_2.png")
btn_yes=PhotoImage(file="resource/yes.png")
btn_no=PhotoImage(file="resource/no.png")
frames = [PhotoImage(file=im1,format = 'gif -index %i' %(i)) for i in range(60)]


famous=open("resource/famous_ftp.txt","r+")
ftp=open("resource/ftp_server.txt","r+")
movie=open("resource/movie_server.txt","r+")
tv=open("resource/tv_server.txt","r+")


famous_data=famous.read().split()
ftp_data=ftp.read().split()
movie_data=movie.read().split()
tv_data=tv.read().split()


set_timeout=IntVar()


g=False
func_start_checker=0
stop_anim=None
func_stop_checker=0

famous_ftp_server=[]
ftp_server=[]
movie_server=[]
tv_server=[]

famous_ftp_server_final=[]
ftp_server_final=[]
movie_server_final=[]
tv_server_final=[]
all_server_final=[]



def list_maker(input_data,output_list):
    for i in input_data:
        output_list.append(i)

list_maker(famous_data,famous_ftp_server)
list_maker(ftp_data,ftp_server)
list_maker(movie_data,movie_server)
list_maker(tv_data,tv_server)

root.minimized = False
root.maximized = False


LGRAY = '#3e4042'
DGRAY = 'black'
RGRAY = '#333230'
FRGB='#66ffff' 

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)



title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)
title_bar.grid(row=0,column=0,sticky="wen")

win_1st=Frame(root,borderwidth=0,highlightthickness=0,bg="black")
win_1st.grid(row=1,column=0)

win_2nd=Frame(root,borderwidth=0,highlightthickness=0)
win_2nd.grid(row=1,column=0)


def set_appwindow(mainWindow):

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def minimize_me():
    root.attributes("-alpha",0)
    root.minimized = True       

def deminimize(event):

    root.focus() 
    root.attributes("-alpha",1)
    if root.minimized == True:
        root.minimized = False  

def show_frame(frame_raise):
    frame_raise.tkraise()

def server_check(input_list,output_list,timeout): 
    try:
        request_response = requests.head(input_list,timeout=set_timeout.get())
        
        if request_response.status_code == 200:
            output_list.append(input_list)
            all_server_final.append(input_list)

    except:
        pass

    
def start_():
    count=0
    famous_ftp_server_len=len(famous_ftp_server)
    ftp_server_len=len(ftp_server)
    movie_server_len=len(movie_server)
    tv_server_len=len(tv_server)
    total_server=len(ftp_server)+len(movie_server)+len(tv_server)+len(famous_ftp_server)
    devider=total_server
    global func_start_checker
    func_start_checker=1
    root.after(0,update,0)

    def get_timeout():
        timeout=set_timeout.get()
        return timeout
    
    timeout=get_timeout()


    for i in range(10000):
        if count==1 and famous_ftp_server_len>=1:
            server_check(famous_ftp_server[0],famous_ftp_server_final,timeout)
            del famous_ftp_server[0]
            famous_ftp_server_len-=1
            total_server-=1
        elif count==2 and ftp_server_len>=1:
            server_check(ftp_server[0],ftp_server_final,timeout)
            del ftp_server[0]
            ftp_server_len-=1
            total_server-=1
        elif count==3 and movie_server_len>=1:
            server_check(movie_server[0],movie_server_final,timeout)
            del movie_server[0]
            movie_server_len-=1
            total_server-=1
        elif count==4 and tv_server_len>=1:
            server_check(tv_server[0],tv_server_final,timeout)
            del tv_server[0]
            tv_server_len-=1
            total_server-=1
        else:
            pass
        if devider>=1:
            par=(total_server*100)//devider

        if total_server>=10:
            parcentage=100-par
        elif total_server>=1:
            parcentage=99
        else:
            parcentage=100
    
        if count==4:
            count=0    
        count+=1

        if g:
            break
    
        if famous_ftp_server_len==0 and ftp_server_len==0 and movie_server_len==0 and tv_server_len==0:
            break
        
        parcentage_shower.set(f"{parcentage}%")
        

    root.after(1,start_)
    global stop_anim
    root.after_cancel(stop_anim)

    parcentage_shower.set("100%")
    total_active_server=len(all_server_final)
    parcentage_shower.set(f"Total Active Server :  {total_active_server}")
    label4.place(x=200,y=37)
    
    famous_ftp_index_list=[]
    ftp_server_index_list=[]
    movie_server_index_list=[]
    tv_server_index_list=[]
    all_server_index_list=[]

    def index_number_generator(index_list,source_list):
        for x in range(1,len(source_list)):
            index_list.append(x)

    index_number_generator(famous_ftp_index_list,famous_ftp_server_final)
    index_number_generator(ftp_server_index_list,ftp_server_final)
    index_number_generator(movie_server_index_list,movie_server_final)
    index_number_generator(tv_server_index_list,tv_server_final)
    index_number_generator(all_server_index_list,all_server_final)

    global famous_ftp_server_tuples
    global ftp_server_tuples
    global movie_server_tuples
    global tv_server_tuples
    global all_server_tuples

    famous_ftp_server_tuples=tuple(zip(famous_ftp_index_list,famous_ftp_server_final))
    ftp_server_tuples=tuple(zip(ftp_server_index_list,ftp_server_final))
    movie_server_tuples=tuple(zip(movie_server_index_list,movie_server_final))
    tv_server_tuples=tuple(zip(tv_server_index_list,tv_server_final))
    all_server_tuples=tuple(zip(all_server_index_list,all_server_final))
    global func_stop_checker
    func_stop_checker=1


def stop_animation():
        global stop_anim

        if func_start_checker==10:
            root.after_cancel(stop_anim)
        else:
            pass
        root.after(1,stop_animation)


def start_thrading_1():
    if func_start_checker==0:
        try:
            #internet_connection_check=requests.head("https://www.google.com",timeout=5)
        
            t1=Thread(target=start_)
            t1.start()
       
        except:
            show_error=messagebox.showerror("Network not connected","Check your internet connection")

    else:
        pass
        root.after(1,start_thrading_1)

def window_2_opener(frame):
    global back_button

    if func_stop_checker==0 and func_start_checker==1:
        top=Toplevel(root)
        bg_="#333230"
        top.geometry("400x120+450+250")
        top.iconbitmap("resource/title_icon.ico")
        top.maxsize(400,120)
        top.minsize(400,120)
        top.configure(bg=bg_)
    
        def output(data):
            if data==1:
                stop_process()
                t2=Thread(target=show_frame(frame))
                t2.start()
                back_button.pack(side=LEFT,ipadx=7,ipady=10)
                top.destroy()     
            else:
                top.destroy()
                pass

        text_lable_1=Label(top,text="Please wait until the test is finished or select yes  ",bg="#333230",fg="#66ffff",font=(15))
        text_lable_1.place(x=32,y=20)

        text_lable_2=Label(top,text="if you went to stop the test and view the server list",bg="#333230",fg="#66ffff",font=(15))
        text_lable_2.place(x=25,y=50)

        button_yes=Button(top,image=btn_yes,background=bg_,activebackground=bg_,borderwidth=0,command=lambda:output(1))
        button_yes.place(x=50,y=80)

        button_no=Button(top,image=btn_no,background=bg_,activebackground=bg_,borderwidth=0,command=lambda:output(0))
        button_no.place(x=300,y=80)   
    
    else:
        t2=Thread(target=show_frame(frame))
        t2.start()
        back_button.pack(side=LEFT,ipadx=7,ipady=10)
    
def window_1st_opener(frame):
    back_button.pack_forget()
    t3=Thread(target=show_frame(frame))
    t3.start()
    
def stop_process():
    global g
    g=True

def update(ind):

    global stop_anim
    frame = frames[ind]
    ind += 1
    if ind == 60:
        ind = 0
    label.configure(image=frame)
    stop_anim=root.after(50, update, ind)


frm=Frame(win_1st,width=400)
frm.grid(row=0,column=0)

label2=Label(win_1st,image=background_1)

label2.grid(row=0,column=0)

label = Label(win_1st,image=frames[0],bg="black")
label.place(x=0,y=100)

parcentage_shower=StringVar()

parcentage_shower.set("00%")

label4=Label(win_1st,textvariable=parcentage_shower,bg="black",fg="#00ffff",font=("Arial",30))
label4.place(x=340,y=37)

btn_1=Button(win_1st,image=button1,background="black",borderwidth=0,activebackground="black",command=start_thrading_1)
btn_1.place(x=40,y=265)

btn_2=Button(win_1st,image=button4,bg="black",borderwidth=0,activebackground="black")
btn_2.place(x=280,y=265)

btn_2=Button(win_1st,image=button2,bg="black",borderwidth=0,activebackground="black",command=stop_process)
btn_2.place(x=650,y=265)

btn_4=Button(win_1st,image=button3,borderwidth=0,bg="black",activebackground="black",command=lambda:window_2_opener(win_2nd))
btn_4.place(x=280,y=195)

style=ttk.Style()

style.theme_use("clam")
style.configure("BW.TLabel",background='black', foreground='#00ffff',selectbackground="black",selectforeground='red',insertbackground="black",fieldbackground= 'blue')
combo_box1=ttk.Combobox(win_1st,width=2,font=("#00ffff",25),style="BW.TLabel",textvariable=set_timeout)
combo_box1["values"]=("01","02","03","04","05")
combo_box1["state"]="readonly"
combo_box1.current(0)
combo_box1.place(x=480,y=270)

def tree(tuple):

    def link_opener(a):
        select=treeview.focus()
        values=treeview.item(select,"values")
        val=values[1]
        webbrowser.open(val)

    def seleacted(b):
        select=treeview.focus()
        values=treeview.item(select,"values")
        val=values[1]
        def copy():
            win_2nd.clipboard_clear()
            win_2nd.clipboard_append(val)
        btn_copy=Button(image=b_nextwindowcopy,command=copy,activebackground="black",highlightthickness=0,borderwidth=0,background="black")
        btn_copy.place(x=10,y=335)


    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
    background="#b3b3b3",
    foreground="red",
    rowheight=32,
    fieldbackground="#b3b3b3",

    )

    style.map("Treeview",
    background=[("selected","#333230")])

    treeview = ttk.Treeview(win_2nd,style="mystyle.Treeview")

    treeview["columns"]=("ID","SERVER LIST")

    treeview.column("#0",width=0,stretch=NO)
    treeview.column("ID",width=40,stretch=FALSE)
    treeview.column("SERVER LIST",width=470,stretch=FALSE)

    treeview.heading("#0",text="nothing")
    treeview.heading("ID",text="ID")
    treeview.heading("SERVER LIST",text="SERVER LIST")

    count=0

    for data in tuple:
        treeview.insert(parent="",index="end",iid=count,text=count,values=(data[0],data[1]))
        count +=1


    treeview.place(x=286,y=10)

    treeview.bind('<Double-Button-1>',link_opener)
    treeview.bind("<ButtonRelease-1>",seleacted)

def start_thrading_2(tuples):
    t2=Thread(target=tree(tuples))
    t2.start()

tree_frame=Frame(win_2nd)
tree_frame.place(x=200,y=0)

labal=Label(win_2nd,image=background_2)
labal.pack()

btn_all=Button(win_2nd,image=b_nextwindowall,activebackground="black",highlightthickness=0,borderwidth=0,background="black",command= lambda:start_thrading_2(all_server_tuples))
btn_all.place(x=10,y=10)

btn_movie=Button(win_2nd,image=b_nextwindowmovie,activebackground="black",highlightthickness=0,borderwidth=0,background="black",command= lambda: start_thrading_2(movie_server_tuples))
btn_movie.place(x=10,y=70)

btn_ftp=Button(win_2nd,image=b_nextwindowftp,activebackground="black",highlightthickness=0,borderwidth=0,background="black",command=lambda:start_thrading_2(ftp_server_tuples))
btn_ftp.place(x=10,y=130)

btn_tv=Button(win_2nd,image=b_nextwindowtv,activebackground="black",highlightthickness=0,borderwidth=0,background="black",command=lambda:start_thrading_2(tv_server_tuples))
btn_tv.place(x=10,y=250)

btn_famous=Button(win_2nd,image=b_nextwindowfamous,activebackground="black",highlightthickness=0,borderwidth=0,background="black",command=lambda:start_thrading_2(famous_ftp_server_tuples))
btn_famous.place(x=10,y=190)

close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 15),bd=0,fg=FRGB,highlightthickness=0,activebackground=RGRAY,activeforeground=FRGB)
minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg=FRGB,font=("calibri", 15),highlightthickness=0,activebackground=RGRAY,activeforeground=FRGB)
back_button = Button(title_bar, text=' 🡸 ',command=lambda: window_1st_opener(win_1st),bg=RGRAY,padx=2,pady=2,bd=0,fg=FRGB,font=("calibri", 15),highlightthickness=0,activebackground=RGRAY,activeforeground=FRGB)

title_bar_title = Label(title_bar, text="BDIX TESTER BY BORANNO GOLDER", bg=RGRAY,bd=0,fg=FRGB,font=("helvetica", 15),highlightthickness=0)

window = Frame(root, bg=DGRAY,highlightthickness=0)

close_button.pack(side=RIGHT,ipadx=7,ipady=10)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=10)

title_bar_title.place(x=210,y=5)

def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=RGRAY

def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=RGRAY

def change_bg_on_hovering(event):
    global back_button
    back_button['bg']=LGRAY
def return_orginal_color(event):
    global back_button
    back_button['bg']=RGRAY

def get_pos(event):
    if root.maximized == False:
        
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

        def release_window(event):
            root.config(cursor="arrow")
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        pass

title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos)

close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)
back_button.bind('<Enter>', change_bg_on_hovering)
back_button.bind('<Leave>', return_orginal_color)

root.bind("<FocusIn>",deminimize)

window_1st_opener(win_1st)

root.mainloop()