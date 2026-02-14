"""
vous etes administrateur sysytème d'une banque. Vous êtes chargé d'écrire un scrypt pour automatiser les tâches suivantes
- Fonction qui permet de créer un dossier dont le nom est saisie
- Fonction qui affiche le contenu du disque local C
- Fonction qui supprime un dossier
- fonction qui permet de chercher un fichier ou dossier dans le répertoire (répertoire courant)
- Fonction qui affiche le répertoire courant
- Fonction qui affiche le contenu d'un répertoire passé en paramètre
- Fonction qui saisie les informations d'un équipement informatique
- Fonction qui sauvegarde dans une liste un lot d'équipements saisie
- Fonction qui affiche les données d'un équipements
- Fonction qui permet de chercher un équipement par rapport à sa marque
- Fonction pour le menu principal
Equipements(code, nom, marque, fournisseur, date d'acquisition, coût d'acquisition

"""
#Fonction qui permet de créer un dossier dont le nom est saisie
def creation_dossier():
    nom_dossier=input("Entrer le nom du dossier à créer : ")
    import os
    if os.path.exists(nom_dossier):
        print("Un dossier de même nom exite déja")
    else:
        os.mkdir(nom_dossier)
        print("Le dossier",nom_dossier, "est créé avec succès ")
#creation_dossier()

#- Fonction qui affiche le contenu du disque local C
def affiche_contenu_disquelocalC():
    os.chdir("C://")
    print("Le contenu du disque local C est : ")
    contenu = os.listdir()
    for c in contenu:
        print(c, end="\t")
    print()
#affiche_contenu_disquelocalC()

#- Fonction qui supprime un dossier
def supprimer_dossier():
    nom_dossier = input("entrer le nom du dossier à supprimer")
    if os.path.exists(nom_dossier):
        os.rmdir(nom_dossier)
        print("Le dossier", nom_dossier, "est supprimé avec succès")
    else:
        print("le dossier n'existe pas")
#-fonction qui permet de rechercher un fichier ou dossier dans un repertoire(courant)
def recherche_dossier_ou_fichier():
    dossier_ou_fichier = input("Entrez le nom du dossier ou du fichier à rechercher : ")
    if os.path.exists(dossier_ou_fichier):
        print(dossier_ou_fichier,"est présent dans le répertoire")
    else:
        print(dossier_ou_fichier,"n'est pas présent dans le répertoire")
#recherche_dossier_ou_fichier()
#-fonction qui affiche le repertoire courant
def affiche_repertoire_courant():
    print("Le répertoire courant est : ", os.getcwd())
#affiche_repertoire_courant()
# fonction qui affiche le contenu d'un répertoire passé en paramètre
def affiche_repertoire_quelconque(repertoire):
    if os.path.exists(repertoire):
        contenu = os.listdir(repertoire)
        print("Le contenu du répertoire est : ")
        for c in contenu:
            print(c, end="\t")
    else:
        print("Le répertoire n'existe pas")

#repertoire = input("Entrez le nom du répertoire : ")
#affiche_repertoire_quelconque(repertoire)

#- Fonction qui saisie les informations d'un équipement informatique
def infos_equipements():
    print("----------------"*10)
    print("\t saisie d'un nouveau equipement")
    print("----------------"*10)
    code = input("Entrer le code")
    nom=input("entrer le nom")
    marque=input("entrer la marque")
    fournisseur=input("entrer le fournisseur")
    date_acqui=input("entrer la date d'acquisition")
    while True:
        cout =input("entrer le cout d'acquisition ")
        if cout.isdigit():
            break
        else:
            print("Erreur, le cout est un numerique")
    equipements = [code, nom, marque, fournisseur, date_acqui, cout]
    return equipements
#equipement=infos_equipements()
#print(equipement)

#- Fonction qui sauvegarde dans une liste un lot d'équipements saisie
equipements=[]
def liste_equipements():
    while True:
        reponse = input("Voulez vous ajouter un nouvel equipement O/N : ")
        if reponse.upper()=="O":
            equipements=infos_equipements()
            equipements.append(equipements)
            print("Equipement ajoutés avec succcès")
        elif reponse.upper()=="N":
            break
        else:
            print("Erreur de saisie de réponse")
liste_equipements()
print("les équipements de la liste sont : ")
print(equipements)
# Fonction qui affiche les données d'un équipement
def afficher_equipement(equipement):
    print("~~~~~~~~~~~~~~~~~~~~~"*3)
    print("\t Informations de l'équipement")
    print("~~~~~~~~~~~~~~~~~~~~~"*3)
    print(f"Code : {equipement[0]}")
    print(f"Nom : {equipement[1]}")
    print(f"Marque : {equipement[2]}")
    print(f"Fournisseur : {equipement[3]}")
    print(f"Date d'acquisition : {equipement[4]}")
    print(f"Coût : {equipement[5]}")


# Fonction qui permet de rechercher un équipement par marque
def rechercher_par_marque(equipements):
    marque_recherche = input("Entrez la marque à rechercher : ")
    trouve = False
    for equipement in equipements:
        if equipement[2].lower() == marque_recherche.lower():
            afficher_equipement(equipement)
            trouve = True
    if not trouve:
        print(f"Aucun équipement trouvé avec la marque '{marque_recherche}'.")


# Fonction pour le menu principal
def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Créer un dossier")
        print("2 - Afficher le contenu du disque C")
        print("3 - Supprimer un dossier")
        print("4 - Rechercher un fichier ou dossier")
        print("5 - Afficher le répertoire courant")
        print("6 - Afficher le contenu d'un répertoire")
        print("7 - Ajouter un équipement")
        print("8 - Afficher tous les équipements")
        print("9 - Rechercher un équipement par marque")
        print("0 - Quitter")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            creation_dossier()
        elif choix == "2":
            affiche_contenu_disquelocalC()
        elif choix == "3":
            supprimer_dossier()
        elif choix == "4":
            recherche_dossier_ou_fichier()
        elif choix == "5":
            affiche_repertoire_courant()
        elif choix == "6":
            rep = input("Entrez le chemin du répertoire : ")
            afficher_repertoire_quelconque(rep)
        elif choix == "7":
            liste_equipements()
        elif choix == "8":
            if len(equipements) == 0:
                print("Aucun équipement enregistré")
            for eq in equipements:
                afficher_equipement(eq)
        elif choix == "9":
            rechercher_par_marque(equipements)
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Lancer le menu
menu()

            
        
    



    
