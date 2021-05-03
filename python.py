#!/usr/bin/env python
# coding: utf-8

# # Juste prix
# 
# 

# In[69]:


import random as rd

prix = rd.randrange(1001)

print("Le prix est: " , prix)


cpt = 0


while cpt < 3:
    valeur = input(" Entrez le prix ")
    cpt += 1
    if valeur.isdigit():
        valeur = int(valeur)
        if valeur < prix:
            print("Trop bas")
            cpt += 1
        else:
            print("Trop élévé")
            cpt += 1
        
print(cpt)
    


# # Pierre papier ciseaux

# ## Une fonction qui génère de l’aléatoire : pierre, papier ou ciseaux 

# In[64]:


def ppc():
    choix = rd.choice(['pierre', 'papier', 'ciseaux'])
    return choix
    
print(choix)


# ## Une fonction pour vérifier et valider le coup qui vient d’être joué 

# In[109]:


def verif_and_valid():
    coup = input("Entrez votre choix ")
    if coup.isdigit():
        if(coup == 'pierre' or coup == 'papier' or coup == 'ciseaux'):
            return True
    while True:
        try:
            x = input("Entrez votre choix ")
            break
        except ValueError:
            print("Essayez pierre, papier ou ciseaux")
    

    


# ## Une fonction de résultat pour déclarer le vainqueur du tour 

# In[ ]:


def winner(a,b):
    if a == 'pierre' and b == 'papier':
        print(b,'gagne')
    elif a == 'ciseaux' and b == 'pierre':
        print(b,'gagne')
    elif a == 'papier' and b == 'ciseaux' :
        print(b,'gagne')
    else print(b,'gagne')


        


# # Pendu
# 

# In[110]:


mot = input("Entrez un mot: ").upper()
l = [i for i in mot]
print(l)
cpt = 0
res = ['_'] * (len(l)-1)
print(res)
while cpt < 6:
    i = input("Entrez une lettre ").upper()
    if i in l:
        res.insert(l.index(i),i)
        print(res)
        print(cpt)
    else:
        cpt += 1
        input("Essayez une autre ")
        print(cpt)
    
    


# In[ ]:




