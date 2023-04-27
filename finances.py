#dodajemy informacje o typie zmiennych, strzalka -> float oznacza ze wartosc zwrocona to tez bedzie float
def calculate_brutto(netto:float, vat: float) -> float:
    """
    Function that calculates brutto for netto and vat
    :param netto: value of netto
    :param vat: value of vat like 0.23
    :return: value of brutto
    """
    return netto *(1 + vat)
