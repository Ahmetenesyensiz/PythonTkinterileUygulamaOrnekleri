import tkinter as tk
from tkinter import ttk, messagebox
import random
import sqlite3

GENISLIK = 400
YUKSEKLIK = 400
YILAN_BOYUT = 20
VERITABANI_DOSYASI = "oyun_veritabani.db"


class YilanOyunu:
    def __init__(self, pencere, kullanici_ad):
        self.pencere = pencere
        self.pencere.title("Yılan Oyunu")
        self.canvas = tk.Canvas(pencere, width=GENISLIK, height=YUKSEKLIK, bg="black")
        self.canvas.pack()

        self.yilan_bas_x = GENISLIK / 2
        self.yilan_bas_y = YUKSEKLIK / 2
        self.yilan_parcalari = []
        self.yon = "yukari"

        self.yem_x = 0
        self.yem_y = 0
        self.yem = None

        self.puan = 0
        self.kullanici_ad = kullanici_ad

        self.canvas.bind_all("<KeyPress>", self.tus_takip)

        self.yilan_parcalari.append(
            self.canvas.create_rectangle(self.yilan_bas_x, self.yilan_bas_y, self.yilan_bas_x + YILAN_BOYUT,
                                         self.yilan_bas_y + YILAN_BOYUT, fill="green"))

        self.yem_olustur()
        self.oyun_hareket()

    def oyun_hareket(self):
        if self.yilan_duvarlara_carpti_mi() or self.yilan_kendine_carpti_mi():
            self.oyun_bitir()
            return

        self.yilan_hareket()

        self.pencere.after(100, self.oyun_hareket)

    def yilan_hareket(self):
        yeni_bas_x, yeni_bas_y, _, _ = self.canvas.coords(self.yilan_parcalari[0])

        if self.yon == "yukari":
            yeni_bas_y -= YILAN_BOYUT
            if yeni_bas_y < 0:
                yeni_bas_y = YUKSEKLIK - YILAN_BOYUT
        elif self.yon == "asagi":
            yeni_bas_y += YILAN_BOYUT
            if yeni_bas_y >= YUKSEKLIK:
                yeni_bas_y = 0
        elif self.yon == "sol":
            yeni_bas_x -= YILAN_BOYUT
            if yeni_bas_x < 0:
                yeni_bas_x = GENISLIK - YILAN_BOYUT
        elif self.yon == "sag":
            yeni_bas_x += YILAN_BOYUT
            if yeni_bas_x >= GENISLIK:
                yeni_bas_x = 0

        self.yilan_parcalari.insert(0, self.canvas.create_rectangle(yeni_bas_x, yeni_bas_y, yeni_bas_x + YILAN_BOYUT,
                                                                    yeni_bas_y + YILAN_BOYUT, fill="green"))

        if self.yilan_yem_yedi_mi():
            self.puan += 10
            self.canvas.itemconfig(self.yem, fill="black")
            self.yem_olustur()
        else:
            self.canvas.delete(self.yilan_parcalari[-1])
            self.yilan_parcalari.pop()

        self.puan_guncelle()

    def yem_olustur(self):
        self.yem_x = random.randint(0, (GENISLIK - YILAN_BOYUT) // YILAN_BOYUT) * YILAN_BOYUT
        self.yem_y = random.randint(0, (YUKSEKLIK - YILAN_BOYUT) // YILAN_BOYUT) * YILAN_BOYUT

        self.yem = self.canvas.create_rectangle(self.yem_x, self.yem_y, self.yem_x + YILAN_BOYUT,
                                                self.yem_y + YILAN_BOYUT, fill="red")

    def yilan_yem_yedi_mi(self):
        yilan_bas_x, yilan_bas_y, _, _ = self.canvas.coords(self.yilan_parcalari[0])
        return yilan_bas_x == self.yem_x and yilan_bas_y == self.yem_y

    def yilan_duvarlara_carpti_mi(self):
        yilan_bas_x, yilan_bas_y, _, _ = self.canvas.coords(self.yilan_parcalari[0])
        return False

    def yilan_kendine_carpti_mi(self):
        yilan_bas_konum = self.canvas.coords(self.yilan_parcalari[0])
        return any(yilan_bas_konum == self.canvas.coords(parca) for parca in self.yilan_parcalari[1:])

    def tus_takip(self, event):
        tus = event.keysym
        if tus == "Up" and self.yon != "asagi":
            self.yon = "yukari"
        elif tus == "Down" and self.yon != "yukari":
            self.yon = "asagi"
        elif tus == "Left" and self.yon != "sag":
            self.yon = "sol"
        elif tus == "Right" and self.yon != "sol":
            self.yon = "sag"

    def puan_guncelle(self):
        self.canvas.delete("puan")
        self.canvas.create_text(10, 10, text=f"Puan: {self.puan}", fill="white", anchor="nw", tags="puan")

    def oyun_bitir(self):
        self.canvas.delete("all")
        self.canvas.create_text(GENISLIK / 2, YUKSEKLIK / 2, text="Oyun Bitti!", fill="white", font=("Arial", 20),
                                anchor="center")
        self.canvas.create_text(GENISLIK / 2, YUKSEKLIK / 2 + 30, text=f"Puanınız: {self.puan}", fill="white",
                                font=("Arial", 16), anchor="center")

        self.kayit_ekle(self.kullanici_ad, self.puan)

        self.yeniden_baslat_button = ttk.Button(self.pencere, text="Yeniden Başlat", command=self.yeniden_baslat)
        self.yeniden_baslat_button.pack()

        self.puan_tablosu_button = ttk.Button(self.pencere, text="Puan Tablosu", command=self.puan_tablosunu_goster)
        self.puan_tablosu_button.pack()

    def kayit_ekle(self, kullanici_ad, puan):
       baglanti = sqlite3.connect(VERITABANI_DOSYASI)
       cursor = baglanti.cursor()

       # Tablo kontrolü yapılıyor
       cursor.execute("CREATE TABLE IF NOT EXISTS puanlar (kullanici_ad TEXT, puan INTEGER)")

       cursor.execute("INSERT INTO puanlar (kullanici_ad, puan) VALUES (?, ?)", (kullanici_ad, puan))
       baglanti.commit()
       baglanti.close()


    def yeniden_baslat(self):
        self.pencere.destroy()
        ana_pencere.deiconify()

    def puan_tablosunu_goster(self):
        baglanti = sqlite3.connect(VERITABANI_DOSYASI)
        cursor = baglanti.cursor()
        cursor.execute("SELECT kullanici_ad, puan FROM puanlar ORDER BY puan DESC")
        puanlar = cursor.fetchall()
        baglanti.close()

        puan_tablosu_pencere = tk.Toplevel(self.pencere)
        puan_tablosu_pencere.title("Puan Tablosu")

        treeview = ttk.Treeview(puan_tablosu_pencere, columns=("Kullanıcı Adı", "Puan"), show="headings")
        treeview.heading("Kullanıcı Adı", text="Kullanıcı Adı")
        treeview.heading("Puan", text="Puan")

        for kullanici_ad, puan in puanlar:
            treeview.insert("", "end", values=(kullanici_ad, puan))

        treeview.pack()


def baslat():
    kullanici_ad = kullanici_entry.get()
    if kullanici_ad:
        kullanici_label.config(text=f"Kullanıcı Adı: {kullanici_ad}")
        oyun_penceresi = tk.Toplevel(ana_pencere)
        YilanOyunu(oyun_penceresi, kullanici_ad)
        ana_pencere.withdraw()
    else:
        messagebox.showerror("Hata", "Lütfen kullanıcı adınızı girin.")


ana_pencere = tk.Tk()
ana_pencere.title("Yılan Oyunu Giriş")

kullanici_label = ttk.Label(ana_pencere, text="Kullanıcı Adı:")
kullanici_label.pack()

kullanici_entry = ttk.Entry(ana_pencere)
kullanici_entry.pack()

baslat_button = ttk.Button(ana_pencere, text="Başlat", command=baslat)
baslat_button.pack()

ana_pencere.mainloop()