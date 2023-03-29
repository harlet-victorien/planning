from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import *
import mysql.connector as MC
import random as r






fenetre = Tk()
fenetre.title('planning')
fenetre.attributes('-fullscreen', True)
print
#variables
count=0

def f(event):
    if event.keysym == "c":
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
fenetre.bind("<Key>", f)

def compte():
    global count
    count=0

tableau = ttk.Treeview(fenetre, columns=('heure', 'lundi', 'mardi','mercredi','jeudi','vendredi','samedi','dimanche'),show = 'headings')
#j'ai rajouté ça pour pouvoir modifier la taille des colonnes bro (ok brotheeeer)
tableau.column('heure',width=200)
tableau.column('lundi',width=150)
tableau.column('mardi',width=150)
tableau.column('mercredi',width=150)
tableau.column('jeudi',width=150)
tableau.column('vendredi',width=150)
tableau.column('samedi',width=150)
tableau.column('dimanche',width=150)

tableau.heading('heure', text=' ')
tableau.heading('lundi', text='Lundi')
tableau.heading('mardi', text='Mardi')
tableau.heading('mercredi', text='Mercredi')
tableau.heading('jeudi', text='Jeudi')
tableau.heading('vendredi', text='Vendredi')
tableau.heading('samedi', text='Samedi')
tableau.heading('dimanche', text='Dimanche')

tableau.heading('vendredi', text='Vendredi 12-02')

L2=[["8h--8h55"],["8h55--9h50"],["10h10-11h05"],["11h05--12h"],["12h--13h30"],["13h30--14h25"],["14h25--15h20"],["15h40--16h35"],["16h35--17h30"]]
for j in range (0,len(L2)):
    for i in range (7):
        L2[j]=L2[j]+[""]
#print(L2)
for i in range(9):
    tableau.insert('', 'end', iid=L2[i][0], values=(L2[i][0],L2[i][1], L2[i][2], L2[i][3],L2[i][4], L2[i][5], L2[i][6], L2[i][7]))
tableau.place(x=75,y=200)

ajouter_f = Frame(fenetre)
ajouter_f.place(x=0,y=0)
#etiquettes
date=Label(ajouter_f, text='Date')
date.grid(row=0, column=0)
Debut=Label(ajouter_f,text='Debut')
Debut.grid(row=0, column=1)
Fin=Label(ajouter_f,text='Fin')
Fin.grid(row=0, column=2)
#cases pour boutons

dateb=Entry(ajouter_f)
dateb.grid(row=1, column=0)
Debutb=Entry(ajouter_f)
Debutb.grid(row=1, column=1)
Finb=Entry(ajouter_f)
Finb.grid(row=1, column=2)
date.grid_forget(), Debut.grid_forget(), Fin.grid_forget(), dateb.grid_forget(), Debutb.grid_forget(), Finb.grid_forget()

#boutons

#menu déroulant
def Ajouter_cours():
    global count
    if count ==0:
        count=1
        date.grid(row=1, column=4), Debut.grid(row=1, column=5),Fin.grid(row=1, column=6),dateb.grid(row=2, column=4),Debutb.grid(row=2, column=5),Finb.grid(row=2, column=6)
        #bouton retour qui s'efface lui et les étiquettes
        Retour = Button(fenetre, text='Retour', command = lambda : [Retour.place_forget(),compte(), date.grid_forget(), Debut.grid_forget(), Fin.grid_forget(), dateb.grid_forget(), Debutb.grid_forget(), Finb.grid_forget()])
        Retour.place(x=135,y=75)

def Quitter3():
    fenetre_planning.destroy()


def planning_ds():
    global fenetre_planning
    fenetre_planning =Tk()
    fenetre_planning.geometry('1400x600')
    Menu_planning = Frame(fenetre_planning)
    Menu_planning.place(x=0,y=0)
    def Planning_CPG1():
        print('1')
    def Planning_CPG2():
        print('1')
    def Planning_CIR():
        print('1')
    def Planning_CNB():
        print('1')
    Quitter = Button(fenetre_planning,text='Quitter',command=Quitter3)
    Quitter.place(x=1280,y=550)
    menuDeroulant = Menubutton(Menu_planning, text='Menu', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    menuDeroulant1.add_command(label='CPG1', command = Planning_CPG1)
    menuDeroulant1.add_command(label='CPG2', command = Planning_CPG2)
    menuDeroulant1.add_command(label='CIR', command = Planning_CIR)
    menuDeroulant1.add_command(label='CNB', command = Planning_CNB)
    menuDeroulant.configure(menu=menuDeroulant1)




menuDeroulant = Menubutton(ajouter_f, text='Menu', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
menuDeroulant.grid()
menuDeroulant1 = Menu(menuDeroulant)
menuDeroulant1.add_command(label='Ajouter un cours', command = Ajouter_cours)
menuDeroulant1.add_command(label='Planning de DS', command = planning_ds)

# Attribution du menu déroulant au menu Affichage

menuDeroulant.configure(menu=menuDeroulant1)
#bouton quitter
def Quitter2():
    fenetre.destroy()

Quitter = Button(fenetre,text='Quitter',command=Quitter2)
Quitter.place(x=1280,y=550)







pixel = PhotoImage(width=1, height=1)

color='#B1FF7D'
def afficher_buttons(L):
    for i in range (9):
        for j in range (7):
            cours1 = Button(fenetre,image=pixel,width=142,bg=L[i][j][1],height=14)
            cours1.place(x=275+150*j,y=225+20*i)

L=[]
for i in range (9):
    L=L+[[[""]]]

    for j in range (8):
        L[i]=L[i]+[["#"]]
        for z in range (3):
            L[i][j]=L[i][j]+["#"]

for i in range (9):
    for j in range (8):
        L[i][j][1]=color
        L[4][j][1]='#928AFF'

#print(L)
L[0][2][1]='#F5225A'
L[1][2][1]='#F5225A'
L[7][3][1]='#FFFFFF'
L[6][3][1]='#FFFFFF'
L[8][3][1]='#FFFFFF'
L[5][3][1]='#FFFFFF'
afficher_buttons(L)





def lignedeplus():
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_bdd')

    cursor = cnx.cursor()
    req = 'INSERT INTO PROFS (ProfID, Prenom, Nom, AutoModif1, AutoModif2) VALUES (%s, %s, %s, %s, %s)'
    mpsza = r.randint(100,1000)
    infos = (mpsza, 'moi', 'moi', 0, 0)

    cursor.execute(req,infos)
    cnx.commit()

    cnx.close()



cours1 = Button(fenetre,image=pixel,width=142,bg='#F5225A',height=14,command=lignedeplus)
cours1.place(x=600,y=800)













fenetre.mainloop()