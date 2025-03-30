import tkinter as tk
from PIL import Image, ImageTk
import time
import random

# Samotné okno aplikace
okno = tk.Tk()
okno.title("Blackjack")
okno.geometry("1200x720")
okno.resizable(False, False)
okno.configure(bg="darkgreen")

######################### Globální promněné #########################
# Seznam pro sledování štítků s obrázky
obrazky_popis = [] 

celkem_her = 0 

vyhra_nej = 0 
vklad_nej = 0 
vyhra_kolik = 0 

balanc = int(10000) # Počáteční kredit
mezi_vklad = 0

obtiznost = 0

hrac_skore = 0 
dealer_skore = 0 
bot_skore = 0

hrac_karty_list = 0
dealer_karty_list = 0
bot_karty_list =0 

vyhra_hrac = 0
vyhra_dealer = 0
vyhra_bot = 0

######################### Balíček #########################

# Balíček karet
puvodni_balicek = ["2♧","3♧","4♧","5♧","6♧","7♧","8♧","9♧","10♧","J♧","Q♧","K♧","A♧",
                    "2♤","3♤","4♤","5♤","6♤","7♤","8♤","9♤","10♤","J♤","Q♤","K♤","A♤",
                    "2♡","3♡","4♡","5♡","6♡","7♡","8♡","9♡","10♡","J♡","Q♡","K♡","A♡",
                    "2♢","3♢","4♢","5♢","6♢","7♢","8♢","9♢","10♢","J♢","Q♢","K♢","A♢"]

balicek = []

# Přiřazení hodnoty k obrázku
obrazky = {
    "2♧": "PNG-cards-1.3/2_of_clubs.png",
    "3♧": "PNG-cards-1.3/3_of_clubs.png",
    "4♧": "PNG-cards-1.3/4_of_clubs.png",
    "5♧": "PNG-cards-1.3/5_of_clubs.png",
    "6♧": "PNG-cards-1.3/6_of_clubs.png",
    "7♧": "PNG-cards-1.3/7_of_clubs.png",
    "8♧": "PNG-cards-1.3/8_of_clubs.png",
    "9♧": "PNG-cards-1.3/9_of_clubs.png",
    "10♧": "PNG-cards-1.3/10_of_clubs.png",
    "J♧": "PNG-cards-1.3/jack_of_clubs2.png",
    "Q♧": "PNG-cards-1.3/queen_of_clubs2.png",
    "K♧": "PNG-cards-1.3/king_of_clubs2.png",
    "A♧": "PNG-cards-1.3/ace_of_clubs.png",
    "2♤": "PNG-cards-1.3/2_of_spades.png",
    "3♤": "PNG-cards-1.3/3_of_spades.png",
    "4♤": "PNG-cards-1.3/4_of_spades.png",
    "5♤": "PNG-cards-1.3/5_of_spades.png",
    "6♤": "PNG-cards-1.3/6_of_spades.png",
    "7♤": "PNG-cards-1.3/7_of_spades.png",
    "8♤": "PNG-cards-1.3/8_of_spades.png",
    "9♤": "PNG-cards-1.3/9_of_spades.png",
    "10♤": "PNG-cards-1.3/10_of_spades.png",
    "J♤": "PNG-cards-1.3/jack_of_spades2.png",
    "Q♤": "PNG-cards-1.3/queen_of_spades2.png",
    "K♤": "PNG-cards-1.3/king_of_spades2.png",
    "A♤": "PNG-cards-1.3/ace_of_spades2.png",
    "2♡": "PNG-cards-1.3/2_of_hearts.png",
    "3♡": "PNG-cards-1.3/3_of_hearts.png",
    "4♡": "PNG-cards-1.3/4_of_hearts.png",
    "5♡": "PNG-cards-1.3/5_of_hearts.png",
    "6♡": "PNG-cards-1.3/6_of_hearts.png",
    "7♡": "PNG-cards-1.3/7_of_hearts.png",
    "8♡": "PNG-cards-1.3/8_of_hearts.png",
    "9♡": "PNG-cards-1.3/9_of_hearts.png",
    "10♡": "PNG-cards-1.3/10_of_hearts.png",
    "J♡": "PNG-cards-1.3/jack_of_hearts2.png",
    "Q♡": "PNG-cards-1.3/queen_of_hearts2.png",
    "K♡": "PNG-cards-1.3/king_of_hearts2.png",
    "A♡": "PNG-cards-1.3/ace_of_hearts.png",
    "2♢": "PNG-cards-1.3/2_of_diamonds.png",
    "3♢": "PNG-cards-1.3/3_of_diamonds.png",
    "4♢": "PNG-cards-1.3/4_of_diamonds.png",
    "5♢": "PNG-cards-1.3/5_of_diamonds.png",
    "6♢": "PNG-cards-1.3/6_of_diamonds.png",
    "7♢": "PNG-cards-1.3/7_of_diamonds.png",
    "8♢": "PNG-cards-1.3/8_of_diamonds.png",
    "9♢": "PNG-cards-1.3/9_of_diamonds.png",
    "10♢": "PNG-cards-1.3/10_of_diamonds.png",
    "J♢": "PNG-cards-1.3/jack_of_diamonds2.png",
    "Q♢": "PNG-cards-1.3/queen_of_diamonds2.png",
    "K♢": "PNG-cards-1.3/king_of_diamonds2.png",
    "A♢": "PNG-cards-1.3/ace_of_diamonds.png"
}

######################### Správa okna #########################

# Čistění okna
def okeno():
    # Vyčistění okna
    for widget in okno.winfo_children():
        widget.pack_forget() # Všechny widgety pod .pack se schovají 
        widget.place_forget() # Všechny widgety pod .place se schovají

    # Vymazání starých obrázků (widgetů)
    for label in obrazky_popis:
        label.destroy()
    obrazky_popis.clear()

# Úvodní menu
def zobraz_menu():
    okeno()

    # Nadpis
    nadpis = tk.Label(okno, text="BLACKJACK", fg="#FCE6C9", bg="darkgreen", font=("Modak", 69)) # Definuje nadpis
    nadpis.pack(padx=10, pady=75) # Generuje nadpis

    # Tlačítka v hlavním menu
    moznosti = tk.Frame(okno, bg="darkgreen") 
    moznosti.pack(padx=10, pady=65) # Definuje možnosti

    zacatek_btn = tk.Button(moznosti, text ="Začátek hry", command=lambda: obtiznost_menu())
    zacatek_btn.pack(padx=10, pady=20) # Tlačítko pro začátek hry
    pravidla_btn = tk.Button(moznosti, text ="Pravidla", command=lambda: zobraz_pravidla())
    pravidla_btn.pack(padx=10, pady=20) # Tlačítko pro zobrazení pravidel
    konec_btn = tk.Button(moznosti, text ="Konec", command=okno.quit)
    konec_btn.pack(padx=10, pady=20) # Tlačítko pro ukončení hry

# Pravidla hry
def zobraz_pravidla():
    okeno()
    
    # Zobrazit pravidla
    pravidla_nadpis = tk.Label(okno, text="Pravidla Blackjacku", bg="darkgreen", fg="#FCE6C9", font=("Modak", 33)) # Nadpis
    pravidla_nadpis.pack(padx=10, pady=10) # Zobrazení nadpisu

    frame = tk.Frame(okno, bg="darkgreen") 
    frame.pack(padx=10, pady=80)

    prom = tk.Label(frame, text="""1. Cíl hry
Cílem je mít na ruce součet blíže k hodnotě 21 než dealer,
aniž bys překročil tuto hodnotu (tzv. "přebití" neboli bust).""", font=("Arial", 20)) # Nadpis
    prom.pack()

    btn1 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""2. Hodnota karet
Karty 2–10  mají svou nominální hodnotu.
J, Q, K (kluk, dáma, král) mají hodnotu 10.
Eso (A) má hodnotu 1 nebo 11, podle toho, co je pro hráče výhodnější."""), btn2.place(x=1000, y=625), btn1.place_forget))
    btn1.place(x=1000, y=625)

    btn2 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""3. Průběh hry
Každý hráč dostane dvě otevřené karty.
Dealer dostane jednu otevřenou kartu a jednu zakrytou (tzv. "hole card").
Hráči se střídají a rozhodují, jak budou pokračovat."""), btn3.place(x=1000, y=625), btn2.place_forget))
    
    btn3 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""4. Možnosti hráče
Stát (Stand): Ukončit tah a nepožadovat další karty.
Táhnout (Hit): Vzít si další kartu. Toto se opakuje, dokud hráč nestojí nebo nepřebije.
Double Down (zdvojnásobení sázky):  Vsadit dvojnásobek původní sázky a vzít si právě jednu kartu."""), btn4.place(x=1000, y=625), btn3.place_forget))
    
    btn4 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""5. Dealerovy pravidla
Dealer musí táhnout (hit), dokud nemá součet alespoň 17.
Pokud dealer přebije (bust), všichni zbývající hráči vyhrávají.
Dealer nesmí double down, split ani surrender."""), btn5.place(x=1000, y=625), btn4.place_forget))

    btn5 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""6. Speciální situace
Push: Pokud hráč i dealer skončí se stejným součtem, jedná se o remízu a sázka se vrací."""), btn6.place(x=1000, y=625), btn5.place_forget))

    btn6 = tk.Button(okno, text="Další", command=lambda: (prom.config(text="""7. Výplaty
Výhra v jednoduchém režimu: Pokud hráč porazí dealera, vyhrává 2,5 krát to co vsadil
                   (např. sázka 100 = výhra 250 -> 100 je ze sázky a 150 jste vydělali)

Výhra v normálním režimu: Pokud hráč porazí dealera, vyhrává 2 krát to co vsadil
                   (např. sázka 100 = výhra 200 -> 100 je ze sázky a 100 je výhra)

Výhra v těžkém režimu: Pokud hráč porazí dealera, vyhrává 1,5 krát to co vsadil
                   (např. sázka 100 = výhra 150 -> 100 je ze sázky a 50 jste vyhráli)

Přebití:  Pokud hráč přebije 21, prohrává automaticky."""), zpet_btn.place(x=1002, y=625)))
    
    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu)

# Zobrazení statistiky
def stat():
    okeno()

    global vyhra_nej, vyhra_kolik, vklad_nej, balanc, celkem_her

    frame = tk.Frame(okno, bg="darkgreen")
    frame.pack(padx=12, pady=110)

    # Label pro celkem odehraných her
    celkem = tk.Label(frame, text=f"Hráli jste celkem................{celkem_her} her", bg="darkgreen", fg="#FCE6C9", font=("Arial", 20))
    celkem.pack(padx=12, pady=12)

    # Label pro celkový počet výher skrz obtížností
    vyhra = tk.Label(frame, text=f"Vyhrali jste................{vyhra_kolik}x", bg="darkgreen", fg="#FCE6C9", font=("Arial", 20))
    vyhra.pack(padx=12, pady=12)

    # Výpočet procenta
    if celkem_her == 0: # Pokus není odehraná ani jedna hra tak se celkový počet her dělí 1
        pro_h = (vyhra_kolik / 1) * 100
    else: # Pro ostatní případy se procento počítá jakož to kolik krát hráč vyhrál děleno celkovým počtem her
        pro_h = (vyhra_kolik / celkem_her) * 100
    
    procento = tk.Label(frame, text=f"Procentuálně jste vyhrál................{int(pro_h)} %", bg="darkgreen", fg="#FCE6C9", font=("Arial", 20))
    procento.pack(padx=12, pady=12)

    # Label pro určovaní kolik jste vyhráli nejvíc v jedné hře 
    nej_vyhra = tk.Label(frame, text=f"Nejvíc jste vyhrál................{int(vyhra_nej)}", bg="darkgreen", fg="#FCE6C9", font=("Arial", 20))
    nej_vyhra.pack(padx=12, pady=12)

    # Label pro určení největšího vkladu 
    nej_vklad = tk.Label(frame, text=f"Největší vklad činil................{int(vklad_nej)}", bg="darkgreen", fg="#FCE6C9", font=("Arial", 20))
    nej_vklad.pack(padx=12, pady=12)

    # Určování proměné obce pro obrazovku stat, když vám dojdou peníze končíte hru
    if balanc > 0:
        obce = 1
    else:
        obce = 0

    if obce == 0:
        konec_text = tk.Label(okno, text="Konec hry", bg="darkgreen", fg="#FCE6C9", font=("Modak", 45))
        konec_text.pack(side="top", padx=10, pady=10)

        konec_btn = tk.Button(okno, text ="Konec", command=okno.quit)
        konec_btn.place(x=950, y=100) # Tlačítko pro ukončení hry
    else:
        zpet_btn = tk.Button(okno, text="Zpět do menu", command=obtiznost_menu)
        zpet_btn.place(x=950, y=100)

######################### Systém pro žetonů #########################

# Tlačítka pro vklad
def vklad(obt):
    okeno()

    global balanc, mezi_vklad, obtiznost

    # Pokud vám dojdou peníze, končíte a ukáže se vám statistika
    if balanc == 0:
        stat()

    else: # Pokud máte peníze můžete stale sázet
        obtiznost += obt

        balanc_text = tk.Label(okno, text=f"Kredit: {int(balanc)}", bg="navy", fg="white", font=("Arial", 24))
        balanc_text.place(x=25, y=25) # Vypíše zbylé kredity 
        sazka_text = tk.Label(okno, text=f"{int(mezi_vklad)}", bg="black", fg="white", font=("Arial", 37))
        sazka_text.place(x=550, y=250) # Ukazuje kolik sázíte 

        z25 = tk.Button(okno, text="25", command=lambda: (trakce(25), 
                                                      balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                      sazka_text.config(text=f"{int(mezi_vklad)}")))
        z25.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 25 kreditů

        z50 = tk.Button(okno, text="50", command=lambda: (trakce(50), 
                                                      balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                      sazka_text.config(text=f"{int(mezi_vklad)}")))
        z50.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 50 kreditů

        z100 = tk.Button(okno, text="100", command=lambda: (trakce(100),
                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
        z100.pack(side="left", anchor="s", padx=48, pady=175)# Tlačítko pro vklad 100 kreditů

        z200 = tk.Button(okno, text="200", command=lambda: (trakce(200),
                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
        z200.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 200 kreditů

        z500 = tk.Button(okno, text="500", command=lambda: (trakce(500),
                                                            balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                            sazka_text.config(text=f"{int(mezi_vklad)}")))
        z500.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 500 kreditů

        z1000 = tk.Button(okno, text="1 000", command=lambda: (trakce(1000),
                                                           balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                           sazka_text.config(text=f"{int(mezi_vklad)}")))
        z1000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 1000 kreditů

        z2000 = tk.Button(okno, text="2 000", command=lambda: (trakce(2000),
                                                           balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                           sazka_text.config(text=f"{int(mezi_vklad)}")))
        z2000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 2000 kreditů

        z5000 = tk.Button(okno, text="5 000", command=lambda: (trakce(5000),
                                                               balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                               sazka_text.config(text=f"{int(mezi_vklad)}")))
        z5000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 5000 kreditů

    if obtiznost == 1:
        hra_btn = tk.Button(okno, text="Jde se hrát!", command=lambda: hra(1))
    elif obtiznost == 2:
        hra_btn = tk.Button(okno, text="Jde se hrát!", command=lambda: hra(2))
    else:
        hra_btn = tk.Button(okno, text="Jde se hrát!", command=lambda: hra(3))
    
    hra_btn.place(x=525, y=650) # Zobrazení tlačítka

    zrus_btn = tk.Button(okno, text="Zrušit sázku", bg="palevioletred2", fg="black", command=lambda: (trakce(1),
                                                                                                      balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                                                                      sazka_text.config(text=f"{int(mezi_vklad)}")))
    zrus_btn.place(x=990, y=650) # Tlačítko pro zrušení sázky

    all_btn = tk.Button(okno, text=" All-in", bg="cyan3", fg="black", command=lambda: (all_in(),
                                                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
    all_btn.place(x=800, y=650) # Tlačítko pro All-in

    zpet_btn = tk.Button(okno, text="Zpět do menu", command=obtiznost_menu)
    zpet_btn.place(x=950, y=100) # Tlačítko pro zpět do menu

# Vklady pro další hry
def pokracovani(balicek):
    okeno()

    global balanc, mezi_vklad, obtiznost

    # Pokud vám dojdou peníze, končíte a ukáže se vám statistika
    if balanc == 0:
        stat()

    else: # Pokud máte peníze můžete stale sázet
        balanc_text = tk.Label(okno, text=f"Kredit: {int(balanc)}", bg="navy", fg="white", font=("Arial", 24))
        balanc_text.place(x=25, y=25) # Vypíše zbylé kredity 
        sazka_text = tk.Label(okno, text=f"{int(mezi_vklad)}", bg="black", fg="white", font=("Arial", 37))
        sazka_text.place(x=550, y=250) # Ukazuje kolik sázíte

        z25 = tk.Button(okno, text="25", command=lambda: (trakce(25), 
                                                      balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                      sazka_text.config(text=f"{int(mezi_vklad)}")))
        z25.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 25 kreditů

        z50 = tk.Button(okno, text="50", command=lambda: (trakce(50), 
                                                      balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                      sazka_text.config(text=f"{int(mezi_vklad)}")))
        z50.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 50 kreditů

        z100 = tk.Button(okno, text="100", command=lambda: (trakce(100),
                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
        z100.pack(side="left", anchor="s", padx=48, pady=175)# Tlačítko pro vklad 100 kreditů

        z200 = tk.Button(okno, text="200", command=lambda: (trakce(200),
                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
        z200.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 200 kreditů

        z500 = tk.Button(okno, text="500", command=lambda: (trakce(500),
                                                            balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                            sazka_text.config(text=f"{int(mezi_vklad)}")))
        z500.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 500 kreditů

        z1000 = tk.Button(okno, text="1 000", command=lambda: (trakce(1000),
                                                           balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                           sazka_text.config(text=f"{int(mezi_vklad)}")))
        z1000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 1000 kreditů

        z2000 = tk.Button(okno, text="2 000", command=lambda: (trakce(2000),
                                                           balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                           sazka_text.config(text=f"{int(mezi_vklad)}")))
        z2000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 2000 kreditů

        z5000 = tk.Button(okno, text="5 000", command=lambda: (trakce(5000),
                                                               balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                               sazka_text.config(text=f"{int(mezi_vklad)}")))
        z5000.pack(side="left", anchor="s", padx=48, pady=175) # Tlačítko pro vklad 5000 kreditů

        hra_btn = tk.Button(okno, text="Jde se hrát!", command=lambda: hra_se_zbylymi_kartami(balicek))
        hra_btn.place(x=525, y=650) # Zobrazení tlačítka

        zrus_btn = tk.Button(okno, text="Zrušit sázku", bg="palevioletred2", fg="black", command=lambda: (trakce(1),
                                                                                                        balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                                                                        sazka_text.config(text=f"{int(mezi_vklad)}")))
        zrus_btn.place(x=990, y=650) # Tlačítko pro zrušení sázky

        all_btn = tk.Button(okno, text=" All-in", bg="cyan3", fg="black", command=lambda: (all_in(),
                                                                                            balanc_text.config(text=f"Kredit: {int(balanc)}"), 
                                                                                            sazka_text.config(text=f"{int(mezi_vklad)}")))
        all_btn.place(x=800, y=650) # Tlačítko pro All-in

        zpet_btn = tk.Button(okno, text="Zpět do menu", command=obtiznost_menu)
        zpet_btn.place(x=950, y=100) # Tlačítko pro zpět do menu

# Vyplácení výher
def vyplaceni():

    global balanc, mezi_vklad, vklad_nej, vyhra_nej, vyhra_kolik, sazka_text

    # Počítání celkovývh výher (vyplácení kreditů = výhra hráče)
    vyhra_kolik += 1

    # Vyplácení ve hře
    if obtiznost == 1: # Vyplácení kreditů v jednoduché hře
        vyhra = mezi_vklad * 2.5
        balanc += vyhra

        sazka_text.config(text=f"Vyhráváš: {int(vyhra)}") # Aktualizuje sázku

    elif obtiznost == 2: # Vyplácení kreditů ve střední hře
        vyhra = mezi_vklad * 2
        balanc += vyhra

        sazka_text.config(text=f"Vyhráváš: {int(vyhra)}") # Aktualizuje sázku

    else: # Vyplácení kreditů v těžké hře
        vyhra = mezi_vklad * 1.5
        balanc += vyhra

        sazka_text.config(text=f"Vyhráváš: {int(vyhra)}") # Aktualizuje sázku

    # Porovnávání největších výher a sázek
    if mezi_vklad > vklad_nej:
        vklad_nej = mezi_vklad
    
    if vyhra > vyhra_nej:
        vyhra_nej = vyhra

# Definování funkce pro vklad všech peněz
def all_in():
    global balanc, mezi_vklad

    mezi_vklad += balanc
    balanc = 0

# Operace mezi kredity a sázek
def trakce(hodnota):    
    global balanc, mezi_vklad    
    
    # Omezení pro záporných kreditů
    if balanc - hodnota >= 0: # Pokud je sázka menší jak celkový počet kreditů, tak projde
        balanc -= int(hodnota)
        mezi_vklad += int(hodnota)
    else: # V jiném případě vyskoči varování
        varov = tk.Label(okno, text="Nemůžeš víc vsadit, nemáš dostatečný balanc", bg="red2", fg="white", font=("Arial", 20))
        varov.pack(pady=250)
        okno.after(1000, varov.pack_forget)
        
    if hodnota == 1:
        balanc += mezi_vklad
        mezi_vklad = 0

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
def zobrazit_karty(karty_list, opt):
    global obtiznost

    # Zobrazení karet lícema nahoru
    # Pro každou kartu, která se nachází v seznamu karet a bude hraná
    for index, karta in enumerate(karty_list): # Pro každou kartu v seznamu karty_list se získá její index (pozice v seznamu) a hodnota
        img = Image.open(obrazky[karta]) # Otevření obrázku
        img = img.resize((110, 165), Image.LANCZOS) # Změna velikosti obrázku
        img_tk = ImageTk.PhotoImage(img) # Převedení obrázku do formátu, který tkinter může zobrazit
        vize = tk.Label(okno, image=img_tk) # Vytvoření labelu s obrázkem
        vize.image = img_tk # Přiřazení obrázku k labelu
        obrazky_popis.append(vize) # Přidání labelu do listu

        # Zobrazení karty lícem dolů - estetický důvod
        zadni_img = Image.open("poker back /card back blue.png") # Otevření obrázku pro zadní stranu karty
        zadni_img = zadni_img.resize((110, 165), Image.LANCZOS) # Změna velikosti obrázku
        zadni_img_tk = ImageTk.PhotoImage(zadni_img) # Převedení obrázku do formátu, který tkinter může zobrazit
        zadni = tk.Label(okno, image=zadni_img_tk) # Vytvoření labelu s obrázkem
        zadni.image = zadni_img_tk # Přiřazení obrázku k labelu
        obrazky_popis.append(zadni) # Přidání labelu do listu
        zadni.place(x=1050, y=35) # Zobrazí zadní stranu karty v okně

        if obtiznost == 1: # Pokud je obtížnost 1 (lehká)
            if karty_list == hrac_karty_list: # Pokud se jedná o karty hráče
                vize.place(x=500 + 40 * index, y=380) # Zobrazí karty hráče
            else: # Pokud se jedná o karty dealera
                if opt == True: # Pokud je opt True, tak se zobrazí zadní strana karty
                    if index == 1:
                        zadni.place(x=500 + 40, y=70)
                    else: # Pokud je opt False, tak se zobrazí karta lícem nahoru
                        vize.place(x=500 + 40 * index, y=70) # Zobrazí karty dealera
                else:
                    vize.place(x=500 + 40 * index, y=70) # Zobrazí karty dealera

        else: # Pokud je obtížnost střední nebo težká
            if karty_list == hrac_karty_list: # Pokud se jedná o karty hráče
                vize.place(x=750 + 40 * index, y=380) # Zobrazí karty hráče
            elif karty_list == dealer_karty_list: # Pokud se jedná o karty dealera
                if opt == True: # Pokud je opt True, tak se zobrazí zadní strana karty
                    if index == 1:
                        zadni.place(x=500 + 40, y=70)
                    else: # Pokud je opt False, tak se zobrazí karta lícem nahoru
                        vize.place(x=500 + 40 * index, y=70) # Zobrazí karty dealera
                else:
                    vize.place(x=500 + 40 * index, y=70) # Zobrazí karty dealera
            else: # Karty bota
                vize.place(x=230 + 40 * index, y=380) # Zobrazí karty Bota

# Zamíchání balíčku
def michani(obt):
    if obt == 1: # Pokud je obtížnost 1 = lehká
        balicek = puvodni_balicek.copy() # Vytvoří kopii původního balíčku, neboli 52 karet
    elif obt == 2: # Pokud je obtížnost 2 = střední
        balicek = puvodni_balicek * 3 # Vytvoří seznam se třemi balícky, neboli 156 karet
    elif obt == 3: # Pokud je obtížnost 3 = těžká
        balicek = puvodni_balicek * 5 # Vytvoří seznam se pěti balíčky, neboli 260 karet
    random.shuffle(balicek) # Zamíchá seznam s vygenerovanými kartami
    return balicek # Vrátí zamíchaný balíček jako výstup

# Funkce pro rozdání karet
def rozdani_karet(pocet_karet, balicek,):
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

    # Vynulování skóre aobtížnosti
    vyhra_hrac = 0
    vyhra_dealer = 0 
    obtiznost = 0

    # Zobrazit obtiznost
    obtiznost_text = tk.Label(okno, text="Vyber te si obtížnost", bg="darkgreen", fg="#FCE6C9", font=("Modak", 33)) # Nadpis
    obtiznost_text.pack(padx=10, pady=20) # Zobrazení nadpisu

    # Tlačítka pro obtížnost a informace o obtížnosti
    obtiznost_easy = tk.Button(okno, text="Lehká", bg="green", fg="white", command=lambda: vklad(1)) # Tlačítko pro lehkou obtížnost
    info_easy = tk.Label(okno, text="- Jeden blíček karet (52)\n" 
"- Žádný hráč navíc\n"
"- Výhra se násobí x2,5", bg="darkgreen", fg="#FCE6C9", font=("Arial", 13)) # Informace o lehké obtížnosti
    obtiznost_easy.place(x=250, y=150) # Zobrazení tlačítka
    info_easy.place(x=185, y=200) # Zobrazení informací

    obtiznost_medium = tk.Button(okno, text="Střední", bg="orange", fg="white", command=lambda: vklad(2)) # Tlačítko pro střední obtížnost
    info_medium = tk.Label(okno, text="- Tři balíčky karet (156)\n"
"- Jeden hráč navíc\n"
"- Výhra se násobí x2", bg="darkgreen", fg="#FCE6C9", font=("Arial", 13)) # Informace o střední obtížnosti
    obtiznost_medium.place(x=560, y=150) # Zobrazení tlačítka
    info_medium.place(x=503, y=200) # Zobrazení informací

    obtiznost_hard = tk.Button(okno, text="Těžká", bg="red", fg="white", command=lambda: vklad(3)) # Tlačítko pro těžkou obtížnost
    info_hard = tk.Label(okno, text="- Pět balíčků karet (260)\n"
"- Jeden hráč navíc\n"
"- Výhra se násobí x1,5", bg="darkgreen", fg="#FCE6C9", font=("Arial", 13)) # Informace o těžké obtížnosti
    obtiznost_hard.place(x=870, y=150) # Zobrazení tlačítka
    info_hard.place(x=805, y=200) # Zobrazení informací

    # Tlačítko pro návrat do menu
    zpet_btn = tk.Button(okno, text="Zpět", command=zobraz_menu) # Tlačítko pro návrat do hlavního menu
    zpet_btn.pack(padx=10, pady=70, side="bottom") # Zobrazení tlačítka

    # Tlačítko pro stats
    stat_btn = tk.Button(okno, text="Statistika", command=stat) # Tlačítko pro návrat do hlavního menu
    stat_btn.pack(padx=10, pady=70, side="bottom") # Zobrazení tlačítka

# Hra
def hra(balicek):
    okeno()

    global hrac_skore, dealer_skore, bot_skore, hrac_karty_list, dealer_karty_list, bot_karty_list, hrac_text, dealer_text, bot_text, sazka_text, btn, double_btn, ve_hre, balanc, mezi_vklad, obtiznost, celkem_her # Globální proměnné pro skóre, seznamy karet

    # Hraje se první partie a přičítá se kvůli tomu 1
    celkem_her += 1

    # Balíček karet
    balicek = michani(balicek) # Definuje hrací balíček pomocí funkce michani

    # Rozdání karet dealerovi
    dealer_karty_list, dealer_skore = rozdani_karet(2, balicek) # Rozdání první karety
    dealer_text = tk.Label(okno, text="?", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre dealera
    zobrazit_karty(dealer_karty_list, True) # Zobrazí karty dealera
    dealer_text.place(x=500, y=35)

    # Rozdání karet hráči
    hrac_karty_list, hrac_skore = rozdani_karet(2, balicek) # Rozdání první karety
    hrac_text = tk.Label(okno, text=f"{int(hrac_skore)}", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre hráče
    zobrazit_karty(hrac_karty_list, 1) # Zobrazí karty hráče

    text_hrac = tk.Label(okno, text="Vaše karty", bg="black", fg="white", font=("Arial", 14)) # Zobrazí text "Hráč"

    x_hrac_text = 500 if obtiznost == 1 else 750 # Určuje pozici textu podle obtížnosti
    hrac_text.place(x=x_hrac_text, y=345) # Zobrazí skóre hráče
    text_hrac.place(x=x_hrac_text, y=560) # Zobrazí text "Hráč"

    if obtiznost != 1: # Pokud není lehká obtížnost
        # Rozdání karet botovi
        bot_karty_list, bot_skore = rozdani_karet(2, balicek) # Rozdání první karety
        bot_text = tk.Label(okno, text=f"{int(bot_skore)}", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre bota
        zobrazit_karty(bot_karty_list, 1) # Zobrazí karty bota
        bot_text.place(x=230, y=345)

        tom_text = tk.Label(okno, text="Tomáš - Host", bg="black", fg="white", font=("Arial", 14)) # Zobrazí text "Bot"
        tom_text.place(x=230, y=560) # Zobrazí text "Bot"
    
    # Balanc a sázka
    balanc_text = tk.Label(okno, text=f"Kredit: {int(balanc)}", bg="navy", fg="white", font=("Arial", 20)) 
    balanc_text.place(x=10, y=10)
    sazka_text = tk.Label(okno, text=f"Vsazeno: {int(mezi_vklad)}", bg="silver", fg="black", font=("Arial", 17))
    sazka_text.place(x=10, y=50)

    zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
    ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
    ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

    # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
    skore.place(x=950, y=40) # Zobrazí celkové skóre

    btn = tk.Frame(okno, bg="darkslategray4") # Vytvoří frame pro tlačítka

    hit_btn = tk.Button(btn, text="Hit", command=lambda: (double_btn.destroy(), hit(balicek)))  # Tlačítko pro další kartu
    hit_btn.pack(side="left", anchor="s", padx=10, pady=10) # Zobrazí tlačítko
    stand_btn = tk.Button(btn, text="Stand", command=lambda: (double_btn.destroy(), stand(balicek)))  # Tlačítko pro stání
    stand_btn.pack(side="left", anchor="s", padx=10, pady=10) # Zobrazí tlačítko

    btn.pack(side="right", anchor="s", pady=50, padx=70) # Zobrazení frame s tlačítky

    double_btn = tk.Button(okno, text="2x", command=lambda: double(balicek))  # Tlačítko pro double
    if mezi_vklad <= balanc: # Pokud je možné zdvojnásobit sázku
        double_btn.place(x=1020, y=580) # Zobrazí tlačítko

# Další karta
def hit(balicek): 
    
    global hrac_skore, dealer_skore, bot_skore, vyhra_dealer, vyhra_hrac, hrac_text, dealer_text, bot_text, ve_hre, btn, balanc, mezi_vklad, obtiznost, vklad_nej # Globální proměnné pro skóre a seznamy karet

    karta = balicek.pop() # Vybere kartu z balíčku
    hrac_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
    hrac_skore += hodnota_karty(karta, hrac_skore) # Přičte hodnotu karty k celkovému skóre hráče

    hrac_text.config(text=f"{int(hrac_skore)}") # Aktualizuje skóre hráče
    zobrazit_karty(hrac_karty_list, 1) # Zobrazí obrazky karet hráče

    zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
    ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku

    okno.update() # Aktualizuje okno
    
    if hrac_skore > 21: # Pokud hráč má více než 21

        btn.destroy() # Zničí tlačítka

        vyhra_dealer += 1 # Přičte se dealerovi bod za výhru

        hrac_text.config(text=f"{int(hrac_skore)} - Prohrál jsi") # Aktualizuje skóre hráče
        sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

        if obtiznost > 1: # Lízání karet pro bota
            while bot_skore < 19: # Bot líže kartu dokud nemá přes 19 (dealer přes 17)
                time.sleep(1)
                
                karta = balicek.pop() # Vybere kartu z balíčku
                bot_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
                bot_skore += hodnota_karty(karta, bot_skore) # Přičte hodnotu karty k celkovému skóre hráč

                bot_text.config(text=f"{int(bot_skore)}") # Aktualizuje skóre hráče
                zobrazit_karty(bot_karty_list, 1) # Zobrazí obrazky karet hráče

                zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
                ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku

                okno.update() # Aktualizuje okno

            time.sleep(1)

            zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet
            dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera

            okno.update() # Aktualizuje okno

            while dealer_skore < 17 and dealer_skore < bot_skore: # Dealer líže kartu dokud nemá přes 17
                karta = balicek.pop() # Vybere kartu z balíčku
                dealer_karty_list.append(karta) # Přidá kartu do seznamu karet dealera
                dealer_skore += hodnota_karty(karta, dealer_skore) # Přičte hodnotu karty k celkovému skóre dealera

                dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera
                zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet

                zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
                ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku
            
                time.sleep(1)
                okno.update() # Aktualizuje okno

            if dealer_skore > 21: # Pokud dealer má více než 21
                dealer_text.config(text=f"{int(dealer_skore)} - Prohrál i Dealer") # Aktualizuje skóre hráče
            else:
                dealer_text.config(text=f"{int(dealer_skore)} - Vyhrál") # Aktualizuje skóre dealera

            sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

            if mezi_vklad > vklad_nej:
                vklad_nej = mezi_vklad

            mezi_vklad = 0

            # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
            nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
            nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
            nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

        else:
            zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet
            dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera

            okno.update() # Aktualizuje okno

            if mezi_vklad > vklad_nej:
                vklad_nej = mezi_vklad

            hrac_text.config(text=f"{int(hrac_skore)} - Prohrál jsi") # Aktualizuje skóre hráče
            sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

            mezi_vklad = 0

            # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
            nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
            nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
            nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

# Funkce double 
def double(balicek):

    global hrac_skore, dealer_skore, bot_skore, vyhra_dealer, hrac_text, dealer_text, bot_text, sazka_text, ve_hre, btn, double_btn, obtiznost, mezi_vklad, vklad_nej # Globální proměnné pro skóre a seznamy karet

    double_btn.destroy() # Skryje tlačítko pro double
    btn.destroy() # Skryje tlačítka pro hit a stand

    mezi_vklad = mezi_vklad * 2

    karta = balicek.pop() # Vybere kartu z balíčku
    hrac_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
    hrac_skore += hodnota_karty(karta, hrac_skore) # Přičte hodnotu karty k celkovému skóre hráče
    
    hrac_text.config(text=f"{int(hrac_skore)}") # Aktualizuje skóre hráče
    zobrazit_karty(hrac_karty_list, 1) # Zobrazí obrazky karet hráče

    sazka_text.config(text=f"Vsazeno: {int(mezi_vklad)}") # Aktualizuje sázku

    okno.update() # Aktualizuje okno

    if hrac_skore > 21: # Pokud hráč má více než 21

        vyhra_dealer += 1 # Přičte se dealerovi bod za výhru

        hrac_text.config(text=f"{int(hrac_skore)} - Prohrál jsi") # Aktualizuje skóre hráče
        sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

        if obtiznost > 1: # Lízání karet pro bota
            while bot_skore < 19: # Bot líže kartu dokud nemá přes 19 (dealer přes 17)
                time.sleep(1)
                
                karta = balicek.pop() # Vybere kartu z balíčku
                bot_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
                bot_skore += hodnota_karty(karta, bot_skore) # Přičte hodnotu karty k celkovému skóre hráč

                bot_text.config(text=f"{int(bot_skore)}") # Aktualizuje skóre hráče
                zobrazit_karty(bot_karty_list, 1) # Zobrazí obrazky karet hráče

                zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
                ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku

                okno.update() # Aktualizuje okno

            time.sleep(1)

            zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet
            dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera

            okno.update() # Aktualizuje okno

            while dealer_skore < 17 and dealer_skore < bot_skore:
                karta = balicek.pop() # Vybere kartu z balíčku
                dealer_karty_list.append(karta) # Přidá kartu do seznamu karet dealera
                dealer_skore += hodnota_karty(karta, dealer_skore) # Přičte hodnotu karty k celkovému skóre dealera

                dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera
                zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet

                zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
                ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku
            
                time.sleep(1)
                okno.update() # Aktualizuje okno  ####

            if dealer_skore > 21: # Pokud dealer má více než 21
                dealer_text.config(text=f"{int(dealer_skore)} - Prohrál i Dealer") # Aktualizuje skóre hráče
            else:
                dealer_text.config(text=f"{int(dealer_skore)} - Vyhrál") # Aktualizuje skóre dealera

            if mezi_vklad > vklad_nej:
                vklad_nej = mezi_vklad

            mezi_vklad = 0

            # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
            nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
            nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
            nova_hra_btn.place(x=25, y=670) # Změna obtížnosti
            
        else:
            zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet
            dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera

            okno.update() # Aktualizuje okno

            if mezi_vklad > vklad_nej:
                vklad_nej = mezi_vklad

            hrac_text.config(text=f"{int(hrac_skore)} - Prohrál jsi") # Aktualizuje skóre hráče
            sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

            mezi_vklad = 0

            # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
            nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
            nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
            nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
            nova_hra_btn.place(x=25, y=670) # Změna obtížnosti
    else:
        time.sleep(1) # Čeká 1 sekundu
        stand(balicek)

# Stání
def stand(balicek):

    global dealer_skore, bot_skore, vyhra_dealer, vyhra_hrac, hrac_text, dealer_text, bot_text, sazka_text, ve_hre, btn, obtiznost, balanc, mezi_vklad, vklad_nej # Globální proměnné pro skóre a seznamy karet

    btn.destroy() # Skryje tlačítka

    if obtiznost > 1: # Lízání karet pro bota
        while bot_skore < 19: # Bot líže kartu dokud nemá přes 19 (dealer přes 17)
            time.sleep(1)
                
            karta = balicek.pop() # Vybere kartu z balíčku
            bot_karty_list.append(karta) # Přidá kartu do seznamu karet hráče
            bot_skore += hodnota_karty(karta, bot_skore) # Přičte hodnotu karty k celkovému skóre hráč

            bot_text.config(text=f"{int(bot_skore)}") # Aktualizuje skóre hráče
            zobrazit_karty(bot_karty_list, 1) # Zobrazí obrazky karet hráče

            zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
            ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku

            okno.update() # Aktualizuje okno

    time.sleep(1)

    zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet
    dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera

    okno.update() # Aktualizuje okno
    
    while dealer_skore < 17 and (hrac_skore >= dealer_skore or bot_skore >= dealer_skore): # Dealer líže kartu dokud nemá přes 17 (dealer přes 17)
        karta = balicek.pop() # Vybere kartu z balíčku
        dealer_karty_list.append(karta) # Přidá kartu do seznamu karet dealera
        dealer_skore += hodnota_karty(karta, dealer_skore) # Přičte hodnotu karty k celkovému skóre dealera

        dealer_text.config(text=f"{int(dealer_skore)}") # Aktualizuje skóre dealera
        zobrazit_karty(dealer_karty_list, False) # Zobrazí obrazky karet

        zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
        ve_hre.config(text=f"Karet v balíčku {zbytek}") # Zobrazí informaci o počtu karet v balíčku
            
        time.sleep(1)
        okno.update() # Aktualizuje okno

    if dealer_skore > 21:

        vyhra_hrac += 1 # Přičte se hráči bod za výhru

        hrac_text.config(text=f"{int(hrac_skore)} - Vyhrál jsi") # Aktualizuje skóre hráče
        dealer_text.config(text=f"{int(dealer_skore)} - Prohrál") # Aktualizuje skóre dealera

        vyplaceni()

        mezi_vklad = 0

        # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
        nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
        nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
        nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

    elif hrac_skore > dealer_skore:

        vyhra_hrac += 1 # Přičte se hráči bod za výhru

        hrac_text.config(text=f"{int(hrac_skore)} - Vyhrál jsi") # Aktualizuje skóre hráče
        dealer_text.config(text=f"{int(dealer_skore)} - Prohrál") # Aktualizuje skóre dealera

        vyplaceni()

        mezi_vklad = 0

        # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
        nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
        nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
        nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

    elif dealer_skore > hrac_skore:

        vyhra_dealer += 1 # Přičte se dealerovi bod za výhru

        hrac_text.config(text=f"{int(hrac_skore)} - Prohrál jsi") # Aktualizuje skóre hráče
        dealer_text.config(text=f"{int(dealer_skore)} - Vyhrál") # Aktualizuje skóre dealera

        sazka_text.config(text=f"Ztrácíš: {int(mezi_vklad)}") # Aktualizuje sázku

        if mezi_vklad > vklad_nej:
            vklad_nej = mezi_vklad

        mezi_vklad = 0

        # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
        nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
        nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
        nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

    else:
        hrac_text.config(text=f"{int(hrac_skore)} - Push") # Aktualizuje skóre hráče
        dealer_text.config(text=f"{int(dealer_skore)} - Push") # Aktualizuje skóre dealera

        sazka_text.config(text=f"Vrací se ti: {int(mezi_vklad)}") # Aktualizuje sázku

        balanc += mezi_vklad

        if mezi_vklad > vklad_nej:
            vklad_nej = mezi_vklad

        mezi_vklad = 0

        # Vytvoří se dvě tlačítka pro pokračováním hry nebo s možnstí změnit obtížnost
        nova_dvojice_btn = tk.Button(okno, text="Nová sázka", command=lambda: pokracovani(balicek))
        nova_dvojice_btn.place(x=520, y=620) # Pokračování ve hře
        nova_hra_btn = tk.Button(okno, text="Obtížnosti", command=lambda: obtiznost_menu())
        nova_hra_btn.place(x=25, y=670) # Změna obtížnosti

# Po první hře zbydou karty a zde se hraje dál
def hra_se_zbylymi_kartami(balicek):
    okeno()

    global hrac_skore, dealer_skore, bot_skore, hrac_karty_list, dealer_karty_list, bot_karty_list, hrac_text, dealer_text, bot_text, sazka_text, ve_hre, btn, balanc, mezi_vklad, obtiznost, celkem_her # Globální proměnné pro skóre a seznamy karet

    # Hraje se další partie a přičítá se kvůli tomu 1
    celkem_her += 1

    if len(balicek) < 10: # Pokud je v balíčku méně než 10 karet

        # Varování před nízkým počtem karet v balíčku
        upozorneni = tk.Label(okno, text="V balíčku zbývá méně jak 10 karet, chce jej znova zmíchat?", font=("Arial", 14)) # Vytvoří label s upozorněním
        upozorneni.pack(padx=10, pady=10) # Zobrazí upozornění

        michani_btn = tk.Button(okno, text="Zamíchat", command=lambda: okno.after(750, hra(obtiznost))) # Nadpis
        michani_btn.pack(padx=10, pady=20) # Zobrazení tlačítka pro míchání 

        stat_btn = tk.Button(okno, text="Statistika", command=lambda: stat())
        stat_btn.pack(padx=10, pady=20, side="bottom") # Zobrazení tlačítka pro statistiku 

    else:
        # Rozdání karet dealerovi
        dealer_karty_list, dealer_skore = rozdani_karet(2, balicek) # Rozdání první karety
        dealer_text = tk.Label(okno, text="?", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre dealera
        zobrazit_karty(dealer_karty_list, True) # Zobrazí karty dealera
        dealer_text.place(x=500, y=35)

        # Rozdání karet hráči
        hrac_karty_list, hrac_skore = rozdani_karet(2, balicek) # Rozdání první karety
        hrac_text = tk.Label(okno, text=f"{int(hrac_skore)}", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre hráče
        zobrazit_karty(hrac_karty_list, 1) # Zobrazí karty hráče

        text_hrac = tk.Label(okno, text="Vaše karty", bg="black", fg="white", font=("Arial", 14)) # Zobrazí text "Hráč"

        x_hrac_text = 500 if obtiznost == 1 else 750 # Určuje pozici textu podle obtížnosti
        hrac_text.place(x=x_hrac_text, y=345) # Zobrazí skóre hráče
        text_hrac.place(x=x_hrac_text, y=560) # Zobrazí text "Hráč"

        if obtiznost != 1: # Pokud není lehká obtížnost
            # Rozdání karet botovi
            bot_karty_list, bot_skore = rozdani_karet(2, balicek) # Rozdání první karety
            bot_text = tk.Label(okno, text=f"{int(bot_skore)}", bg="black", fg="white", font=("Arial", 14)) # Zobrazí skóre bota
            zobrazit_karty(bot_karty_list, 1) # Zobrazí karty bota
            bot_text.place(x=230, y=345)

            tom_text = tk.Label(okno, text="Tomáš - Host", bg="black", fg="white", font=("Arial", 14)) # Zobrazí text "Bot"
            tom_text.place(x=230, y=560) # Zobrazí text "Bot"
    
        # Balanc a sázka
        balanc_text = tk.Label(okno, text=f"Kredit: {int(balanc)}", bg="navy", fg="white", font=("Arial", 20)) 
        balanc_text.place(x=10, y=10)
        sazka_text = tk.Label(okno, text=f"Vsazeno: {int(mezi_vklad)}", bg="silver", fg="black", font=("Arial", 17))
        sazka_text.place(x=10, y=50)

        zbytek = len(balicek) # Zjistí, kolik karet zbývá v balíčku
        ve_hre = tk.Label(okno, text=f"Karet v balíčku {zbytek}", bg="blue", fg="white") # Vytvoří label s informací o počtu karet v balíčku
        ve_hre.place(x=1047, y=220) # Zobrazí informaci o počtu karet v balíčku

        # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore = tk.Label(okno, text=f"""Dealer: {vyhra_dealer}
Hráč: {vyhra_hrac}""", font=("Arial", 14)) # Vytvoří label s celkovým skóre, kdo vyhrával kolik her
        skore.place(x=950, y=40) # Zobrazí celkové skóre

        btn = tk.Frame(okno, bg="darkslategray4") # Vytvoří frame pro tlačítka

        hit_btn = tk.Button(btn, text="Hit", command=lambda: (double_btn.destroy(), hit(balicek)))  # Tlačítko pro další kartu
        hit_btn.pack(side="left", anchor="s", padx=10, pady=10) # Zobrazí tlačítko
        stand_btn = tk.Button(btn, text="Stand", command=lambda: (double_btn.destroy(), stand(balicek)))  # Tlačítko pro stání
        stand_btn.pack(side="left", anchor="s", padx=10, pady=10) # Zobrazí tlačítko

        btn.pack(side="right", anchor="s", pady=50, padx=70) # Zobrazení frame s tlačítky

        double_btn = tk.Button(okno, text="2x", command=lambda: double(balicek))  # Tlačítko pro double
        if mezi_vklad <= balanc: # Pokud je možné zdvojnásobit sázku
            double_btn.place(x=1020, y=580) # Zobrazí tlačítko

######################### Vykreslování okna #########################

zobraz_menu()
okno.mainloop()