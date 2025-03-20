import tkinter as tk

# Funkce pro přidání hodnoty do balancu
def pridat_hodnotu():
    global balanc
    balanc += 10  # Přidáme 10 k balancu
    label.config(text=f"Balanc: {balanc}")  # Aktualizujeme text labelu

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Přidání hodnoty do balancu")

# Inicializace balancu
balanc = 0

# Vytvoření labelu pro zobrazení balancu
label = tk.Label(root, text=f"Balanc: {balanc}", font=("Arial", 14))
label.pack(pady=20)

# Vytvoření tlačítka pro přidání hodnoty
button = tk.Button(root, text="Přidat 10", command=pridat_hodnotu)
button.pack(pady=10)

# Spuštění hlavní smyčky
root.mainloop()
