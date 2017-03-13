# coding:utf-8

# Importer les modules dont on a besoin après avoir créer environnement de travail virtuel, installer requests et BeautifulSoup4. 
import csv
import requests
from bs4 import BeautifulSoup
import time 

# Créer une variable avec l'URL du site à moissonner. 
url= "http://www.bac-lac.gc.ca/fra/transparence/divulgation-proactive/Pages/divulgation-octrois-subventions-contributions-details.aspx?filterquarter=1&filteryear=2016-2017"

# Personnaliser les entêtes pour s'afficher en tant que journaliste au site web.
entetes = {
    "User-Agent":"Je m'appelle Noémie Laurendeau et je fais du moissonnage pour un cours.",
    "From":"noemie.laurendeau@hotmail.com"
}

# Utiliser requests pour mettre le contenu de la page web dans une variable contenu. 
contenu = requests.get(url,headers=entetes)

# Création de la variable page pour analyser le contenu de la page web.
page = BeautifulSoup(contenu.text,"html.parser")

# Afficher tous les liens de la page web.
# print(page.find_all("a"))

# Insérer un tiers de seconde pour permettre au serveur de respirer entre mes requêtes. 
time.sleep(0.33)

# Créer des listes pour les infos du contrat. 
nom = []
valeur =[]
contrat = [] 

# Afficher les liens de la page web qui mènent aux liens des contrats.
for ligne in page.find_all("tr"):
    try : 
        # print(ligne.a["href"])
# Aller chercher les informations dans les liens, soient les informations des contrats (2e niveau).
        contenu2 = requests.get(ligne.a["href"], headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")
        for rang in page2.find_all("tr"):
#Enlever les espaces blancs entre les éléments.  
            print(str(rang.td.text).strip())
    except :
        print("Y'a rien ici")
        
# Tentative d'enlever le nom des catégories et seulement garder les éléments de réponses dans les informations:

        # for chose in machin:
        # if chose != (class=)"strong"

# Tentative d'aller chercher seulement le nom du bénéficiaire et le valeur du contrat:
        # contenu3 = requests.get(ligne.a["href"], headers=entetes)    
        # page3 = BeautifulSoup(contenu3.text,"html.parser")
        
        # y = 0
                
        # for element in page3.find_all("tr"):
                # if y==1:
                        # if element.div is not None:
                            # beneficiaire = element.div.text
                        # else:
                            # beneficiaire = ""
                            
                # elif y==4:
                        # if element.div is not None:
                            # valeur = element.div.text
                        # else:
                            # valeur = ""
                            # y = y+1
                            
            
# Tentative de création du fichier CSV. 
# contrat.writerow([nom,valeur]) 
