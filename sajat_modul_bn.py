from tkinter import messagebox


def bn_elso_fuggveny(nap):
    if nap <= 3:
        return "Első szakasz: A tetoválás még friss, enyhe érzékenység és bőrpír előfordulhat."
    elif nap <= 10:
        return "Második szakasz: Gyakori a hámlás és a viszketés, de nem szabad vakarni a bőrt."
    else:
        return "Harmadik szakasz: A bőr tovább regenerálódik, a teljes gyógyulás több időt is igénybe vehet."


def bn_masodik_fuggveny(szoveg):
    return szoveg.strip().capitalize()


def bn_harmadik_fuggveny(napok_szama):
    if napok_szama < 0:
        return 0
    return napok_szama


def bn_allapot_fuggveny(allapot):
    if allapot == 1:
        return "Enyhe érzékenység és bőrpír előfordulhat. Ha romlik az állapot, kérj tanácsot szakembertől."
    elif allapot == 2:
        return "A hámlás és a viszketés a gyógyulás része lehet. Ne vakard és ne tépd le a hámló bőrt."
    elif allapot == 3:
        return "Az erős vagy fokozódó fájdalom és a terjedő pirosság fertőzés jele is lehet. Fordulj mielőbb orvoshoz!"
    else:
        return "Válassz a fenti gombokkal, hogy a jelenlegi állapotodról is kapj visszajelzést."


class TetovalasKezeloBN:
    def __init__(self):
        self.statusz = "Gyógyulási folyamat"
        self.nap = 0
        self.allapot = 0

    def bn_szuro_adatok(self, nap):
        if nap <= 3:
            return "Ápolás: kíméletes tisztítás és a tetováló által javasolt utóápolás."
        elif nap <= 10:
            return "Ápolás: óvatos tisztítás, a hámló bőr kímélése és szükség szerint vékony krémezés."
        else:
            return "Ápolás: a bőr tisztán tartása és megfelelő hidratálása."

    def bn_ellenorzes(self, ertek):
        try:
            szam = int(ertek)
            return szam >= 0
        except ValueError:
            return False


def bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes):
    nap = bn_harmadik_fuggveny(kezelo.nap)
    uzenet = bn_masodik_fuggveny(kezelo.bn_szuro_adatok(nap))
    szakasz = bn_elso_fuggveny(nap)

    label_nap.config(text=nap)
    label_eredmeny.config(text=uzenet)
    label_szakasz.config(text=szakasz)

    if kezelo.allapot == 1:
        label_allapot.config(text="Kiválasztott állapot: Enyhén érzékeny / piros")
    elif kezelo.allapot == 2:
        label_allapot.config(text="Kiválasztott állapot: Hámlik / viszket")
    elif kezelo.allapot == 3:
        label_allapot.config(text="Kiválasztott állapot: Erősen fáj / terjed a pirosság")
    else:
        label_allapot.config(text="Még nincs kiválasztott állapot.")

    label_visszajelzes.config(text=bn_allapot_fuggveny(kezelo.allapot))


def bn_lekerdezes(entry, kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes):
    bevitel = entry.get()
    if not kezelo.bn_ellenorzes(bevitel):
        messagebox.showwarning("Hiba", "Kérlek érvényes, nem negatív egész számot adj meg!")
        return

    kezelo.nap = int(bevitel)
    bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def bn_kovetkezo_nap(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes):
    kezelo.nap = kezelo.nap + 1
    bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def bn_elozo_nap(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes):
    if kezelo.nap > 0:
        kezelo.nap = kezelo.nap - 1
    bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)


def bn_allapot_valasztas(kezelo, allapot, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes):
    kezelo.allapot = allapot
    bn_frissites(kezelo, label_nap, label_eredmeny, label_szakasz, label_allapot, label_visszajelzes)
