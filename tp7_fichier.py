"""
vous etes admin d'une PME qui exerce dans la microfinance.
Vous êtes solicité afin de proposer un script python qui permet de gérer les projets de la PME.
Le script comporte les fonctions suivantes :
- Fonction de saisie des informations d'un projet
- Fonction de création d'un dossier dans le disque local C
- Fonction d'affichage des informations d'un projet saisi
- Fonction de création d'un fichier contenant l'ensemnle des projets de la PME
Ce fichier est contenu dans le dossier initialement créé dans le disque local C
- Fonction qui affiche l'ensemble des projets du fichier
- Fonction qui détermine le coût total de tous les projets du fichier
- Fonction qui determine et affiche le projet ddont le coût est est le plus élevé et le projet dont le coût est le plus faible
- Fonction qui ajoute de nouveaux projets dans le fichier
- Fonction pour le module
Projet(Code, nom, secteur_d'activité, porteur_de_projet, cout_du_projet, localisation_du_projet, durée_du_projet)

"""

#Fonction de saisie des informations d'un projet
sep=";"
def saisi_information_projet():
    print("***********************************************************")
    print("Saisi des informations d'un projet : ")
    print("***********************************************************")
    code=input("Entrer le code du projet : ")
    nom=input("Entrer le nom du projet : ")
    
    porteur=input("Entrer le porteur du projet : ")
    
    while True:
        cout=input("Entrer le coût du projet : ")
        if cout.strip().isdigit():
            break
        else:
            print("Erreur : le coût est un numérique")

    secteur=input("Entrer le secteur d'activité du projet : ")
    localisation=input("Entrer la localisation du projet : ")
    duree=input("Entrer la durée du projet : ")
    projet=code+sep+porteur+sep+cout+sep+secteur+sep+localisation+sep+duree+"\n"
    return projet
#projet=saisi_information_projet()
#print(projet)

#Fonction de création d'un dossier dans le disque local C
import os
def creation_dossier():
    nom_dossier=input("Entrer le nom du fichier à créer : ")
    os.chdir("C:/")
    if os.path.exists(nom_dossier):
        print("Un dossier de même nom existe déja")
    else:
        os.mkdir(nom_dossier)
        print("Le dossier", nom_dossier, "est créé dans C ")
#creation_dossier()
        
#Fonction d'affichage des informations d'un projet saisi
def affiche_information_projet(projet):
    if len(projet)==0:
        print("Aucun projet n'est passé en paramètre")
    else:
        print("Les informations du projet sont  : ")
        proj=projet.split(sep)
        for p in proj:
            print(p,end="\t")
        print()
#affiche_information_projet(projet)

#Fonction de création d'un fichier contenant l'ensemnle des projets de la PME
def creation_fichier_projet():
     nom_dossier=input("Entrer le nom du dossier qui va contenir le fichier à créer : ")
     cheminn="C:/Users/ASUS/Desktop/PYTHON"
     os.chdir(cheminn)
     if not os.path.exists(nom_dossier):
        print("Le dossier n'existe pas")
     else:
        nom_fichier="liste_projets.txt"
        os.chdir(nom_dossier)
        if not os.path.exists(nom_fichier):
            f=open(nom_fichier,"w")
            while True:
                reponse=input("Voulez vous ajouter un nouveau projet ? O/N ")
                if reponse.upper()=="O":
                    projet=saisi_information_projet()
                    f.write(projet)
                    print("Projet enregistré avec succès dans le fichier")
                elif reponse.upper()=="N":
                    f.close()
                    print("Fin de la création du fichier")
                    break
                else:
                    print("Erreur de choix")
        else:
            print("Le fichier existe déja")
creation_fichier_projet()
#Fonction qui affiche l'ensemble des projets du fichier
def affiche_fichier_projet():
    nom_dossier=input("Entrer le nom du dossier qui contient les projets : ")
    chemin="C:/Users/ASUS/Desktop/PYTHON"
    os.chdir(chemin)
    if not os.path.exists(nom_dossier):
        print("Le dossier n'existe pas")
    else:
        nom_fichier="liste_projets.txt"
        os.chdir(nom_dossier)
        if os.path.exists(nom_fichier):
            f=open(nom_fichier,"r")
            projets=f.readlines()
            f.close
            if len(projets)==0:
                print("Le fichier de projet est vide ")
            else:
                print("La liste des projets du fichier est : ")
                i=1
                for projet in projets:
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    print("PROJET NUMERO",1)
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

                    affiche_information_projet(projet)
                    i+=1

        else:
            print("Le fichier n'existe pas")
affiche_fichier_projet()      

