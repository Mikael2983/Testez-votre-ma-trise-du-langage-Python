# Écrivez votre code ici !
def calcul_square(value: float):
    """
    Calculate the square of a number
    :param value: number to square
    :type value : float
    :return: square of the number
    :raise: typeError
    :rtype: float or Bool
    """
    try:
        square = value*value
        return square
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None


result = calcul_square(5)
print(result)

result = calcul_square("as")
print(result)
