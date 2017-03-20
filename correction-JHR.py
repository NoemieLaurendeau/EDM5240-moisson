### MES COMMENTAIRES ET CORRECTIONS SONT MARQUÉS PAR TROIS DIÈSES

### Tu étais près du but
### Il ne fallait pas changer grand chose pour que ça fonctionne
### Voici comment s'y prendre dans ce cas-ci

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
# time.sleep(0.33) ### Intéressant, mais c'est plus bas qu'il faut mettre cette pause, car c'est dans les lignes 40 et quelque que tu fais plusieurs requêtes

### Jusqu'ici, tout va bien.

### Créer ces listes ne sert malheureusement pas; une seule suffit
### Et il faut la créer seulement à l'intérieur de la boucle ci-dessous
# Créer des listes pour les infos du contrat. 
nom = []
valeur =[]
contrat = [] 

# Afficher les liens de la page web qui mènent aux liens des contrats.

### Ce «find_all» n'est pas suffisamment détaillé
# for ligne in page.find_all("tr"):

### Ici, on va vraiment chercher les <tr> se trouvant dans la <table> où se trouvent les URL qu'on cherche
for ligne in page.find("table", class_="table table-striped table-bordered").find_all("tr"):
    try : ### Très bien!
        print(ligne.a["href"])
        url2 = ligne.a["href"]

# Aller chercher les informations dans les liens, soient les informations des contrats (2e niveau).
        contenu2 = requests.get(url2, headers=entetes)
        page2 = BeautifulSoup(contenu2.text,"html.parser")

        time.sleep(.5) ### Voici le bon endroit où mettre le «sleep»

        # for rang in page2.find_all("tr"):

### Ici, si tu regardes le code HTML des pages des contrats, tu verras que les infos ne sont pas placées dans un <table>
### Il n'y a donc ni <tr>, ni <td>
### Pour une raison que j'ignore, ils ont choisi de mettre ça dans des <div>
### Il faut donc adapter ton code en conséquence; tu l'as fait dans une tentative ci-dessous; il fallait juste ne pas ajouter «find_all("tr")» à la fin

### C'est ici qu'on peut créer une variable «contrat» afin d'y consigner toutes les informations relatives à chaque contrat
### On y place d'abord l'URL qu'on est en train de moissonner, à des fins de vérification ultérieure
        contrat = []
        contrat.append(url2)

        for rang in page2.find("div",style="width:auto; padding:5px; display:table;").find_all("div", style="float: left; width: 100%; display: block;"):
            # print(rang)

### Les infos qui nous intéressent sont dans un autre <div>, se trouvant dans la variable «rang», <div> identifiable à son attribut «style»
### On les ajoute à la variable «contrat»
            contrat.append(rang.find("div", style="float: left; width: 60%; padding: 2px 2px 12px 0px;").text.strip())

### Et après chaque moissonnage d'un contrat, on l'ajoute à un fichier CSV

        print(contrat)
        allo = open("contrats-BAC-LAC-JHR.csv","a")
        bobo = csv.writer(allo)
        bobo.writerow(contrat)

#Enlever les espaces blancs entre les éléments.  
            # print(str(rang.td.text).strip())
    except :
        print("Y'a rien ici")
        
# Tentative d'enlever le nom des catégories et seulement garder les éléments de réponses dans les informations:

        # for chose in machin:
        # if chose != (class=)"strong"
        
# Autre tentative d'aller chercher les éléments de réponses dans les informations du contrat: 
# for item in page.find("div", "style="float: left; width: 60%; padding: 2px 2px 12px 0px").find_all("tr"):
#     print(item)

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
