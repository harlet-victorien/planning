from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import *
import mysql.connector as MC
import random as r
from datetime import datetime
import calendar

#Fonctions :


def f(event):
    if event.keysym == "c":
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
    if event.keysym == "p":
        affichertableprofs()

def Count():
    global count2
    count2+=1
    return count2

def tableau_cpg1():
    L=[[37, 'mercredi','07/09/2022', '10h-11h30', 'FHS 1', '11h30-12h', 'C854'],[39, 'vendredi' ,'23/09/2022', '10h-12h', 'Maths 1', '12h-12h40', 'Amphi JND'],[40, 'mercredi', '28/09/2022', '8h-10h', 'Physique 1', '7h20-8h', 'C854'],[41, 'mercredi', '05/10/2022', '10h-12h', 'Anglais 1', '12h-12h40', 'C854'],[42, 'jeudi', '13/10/2022', '10h-12h', 'Maths 2', '12h-12h40', 'C854'],[43, 'vendredi', '21/10/2022', '10h-12h', 'SI 1', '12h-12h40', 'C403-C406'],[46, 'mercredi', '09/11/2022', '8h-10h', 'Physique 2', '7h20-8h', 'C854'],[47, 'mercredi', '16/11/2022', '10h-12h', 'FHS 2', '12h-12h40', 'C854'],[48, 'vendredi', '25/11/2022', '10h-12h', 'Maths 3', '12h-12h40', 'C854'],[49, 'mercredi', '30/11/2022', '8h-10h', 'Physique 3', '7h20-8h', 'C854'],[50, 'mardi' ,'06/12/2022', '10h-12h', 'SI 2', '12h-12h40', 'C854'],[51, 'lundi' ,'12/12/2022', '8h-12h' ,'Part. 1-Maths', '12h-13h20', 'B506'],[51, 'mardi' ,'13/12/2022', '8h-12h', 'Part. 1-Phy', '12h-13h20', 'B506'],[51, 'mercredi', '14/12/2022', '8h-12h', 'Part. 1-FHS', '12h-13h20' ,'B506'],[51, 'jeudi' ,'15/12/2022', '8h-11h', 'Part. 1-SI', '11h-12h', 'B506'],[51, 'jeudi' ,'15/12/2022', 'après-midi', 'Part. 1-oraux'],[51, 'vendredi', '16/12/2022', '10h-12h', 'Part. 1-LV 2', '12h-12h40', 'B506'],[51, 'vendredi', '16/12/2022', '13h30-16h30', 'Part. 1-Ag', '16h30-17h30', 'B506']]

    tableau = ttk.Treeview(fenetre_planning, columns=('Semestre', 'Semaine', 'Jour','Date','Horaire','Matière','Tiers-temps','Salle'),show = 'headings')
    tableau.column('Semestre',width=100, anchor=CENTER)
    tableau.column('Semaine',width=150,anchor=CENTER)
    tableau.column('Jour',width=150,anchor=CENTER)
    tableau.column('Date',width=150,anchor=CENTER)
    tableau.column('Horaire',width=150,anchor=CENTER)
    tableau.column('Matière',width=150,anchor=CENTER)
    tableau.column('Tiers-temps',width=150,anchor=CENTER)
    tableau.column('Salle',width=150,anchor=CENTER)

    tableau.heading('Semestre', text='',anchor=CENTER)
    tableau.heading('Semaine', text='Semaine ',anchor=CENTER)
    tableau.heading('Jour', text='Jour ', anchor=CENTER)
    tableau.heading('Date', text='Date ',anchor=CENTER)
    tableau.heading('Horaire', text='Horaire ',anchor=CENTER)
    tableau.heading('Matière', text='Matière ',anchor=CENTER)
    tableau.heading('Tiers-temps', text='Tiers-temps ',anchor=CENTER)
    tableau.heading('Salle', text='Salle ',anchor=CENTER)

    tableau.place(x=50,y=50)
    for i in range(len(L)):
        print(i)
        if int(len(L[i]))==5:
            tableau.insert('', 'end', iid=Count(), values=('',L[i][0],L[i][1], L[i][2], L[i][3],L[i][4]))
        else:
            tableau.insert('', 'end', iid=Count(), values=('',L[i][0],L[i][1], L[i][2], L[i][3],L[i][4], L[i][5], L[i][6]))

def compte():
    global count
    count=0

def calendrier (date_auj):
    #date du calendrier
    
    int_day=int((calendar.weekday(int(date_auj[0]),int(date_auj[1]),int(date_auj[2]))))
    previous_month=calendar.monthrange(int(date_auj[0]),int(date_auj[1])-1)
    act_month=calendar.monthrange(int(date_auj[0]),int(date_auj[1]))
    act_month=act_month[1]
    previous_month=previous_month[1]
    
    week_act=[]
    for i in range(7):
        if int(date_auj[2])+(i-int_day)<1:
            week_act=week_act +[previous_month-int_day+i+1]
            week_act[i]=str(week_act[i])+ '/' + str(int(date_auj[1])-1)


        elif int(date_auj[2])+(i-int_day)>act_month:
            week_act=week_act+[i-int_day]
            week_act[i]=str(week_act[i])+ '/' + str(int(date_auj[1])+1)
        else:
            week_act=week_act+[int(date_auj[2])+(i-int_day)]
            week_act[i]=str(week_act[i])+ '/' + str(int(date_auj[1]))
    return(week_act)

def tab ():
    

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
    tableau.heading('lundi', text='Lundi '+ week_act[0])
    tableau.heading('mardi', text='Mardi '+week_act[1])
    tableau.heading('mercredi', text='Mercredi '+week_act[2])
    tableau.heading('jeudi', text='Jeudi '+week_act[3])
    tableau.heading('vendredi', text='Vendredi '+week_act[4])
    tableau.heading('samedi', text='Samedi '+week_act[5])
    tableau.heading('dimanche', text='Dimanche '+week_act[6])

    L2=[["8h--8h55"],["8h55--9h50"],["10h10-11h05"],["11h05--12h"],["12h--13h30"],["13h30--14h25"],["14h25--15h20"],["15h40--16h35"],["16h35--17h30"]]
    for j in range (0,len(L2)):
        for i in range (7):
            L2[j]=L2[j]+[""]
    #print(L2)
    for i in range(9):
        tableau.insert('', 'end', iid=L2[i][0], values=(L2[i][0],L2[i][1], L2[i][2], L2[i][3],L2[i][4], L2[i][5], L2[i][6], L2[i][7]))
    tableau.place(x=placementF,y=300)

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

def classeget():
    b=-1
    a=(Classeb.get(),)
    cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = 'SELECT ClasseID FROM CLASSES'
    cursor.execute(req)
    L = cursor.fetchall()
    req = 'SELECT Nom FROM CLASSES'
    cursor.execute(req)
    L2 = cursor.fetchall()
    for i in L2:
        b+=1
        if i==a:
            a=L[b][0]    
    cnx.close()
    return(a)
            

    

def setup():
    dateNow=list(str(datetime.now()))
    dateNow=[dateNow[0]+dateNow[1]+dateNow[2]+dateNow[3],dateNow[5]+dateNow[6],dateNow[8]+dateNow[9]]
    global week_act
    week_act=calendrier(dateNow)
    Quitter = Button(fenetre,text='Quitter',command=Quitter2)
    Quitter.place(x=widthF-100,y=heightF-100)


    fenetre.bind("<Key>", f)

    tab()

    deroulant= Frame(fenetre)
    deroulant.place(x=0,y=0)
    ajouter_f = Frame(fenetre)
    ajouter_f.place(x=placementF/2,y=heightF-200)
    #etiquettes
    global Titre
    Titre=Label(ajouter_f,text='Titre')
    Titre.grid(row=0, column=0)
    global date
    date=Label(ajouter_f, text='Date')
    date.grid(row=0, column=1)
    global Debut
    Debut=Label(ajouter_f,text='Debut')
    Debut.grid(row=0, column=2)
    global Fin
    Fin=Label(ajouter_f,text='Fin')
    Fin.grid(row=0, column=3)
    global Categorie
    Categorie=Label(ajouter_f,text='Categorie')
    Categorie.grid(row=0, column=4)
    global Salle
    Salle=Label(ajouter_f,text='Salle')
    Salle.grid(row=0, column=5)
    global Classe
    Classe=Label(ajouter_f,text='Classe')
    Classe.grid(row=0, column=6)
    global Description
    Description=Label(ajouter_f,text='Description')
    Description.grid(row=0, column=7)

    #cases pour boutons
    global Titreb
    Titreb=Entry(ajouter_f)
    Titreb.grid(row=1, column=0)
    global dateb
    dateb=Entry(ajouter_f)
    dateb.grid(row=1, column=1)
    global Debutb
    Debutb=Entry(ajouter_f)
    Debutb.grid(row=1, column=2)
    global Finb
    Finb=Entry(ajouter_f)
    Finb.grid(row=1, column=3)
    global Categorieb
    Categorieb=Entry(ajouter_f)
    Categorieb.grid(row=1, column=4)
    global Salleb
    Salleb=Entry(ajouter_f)
    Salleb.grid(row=1, column=5)
    global Classeb
    Classeb=Entry(ajouter_f)
    Classeb.grid(row=1, column=6)
    global Descriptionb
    Descriptionb=Entry(ajouter_f)
    Descriptionb.grid(row=1, column=7)
    date.grid_forget(), Debut.grid_forget(), Fin.grid_forget(),Titre.grid_forget(),Categorie.grid_forget(),Salle.grid_forget(),Classe.grid_forget(),Classeb.grid_forget(),Description.grid_forget(), dateb.grid_forget(), Debutb.grid_forget(), Finb.grid_forget(),Salleb.grid_forget(),Categorieb.grid_forget(), Titreb.grid_forget(),Descriptionb.grid_forget()
    menuDeroulant = Menubutton(deroulant, text='Menu', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    menuDeroulant1.add_command(label='Ajouter un événement', command = Ajouter_cours)
    menuDeroulant1.add_command(label='Planning de DS', command = planning_ds)


    # Attribution du menu déroulant au menu Affichage

    menuDeroulant.configure(menu=menuDeroulant1)


    # cours1 = Button(fenetre,image=pixel,width=142,bg='#F5225A',height=14,command=lignedeplus)
    # cours1.place(x=600,y=800)


#menu déroulant
def ajouter_event():
    global count1
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = "INSERT INTO EVENTS (EventID, Titre, Date, Heuredebut, Heurefin, Categorie, Salle, Reserve, Description, ClasseIDext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    infos = (count1, Titreb.get(), dateb.get(), Debutb.get(), Finb.get(), Categorieb.get() ,Salleb.get(), True, Descriptionb.get(), classeget())
    cursor.execute(req,infos)
    cnx.commit()
    cnx.close()
    count1+=1
    Titreb.delete(0, END)
    dateb.delete(0, END)
    Finb.delete(0, END)
    Debutb.delete(0, END)
    Descriptionb.delete(0, END)
    Salleb.delete(0, END)
    Classeb.delete(0, END)
    Categorieb.delete(0, END)

def Ajouter_cours():
    global count
    if count ==0:
        count=1
        Titre.grid(row=1, column=4), date.grid(row=1, column=5),Debut.grid(row=1, column=6),Fin.grid(row=1, column=7),Categorie.grid(row=1, column=8),Salle.grid(row=1, column=9),Classe.grid(row=1, column=10),Description.grid(row=1, column=11),dateb.grid(row=2, column=5),Debutb.grid(row=2, column=6),Finb.grid(row=2, column=7),Titreb.grid(row=2, column=4),Categorieb.grid(row=2, column=8),Salleb.grid(row=2, column=9),Classeb.grid(row=2, column=10),Descriptionb.grid(row=2, column=11)
        #bouton retour qui s'efface lui et les étiquettes
        Ajouter_event = Button(fenetre, text="ajouter l'événement", command =ajouter_event)
        Ajouter_event.place(x=405,y=755)
        Retour = Button(fenetre, text='Retour', command = lambda : [Ajouter_event.place_forget(),Titre.grid_forget(),Classe.grid_forget(),Classeb.grid_forget(),Titreb.grid_forget(),Categorie.grid_forget(),Categorieb.grid_forget(),Description.grid_forget(),Descriptionb.grid_forget(),Salle.grid_forget(),Salleb.grid_forget(),Titre.grid_forget(),Retour.place_forget(),compte(), date.grid_forget(), Debut.grid_forget(), Fin.grid_forget(), dateb.grid_forget(), Debutb.grid_forget(), Finb.grid_forget()])
        Retour.place(x=874,y=769)

#def Connexion():



def Quitter3():
    fenetre_planning.destroy()


def planning_ds():
    global fenetre_planning
    fenetre_planning =Tk()
    fenetre_planning.geometry('1400x600')
    Menu_planning = Frame(fenetre_planning)
    Menu_planning.place(x=0,y=0)

    Quitter = Button(fenetre_planning,text='Quitter',command=Quitter3)
    Quitter.place(x=1280,y=550)
    menuDeroulant = Menubutton(Menu_planning, text='Menu', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = RAISED)
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    menuDeroulant1.add_command(label='CPG1', command = tableau_cpg1)
    menuDeroulant1.add_command(label='CPG2', command = Planning_CPG2)
    menuDeroulant1.add_command(label='CIR', command = Planning_CIR)
    menuDeroulant1.add_command(label='CNB', command = Planning_CNB)
    menuDeroulant.configure(menu=menuDeroulant1)
        
def Planning_CPG2():
    print('1')
def Planning_CIR():
    print('1')
def Planning_CNB():
    print('1')




#bouton quitter
def Quitter2():
    fenetre.destroy()



def afficher_buttons(L):
    bigFont = Font(size=20, weight='bold')
    for i in range (9):
        for j in range (7):
            cours1 = Button(fenetre,image=pixel,width=142,bg=L[i][j][1],height=14)
            cours1.place(x=placementF+200+150*j,y=325+20*i)
    semaine_prec = Button(fenetre,text='<',bg='#dee26b')
    semaine_suiv = Button(fenetre,text='>',bg='#dee26b')
    semaine_prec['font']=bigFont
    semaine_suiv['font']=bigFont
    semaine_prec.place(x=50,y=heightF//2-40)
    semaine_suiv.place(x=widthF-90,y=heightF//2-40)








def lignedeplus():
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

    cursor = cnx.cursor()
    req = 'INSERT INTO PROFS (ProfID, Prenom, Nom, AutoModif1, AutoModif2, MotDePasse) VALUES (%s, %s, %s, %s, %s, %s)'
    mpsza = r.randint(100,1000)
    infos = (mpsza, 'moi', 'moi', 0, 0,'moi')

    cursor.execute(req,infos)
    cnx.commit()

    cnx.close()

def affichertableprofs():
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

    cursor = cnx.cursor()
    req = 'SELECT * FROM PROFS'
    cursor.execute(req)
    L = cursor.fetchall()
    for i in L:
        print(i)
    cnx.close()


def setup2():
    global v,v2,e,e2


    v = StringVar()   #importation de la zone de saisie StringVar
    v2 = StringVar()
    e = Entry(Co, textvariable=v, width=50, fg="black")
    e2 = Entry(Co, textvariable=v2, width=50, fg="black")
    e.pack(),e2.pack()    #insertion de la zone de saisie
    Button(Co, text="Annuler", command = Co.destroy).pack(side=LEFT)
    Button(Co, text="Valider", command = verification).pack(side=LEFT) #Bouton qui verifie que le mot de passe est bon
    Co.bind('<Return>',verification)


def verification(event):
    global lancer1
    for i in range (len(L)):
        if e.get() == L[i][2] and e2.get()==L[i][5]:
            lancer1=True
            Co.destroy()
    for i in range (len(L2)):
        if e.get() == L2[i][2] and e2.get()==L2[i][5]:
            lancer1=True
            Co.destroy()
    if lancer1==False:
        champ_label = Label(Co, text="Identifiants incorrects !!!",background="red")
        champ_label.pack()
        champ_label.after(2000, champ_label.destroy)







#Exploitation

cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

cursor = cnx.cursor()
req = 'SELECT * FROM PROFS'
cursor.execute(req)
L = cursor.fetchall()
req = 'SELECT * FROM ELEVES'
cursor.execute(req)
L2 = cursor.fetchall()
for i in L:
    print(i)
for i in L2:
    print(i)
cnx.close()





lancer1 = False
Co = Tk()
Co.title('Connexion')
setup2()
Co.mainloop()
if lancer1 :
    fenetre = Tk()
    fenetre.title('planning')
    fenetre.attributes('-fullscreen', True)

    fenetre.update()

    #variables
    count=0
    # cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    # cursor = cnx.cursor()
    # req = 'SELECT * FROM EVENT'
    # cursor.execute(req)
    # L = cursor.fetchall()
    # for i in L:
    #     print(i)
    # cnx.close()
    global count1
    cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = 'SELECT EventID FROM EVENTS'
    cursor.execute(req)
    L = cursor.fetchall()
    count1=L[-1][0]+1
    widthF = fenetre.winfo_width()
    heightF = fenetre.winfo_height()
    placementF = (widthF-1250)/2
    pixel = PhotoImage(width=1, height=1)
    color='#B1FF7D'
    count2=0

    setup()
    fenetre.mainloop()

#pour delete une ligne
# import mysql.connector as MC
# cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
# cursor = cnx.cursor()
# req = "DELETE FROM EVENTS WHERE EventID=5"
# cursor.execute(req)
# cnx.commit()
# cnx.close()