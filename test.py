balanc = 10000  # Počáteční zůstatek

# Funkce pro snížení zůstatku
def sniz_balanc(odecteno):
    global balanc
    # Zkontrolujeme, zda po odečtení nebude balanc menší než 0
    if balanc - odecteno >= 0:
        balanc -= odecteno
        print(f"Nový zůstatek: {balanc}")
    else:
        print("Operace není možná, protože by zůstatek šel do mínusu.")

# Příklad volání funkce
sniz_balanc(5000)  # Odečítá 5000, nově bude balanc 5000
sniz_balanc(6000)  # Pokusí se odečíst 6000, což způsobí, že balanc by byl záporný
