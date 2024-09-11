import tkinter
import random


def citation(): #numero 3
    x = 0
    with open('citations.txt', mode="r") as fichier:
        for i in fichier:
            fichier.readline()
            x += 1
    nbcitation = x
    citationchoisi = random.randint(0, nbcitation)
    with open('citations.txt',mode="r", encoding="utf8") as fichier:
           texte= fichier.readlines()
           citationfinal = texte[citationchoisi]
           mots = []
           liste = citationfinal.split()
           for i in range(0, len(liste), 3):
               mot3 = " ".join(liste[i:i + 3]) + "\n"
               mots.append(mot3)
           auteur = mots[-1].find("-")
           auteurfinal = mots[-1][0:auteur] + "\n-" + mots[-1][auteur + 1:]
           mots.pop()
           mots.append(auteurfinal)
           stringfinal = ""
           for i in range(len(mots)):
               string = "".join(mots[i]) + ' '
               stringfinal += string
           return stringfinal

class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sagesse")
        self.label = tkinter.Label(text=citation())
        self.label.pack()
        self.button = tkinter.Button(text="fermer", command=self.buttonpress)
        self.button.pack()

    def buttonpress(self):
        self.destroy()


window = Window()
window.mainloop()


