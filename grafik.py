import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot():
    # Verileri oluştur
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Şekil oluştur ve grafiği çiz
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Şekili Tkinter penceresine ekle
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Tuval widget'ı güncelle
    toolbar.update()

# Ana pencereyi oluştur
window = tk.Tk()
window.title("Grafik Çizen Program")
window.geometry("800x600")

# Bir çerçeve oluştur ve pack metodu ile yerleştir
frame = ttk.Frame(window)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Çizim butonunu ekle
plot_button = ttk.Button(window, text="Grafik Çiz", command=plot)
plot_button.pack(side=tk.BOTTOM)

# Matplotlib araç çubuğunu ekle
toolbar_frame = ttk.Frame(window)
toolbar_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Tkinter ana döngüsünü başlat
window.mainloop()
