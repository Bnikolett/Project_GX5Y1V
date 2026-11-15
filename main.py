import tkinter as tk
from sajat_modul_bn import TetovalasKezeloBN, bn_lekerdezes, bn_kovetkezo_nap, bn_elozo_nap, bn_frissites, bn_allapot_valasztas


def gomb_kattintas():
    bn_lekerdezes(entry, kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def plusz_kattintas():
    bn_kovetkezo_nap(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def minusz_kattintas():
    bn_elozo_nap(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def enyhe_kattintas():
    bn_allapot_valasztas(kezelo, 1, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def hamlas_kattintas():
    bn_allapot_valasztas(kezelo, 2, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def problema_kattintas():
    bn_allapot_valasztas(kezelo, 3, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


kezelo = TetovalasKezeloBN()
app = tk.Tk()
app.title("Tetoválás gyógyulási időzítő")
app.geometry("620x750")

label_cim = tk.Label(app, text="Tetoválás gyógyulási időzítő", font=("Arial", 18, "bold"))
label_cim.pack(pady=7)

label_leiras = tk.Label(app, text="Add meg a tetoválás óta eltelt napok számát:")
label_leiras.pack(pady=4)

entry = tk.Entry(app, width=20, font=("Arial", 16))
entry.pack(pady=4)

button_kalkulal = tk.Button(app, text="Lekérdezés", command=gomb_kattintas, width=22, height=2)
button_kalkulal.pack(pady=4)

button_minusz = tk.Button(app, text="− Előző nap", command=minusz_kattintas, width=22)
button_minusz.pack(pady=2)

button_plusz = tk.Button(app, text="+ Következő nap", command=plusz_kattintas, width=22)
button_plusz.pack(pady=2)

label_nap_cim = tk.Label(app, text="Kiválasztott nap:", font=("Arial", 12, "bold"))
label_nap_cim.pack(pady=3)

label_nap = tk.Label(app, text="0", font=("Arial", 16))
label_nap.pack(pady=2)

label_szakasz = tk.Label(app, text="", wraplength=570, font=("Arial", 12, "italic"), fg="purple")
label_szakasz.pack(pady=5)

label_eredmeny = tk.Label(app, text="", wraplength=570, font=("Arial", 12))
label_eredmeny.pack(pady=5)

label_kerdes = tk.Label(app, text="Milyen állapotban van most a tetoválásod?", font=("Arial", 12, "bold"))
label_kerdes.pack(pady=7)

button_enyhe = tk.Button(app, text="Enyhén érzékeny / piros", command=enyhe_kattintas, width=30)
button_enyhe.pack(pady=2)

button_hamlas = tk.Button(app, text="Hámlik / viszket", command=hamlas_kattintas, width=30)
button_hamlas.pack(pady=2)

button_problema = tk.Button(app, text="Erősen fáj / terjed a pirosság", command=problema_kattintas, width=30)
button_problema.pack(pady=2)

label_allapot = tk.Label(app, text="", wraplength=570, font=("Arial", 11, "bold"))
label_allapot.pack(pady=6)

label_visszajelzes = tk.Label(app, text="", wraplength=570, font=("Arial", 11))
label_visszajelzes.pack(pady=5)

bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)

app.mainloop()
