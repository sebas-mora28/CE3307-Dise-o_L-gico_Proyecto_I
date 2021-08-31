from tkinter import *
from tkinter.messagebox import *
import plot_nrzi 
import conversions
import Hammin_code
#         ____________________
# _______/Constants

#Display
widht_value = 1080
height_value = 720

#Color & fonts
bg_color = '#011936'
text_color = '#CDE6F5'
btn_color = '#ACF39D'
t_font ='Times New Roman'
t_font_size = 18
subt_font_size = 16
small_text_size = 12

#         ____________________
# _______/Create Window
gui = Tk()
gui.title('Proyecto 1')
gui.geometry("%dx%d+0+0" % (widht_value, height_value))
gui.resizable(False, False)

#         ______________________
# _______/Main canvas + elements
main_canvas = Canvas(gui, width=widht_value, height=height_value, bg=bg_color)
main_canvas.place(x=-2,y=-2)

#Tittles
main_canvas.create_text(155,100, fill= text_color, text="Conversion Module",font= (t_font, t_font_size))
main_canvas.create_text(515,100, fill= text_color, text="NZRI Ploter", font= (t_font, t_font_size))
main_canvas.create_text(865,100, fill= text_color, text="Hamming Code Generator", font= (t_font, t_font_size))

#Sections
##Conversion
conv_entry = Entry(main_canvas,font=(t_font,16))
conv_entry.place(x=50,y=200)
main_canvas.create_text(110,190, fill= text_color, text="Enter a octal number",font= (t_font,small_text_size))
hex_text = main_canvas.create_text(90,400,  anchor=W, fill= text_color, text="Hex: ",font= (t_font,subt_font_size))
decimal_text = main_canvas.create_text(90,500, anchor=W,  fill= text_color, text="Decimal: ",font= (t_font,subt_font_size))
bin_text = main_canvas.create_text(90,600, anchor=W,  fill= text_color, text="Binary: ",font= (t_font,subt_font_size))

##NZRI
NZRI_entry = Entry(main_canvas,font=(t_font,16))
NZRI_entry.place(x=410,y=200)
main_canvas.create_text(470,190, fill= text_color, text="Enter a binary signal",font= (t_font,small_text_size))

initial_state = BooleanVar()
init_zero = Radiobutton(main_canvas,text="Initiate with 0", variable=initial_state, value=False , font=(t_font,subt_font_size),fg=text_color,activeforeground=btn_color,activebackground=bg_color,bg=bg_color,highlightcolor=btn_color,selectcolor=bg_color)
init_zero.place(x=445,y=280)
init_one = Radiobutton(main_canvas,text="Initiate with 1", variable=initial_state, value=True , font=(t_font,subt_font_size),fg=text_color,activeforeground=btn_color,activebackground=bg_color,bg=bg_color,highlightcolor=btn_color,selectcolor=bg_color)
init_one.place(x=445,y=310)


##Hamming Code
hamming_entry = Entry(main_canvas,font=(t_font,16))
hamming_entry.place(x=770,y=200)
main_canvas.create_text(835,190,fill= text_color,  text="Enter a binary number",font= (t_font,small_text_size))

parity = BooleanVar()
odd = Radiobutton(main_canvas,text="Odd parity", variable=parity, value=False , font=(t_font,subt_font_size),fg=text_color,activeforeground=btn_color,activebackground=bg_color,bg=bg_color,highlightcolor=btn_color,selectcolor=bg_color)
odd.place(x=805,y=280)
even = Radiobutton(main_canvas,text="Even parity", variable=parity, value=True , font=(t_font,subt_font_size),fg=text_color,activeforeground=btn_color,activebackground=bg_color,bg=bg_color,highlightcolor=btn_color,selectcolor=bg_color)
even.place(x=805,y=310)

#         _______________________________
# _______/Button functionality
def to_num(num):
    try:
        return int(num)
    except:
        return float(num)

def convert():
    try:
        oct_num = to_num(conv_entry.get())
        converted = conversions.convertir(oct_num)
        main_canvas.itemconfig(decimal_text,text="Decimal: "+converted[0])
        main_canvas.itemconfig(hex_text,text="Hex: "+converted[2])
        main_canvas.itemconfig(bin_text,text="Binary: "+converted[1])
        
    except:
        if conv_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a octal number")
        else:
            showerror(title="Error!", message="Invadid octal number")
    
def plot():
    try:
        signal = int (NZRI_entry.get(),2)
        if initial_state.get():
            plot_nrzi.plot_NRZI(signal,0b1)
        else:
            plot_nrzi.plot_NRZI(signal,0b0)
    except:
        if NZRI_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a binary signal")
        else:
            showerror(title="Error!", message="Invalid signal")

def encode():
    try:
        int(hamming_entry.get(),2)
        encoded = Hammin_code.hamming_encode(hamming_entry.get(),parity.get())
        create_new_encription(encoded)
    except:
        if hamming_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a binary number")
        else:
            showerror(title="Error!", message="Invalid binary number")

def check():
    try:
        int(hamming_entry.get(),2)
        checked = Hammin_code.check_hamming_encode(hamming_entry.get(),parity.get())
        create_new_check(checked[0],checked[1],int(parity.get()))
    except:
        if hamming_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a binary number")
        elif len(hamming_entry.get()) == 1:
            showerror(title="Error!", message="Please enter a binary number with not less than 2 bits")
        else:
            showerror(title="Error!", message="Invalid binary number")


def create_new_encription(list):

    # find total number of rows and
    # columns in list
    total_rows = len(list)+1
    total_columns = len(list[-1])+1

    window_w = (total_columns-1)*37 + 188
    window_h = total_rows*27

    new_encript = Toplevel()
    new_encript.resizable(False, False)
    new_encript.title('Encoded number')
    new_encript.geometry("%dx%d+0+0" % (window_w, window_h))

    # Canvas
    encript_canvas = Canvas(new_encript, width= window_w, height=window_h, bg=bg_color)
    encript_canvas.place(x=-2, y=-2)

    d=0
    p=0
    
    for i in range(total_rows):
            for j in range(total_columns):

                #(0,0)
                if i==0 and j==0:
                    Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold')).grid(row=i,column=j)

                #(1,0)
                elif i==1 and j==0:
                    e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, "Input(No parity)")
                    p=0
                    d=0

                #(p's column)
                elif i!=0 and i!=1 and  j==0 and i != total_rows - 1:
                    e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, "p" + str(i-1))

                #(n,0)
                elif i == total_rows-1 and j==0:
                    e = Entry(encript_canvas, width=17, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, "Output(with parity)")

                #(p & d row)
                elif i==0 and j!=0:
                    e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    
                    e.grid(row=i, column=j)
                    if j == 2**p:
                        e.insert(END, "p" + str(p+1))
                        p=p+1
                    else:
                        d=d+1
                        e.insert(END, "d" + str(d))
                
                #(input string)
                elif i==1 and j!=0:
                    if j != 2**p:
                        e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END,list[0][d])    
                        d=d+1
                    else:
                        e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        p=p+1
                    
                #(output string)
                elif i==total_rows-1:
                    e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    
                    e.grid(row=i, column=j)
                    e.insert(END,list[-1][j-1])
                
                #(inner lists)
                else:
                    e = Entry(encript_canvas, width=3, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    
                    e.grid(row=i, column=j)
                    e.insert(END,list[i-1][j-1])


def create_new_check(list,error,parity):
    if error == 0: 
        showinfo(title="Success!", message="No errors were detected")
    else:
        showerror(title="Error detected!",message="Error found on bit " + str(error))
    # find total number of rows and
    # columns in list
    total_rows = len(list)+1
    total_columns = len(list[0])+3

    window_w = (total_columns-3)*37 + (110*3)
    window_h = total_rows*27



    new_check = Toplevel()
    new_check.resizable(False, False)
    new_check.title('Checked parity')
    new_check.geometry("%dx%d+0+0" % (window_w, window_h))

    # Canvas
    check_canvas = Canvas(new_check, width= window_w, height=window_h, bg=bg_color)
    check_canvas.place(x=-2, y=-2)

    d=0
    p=0
    
    for i in range(total_rows):
            for j in range(total_columns):

                #(0,0)
                if i==0 and j==0:
                    Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold')).grid(row=i,column=j)
                #(1,0)
                elif i==1 and j==0:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, "Input")
                    p=0
                    d=0

                #(0,m-1)
                elif i==0 and j==total_columns-1:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, "Parity Bit")

                #(0,m-2)
                elif i==0 and j==total_columns-2:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, "Parity check")

                #(1,m-1)
                elif i==1 and j==total_columns-1:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)

                #(2,m-2)
                elif i==1 and j==total_columns-2:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i,column=j)
                    e.insert(END, str(parity))

                #(p's column)
                elif i!=0 and i!=1 and j==0:
                    e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, "p" + str(i-1))

                #(p & d row)
                elif i==0 and j!=0:
                    e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    
                    e.grid(row=i, column=j)
                    if j == 2**p:
                        e.insert(END, "p" + str(p+1))
                        p=p+1
                    else:
                        d=d+1
                        e.insert(END, "d" + str(d))
                
                elif i==1 and j!=0 and j < total_columns-2:
                    e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                font=(t_font,subt_font_size,'bold'))
                    
                    e.grid(row=i, column=j)
                    e.insert(END,list[0][j-1])
                     
                else:

                    this_list = list[i-1]

                    if j == total_columns-1:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END,this_list[0])

                    elif j == total_columns-2:
                        e = Entry(check_canvas, width=10, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END,this_list[1])

                    else:
                        e = Entry(check_canvas, width=3, fg=text_color, background=bg_color,
                                    font=(t_font,subt_font_size,'bold'))
                        e.grid(row=i, column=j)
                        e.insert(END,this_list[2][j-1])



conv_btn = Button(main_canvas, text="Convert!", command=convert, font=(t_font,subt_font_size), fg='black', bg=btn_color)
conv_btn.config(height=1, width=10)
conv_btn.place(x=90,y=280)

plot_btn =  Button(main_canvas, text="Plot!", command=plot, font=(t_font,subt_font_size), fg='black', bg=btn_color)
plot_btn.config(height=1, width=10)
plot_btn.place(x=450,y=380)

encode_btn =  Button(main_canvas, text="Encode!", command=encode, font=(t_font,subt_font_size), fg='black', bg=btn_color)
encode_btn.config(height=1, width=10)
encode_btn.place(x=810,y=380)

encode_btn =  Button(main_canvas, text="Check!", command=check, font=(t_font,subt_font_size), fg='black', bg=btn_color)
encode_btn.config(height=1, width=10)
encode_btn.place(x=810,y=450)



gui.mainloop()