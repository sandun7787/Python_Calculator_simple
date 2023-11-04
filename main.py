import tkinter as tk


calculation=''

def add_to_calculation(symbol):
   global calculation
   calculation += str(symbol)
   text_result.delete(1.0,"end")
   text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        print(calculation)
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
        text_result(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")



root = tk.Tk()
root.geometry("300*275")
text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

btn_1 =tk.Button(root,text="1",command=lambda :add_to_calculation(1),width=5,font=("Arial",1))
btn_1.grid(row=2,column=1)
btn_2 =tk.Button(root,text="2",command=lambda :add_to_calculation(2),width=5,font=("Arial",1))
btn_2.grid(row=2,column=2)
btn_3 =tk.Button(root,text="3",command=lambda :add_to_calculation(3),width=5,font=("Arial",1))
btn_3.grid(row=2,column=3)
btn_4 =tk.Button(root,text="4",command=lambda :add_to_calculation(4),width=5,font=("Arial",1))
btn_4.grid(row=2,column=4)
btn_5 =tk.Button(root,text="5",command=lambda :add_to_calculation(5),width=5,font=("Arial",1))
btn_5.grid(row=2,column=5)
btn_6 =tk.Button(root,text="6",command=lambda :add_to_calculation(6),width=5,font=("Arial",1))
btn_6.grid(row=2,column=6)
btn_7 =tk.Button(root,text="7",command=lambda :add_to_calculation(7),width=5,font=("Arial",1))
btn_7.grid(row=2,column=7)
btn_8 =tk.Button(root,text="8",command=lambda :add_to_calculation(8),width=5,font=("Arial",1))
btn_8.grid(row=2,column=8)
btn_9 =tk.Button(root,text="9",command=lambda :add_to_calculation(9),width=5,font=("Arial",1))
btn_9.grid(row=2,column=9)
btn_0 =tk.Button(root,text="0",command=lambda :add_to_calculation(0),width=5,font=("Arial",1))
btn_0.grid(row=2,column=0)
btn_plus =tk.Button(root,text="+",command=lambda :add_to_calculation("+"),width=5,font=("Arial",1))
btn_plus.grid(row=2,column=4)
btn_minus =tk.Button(root,text="-",command=lambda :add_to_calculation("-"),width=5,font=("Arial",1))
btn_minus.grid(row=2,column=4)
btn_div =tk.Button(root,text="/",command=lambda :add_to_calculation("/"),width=5,font=("Arial",1))
btn_div.grid(row=2,column=4)
btn_mul =tk.Button(root,text="*",command=lambda :add_to_calculation("*"),width=5,font=("Arial",1))
btn_mul.grid(row=2,column=4)
btn_open =tk.Button(root,text="(",command=lambda :add_to_calculation("("),width=5,font=("Arial",1))
btn_open.grid(row=2,column=4)
btn_close =tk.Button(root,text="(",command=lambda :add_to_calculation("("),width=5,font=("Arial",1))
btn_close.grid(row=2,column=4)
btn_equal =tk.Button(root,text="=",command=lambda :add_to_calculation("="),width=5,font=("Arial",1))
btn_equal.grid(row=2,column=4)
root.mainloop()