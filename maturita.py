import tkinter as tk
from PIL import Image, ImageTk
import time
import random

# Samotné okno aplikace
okno = tk.Tk()
okno.title("Blackjack")
okno.geometry("1200x720")
okno.resizable(False, False)
okno.configure(bg="green")

# List to keep track of image labels
image_labels = []

# Nadpis
nadpis = tk.Label(okno, text="Blackjack", font=("Arial", 64))

# Tlačítka v hlavním menu
moznosti = tk.Frame(okno) 
zacatek_btn = tk.Button(moznosti, text ="Začátek hry", command=lambda: obtiznost_menu()) 
pravidla_btn = tk.Button(moznosti, text ="Pravidla", command=lambda: zobraz_pravidla()) 
konec_btn = tk.Button(moznosti, text ="Konec", command=okno.quit) #

######################### Globální promněné #########################


######################### Balíček #########################

# Balíček karet
puvodni_balicek = ["2♧","3♧","4♧","5♧","6♧","7♧","8♧","9♧","10♧","J♧","Q♧","K♧","A♧",
                    "2♤","3♤","4♤","5♤","6♤","7♤","8♤","9♤","10♤","J♤","Q♤","K♤","A♤",
                    "2♡","3♡","4♡","5♡","6♡","7♡","8♡","9♡","10♡","J♡","Q♡","K♡","A♡",
                    "2♢","3♢","4♢","5♢","6♢","7♢","8♢","9♢","10♢","J♢","Q♢","K♢","A♢"]

balicek = []

# Přiřazení hodnoty k obrázku
obrazky = {
    "2♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/2_of_clubs.png",
    "3♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/3_of_clubs.png",
    "4♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/4_of_clubs.png",
    "5♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/5_of_clubs.png",
    "6♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/6_of_clubs.png",
    "7♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/7_of_clubs.png",
    "8♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/8_of_clubs.png",
    "9♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/9_of_clubs.png",
    "10♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/10_of_clubs.png",
    "J♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/jack_of_clubs2.png",
    "Q♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/queen_of_clubs2.png",
    "K♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/king_of_clubs2.png",
    "A♧": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/ace_of_clubs.png",
    "2♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/2_of_spades.png",
    "3♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/3_of_spades.png",
    "4♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/4_of_spades.png",
    "5♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/5_of_spades.png",
    "6♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/6_of_spades.png",
    "7♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/7_of_spades.png",
    "8♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/8_of_spades.png",
    "9♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/9_of_spades.png",
    "10♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/10_of_spades.png",
    "J♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/jack_of_spades2.png",
    "Q♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/queen_of_spades2.png",
    "K♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/king_of_spades2.png",
    "A♤": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/ace_of_spades2.png",
    "2♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/2_of_hearts.png",
    "3♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/3_of_hearts.png",
    "4♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/4_of_hearts.png",
    "5♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/5_of_hearts.png",
    "6♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/6_of_hearts.png",
    "7♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/7_of_hearts.png",
    "8♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/8_of_hearts.png",
    "9♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/9_of_hearts.png",
    "10♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/10_of_hearts.png",
    "J♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/jack_of_hearts2.png",
    "Q♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/queen_of_hearts2.png",
    "K♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/king_of_hearts2.png",
    "A♡": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/ace_of_hearts.png",
    "2♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/2_of_diamonds.png",
    "3♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/3_of_diamonds.png",
    "4♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/4_of_diamonds.png",
    "5♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/5_of_diamonds.png",
    "6♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/6_of_diamonds.png",
    "7♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/7_of_diamonds.png",
    "8♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/8_of_diamonds.png",
    "9♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/9_of_diamonds.png",
    "10♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/10_of_diamonds.png",
    "J♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/jack_of_diamonds2.png",
    "Q♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/queen_of_diamonds2.png",
    "K♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/king_of_diamonds2.png",
    "A♢": "/home/johnmateo/Dokumenty/Skola/AAAAAA/PNG-cards-1.3/ace_of_diamonds.png"
}

######################### Správa okna #########################

# Čistění okna
def okeno():
    # Vyčistění okna
    for widget in okno.winfo_children():
        widget.pack_forget() # Všechny widgety pod .pack se schovají 
        widget.place_forget() # Všechny widgety pod .place se schovají

    # Vymazání starých obrázků (widgetů)
    for label in image_labels:
        label.destroy()
    image_labels.clear()

# Úvodní menu
def zobraz_menu():
    okeno() 
    
    # Vytvoření menu
    nadpis.pack(padx=10, pady=10) # Generuje nadpis
    moznosti.pack() # Definuje možnosti
    zacatek_btn.pack(padx=10, pady=10) # Tlačítko pro začátek hry
    pravidla_btn.pack(padx=10, pady=10) # Tlačítko pro zobrazení pravidel
    konec_btn.pack(padx=10, pady=10) # Tlačítko pro ukončení hry

# Pravidla hry
def zobraz_pravidla():
    okeno()
    
    # Zobrazit pravidla
    pravidla_nadpis = tk.Label(okno, text="Pravidla Blackjacku:\n\n", font=("Arial", 20)) # Nadpis
    pravidla_text = tk.Label(okno, text="""1. Cílem je dostat se co nejblíže k 21, aniž byste překročili tuto hodnotu.
2. Číselné karty mají hodnotu podle své nominální hodnoty.
3. Obrázkové karty (Král, Královna, Kluk) mají hodnotu 10.
4. Eso může mít hodnotu 11 nebo 1.
5. Můžete 'Táhnout' (Hit) další kartu nebo 'Stát' (Stand) a ponechat si svůj aktuální součet.
6. Dealer musí táhnout, dokud nedosáhne 17 nebo více.
7. Pokud překročíte 21, prohrajete a končíte.""", font=("Arial", 14)) # Text pravidel
    pravidla_nadpis.pack(padx=10, pady=10) # Zobrazení nadpisu
    pravidla_text.pack(padx=10, pady=50) # Zobrazení textu
    
    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu)
    zpet_btn.pack(padx=10, pady=10)

######################### Systém pro žetonů #########################

def vklad(obtiznost):
    okeno()

    global balanc # Globální proměnná pro zůstatek


######################### Úpravy s karetami #########################

# Definování hosnoty
def hodnota_karty(karta, skore):
    # Odstranění symbolu (např. '♤') z karty
    karta = karta[:-1]  # Tím odstraníme poslední znak (symbol)
    
    if karta in ["J", "Q", "K"]:  # Kluk, dáma, král mají hodnotu 10
        return 10
    elif karta == "A":  # Eso má hodnotu 11 nebo 1, záleží na skóre
        return 11 if skore + 11 <= 21 else 1
    else:  # Ostatní karty (2-10) mají hodnotu podle jejich čísla
        return int(karta)

# Zobrazit karty
def zobrazit_karty(karty_list):
    # Zobrazení karet lícema nahoru
    # Pro každou kartu, která se nachází v seznamu karet a bude hraná
    for karta in karty_list:
        img = Image.open(obrazky[karta]) # Otevření obrázku
        img = img.resize((110, 165), Image.LANCZOS) # Změna velikosti obrázku
        img_tk = ImageTk.PhotoImage(img) # Převedení obrázku do formátu, který tkinter může zobrazit
        vize = tk.Label(okno, image=img_tk) # Vytvoření labelu s obrázkem
        vize.image = img_tk # Přiřazení obrázku k labelu
        image_labels.append(vize) # Přidání labelu do listu
        if karty_list == hrac_karty_list: # Pokud se jedná o karty hráče
            vize.place(x=330 + 45 * hrac_karty_list.index(karta), y=380) # Zobrazí karty hráče
        else: # Pokud se jedná o karty dealera
            vize.place(x=330 + 45 * dealer_karty_list.index(karta), y=70) # Zobrazí karty dealera

    # Zobrazení karty lícem dolů - estetický důvod
    zadni_img = Image.open("/home/johnmateo/Dokumenty/Skola/AAAAAA/poker back /card back blue.png") # Otevření obrázku pro zadní stranu karty
    zadni_img = zadni_img.resize((110, 165), Image.LANCZOS) # Změna velikosti obrázku
    zadni_img_tk = ImageTk.PhotoImage(zadni_img) # Převedení obrázku do formátu, který tkinter může zobrazit
    zadni = tk.Label(okno, image=zadni_img_tk) # Vytvoření labelu s obrázkem
    zadni.image = zadni_img_tk # Přiřazení obrázku k labelu
    image_labels.append(zadni) # Přidání labelu do listu
    zadni.place(x=1050, y=35) # Zobrazí zadní stranu karty v okně

# Zamíchání balíčku
def michani(obtinost):
    if obtinost == 1: # Pokud je obtížnost 1 = lehká
        balicek = puvodni_balicek.copy() # Vytvoří kopii původního balíčku, neboli 52 karet
    elif obtinost == 2: # Pokud je obtížnost 2 = střední
        balicek = puvodni_balicek * 3 # Vytvoří seznam se třemi balícky, neboli 156 karet
    elif obtinost == 3: # Pokud je obtížnost 3 = těžká
        balicek = puvodni_balicek * 5 # Vytvoří seznam se pěti balíčky, neboli 260 karet
    random.shuffle(balicek) # Zamíchá seznam s vygenerovanými kartami
    return balicek # Vrátí zamíchaný balíček jako výstup

# Funkce pro rozdání karet
def rozdani_karet(kdo, pocet_karet, balicek,): 
    karty_list = [] # Seznam karet
    skore = 0

    for _ in range(pocet_karet): # Pro každou kartu, která je v možnosti, aby byla rozdána
        karta = balicek.pop() # Vybere kartu z balíčku
        karty_list.append(karta) # Přidá kartu do seznamu karet
        skore += hodnota_karty(karta, skore) # Přičte hodnotu karty k celkovému skóre
    return karty_list, skore # Vrátí seznam karet a celkové skóre

######################### Hlavní funkce hry #########################

# Menu pro výběr obtížnosti
def obtiznost_menu():
    okeno()
    
    global vyhra_hrac, vyhra_dealer, obtiznost # Globální proměnné pro skóre a obtiznost

    # Vynulování skóre a obtížnosti
    vyhra_hrac = 0
    vyhra_dealer = 0
    obtiznost = 0

    # Zobrazit obtiznost
    obtiznost_text = tk.Label(okno, text="Vyber obtiznost", font=("Arial", 14)) # Nadpis
    obtiznost_text.pack(padx=10, pady=20) # Zobrazení nadpisu

    # Tlačítka pro obtížnost a informace o obtížnosti
    obtiznost_easy = tk.Button(okno, text="Lehká", bg="green", fg="white", command=lambda: hra(1, 1)) # Tlačítko pro lehkou obtížnost
    info_easy = tk.Label(okno, text="- Jeden blíček karet (52)\n" 
"- Žádný hráč navíc", font=("Arial", 10)) # Informace o lehké obtížnosti
    obtiznost_easy.pack(padx=10, pady=5) # Zobrazení tlačítka
    info_easy.pack(pady=2) # Zobrazení informací

    obtiznost_medium = tk.Button(okno, text="Střední", bg="orange", fg="white", command=lambda: hra(2, 2)) # Tlačítko pro střední obtížnost
    info_medium = tk.Label(okno, text="- Tři balíčky karet (156)\n"
"- Jeden hráč navíc", font=("Arial", 10)) # Informace o střední obtížnosti
    obtiznost_medium.pack(padx=10, pady=5) # Zobrazení tlačítka
    info_medium.pack(pady=2) # Zobrazení informací

    obtiznost_hard = tk.Button(okno, text="Těžká", bg="red", fg="white", command=lambda: hra(3, 3)) # Tlačítko pro těžkou obtížnost
    info_hard = tk.Label(okno, text="- Pět balíčků karet (260)\n"
"- Dva hráči navíc", font=("Arial", 10)) # Informace o těžké obtížnosti
    obtiznost_hard.pack(padx=10, pady=5) # Zobrazení tlačítka
    info_hard.pack(pady=2) # Zobrazení informací

    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu) # Tlačítko pro návrat do hlavního menu
    zpet_btn.pack(padx=10, pady=70, side="bottom") # Zobrazení tlačítka

# Hra
def hra(balicek, obtiznost):
    okeno()

    global hrac_skore, dealer_skore, hrac_karty_list, dealer_karty_list # Globální proměnné pro skóre, seznamy karet

    # Balíček karet
    balicek = michani(balicek) # Definuje hrací balíček pomocí funkce michani

    # Hráč
    hrac_karty_list, hrac_skore = rozdani_karet("hráč", 2, balicek) # Rozdání prvních dvou karet pro hráče
    hrac_text = tk.Label(okno, text=f"({hrac_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče
    hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
    zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

    # Dealer
    dealer_karty_list, dealer_skore = rozdani_karet("dealer", 1, balicek) # Rozdání první karety
    dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče
    dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
    zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera
    
    stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek)) # Tlačítko pro stání
    stand_btn.pack(padx=10, pady=10, side="bottom") # Zobrazení tlačítka
    hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek)) # Tlačítko pro další kartu
    hit_btn.pack(padx=10, pady=10, side="bottom") # Zobrazení tlačítka

    zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
    ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
    ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

    # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore.place(x=10, y=10) # Zobrazí celkové skóre

# Další karta
def hit(balicek):
    okeno() 

    global hrac_skore, hrac_karty_list, dealer_skore, dealer_karty_list, vyhra_dealer, vyhra_hrac, obtiznost # Globální proměnné pro skóre a seznamy karet

    karta = balicek.pop() # Vybere kartu z balíčku
    hrac_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
    hrac_skore += hodnota_karty(karta, hrac_skore) # Přičte hodnotu karty k celkovému skóre hráče
    hrac_text = tk.Label(okno, text=f"({hrac_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče
    hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
    zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

    dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera
    dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
    zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

    if hrac_skore == 21: # Pokud hráč dosáhne 21
        okeno() 

        vyhra_hrac += 1 # Přičte se hráči bod

        hrac_text = tk.Label(okno, text=f"({hrac_skore}) - VYHRÁL JSI +1 :)", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče a informací o výhře
        hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
        zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

        dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera
        dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
        zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

         # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
        konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit) 
        konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
        nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
        nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
        nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

    elif hrac_skore < 21: # Pokud hráč má méně než 21
        stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek)) 
        stand_btn.pack(padx=10, pady=10, side="bottom")
        hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek))
        hit_btn.pack(padx=10, pady=10, side="bottom")

        # Kolik karet zbývá v balíčku
        zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
        ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
        ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

        # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore.place(x=10, y=10) # Zobrazí celkové skóre

    elif hrac_skore > 21: # Pokud hráč má více než 21
        okeno()

        vyhra_dealer += 1 # Přičte se dealerovi bod za výhru

        hrac_text = tk.Label(okno, text=f"({hrac_skore}) - PROHRÁL JSI :(", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče a informací o prohře
        hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
        zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

        dealer_text = tk.Label(okno, text=f"({dealer_skore}) - VYHRÁL +1", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera a informací o výhře
        dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
        zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

        # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
        konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit)
        konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
        nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
        nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
        nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

# Stání
def stand(balicek):
    okeno()

    global dealer_skore, dealer_karty_list, vyhra_dealer, vyhra_hrac, obtiznost # Globální proměnné pro skóre a seznamy karet

    while dealer_skore < 17: # Dokud dealer nemá 17 a méně
        karta = balicek.pop() # Vybere kartu z balíčku
        dealer_karty_list.append(karta) # Přidá kartu do seznamu karet dealera
        dealer_skore += hodnota_karty(karta, dealer_skore) # Přičte hodnotu karty k celkovému skóre dealera
        
        okeno()
        
        # Hráč
        hrac_text = tk.Label(okno, text=f"({hrac_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre
        hrac_text.place(x=330 , y=345) # Zobrazí součet
        zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet

        # Dealer
        dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre
        dealer_text.place(x=330, y=35) # Zobrazí součet
        zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet
        
        # Kolik karet zbývá v balíčku
        zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
        ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
        ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

        # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore.place(x=10, y=10) # Zobrazí celkové skóre
        
        okno.update() # Aktualizuje okno
        time.sleep(1) # Čeká 1 sekundu

    hrac_text = tk.Label(okno, text=f"({hrac_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče
    hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
    zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

    dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera
    dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
    zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

    # Kolik karet zbývá v balíčku
    zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
    ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
    ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

    # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14))# Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore.place(x=10, y=10) # Zobrazí celkové skóre

    if dealer_skore > 21: # Pokud dealer má více než 21
        okeno()

        vyhra_hrac += 1 # Přičte se hráči bod za výhru

        hrac_text = tk.Label(okno, text=f"({hrac_skore}) - VYHRÁL JSI +1 :)", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče a informací o výhře
        hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
        zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

        dealer_text = tk.Label(okno, text=f"({dealer_skore}) - PROHRÁL", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera a informací o prohře
        dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
        zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

        # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
        konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit)
        konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
        nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
        nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
        nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

    else:
        if dealer_skore > hrac_skore: # Pokud dealer má více než hráč
            okeno()

            vyhra_dealer += 1 # Přičte se dealerovi bod za výhru

            hrac_text = tk.Label(okno, text=f"({hrac_skore}) - PROHRÁL JSI :(", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče a informací o prohře
            hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
            zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

            dealer_text = tk.Label(okno, text=f"({dealer_skore}) - VYHRÁL +1", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera a informací o výhře
            dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
            zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

            # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
            konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit) 
            konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
            nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
            nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
            nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

        elif dealer_skore < hrac_skore: # Pokud dealer má méně než hráč a zaroveň více než 17
            okeno()

            vyhra_hrac += 1 # Přičte se hráči bod za výhru

            hrac_text = tk.Label(okno, text=f"({hrac_skore}) - VYHRÁL JSI +1 :)", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče a informací o výhře
            hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
            zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče
            
            dealer_text = tk.Label(okno, text=f"({dealer_skore}) - PROHRAL", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera a informací o prohře
            dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
            zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

            # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
            konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit)
            konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
            nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
            nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
            nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

        else: # Pokud je remíza
            okeno()

            hrac_text = tk.Label(okno, text=f"({hrac_skore}) - SÁZKY SE VRACÍ", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre hráče
            hrac_text.place(x=330 , y=345) # Zobrazí součet u hráče
            zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

            dealer_text = tk.Label(okno, text=f"({dealer_skore}) - SÁZKY SE VRACÍ", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre dealera
            dealer_text.place(x=330, y=35) # Zobrazí součet u dealera
            zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

            # Vytvoří se tři tlačítka pro ukončení aplikace, pro pokračováním hry nebo s možnstí změnit obtížnost
            konec_btn = tk.Button(okno, text="ukoncit app", command=okno.quit)
            konec_btn.pack(padx=10, pady=10, side="bottom") # Ukončení aplikace
            nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
            nova_dvojice_btn.pack(padx=10, pady=10, side="bottom") # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="jina obtiznost", command=lambda: obtiznost_menu())
            nova_hra_btn.pack(padx=10, pady=10, side="bottom") # Změna obtížnosti

# Po první hře zbydou karty a zde se hraje dál
def hra_se_zbylymi_kartami(balicek):
    okeno()

    global hrac_skore, dealer_skore, hrac_karty_list, dealer_karty_list, obtiznost # Globální proměnné pro skóre a seznamy karet

    if len(balicek) < 10: # Pokud je v balíčku méně než 10 karet
        okeno()

        upozorneni = tk.Label(okno, text="V balíčku zbývá méně karet, než je doporučeno", font=("Arial", 14)) # Vytvoří label s upozorněním
        upozorneni.pack(padx=10, pady=10) # Zobrazí upozornění

        print(f"obtiznsot:{obtiznost}")
    
    else:
        print(f"Obtiznost:{obtiznost}")
        # Hráč
        hrac_karty_list, hrac_skore = rozdani_karet("hráč", 2, balicek) # Rozdání prvních dvou karet
        hrac_text = tk.Label(okno, text=f"({hrac_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre
        hrac_text.place(x=330 , y=345) # Zobrazí součet
        zobrazit_karty(hrac_karty_list) # Zobrazí obrazky karet hráče

        # Dealer
        dealer_karty_list, dealer_skore = rozdani_karet("dealer", 1, balicek) # Rozdání první karety
        dealer_text = tk.Label(okno, text=f"({dealer_skore})", bg="black", fg="white", font=("Arial", 14)) # Vytvoří label s celkovým skóre
        dealer_text.place(x=330, y=35) # Zobrazí součet
        zobrazit_karty(dealer_karty_list) # Zobrazí obrazky karet dealera

        # Tlačítka pro Hit a Stand
        stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek))
        stand_btn.pack(padx=10, pady=10, side="bottom")
        hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek))
        hit_btn.pack(padx=10, pady=10, side="bottom")

        # Kolik karet zbývá v balíčku
        zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
        ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
        ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

        # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore.place(x=10, y=10) # Zobrazí celkové skóre

######################### Vykreslování okna #########################

zobraz_menu()
okno.mainloop()