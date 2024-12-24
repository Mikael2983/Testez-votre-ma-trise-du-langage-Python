words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def count_vowels(text: str):
    vowels = set("aAeEiIoOuUyYàéèêëöôîï")
    return sum(1 for char in text if char in vowels)


list_understandings = []

for word in words:
    vowels_number = count_vowels(word)
    list_understandings.append((word,vowels_number))

print(list_understandings)
