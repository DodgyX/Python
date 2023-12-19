class Voiture:
    def __init__(self, marque, model, couleur):
        self.marque = marque
        self.model = model
        self.couleur = couleur
    
    def roule(self):
        print(f'La {self.marque} {self.model} va hyper vite !!!')
    
    def depasser(self, Autre_Voiture):
        print(f'La {self.marque} {self.model} à dépassé la {Autre_Voiture.marque} {Autre_Voiture.model} !!!')


# ici, le "self" devient "MaVoiture" (juste pour cet objet, on peut en creer d'autres avec la même classe)
MaVoiture = Voiture('Mercedes', '300 SLR Uhlenhaut', "gris")
Autre_Voiture = Voiture('Lamborghini', 'Revuelto', "Bleu")

print(MaVoiture.marque)
MaVoiture.depasser(Autre_Voiture)