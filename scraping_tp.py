from tkinter import *
import os
from tkinter import font
from turtle import color
import bs4 as bs
import urllib.request
import ssl

from numpy import size

def soup():
    name = barre_musique.get()
    artiste = barre_artiste.get()
    ssl._create_default_https_context = ssl._create_unverified_context
    print(name,artiste)

    sauce1 = urllib.request.urlopen (f"https://www.paroles.net/{artiste}/paroles-{name}")
    soup1 = bs.BeautifulSoup(sauce1,'html5lib')
    tmp = soup1.find('div','song-text').text
    print(tmp)
    return tmp

#booyemoor
def saut(cle) :
    #création de recherche en décalant
    d = {}
    for i in range(len(cle)-1):
        d[cle[i]] = len(cle) - i - 1
    return d

def boyer_moore(texte, cle):
    position = []
    text = len(texte)
    key = len(cle)
     
    if key <= text :
        decalage = saut(cle) 
    i=0
    trouve = False
    while (i <= text-key):

        for j in range (key -1, -1, -1): 
            trouve = True
            if texte[i+j] != cle[j] : 
                if (texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                    i+=decalage[texte[i+j]] 

                else :
                    i+=j+1 
                trouve = False
        if trouve :
            position.append(i) 
            print(position)
            i=i+1
            trouve = False 
    return len(position)
def nb_occurrence_theme() :
    texte= soup()
    compteur = 0
    for mot in liste_amour :
        print(mot)
        nb = boyer_moore(texte,mot)
        compteur = compteur + nb
    print(compteur)
    return compteur

liste_amour=['mariage','aim','coeur','quitte']
#paramètre fenêtre
fenetre = Tk()
fenetre.geometry('460x751')
fenetre.title("Scrapping")

#fond
Photo = PhotoImage(file = "fond_piano.png")
label=Label(fenetre, image = Photo)
label.place(x=-2, y=0)

#partie titre
frame_titre = Frame(fenetre)
txt_titre = Label(frame_titre, text='Recherche :', font=('Arial', 30))
frame_titre.place(x=130, y=80)
txt_titre.pack()

#partie artiste
frame_artiste = Frame(fenetre)
txt_artiste = Label(frame_artiste, text="Artiste", background='white' )
barre_artiste=Entry(fenetre,width=50,bg="black",relief="ridge",bd=5,fg="white")
frame_artiste.place(x=210, y=160)
txt_artiste.pack()
barre_artiste.place(x=70, y=300)

#partie musique
frame_musique = Frame(fenetre)
txt_musique = Label(frame_musique, text="Musique", background='white' )
barre_musique=Entry(fenetre,width=50,bg="black",relief="ridge",bd=5,fg="white")
frame_musique.place(x=200, y=250)
barre_musique.place(x=70, y=200)
txt_musique.pack()

#affichage boutons tah l'acnée
sf1 = Frame(fenetre)
b1=Button(sf1,text='Valider',width=5,height=2,bg='black',fg='white', command=nb_occurrence_theme)
b1.pack()
sf1.pack(pady = 340)

fenetre.mainloop()