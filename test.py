import tkinter as tk
import random

# Samotné okno aplikace
okno = tk.Tk()
okno.title("Blackjack")
okno.geometry("800x600")

# Nadpis
nadpis = tk.Label(okno, text="Blackjack", font=("Arial", 63))

# Tlačítko pro zahájení hry
frame = tk.Frame(okno)
moznosti = tk.Frame(okno) 
zacatek_btn = tk.Button(moznosti, text ="Začátek hry", command=lambda: obtiznost()) 
pravidla_btn = tk.Button(moznosti, text ="Pravidla", command=lambda: zobraz_pravidla()) 
konec_btn = tk.Button(moznosti, text ="Konec", command=okno.quit)

# Definice hráče a dealera - karty a skóre
hraci_karty = tk.Label(okno, text="Hraci karty: ", font=("Arial", 14))
dealer_karty = tk.Label(okno, text="Dealer karty: ", font=("Arial", 14))
hraci_skore = tk.Label(okno, text="Hraci skore: ", font=("Arial", 14))
dealer_skore = tk.Label(okno, text="Dealer skore: ", font=("Arial", 14))

# Globální proměnné
hrac_skore = 0
dealer_skore = 0
hrac_karty_list = []
dealer_karty_list = []

# Funkce pro určení hodnoty karty
def hodnota_karty(karta, aktualni_skore):
    if karta[0] in ['J', 'Q', 'K']:
        return 10
    elif karta[0] == 'A':
        return 11 if aktualni_skore + 11 <= 21 else 1
    else:
        return int(karta[:-1])

def kontrola_balicku(balicek, puvodni_balicek, multiplikator=1):
    """Ověří, zda balíček obsahuje karty, a případně jej obnoví."""
    if len(balicek) < 10:  # Lze upravit na libovolný počet
        balicek[:] = puvodni_balicek * multiplikator
        random.shuffle(balicek)

def rozdani_karet(hrac, pocet, balicek, puvodni_balicek, multiplikator=1):
    """Rozdá požadovaný počet karet hráči."""
    kontrola_balicku(balicek, puvodni_balicek, multiplikator)
    karty = []
    skore = 0
    for _ in range(pocet):
        karta = random.choice(balicek)
        karty.append(karta)
        skore += hodnota_karty(karta, skore)
        balicek.remove(karta)
    return karty, skore

# Úvodní menu
def zobraz_menu():
    # Vymazat okno
    for widget in okno.winfo_children():
        widget.pack_forget()
    
    # Vytvoření menu
    frame.pack()
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
    pravidla_text = tk.Label(okno, text="""
                             Pravidla: 
                             1. Hrac a dealer dostanou 2 karty.
                             2. Hrac muze zvolit dalsi kartu nebo ukoncit hru.
                             3. Hrac s nejblizsim skore 21 vyhrava.""", 
                            font=("Arial", 14))
    pravidla_text.pack()
    
    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu)
    zpet_btn.pack(padx=10, pady=10)

# Výběr obtížnosti
def obtiznost():
    for widget in okno.winfo_children():
        widget.pack_forget()
    
    obtiznost_text = tk.Label(okno, text="Vyber si obtížnost", font=("Arial", 14))
    obtiznost_text.pack(padx=10, pady=40)

    # Definice původního balíčku
    puvodni_balicek = ["2♤","3♤","4♤","5♤","6♤","7♤","8♤","9♤","10♤","J♤","Q♤","K♤","A♤",
                       "2♧","3♧","4♧","5♧","6♧","7♧","8♧","9♧","10♧","J♧","Q♧","K♧","A♧",
                       "2♡","3♡","4♡","5♡","6♡","7♡","8♡","9♡","10♡","J♡","Q♡","K♡","A♡",
                       "2♢","3♢","4♢","5♢","6♢","7♢","8♢","9♢","10♢","J♢","Q♢","K♢","A♢"]

    obtiznost_easy = tk.Button(okno, text="Lehká", command=lambda: zacatek_hry(1, puvodni_balicek))
    obtiznost_medium = tk.Button(okno, text="Střední", command=lambda: zacatek_hry(3, puvodni_balicek))
    obtiznost_hard = tk.Button(okno, text="Těžká", command=lambda: zacatek_hry(5, puvodni_balicek))
    obtiznost_easy.pack(padx=10, pady=10)
    obtiznost_medium.pack(padx=10, pady=10)
    obtiznost_hard.pack(padx=10, pady=10)

# Zobrazení hracího pole
def zacatek_hry(multiplikator, puvodni_balicek):
    balicek = puvodni_balicek * multiplikator
    random.shuffle(balicek)

    # Připravit nové okno
    for widget in okno.winfo_children():
        widget.pack_forget()

    # Globální proměnné pro skóre a karty
    global hrac_skore, dealer_skore, hrac_karty_list, dealer_karty_list
    hrac_skore = 0
    dealer_skore = 0
    hrac_karty_list = []
    dealer_karty_list = []

    # Rozdání prvních dvou karet
    hrac_karty_list, hrac_skore = rozdani_karet("hráč", 2, balicek, puvodni_balicek, multiplikator)
    dealer_karty_list, dealer_skore = rozdani_karet("dealer", 2, balicek, puvodni_balicek, multiplikator)

    hraci_karty["text"] = "Tvoje karty: " + " ".join(hrac_karty_list)
    hraci_skore["text"] = "Tvoje skóre: " + str(hrac_skore)

    dealer_karty["text"] = "Karty Dealera: " + dealer_karty_list[0] + " [skryto]"
    dealer_skore["text"] = "Skóre Dealera: ???"

    # Zobrazení prvních karet
    hraci_karty.pack(side=tk.BOTTOM, padx=5, pady=50)
    dealer_karty.pack(padx=10, pady=10)
    hraci_skore.pack(side=tk.BOTTOM, pady=10)
    dealer_skore.pack(padx=10, pady=10)

    # Tlačítka Hit a Stand
    hit_btn = tk.Button(okno, text="Hit", command=lambda: dalsi_karta(balicek, puvodni_balicek, multiplikator))
    stand_btn = tk.Button(okno, text="Stand", command=lambda: dealer_tah(balicek, puvodni_balicek, multiplikator))

    hit_btn.pack(side=tk.LEFT, padx=10, pady=20)
    stand_btn.pack(side=tk.RIGHT, padx=10, pady=20)

def dalsi_karta(balicek, puvodni_balicek, multiplikator):
    global hrac_skore, hrac_karty_list
    kontrola_balicku(balicek, puvodni_balicek, multiplikator)

    karta = random.choice(balicek)
    balicek.remove(karta)
    hrac_karty_list.append(karta)
    hrac_skore += hodnota_karty(karta, hrac_skore)

    hraci_karty["text"] = "Tvoje karty: " + " ".join(hrac_karty_list)
    hraci_skore["text"] = "Tvoje skóre: " + str(hrac_skore)

    # Kontrola, zda hráč nepřekročil 21
    if hrac_skore > 21:
        tk.Label(okno, text="Překročil jsi 21! Prohrál jsi.", font=("Arial", 16), fg="red").pack()

def dealer_tah(balicek, puvodni_balicek, multiplikator):
    global dealer_skore, dealer_karty_list
    dealer_karty["text"] = "Karty Dealera: " + " ".join(dealer_karty_list)
    dealer_skore["text"] = "Skóre Dealera: " + str(dealer_skore)

    # Dealer táhne, dokud nemá alespoň 17
    while dealer_skore < 17:
        karta = random.choice(balicek)
        balicek.remove(karta)
        dealer_karty_list.append(karta)
        dealer_skore += hodnota_karty(karta, dealer_skore)
        dealer_karty["text"] = "Karty Dealera: " + " ".join(dealer_karty_list)
        dealer_skore["text"] = "Skóre Dealera: " + str(dealer_skore)

    # Vyhodnocení vítěze
    if dealer_skore > 21 or hrac_skore > dealer_skore:
        tk.Label(okno, text="Vyhrál jsi!", font=("Arial", 16), fg="green").pack()
    elif hrac_skore < dealer_skore:
        tk.Label(okno, text="Prohrál jsi.", font=("Arial", 16), fg="red").pack()
    else:
        tk.Label(okno, text="Remíza!", font=("Arial", 16), fg="blue").pack()

zobraz_menu()
okno.mainloop()