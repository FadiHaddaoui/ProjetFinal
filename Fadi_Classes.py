import datetime
from pathlib import Path
import json
import jsonpickle


#La classe Compte
class Personne(object):

        #definition des methodes d'acces
    def set_nom(self, value:str):
        if 6<=len(value)<=20 and value[1].isupper():
            self.__nom= value
        else:
            raise ValueError('Le nom doit etre en 6 et 20 lettre et commencer par une majuscule')
    def get_nom(self)->str:
        return self.__nom

    def set_prenom(self, value:str):
        if 6<=len(value)<=20 and value[1].isupper():
            self.__prenom= value
        else:
            raise ValueError('Le prenom doit etre en 6 et 20 lettre et commencer par une majuscule')
    def get_prenom(self)->str:
        return self.__prenom

        #definition du constructeur
    def __init__(self,nom='', prenom=''):
        #initialisation des attributs
        self.set_nom(nom)
        self.set_prenom(prenom)

        #definir le str
    def __str__(self):
        return f"{self.get_nom()} , {self.get_prenom()}"

#La classe Employe
class Employe(object):

        #definition des methodes d'acces
    def set_code(self, value:int):
        self.__code= value

    def get_code(self)->int:
        return self.__code

    def set_fonction(self, value:str):
        self.__fonction= value

    def get_fonction(self)->str:
        return self.__fonction

    #definition du constructeur
    def __init__(self,code=0, fonction=''):
        #initialisation des attributs
        self.set_code(code)
        self.set_fonction(fonction)

            #definir le str
    def __str__(self):
        return f"{self.get_code()} , {self.get_fonction()}"

#La classe Client
class Client(object):

        #definition des methodes d'acces
    def set_telephone(self, value:str):
        self.__telephone= value

    def get_telephone(self)->str:
        return self.__telephone

    def set_courriel(self, value:str):
        self.__courriel= value

    def get_courriel(self)->str:
        return self.__courriel

    #definition du constructeur
    def __init__(self,telephone='', courriel=''):
        #initialisation des attributs
        self.set_telephone(telephone)
        self.set_courriel(courriel)

        #definition du str
    def __str__(self):
        return f"{self.get_telephone()} , {self.get_courriel()}"

#La classe Reparation
class Reparation(object):

        #definition des methodes d'acces
    def set_code(self, value:int):
        self.__code= value

    def get_code(self)->int:
        return self.__code

    def set_description(self, value:str):
        self.__description= value

    def get_description(self)->str:
        return self.__description

    def set_montant(self, value:float):
        self.__montant= value

    def get_montant(self)->float:
        return self.__montant

    def set_datereparation(self, value:datetime.datetime):
        self.__datereparation= value

    def get_datereparation(self)->datetime:
        return self.__datereparation

    def set_codeemploye(self, value:int):
        self.__codeemploye= value

    def get_codeemploye(self)->int:
        return self.__codeemploye



    #definition du constructeur
    def __init__(self,code=0, description='', montant=0,datereparation = datetime, codeemploye = 0):
        #initialisation des attributs
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

#La classe Voiture
class Voiture(object):

        #definition des methodes d'acces
    def set_numeroplaque(self, value:str):
        self.__numeroplaque= value

    def get_numeroplaque(self)->str:
        return self.__numeroplaque

    def set_marque(self, value:str):
        self.__marque= value

    def get_marque(self)->str:
        return self.__marque

    def set_modele(self, value:str):
        self.__modele= value

    def get_modele(self)->str:
        return self.__modele

    def set_couleur(self, value:str):
        self.__couleur= value

    def get_couleur(self)->str:
        return self.__couleur

    def set_annee(self, value:int):
        self.__annee= value

    def get_annee(self)->int:
        return self.__annee

    def set_proprietaire(self, value:Client):
        self.__proprietaire= value

    def get_proprietaire(self)->Client:
        return self.__proprietaire

    def set_reparations(self, value:list[Reparation]):
        self.__reparations= value

    def get_reparations(self)->list[Reparation]:
        return self.__reparations

    #definition du constructeur
    def __init__(self,numeroplaque='', marque='', modele='',couleur='',annee = 0,proprietaire=Client,reparations=list[Reparation]):
        #initialisation des attributs
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_annee(annee)
        self.set_proprietaire(proprietaire)
        self.set_reparations(reparations)

        #definition de la methode ajouterreparation
    def ajouterreparation(self,element=Reparation)->None:
        self.__reparations.append(element)

#La classe Garage
class Garage(object):

        #definition des methodes d'acces
    def set_nom(self, value:str):
        self.__nom= value

    def get_nom(self)->str:
        return self.__nom

    def set_adresse(self, value:str):
        self.__adresse= value

    def get_adresse(self)->str:
        return self.__adresse

    def set_telephone(self, value:str):
        self.__telephone= value

    def get_telephone(self)->str:
        return self.__telephone

    def set_employes(self, value:list[Employe]):
        self.__employes= value

    def get_employes(self)->list[Employe]:
        return self.__employes

    def set_voitures(self, value:list[Voiture]):
        self.__voitures= value

    def get_voitures(self)->list[Voiture]:
        return self.__voitures


    #definition des methodes serialiser et deserialiser
    @classmethod
    def serialisergarage(cls, element:object, fichier:str)->None:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(fichier)
        #vérifier si le chemin représente un fichier et si elle existe.
        stream=path.open('w')
        if path.is_file() and path.exists():

            #serialiser la valeur vers le fichier
            json.dump(element,stream, indent=4,separators=(',',':'))
            #fermer le stream
            stream.flush()

            stream.close()
        else:
            raise Exception('fichier incorrect ou inexistant')

    @classmethod
    def deserialisergarage(cls, fichier:str)->object:
        #ouvrir le fichier
        path:Path=Path(fichier)

        if path.exists():
            #vérifier si le chemin représente un fichier et si elle existe.
            stream=path.open('r')

            garage = json.load(stream)

            #fermer le stream
            stream.close()

            #retourner le resultat
            return garage
        #si fichier n'existe pas
        else:
            raise Exception('fichier inexistant')

    #methode ajoutervoiture et getvoiture
    def ajoutervoiture(self, element:Voiture)->None:
        self.__voitures.append(Voiture)

    def getvoiture(self, numvoiture:str)->Voiture:
        return Voiture

    #methodes ajouterreparation et getreparations
    def ajouterreparation(self, numvoiture:str, reparation:Reparation)->None:
        Voiture.ajouterreparation(Reparation)

    def getreparation(self, numvoiture:str)->list[Reparation]:
        return list[Reparation]

        #definition du constructeur
    def __init__(self,nom='',adresse='', telephone='',voitures = list[Voiture],employes=list[Employe]):
        #initialisation des attributs
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.set_employes = []
        self.set_voitures = []
        self.__employes.append(Employe)


