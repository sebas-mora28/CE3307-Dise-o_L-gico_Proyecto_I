from tkinter import *
from tkinter.messagebox import *
import plot_nrzi 
import conversions


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

#         _______________________________
# _______/Button functionality

def convert():

    try:
        oct_num = int (conv_entry.get())
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
            plot_nrzi.plot_NRZI(signal,0b1);
        else:
            plot_nrzi.plot_NRZI(signal,0b0);
    except:
        if NZRI_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a binary signal")
        else:
            showerror(title="Error!", message="Invalid signal")

def encode():

    try:
        a = 1/0 ;
    except:
        if hamming_entry.get() == "":
            showwarning(title="Alert!", message="Please enter a binary number")
        else:
            showerror(title="Error!", message="Invalid binary number")


conv_btn = Button(main_canvas, text="Convert!", command=convert, font=(t_font,subt_font_size), fg='black', bg=btn_color)
conv_btn.config(height=1, width=10)
conv_btn.place(x=90,y=280)

plot_btn =  Button(main_canvas, text="Plot!", command=plot, font=(t_font,subt_font_size), fg='black', bg=btn_color)
plot_btn.config(height=1, width=10)
plot_btn.place(x=450,y=380)

encode_btn =  Button(main_canvas, text="Encode!", command=encode, font=(t_font,subt_font_size), fg='black', bg=btn_color)
encode_btn.config(height=1, width=10)
encode_btn.place(x=810,y=280)




gui.mainloop()