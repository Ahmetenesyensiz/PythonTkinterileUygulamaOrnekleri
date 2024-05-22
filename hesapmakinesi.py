import tkinter as tk

# Düğmeye tıklandığında, değeri giriş alanına ekler
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Eşittir düğmesine tıklandığında, ifadeyi değerlendirir ve sonucu gösterir
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Temizle düğmesine tıklandığında, giriş alanını temizler
def button_clear():
    entry.delete(0, tk.END)

# Temel pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinesi")

# Giriş alanını oluştur
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Düğmeleri tanımla
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Düğmeleri arayüze yerleştir
row = 1
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=lambda value=button: button_click(value)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Temizle düğmesini ekle
tk.Button(root, text='C', width=4, height=2, font=('Arial', 18), command=button_clear).grid(row=row, column=0, columnspan=1)

# Tkinter döngüsünü başlat
root.mainloop()
