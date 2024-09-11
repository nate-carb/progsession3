citation = "La vie est un mystère qu'il faut vivre, et non un problème à résoudre -Gandhi"
mots = []
liste = citation.split()
for i in range(0,len(liste),3):
    mot3= " ".join(liste[i:i+3]) + "\n"
    mots.append(mot3)
auteur = mots[-1].find("-")
auteurfinal = mots[-1][0:auteur] + "\n-" + mots[-1][auteur+1:]
mots.pop()
mots.append(auteurfinal)
stringfinal = ""
for i in range(len(mots)):
    string = "".join(mots[i]) + ' '
    stringfinal += string

print(stringfinal)