import tkinter as tk

def smazat_text():
    text_widget.delete(1.0, tk.END)  # Smaže celý text v Text widgetu

# Vytvoření hlavního okna
root = tk.Tk()

# Vytvoření widgetu Text
text_widget = tk.Text(root, height=5, width=40)
text_widget.pack()

# Vložení nějakého textu do Text widgetu
text_widget.insert(tk.END, "Tento text bude smazán za 5 sekund.")

# Zavolání funkce smazat_text po 5000 milisekundách (5 sekund)
root.after(5000, smazat_text)

# Start Tkinter aplikace
root.mainloop()
