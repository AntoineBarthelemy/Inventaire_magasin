# def somme_liste (liste: list) -> int | float:
#     """Cette fonction parcout les élements de la liste fourni en argumants avec la variable nb.
#       Cette variable prend succèsivement les différentes valeurs présente dans cette liste puis 
#       une deuxième variable est chargé d'additioner la variable nb"""
#     somme = 0
#     for nb in liste:
#         somme += nb 
#     return somme


# l = somme_liste([1,2,3,4])

# print(l)

def filter_numbers (numbers: list[int]) -> list[int]:
    if not isinstance(numbers, list):
        raise ValueError
    for nb in numbers:
        if nb % 2 == 0:
            new_list = list()
            new_list = [nb]
            return new_list
        else:
            None
    
a = filter_numbers([20,30,40])
print(a)