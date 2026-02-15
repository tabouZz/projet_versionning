port=input("Saisir un numéro de port : ")
while True:
    try:
        if int(port)<1 or int(port)>65535:
            print("Le numéro de port doit être compris entre 1 et 65535")
            port=input("Saisir un numéro de port valide : ")
        else:
            print("Numéro de port : ", port)
            if int(port)<1024:
                print("ceci est un port bien connu")
                break
            if 1024 <= int(port) <= 49151:
                print("ceci est un port enregistré")
                break
            if int(port)>49151:
                print("ceci est un port dynamique")
                break
    except ValueError:
        print("Le numéro de port doit être un nombre")
        port=input("saisir un numéro de port valide")

        
