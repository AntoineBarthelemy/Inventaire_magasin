inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraise", 76),("prunes", 51)]
inventaire2 = list()


def affichage():
 # Essaie avec une list comprehension
#  [all for all in inventaire2]
 for all in sorted(inventaire2, reverse=True):
  print(all)



def inversement():
 
 for fruits, nombres in inventaire:
    inventaire2.append((nombres, fruits))
 return inventaire2, affichage()

inversement()






    

# [fruits, nombres for fruits, nombres in inventaire]
# # print(sorted(inventaire2))