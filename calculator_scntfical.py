from tkinter import*
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime
import math
import cmath

root= Tk()
root.title("Calculator") #it will give a title   

root.geometry("820x400")
root.configure(background= "black")
#----------------------------------------------Variables------------------------------------------------

display= StringVar()
exp= ""
#----------------------------------------------func def------------------------------------------------

today = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
display.set(today)
    
def to_add():
    global exp
    sign= "+"
    exp= exp + sign
    display.set(exp)

def to_equal():
    try:


        global exp
        exp=  str(eval(exp))
        display.set(exp)

    except SyntaxError:
        display.set("Invalid Expression")
        #messagebox.showinfo(title="Warning: ", message="Expression is not valid, please double check ...")



def to_multply():
    global exp
    sign= "*"
    exp= exp + sign
    display.set(exp)

def to_subtract():
    global exp
    sign= "-"
    exp= exp + sign
    display.set(exp)

def to_divide():
    global exp
    sign= "/"
    exp= exp + sign
    display.set(exp)

def precentage():
    global exp
    sign= "%"
    exp= exp + sign
    display.set(exp)


def to_stop():
    global exp
    sign= "."
    exp= exp + sign
    display.set(exp)

#----------------------------------------------scientific func def------------------------------------------------

def to_int():
    try: 
        global exp
        exp= str(int(float(exp)))
        display.set(exp)
    except ValueError:
        display.set("Invalid Expression")

def to_sqr():
    global exp
    
    exp= str(math.pow(float(exp),2))
    display.set(exp)

def to_factorial():
    global exp
    
    exp= str(math.factorial(int(exp)))
    display.set(exp) 

def to_hyperbola():
    try:
        
        global exp

        if exp == "0":
            x= str(cmath.sinh(int(exp)))
        else:
            x =str(cmath.sinh(int(exp)))
            exp= x.replace(x[-4:], "").replace(x[:1],"")
            display.set(exp)
    except ValueError:
        display.set("Invalid Expression")
    
    

def to_sin():
    try:
        
        global exp
        
        exp =str(math.sin(math.radians(float(exp))))
        display.set(exp)
    except ValueError:
        display.set("Invalid Expression")    

        

def to_dms():
    global exp
    sign= "dms"
    exp= exp + sign
    display.set(exp)            
    
def to_coshyperbolic():
    try:
        
        global exp

        if exp == "0":
            x= str(cmath.cosh(int(exp)))
        else:
            x =str(cmath.cosh(int(exp)))
            exp= x.replace(x[-4:], "").replace(x[:1],"")
            display.set(exp)
    except ValueError:
        display.set("Invalid Expression")
    
                

def to_cosine():
    try:
        
        global exp
        
        exp =str(math.cos(math.radians(float(exp))))
        display.set(exp)
    except ValueError:
        display.set("Invalid Expression")
    
    
    

def to_sqrt():
    global exp
    
    exp=  str(math.sqrt(float(exp)))
    display.set(exp)

def to_power():
    global exp
    sign= "**"   
    exp= exp + sign
    display.set(exp)


def cube_x():
    global exp
    
    exp= str(math.pow(float(exp),3))
    display.set(exp)

def log_x():
    global exp
    
    exp= str(math.log(float(exp)))
    display.set(exp)

def ln_x():
    global exp
    
    exp= str(math.log(float(exp),float(2.718)))
    display.set(exp)

def to_erase():
    global exp
    
    exp=exp[:-1]
    display.set(exp)

def to_make_neg():
    global exp
    
    exp= str(int(exp)*-1)
    display.set(exp)

def to_make_pos():
    global exp
    
    exp= str(abs(int(exp)))
    display.set(exp)

def to_rec():
    global exp
    
    exp=str(math.pow(float(exp),float(-1)))
    display.set(exp)

    
def to_make_Red():
    txtdisplay.configure(bg= "light cyan", fg="red")

def to_make_gren():   #RRGGBB  #FFFFFF
    txtdisplay.configure(bg= "light salmon", fg="green")

    
def to_make_yel():
    #Entry(Display_frame, font=("arial", 35, "bold"), textvariable= display, bd=10, bg= "YELLOW", fg="RED", insertwidth= 2, justify= RIGHT)
    txtdisplay.configure(bg= "#888888", fg="#123456")
 

def to_clr():
    global exp
    
    exp= ""
    display.set(exp)

def to_exit():
    today = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    display.set(today)
    iExit= tkinter.messagebox.askyesno("MY Scientific CALC", "Please confirm if you wish to exit")
    if iExit > 0:
        root.destroy()

#----------------------------------------------NUmber entry func def------------------------------------------------

def Num_0():
    global exp
    num= "0"
    exp= exp + num
    display.set(exp)
  
def Num_1():
    global exp
    num1= "1"
    exp= exp + num1
    display.set(exp)

def Num_2():
    global exp
    num2= "2"
    exp= exp + num2
    display.set(exp)

def Num_3():
    global exp
    num3= "3"
    exp= exp + num3
    display.set(exp)

def Num_4():
    global exp
    num4= "4"
    exp= exp + num4
    display.set(exp)

def Num_5():
    global exp
    num5= "5"
    exp= exp + num5
    display.set(exp)
    
def Num_6():
    global exp
    num6= "6"
    exp= exp + num6
    display.set(exp)
    
def Num_7():
    global exp
    num7= "7"
    exp= exp + num7
    display.set(exp)
   
def Num_8():
    global exp
    num8= "8"
    exp= exp + num8
    display.set(exp)
    

def Num_9():
    global exp
    num9= "9"
    exp= exp + num9
    display.set(exp)
    

#---------------------------------------For heading and frames---------------------------------------

MainFrame= Frame(root)
MainFrame.grid()

Top= Frame(MainFrame, bd= 15, width= 900, relief= RIDGE)
Top.pack(side= TOP)

MainTitle= Label(Top, font=("arial", 20, "bold"), text= "Scientific Calculator")
MainTitle.grid()

btn_Display_frame = Frame(MainFrame, bd= 10, width= 900, height= 50, relief= RIDGE)
btn_Display_frame.pack(side= BOTTOM)

Display_frame = Frame(btn_Display_frame, bd= 5, width= 900, height= 40, relief= RIDGE)
#Display_frame.pack(side= BOTTOM)
Display_frame.grid(row=0, column=0)

Button_frame = Frame(btn_Display_frame, bd= 10, width= 900, height= 400, relief= RIDGE)
Button_frame.grid(row=1, column=0)



#---------------------------------------For dispay---------------------------------------

# txt_display= Text(Display_frame, width=60, height= 10, font= ("arial", 10, "bold"))
# txt_display.grid(row=0, column=0)


txtdisplay= Entry(Display_frame, font=("arial", 35, "bold"), textvariable= display, bd=10, bg= "black", fg="white", insertwidth= 2, justify= RIGHT)
txtdisplay.grid(row=0, column=0)


#---------------------------------------For buttons---------------------------------------

btnplus= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "+", command= to_add)
btnplus.grid(row=0, column=8)

btnequal= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "=", command= to_equal)
btnequal.grid(row=0, column=9)

btnminus= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "-", command= to_subtract)
btnminus.grid(row=1, column=8)

btnmultipln= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "*", command= to_multply)
btnmultipln.grid(row=1, column=9)

btndivide= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "/", command= to_divide)
btndivide.grid(row=2, column=8)

btnpercentg= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "%", command= precentage)
btnpercentg.grid(row=2, column=9)

btncube= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "x^3", command= cube_x)
btncube.grid(row=2, column=0)

btnlog= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "log(x)", command= log_x)
btnlog.grid(row=2, column=1)

btnln= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "lnx", command= ln_x)
btnln.grid(row=2, column=2)

btneras= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "<-", command= to_erase)
btneras.grid(row=2, column=3)

btnneg= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "NEG", command= to_make_neg)
btnneg.grid(row=2, column=4)

btnpos= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "POS", command= to_make_pos)
btnpos.grid(row=3, column=0)

btnrec= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "1/x", command= to_rec)
btnrec.grid(row=3, column=1)

btnred= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "RED", command= to_make_Red)
btnred.grid(row=3, column=2)

btngreen= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "GRN", command= to_make_gren)
btngreen.grid(row=3, column=3)

btnyellow= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "YEW", command= to_make_yel)
btnyellow.grid(row=3, column=4)

btndot= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= ".", command= to_stop)
btndot.grid(row=3, column=7)

btnclr= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "clr", command= to_clr)
btnclr.grid(row=3, column=8)

btnexit= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "exit", command= to_exit)
btnexit.grid(row=3, column=9)

#----------------------------------------------Scientfic Buttons------------------------------------------------

btnint= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "int", command= to_int)
btnint.grid(row=0, column=0)

btnsinh= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "sinh", command= to_hyperbola)
btnsinh.grid(row=0, column=1)

btnsin= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "sin", command= to_sin)
btnsin.grid(row=0, column=2)

btnsqur= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "sq(x)", command= to_sqr)
btnsqur.grid(row=0, column=3)

btnfctrial= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "n!", command= to_factorial)
btnfctrial.grid(row=0, column=4)

btndms= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "dms", command= to_dms)
btndms.grid(row=1, column=0)

btncosh= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "cosh", command= to_coshyperbolic)
btncosh.grid(row=1, column=1)

btncos= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "cos", command= to_cosine)
btncos.grid(row=1, column=2)

btnpower= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "x^y", command= to_power)
btnpower.grid(row=1, column=3)

btnroot= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "sqrt(x)", command= to_sqrt)
btnroot.grid(row=1, column=4)




#---------------------------------------For number buttons---------------------------------------

btn7= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "7", command= Num_7)
btn7.grid(row=0, column=5)

btn8= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "8", command= Num_8)
btn8.grid(row=0, column=6)

btn9= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "9", command= Num_9)
btn9.grid(row=0, column=7)

btn4= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "4", command= Num_4)
btn4.grid(row=1, column=5)

btn5= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "5", command= Num_5)
btn5.grid(row=1, column=6)

btn6= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "6", command= Num_6)
btn6.grid(row=1, column=7)

btn1= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "1", command= Num_1)
btn1.grid(row=2, column=5)

btn2= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "2", command= Num_2)
btn2.grid(row=2, column=6)

btn3= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "3", command= Num_3)
btn3.grid(row=2, column=7)

btn0= Button(Button_frame, padx=5, bd=7, font= ("arial", 16, "bold"), width= 10, text= "0", command= Num_0)
btn0.grid(row=3, column=5, columnspan=2)



root.mainloop() # it will run with an infinite loop
