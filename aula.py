import tkinter as tk

def calcular_soma():
    n1 = int(inputt_n1.get())
    n2 = int(inputt_n2.get())
    resultado = n1+n2
    label_resultado['text'] = f'resultado{resultado}'



root = tk.Tk()
root.title('Calculadora de soma')


label_n1 = tk.Label(root, text='numero 1')
label_n1.grid(row=0, column=0)
inputt_n1 = tk.Entry(root)
inputt_n1.grid(row=0, column=1)


label_n2 = tk.Label(root, text='numero 2')
label_n2.grid(row=1, column=0)
inputt_n2 = tk.Entry(root)
inputt_n2.grid(row=1, column=1)

btn_calcular = tk.Button(root, text='calcula', command=calcular_soma)
btn_calcular.grid(row=2, column=0, columnspan=2)
#tn_calcular.place(x=50,y=80)

label_resultado = tk.Label(root, text='Resultado: ')
label_resultado.grid(row=3, column=0, columnspan=2)

root.mainloop()
