# Calculator-top-iit-level-project-bill-gates-calling-
import tkinter as tk

def button_click(value):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, current +str(value))
def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        result=eval(entry.get())    
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Calculator")
window.geometry("350x300")
entry=tk.Entry(window, font=("courier",20), borderwidth=5, relief="raised", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons=[ 
    "1","2","3","+"
    ,"4","5","6","-"
    ,"7","8","9","*"
    ,"C","0","=","/"    
]

row=1
col=0

for btn in buttons:
    if btn == "=":
        tk.Button(window, text=btn, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(window, text=btn, width=5, height=2,
                  command=lambda x=btn: button_click(x)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(window, text="C", width=22, height=2,
          command=clear).grid(row=row, column=0, columnspan=4)

window.mainloop()
