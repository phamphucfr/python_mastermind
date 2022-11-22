""" 
    Nom : Jeu du mastermind 
    Auteurs : Sonia FIROUZI, Yann NORET, Phuc PHAM NGOC
    Date : 10/09/2022
    Description : Code permettant de jouer au fameux jeu de stratégie mastermind. Plusieurs niveaux de diffculté sont possibles.
    Le script nécessite d'importer les modules random et unittest
    Le fichier peut aussi être importé comme module et contient les fonctions suivantes :
        *pions_noirblanc
        *result_inline
        *main_test
    
    Le but est de s'amuser, d'améliorer son niveau intellectuel et de devenir un fin stratège.
    Serez-vous un vrai mastermind ? 
"""
# Import de modules
# import mariadb
import random
from colors import Colors

# Cette partie concernant Mariadb est optionnelle
# Connexion à la plateforme MariaDB 
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="soso-root",
#         host="172.17.0.4",
#         port=3306,
#         database="mastermind"

#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# Obtenir le curseur
# cur = conn.cursor()

#Récupérer les data
# cur.execute(
#     "SELECT * FROM score")
# # Print Result-set
# for (user_ip, code, status, score) in cur:
#     print(f"ip_joueur: {user_ip}, code: {code}, status: {status}, score_joueur: {score}")

#Instanciation d'un objet Colors pour colorier les texts dans CLI
clr = Colors()

print("-----------------------------------------")
print("\t      MASTERMIND")
print("-----------------------------------------")
print ("\t")
print ("---Règles du jeu---")
print ("\t")
print ("Le joueur doit trouver la combinaison secrète en un minimum de coups.")
print ("Il perd s'il n'a pas trouvé la combinaison.")
print ("Si dans la proposition, un ou plusieurs pions de couleurs sont bien dans la combinaison \nmais pas à la bonne place, un pion blanc est sorti.")
print ("Si dans la proposition, un ou plusieurs pions de couleurs sont bien dans la combinaison \net à la bonne place, un pion noir est sorti.")
print ("\t")
print ("---Comment jouer ?---")
print ("\t")
print ("Vous pouvez choisir parmi 3 niveaux de difficulté.")
print ("Au niveau easy, il faudra deviner 4 couleurs en 10 tentatives.")
print ("Au niveau medium, il faudra deviner 6 couleurs en 8 tentatives.")
print ("Au niveau hard, il faudra deviner 8 couleurs en 4 tentatives.")
print ("Les couleurs disponibles sont les suivantes :\n-Green\n-Yellow\n-Red\n-Blue\n-Pink\n-Orange")
print("\t")
print ("---Menu---")
print("\t")
print("Entrez le code en utilisant des initiales.")
print("R - RED, G - GREEN, Y - YELLOW, B - BLUE, P - PINK, O - ORANGE")
print("Exemple : RED YELLOW ORANGE PINK ---> RYOP")
print ("\t")

# Liste de couleurs
colors = ["R", "G", "B", "Y", "P", "O"]

# Inputs user choix de la difficulté (par rapport au nombre de pions, de couleurs différentes et nombre de tentatives): 

while True:
    input_difficulty = int(input("Choix du nombre de pions à deviner (4, 6, 8) : "))

    if input_difficulty == 4:
      print(f"Vous jouez en mode easy avec {input_difficulty} pions !")
      print ("\t")
      break     
    elif input_difficulty == 6:
      print(f"Vous jouez en mode medium avec {input_difficulty} pions !")
      print ("\t")
      break      
    elif input_difficulty == 8:
      print(f"Vous jouez en mode nightmare avec {input_difficulty} pions !")
      print ("\t")
      break 
    else:
      print("Veuillez choisir parmi 4, 6 ou 8")      
      print ("\t")                                 

while True:
    input_colors = int(input("Choix du nombre de couleurs différentes (2, 3, 4, 5, 6) ? "))

    if (2 <= input_colors <= 6):
        break        
    print (f"{input_colors} n'est pas acceptable, veuillez choisir entre 2 et 6 couleurs")
    print ("\t")    

print (f"Vous jouez avec {input_colors} couleurs")
print ("\t")

input_tentative = int(input("Choix du nombre de tentatives : "))
print (f"Vous avez {input_tentative} tentatives, bonne chance !")
print ("\t")

# Mélange et sélection des couleurs au hasard
random.shuffle(colors)
nbr_colors = colors[:input_colors]

# Génération d'un code aléatoire
code = random.choices(nbr_colors, k = input_difficulty)

def pions_noirblanc(code:list, guess:list) -> list:
    """ Affiche le décompte du nombre de pions blancs et/ou noirs 

        Parameters :
        -----------
        code : list
            Il s'agit du code secret à deviner.
        guess : list
            Le code que l'utilisateur a rentré afin de deviner le code secret.
        
        Return :
        -------
        List
            Compte le nombre de pions noirs et/ou blancs sous forme de liste. 
    """
    i = 0
    pnoir = 0
    pblanc = 0
    for g in guess:
        if(g == code[i]):
            pnoir += 1
        else:
            if(g in code):
                pblanc += 1
        i += 1 
    return [pnoir, pblanc]


# Fonction affichant des pions noirs et blancs selon la réponse de l'user

def result_inline(code:list, guess:list) -> str:
    """ Affiche la ligne de résultat par rapport à l'input user. Permet ainsi de retourner le nombre de pions blans
    et/ou noirs sous forme de phrase. Ainsi que un message de Victoire ou de changement d'input user s'il n'y a ni
    pions noirs ni pions blancs.

        Parameters :
        ------------
        code : list
            Il s'agit du code secret à deviner.
        guess : list
            Le code que l'utilisateur a rentré afin de deviner le code secret.
        
        Return :
        ---------
        String
            Suivant la réponse de l'utilisateur, affiche un message indiquant victoire si le code retourné est bon, ou rien n'est bon 
            si aucun des pions n'est de la bonne couleur ou bien placé (aucun pion noir et/ou blanc).
    
    """
    response = pions_noirblanc(code,guess)
    pnoir = 'pion ' + clr.bold + clr.bg('GY','') + clr.fg('BK','Noir') + clr.reset
    pblanc = 'pion ' + clr.bold + clr.bg('GY','') + clr.fg('W','Blanc') + clr.reset
    string_result = ""
    if (response[0] > 0) and (response[1] > 0):
        string_result =  f"{response[0]} {pnoir} et {response[1]} {pblanc}"   
    elif (response[0] > 0) and (response[1] == 0):
        if (response[0] == len(guess)):
            string_result = "BRAVO!"
        else:
            string_result = f"{response[0]} {pnoir}"
    elif (response[0] == 0) and (response[1] > 0):
        string_result = f"{response[1]} {pblanc}"    
    else:
        string_result = "Rien n'est bon"
    return string_result

    
# Fonction main() -> Le programme principal
def main() -> None:
    """ Fonction principale regroupant les résultats des autres fonctions et permettant d'indiquer la victoire finale ou le game over.

        Return :
        -----------
        String
            Suivant la réponse de l'utilisateur, affiche le nombre de tentatives avec le message victory, ou le
            message vous avez échoué avec le nombre de tentatives. 

    
    """
    tentative = 1
    score = 0
    guess = []
    while (tentative <= input_tentative):
        while True:
            cond1 = False
            cond2 = False
            userinput = input("Votre proposition : ")
            guess = list(userinput.upper())
            if len(guess) == len(code):
                cond1 = True
            else:
                print(f"Merci de saisir {input_difficulty} couleurs dans le code !")
            i = 0
            for g in guess:
                if (g not in colors):
                    i += 1
            if i == 0 :
                cond2 = True
            else:
                print(f"Merci de choisir uniquement les couleurs disponibles du jeu {colors} !")
            if cond1 and cond2:
                break
            
        couleur_guess = clr.colorize_list(guess)
        tentatives_left = input_tentative - tentative
        results = result_inline(code,guess)
        
        print('Couleurs entrées'.ljust(20), " ", 'Tentatives restantes', " ".ljust(6), 'Résultats')
        print(f"{couleur_guess}".ljust(60), " ".ljust(15), f"{tentatives_left}", " ".ljust(20), f"{results}", )
        score = input_colors + input_difficulty + tentatives_left
        
        if (results == "BRAVO!"):
            print(f"Vous avez réussi avec {tentative} tentatives")
            break     
        tentative += 1  
        
    if(results != "BRAVO!"):
        print("Vous avez échoué")
      
    print(f"Votre score : {clr.bold + clr.fg('R',score) + clr.reset}")
                     
main()


 
