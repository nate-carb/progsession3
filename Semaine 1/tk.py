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
    mots=[]
    for i in citationfinal:
        mot = citationfinal.split(" ")
        mots.append(mot)

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



window.mainloop()

