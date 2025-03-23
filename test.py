def count_cards(cards_dealt):
    """
    Funkce pro počítání karet podle Hi-Lo systému.
    
    :param cards_dealt: seznam karet, které byly rozdány
    :return: celkový počet karet (hi-lo count)
    """
    count = 0
    for card in cards_dealt:
        if card in [2, 3, 4, 5, 6]:
            count += 1
        elif card in [10, 11, 12, 13, 14]:  # 10, Jack, Queen, King, Ace
            count -= 1
    return count

# Příklad použití:
cards_dealt = [2, 10, 5, 14, 8]
count = count_cards(cards_dealt)
print(f"Počet karet: {count}")