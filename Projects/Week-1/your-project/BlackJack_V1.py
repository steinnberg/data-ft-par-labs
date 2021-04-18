# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:22:45 2021

@author: Keredine
"""
import random

valeur = { 'valeur' :  [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 'R', 'D', 'V', 'A']}   
couleur = { 'couleur' : ['carreau', 'coeur', 'trefle', 'pique'] }



def ma_carte(valeur, couleur):
    a = random.randrange(12)
    b = random.randrange(3)
    carte = (valeur['valeur'][a], couleur['couleur'][b])
    return carte



def main():
    main =[]
    return main



def mon_jeu(valeur, couleur):
    paquet = []
    for elt1 in valeur['valeur']:
        for elt2 in couleur['couleur']:
            paquet.append((elt1, elt2))
    return paquet
            
paquet = mon_jeu(valeur, couleur)
print(paquet)



#fonction qui mélenge le paquet
def melange (lst):
    new_paquet = []
    new_paquet = random.sample(lst, k = len(lst))
    return new_paquet
    #return random.shuffle(lst)

new_paquet = melange(paquet)
print(new_paquet)



#fonction tirer un carte au hasard du paquet
def tirer_une_carte(set_):
    #tirer une carte du haut du paquet
    #nbr = random.randrange(len(set_))
    t = len(set_)
    if t >0 :
        new_carte = set_[0]
        set_.remove(new_carte)
        return new_carte
     



# Fonction qui ajoute une carte
def ajoute(list_):
    return list_.append(carte[0])


#Fonction qui compare les cartes d une main
def calculer_valeur_une_main(cartes):
    val = 0
    for carte in cartes:
        if (carte[0] == 'R'):
            val += 10
        elif ( carte[0] == 'D'):
            val += 10
        elif (carte[0] == 'V'):
            val += 10
        elif (carte[0] == 'A'):
            val += 11
        elif 1 < carte[0] <= 10:
            val += carte[0]
    nb_as = cartes.count(1) # Attention s'il y a plusieurs as dans la main
    while nb_as>1:
        val += 1    # un seul as peut valoir 11 pts. Les autres valent 1.
        nb_as -= 1
    if nb_as == 1 and val + 11 <= 21:
        return val + 11
    elif 1 in cartes:
        return val + 1
    else:
        return val
    return val



def ajoute(lst, c):
    "Ajoute la carte c"
    # 1:as, 2...10, 11:valet, 12:dame, 13:roi
    lst =[]
    return lst.append(c)


#Fonction main du joueur
def main_joueur(carte):
    mainJ = [] #main()
    mainJ.append(carte)
    return mainJ



#Fonction main de la banq
def main_banq(carte):
    main_b = []
    main_b.append(carte)
    return main_b



#Fonction affiche resultat des deux mains
def affiche (main_du_joueur,main_de_la_banq):
    #affiche nombre de carte de chaque main, la valeur des deux mains
    val_j = calculer_valeur_une_main(main_du_joueur)
    val_b = calculer_valeur_une_main(main_de_la_banq)
    return(val_j, val_b)
    
#res = affiche(main_du_joueur, main_de_la_banq)
#print(res)
#def reinitialiser()


#fonction du deroulement du jeu

def deroulement():
    nbr_carte = 0
    while nbr_carte <=5:
        nbr_carte = 0
        #step0 : creer le paquet de jeu
        jeu = mon_jeu(valeur, couleur)
        #print(jeu)
        # Step1: melange du paquet
        paquet = melange(jeu)
        #print(paquet)
        #creation de la main du joueur
        main_du_joueur = []
        #tirer 2 cartes au joueur et a la banque du haut du paquet
        #carte_j_1 = tirer_une_carte(paquet)
        main_du_joueur.append(tirer_une_carte(paquet))
        print (main_du_joueur)
        #carte_j_2 = tirer_une_carte(paquet)
        main_du_joueur.append(tirer_une_carte(paquet))
        print(main_du_joueur)
        nbr_carte = len(main_du_joueur)
        print(nbr_carte)
        #creation de la main de la banq
        main_du_croupier = []
        #tirer 2 cartes au joueur et a la banque du haut du paquet
        #carte_b_1 = tirer_une_carte(paquet)
        main_du_croupier.append(tirer_une_carte(paquet))
        print (main_du_croupier)
        #carte_b_2 = tirer_une_carte(paquet)
        main_du_croupier.append(tirer_une_carte(paquet))
        print(main_du_croupier)
        # Calcul des valeur de chaque main
        val_main_joueur = calculer_valeur_une_main(main_du_joueur)
        val_main_croupier = calculer_valeur_une_main(main_du_croupier)
        #Afficher la valeur des deux mains
        (joueur, banq) = affiche(main_du_joueur, main_du_croupier)
        print((joueur, banq))
        if joueur == 21 :
            print('BlackJack j ai gagné')
            break
            
        elif joueur > 21:
            print('Le joueur a perdu')
            break
            
        elif banq == 21:
            print ('la Banque a gagné')
            break
            
        elif joueur < 21:
            #demande de continuer de jouer
            answer = input("Voulez vous continuer de joueur Enter yes or no: ") 
            if answer == "yes": 
                nbr_carte += 1
                #Continuer de jouer
                #carte_j_3 = tirer_une_carte(paquet)
                main_du_joueur.append(tirer_une_carte(paquet))
                #carte_b_3 = tirer_une_carte(paquet)
                main_du_croupier.append(tirer_une_carte(paquet))
                nbr_carte = len(main_du_joueur)
                print(nbr_carte)
                # Calcul des valeurs de chaque main
                (joueur, banq) = affiche(main_du_joueur, main_du_croupier)
                print((joueur, banq))
                print(nbr_carte)
                if joueur == 21 :
                    print('BlackJack j ai gagné')
                    break
                elif banq == 21:
                    print ('la Banque a gagné')
                    break
    
            elif answer == "no": 
                print("le score final est :", (joueur, banq)) 
                break
               
   
    
res = deroulement()           

























