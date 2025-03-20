import tkinter as tk
from PIL import Image, ImageTk
import time
import random

# Samotné okno aplikace
okno = tk.Tk()
okno.title("Blackjack")
okno.geometry("800x600")

# List to keep track of image labels
image_labels = []

# Nadpis
nadpis = tk.Label(okno, text="Blackjack", font=("Arial", 64))

# Tlačítko pro zahejení hry
frame = tk.Frame(okno)
moznosti = tk.Frame(okno) 
zacatek_btn = tk.Button(moznosti, text ="Začátek hry", command=lambda: obtiznost()) 
pravidla_btn = tk.Button(moznosti, text ="Pravidla", command=lambda: zobraz_pravidla()) 
konec_btn = tk.Button(moznosti, text ="Konec", command=okno.quit)

# Globální proměnné
vyhra_hrac = 0
vyhra_dealer = 0
hrac_skore = 0
dealer_skore = 0
hrac_karty_list = []
dealer_karty_list = []

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

# Zobrazit karty
def zobrazit_karty(karty_list):
    for karta in karty_list:
        img = Image.open(obrazky[karta])
        img = img.resize((100, 150), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        vize = tk.Label(okno, image=img_tk)
        vize.image = img_tk
        image_labels.append(vize)
        if karty_list == hrac_karty_list:
            vize.place(x=200 + 45 * hrac_karty_list.index(karta), y=300)
        else:
            vize.place(x=200 + 45 * dealer_karty_list.index(karta), y=50)

# Úvodní menu
def zobraz_menu():
    # Vymazat okno
    for widget in okno.winfo_children():
        widget.pack_forget()
    
    # Vytvoření menu
    frame.pack() # Definuju tlačítka do framu 
    nadpis.pack(padx=10, pady=10)
    moznosti.pack()
    zacatek_btn.pack(padx=10, pady=10)
    pravidla_btn.pack(padx=10, pady=10)
    konec_btn.pack(padx=10, pady=10)

# Pravidla hry
def zobraz_pravidla():
    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()
    
    # Zobrazit pravidla
    pravidla_text = tk.Label(okno, text="Pravidla Blackjacku:\n\n"
"1. Cílem je dostat se co nejblíže k 21, aniž byste překročili tuto hodnotu.\n"
"2. Číselné karty mají hodnotu podle své nominální hodnoty.\n"
"3. Obrázkové karty (Král, Královna, Kluk) mají hodnotu 10.\n"
"4. Eso může mít hodnotu 11 nebo 1.\n"
"5. Můžete 'Táhnout' (Hit) další kartu nebo 'Stát' (Stand) a ponechat si svůj aktuální součet.\n"
"6. Dealer musí táhnout, dokud nedosáhne 17 nebo více.\n"
"7. Pokud překročíte 21, prohrajete a končíte hru.\n", 
                            font=("Arial", 14))
    pravidla_text.pack(padx=10, pady=50)
    
    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu)
    zpet_btn.pack(padx=10, pady=10)

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

# Obtížnost hry
def obtiznost():
    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()

     # Vymazání všech starých obrázků (widgetů)
    for label in image_labels:
        label.destroy()
    image_labels.clear()
    
    # Nulování skóre
    global vyhra_hrac, vyhra_dealer
    vyhra_hrac = 0
    vyhra_dealer = 0

    # Zobrazit obtiznost
    obtiznost_text = tk.Label(okno, text="Vyber obtiznost", font=("Arial", 14))
    obtiznost_text.pack(padx=10, pady=20)

    # Tlačítka pro obtížnost a informace o obtížnosti
    obtiznost_easy = tk.Button(okno, text="Lehká", command=lambda: hra(1))
    info_easy = tk.Label(okno, text="- Jeden blíček karet (52)\n"
"- Žádný hráč navíc", font=("Arial", 10))
    obtiznost_easy.pack(padx=10, pady=5)
    info_easy.pack(pady=2)

    obtiznost_medium = tk.Button(okno, text="Střední", command=lambda: hra(2))
    info_medium = tk.Label(okno, text="- Tři balíčky karet (156)\n"
"- Jeden hráč navíc", font=("Arial", 10))
    obtiznost_medium.pack(padx=10, pady=5)
    info_medium.pack(pady=2)

    obtiznost_hard = tk.Button(okno, text="Těžká", command=lambda: hra(3))
    info_hard = tk.Label(okno, text="- Pět balíčků karet (260)\n"
"- Dva hráči navíc", font=("Arial", 10))
    obtiznost_hard.pack(padx=10, pady=5)
    info_hard.pack(pady=2)

    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu)
    zpet_btn.pack(padx=10, pady=70, side="bottom")

# Zamíchání balíčku
def michani(obtinost):
    if obtinost == 1:
        balicek = puvodni_balicek.copy()
    elif obtinost == 2:
        balicek = puvodni_balicek * 3
    elif obtinost == 3:
        balicek = puvodni_balicek * 5
    random.shuffle(balicek)
    return balicek

# Rozdání karet
def rozdani_karet(kdo, pocet_karet, balicek,):
    karty_list = []
    skore = 0

    for _ in range(pocet_karet):
        karta = balicek.pop()
        karty_list.append(karta)
        skore += hodnota_karty(karta, skore)
    return karty_list, skore

# Hra
def hra(balicek):
    global hrac_skore, dealer_skore, hrac_karty_list, dealer_karty_list
    
    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()
    
    # Balíček karet
    balicek = michani(balicek)

    # Hráč
    hrac_karty_list, hrac_skore = rozdani_karet("hráč", 2, balicek) # Rozdání prvních dvou karet
    hrac_text = tk.Label(okno, text=f"({hrac_skore})", font=("Arial", 14))
    hrac_text.pack(padx=10, pady=10, side="left", anchor="e")
    zobrazit_karty(hrac_karty_list)

    # Dealer
    dealer_karty_list, dealer_skore = rozdani_karet("dealer", 1, balicek) # Rozdání první karety
    dealer_text = tk.Label(okno, text=f"({dealer_skore})", font=("Arial", 14))
    dealer_text.pack(padx=10, pady=10, side="right", anchor="w")
    zobrazit_karty(dealer_karty_list)
    
    stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek))
    stand_btn.pack(padx=10, pady=10, side="bottom")
    hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek))
    hit_btn.pack(padx=10, pady=10, side="bottom")

    # Kolik karet zbývá v balíčku
    zbytek = len(balicek)
    ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}")
    ve_hre.pack(padx=10, pady=10, side="right")

    skore = tk.Label(okno, text=
    f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14))
    skore.pack(padx=10, pady=10, side="left")

# Další karta
def hit(balicek):
    global hrac_skore, hrac_karty_list, dealer_skore, dealer_karty_list, vyhra_dealer, vyhra_hrac
    
    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()

    karta = balicek.pop()
    hrac_karty_list.append(karta)
    hrac_skore += hodnota_karty(karta, hrac_skore)
    hrac_text = tk.Label(okno, text=f"({hrac_skore})", font=("Arial", 14),)
    hrac_text.pack(padx=10, pady=35)
    zobrazit_karty(hrac_karty_list)
    dealer_text = tk.Label(okno, text=f"({dealer_skore})", font=("Arial", 14))
    dealer_text.pack(padx=10, pady=35)
    zobrazit_karty(dealer_karty_list)

    if hrac_skore == 21:
        # Vyčistit okno
        for widget in okno.winfo_children():
            widget.pack_forget()

        vyhra_hrac += 1
        hrac_text = tk.Label(okno, text=f"({hrac_skore}) - WIN +1", font=("Arial", 14))
        zobrazit_karty(hrac_karty_list)
        hrac_text.pack(padx=10, pady=35)
        dealer_text = tk.Label(okno, text=f"({dealer_skore})", font=("Arial", 14))
        dealer_text.pack(padx=10, pady=35)
        zobrazit_karty(dealer_karty_list)
        konec_btn = tk.Button(okno, text="Odejít", command=okno.quit)
        konec_btn.pack(padx=10, pady=10, side="bottom")
        nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
        nova_dvojice_btn.pack(padx=10, pady=10, side="bottom")
        nova_hra_btn = tk.Button(okno, text="Nová hra", command=obtiznost)
        nova_hra_btn.pack(padx=10, pady=10, side="bottom")

    elif hrac_skore < 21:
        stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek))
        stand_btn.pack(padx=10, pady=10, side="bottom")
        hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek))
        hit_btn.pack(padx=10, pady=10, side="bottom")

        # Kolik karet zbývá v balíčku
        zbytek = len(balicek)
        ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}")
        ve_hre.pack(padx=10, pady=10, side="right")

        skore = tk.Label(okno, text=
    f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14))
        skore.pack(padx=10, pady=10, side="left")

    elif hrac_skore > 21:
        # Vyčistit okno
        for widget in okno.winfo_children():
            widget.pack_forget()

        vyhra_dealer += 1
        hrac_text = tk.Label(okno, text=f"({hrac_skore}) - BUST", font=("Arial", 14))
        hrac_text.pack(padx=10, pady=35)
        zobrazit_karty(hrac_karty_list)
        dealer_text = tk.Label(okno, text=f"({dealer_skore}) - WIN +1", font=("Arial", 14))
        dealer_text.pack(padx=10, pady=35)
        zobrazit_karty(dealer_karty_list)
        konec_btn = tk.Button(okno, text="Odejít", command=okno.quit)
        konec_btn.pack(padx=10, pady=10, side="bottom")
        nova_dvojice_btn = tk.Button(okno, text="Rozdat novou dvojici", command=lambda: hra_se_zbylymi_kartami(balicek))
        nova_dvojice_btn.pack(padx=10, pady=10, side="bottom")
        nova_hra_btn = tk.Button(okno, text="Nová hra", command=obtiznost)
        nova_hra_btn.pack(padx=10, pady=10, side="bottom")

# Stání
def stand(balicek):
    global dealer_skore, dealer_karty_list, vyhra_dealer, vyhra_hrac

    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()

    # Dealer draws cards until score reaches 17 or higher
    while dealer_skore < 17:
        karta = balicek.pop()
        dealer_karty_list.append(karta)
        dealer_skore += hodnota_karty(karta, dealer_skore)
    
    # Show the dealer's cards and score
    dealer_text = tk.Label(okno, text=f"Dealer: {dealer_skore}", font=("Arial", 14))
    dealer_text.pack(padx=10, pady=10)
    zobrazit_karty(dealer_karty_list)

    # Determine winner
    if dealer_skore > 21:
        # Dealer busts
        vyhra_hrac += 1
        result_text = tk.Label(okno, text="Dealer busts! You win!", font=("Arial", 14))
    elif hrac_skore > 21:
        # Player busts
        vyhra_dealer += 1
        result_text = tk.Label(okno, text="You bust! Dealer wins!", font=("Arial", 14))
    elif hrac_skore > dealer_skore:
        # Player wins
        vyhra_hrac += 1
        result_text = tk.Label(okno, text="You win!", font=("Arial", 14))
    elif hrac_skore < dealer_skore:
        # Dealer wins
        vyhra_dealer += 1
        result_text = tk.Label(okno, text="Dealer wins!", font=("Arial", 14))
    else:
        # Tie
        result_text = tk.Label(okno, text="It's a tie!", font=("Arial", 14))

    result_text.pack(padx=10, pady=20)

    # Show current score
    skore = tk.Label(okno, text=f"Dealer: {vyhra_dealer}  Hráč: {vyhra_hrac}", font=("Arial", 14))
    skore.pack(padx=10, pady=10)

    # Add buttons for new game or exit
    nova_hra_btn = tk.Button(okno, text="Nová hra", command=obtiznost)
    nova_hra_btn.pack(padx=10, pady=10)
    konec_btn = tk.Button(okno, text="Konec", command=okno.quit)
    konec_btn.pack(padx=10, pady=10)

# Hra s zbylými kartami
def hra_se_zbylymi_kartami(balicek):
    global hrac_skore, dealer_skore, hrac_karty_list, dealer_karty_list

    # Vyčistit okno
    for widget in okno.winfo_children():
        widget.pack_forget()

    # Vymazání všech starých obrázků (widgetů)
    for label in image_labels:
        label.destroy()
    image_labels.clear()

    # Hráč
    hrac_karty_list, hrac_skore = rozdani_karet("hráč", 2, balicek) # Rozdání prvních dvou karet
    hrac_text = tk.Label(okno, text=f"({hrac_skore})", font=("Arial", 14))
    hrac_text.pack(padx=10, pady=35)
    zobrazit_karty(hrac_karty_list)

    # Dealer
    dealer_karty_list, dealer_skore = rozdani_karet("dealer", 1, balicek) # Rozdání první karety
    dealer_text = tk.Label(okno, text=f"({dealer_skore})", font=("Arial", 14))
    dealer_text.pack(padx=10, pady=35)
    zobrazit_karty(dealer_karty_list)

    stand_btn = tk.Button(okno, text="Stand", command=lambda: stand(balicek))
    stand_btn.pack(padx=10, pady=10, side="bottom")
    hit_btn = tk.Button(okno, text="Hit", command=lambda: hit(balicek))
    hit_btn.pack(padx=10, pady=10, side="bottom")

    # Kolik karet zbývá v balíčku
    zbytek = len(balicek)
    ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}")
    ve_hre.pack(padx=10, pady=10, side="right")

    skore = tk.Label(okno, text=
    f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14))
    skore.pack(padx=10, pady=10, side="left")

zobraz_menu()
okno.mainloop()