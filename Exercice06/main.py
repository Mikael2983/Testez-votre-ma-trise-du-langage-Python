# Fonction calculate_average
def calculate_average(list_numbers: list[float]) -> float:
    """
    calculates the average of numbers in a list.
    :param list_numbers: a list of numbers
    :type list_numbers: list[float]
    :return: the average of the numbers in the list
    :rtype: float
    """
    somme = 0
    for number in list_numbers:
        somme += number

    return somme/len(list_numbers)


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
