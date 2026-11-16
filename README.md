# Project_GX5Y1V
Projektmunka_Tetovalas_gyogyulási_idozito

# Project címe Tetoválás gyógyulási időzítő

**Készítette:** Ballása Nikolett  
**Neptunkód:** GX5Y1V

## A program célja

A projekt egy grafikus Python-alkalmazás, amely segít követni a friss tetoválás gyógyulási szakaszait. A felhasználó megadhatja, hogy hány nap telt el a tetoválás elkészítése óta, és kiválaszthatja a tetoválás jelenlegi állapotát is. A program ezek alapján szöveges tájékoztatást és általános ápolási tanácsokat jelenít meg.

A program **nem használ adatbázist**, és nem számol automatikusan dátumból. A gyógyulási szakaszokat a megadott napok száma alapján, `if`, `elif` és `else` feltételekkel választja ki.

## A program funkciói

- **Napok lekérdezése:** a beviteli mezőbe beírható a tetoválás óta eltelt napok száma, majd a Lekérdezés gombbal megjelennek az információk.
- **Napok léptetése:** a `+ Következő nap` és a `− Előző nap` gombokkal egyesével lehet előre vagy hátra lépni. A megjelenített szöveg gombnyomásra automatikusan frissül. A napok száma nem mehet 0 alá.
- **Gyógyulási szakaszok:** a program három szakaszt különböztet meg: 0–3. nap, 4–10. nap, illetve 11. naptól.
- **Állapot kiválasztása:** három gomb közül lehet választani: „Enyhén érzékeny / piros”, „Hámlik / viszket”, illetve „Erősen fáj / terjed a pirosság”.
- **Állapotfüggő visszajelzés:** a kiválasztott állapothoz külön szöveges visszajelzés jelenik meg. Erős fájdalom vagy terjedő pirosság esetén a program orvosi segítség kérését javasolja.
- **Hibás bevitel kezelése:** ha a felhasználó szöveget, negatív számot vagy nem egész számot ír be, a program figyelmeztetést jelenít meg.

A gombokra kattintás után a kijelzett információk frissülnek, de a beviteli mezőbe gépelés **önmagában nem indít lekérdezést**.

## A program felépítése

A projekt két Python-fájlból áll:

**`main.py`**

Ebben található a Tkinter segítségével készített grafikus felület: az ablak, a címkék, a beviteli mező, a gombok és a gombnyomásokhoz tartozó függvényhívások.

**`sajat_modul_bn.py`**

Ebben találhatók a saját függvények, a `TetovalasKezeloBN` osztály, az adatok ellenőrzése, a gyógyulási szakaszok és ápolási tanácsok kiválasztása, valamint a kijelzett szövegek frissítése. Az osztály tárolja az aktuális napot és a kiválasztott állapotot.

## A program elindítása

1. A `main.py` és a `sajat_modul_bn.py` fájl legyen ugyanabban a mappában.
2. A számítógépen legyen telepítve a Python és működjön a Tkinter.
3. Indítsuk el a `main.py` fájlt, például a következő paranccsal:

   ```bash
   python main.py
   ```

4. Az ablakban adjuk meg az eltelt napokat, vagy használjuk a plusz és mínusz gombokat, majd válasszuk ki a tetoválás jelenlegi állapotát.

A program nem igényel külön telepítendő külső Python-csomagot.

## Példa a használatra

Ha a felhasználó beírja az **5** értéket, majd a **Lekérdezés** gombra kattint, a program a második gyógyulási szakaszt és az ahhoz tartozó ápolási tanácsot jeleníti meg. Ha ezután kiválasztja a **Hámlik / viszket** állapotot, akkor erről is kap egy külön visszajelzést. A `+` és `−` gombokkal a napok módosíthatók anélkül, hogy újra meg kellene nyomni a Lekérdezés gombot.

## Megjegyzés

A megjelenített tanácsok általános tájékoztatásra szolgálnak, nem helyettesítik az orvosi vizsgálatot. A program a felhasználó által kiválasztott állapot alapján ad visszajelzést, nem tudja megállapítani, hogy a tetoválás valóban megfelelően gyógyul-e.

