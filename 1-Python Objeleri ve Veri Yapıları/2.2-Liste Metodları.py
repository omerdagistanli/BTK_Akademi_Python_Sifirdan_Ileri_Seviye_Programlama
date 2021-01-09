numbers = [1, 10, 5, 4, 16, 7]
letters = ["a", "b","c", "m", "y", "o"]

value_Min = min(numbers)
value_Max = max(numbers)

char_Min = min(letters)
char_Max = max(letters)

# 4. indeksin yerine ekler
numbers.insert(4, 14)

# 1. indekteki veriyi siler
numbers.pop(1)

# liste küçükten büyüğe sıralanır
numbers.sort()

# listeyi ters çevirir
numbers.reverse()

print(numbers)
