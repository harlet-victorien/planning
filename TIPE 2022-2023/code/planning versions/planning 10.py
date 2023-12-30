from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import *
import mysql.connector as MC
import random as r
from datetime import datetime
import calendar
import pendulum
import colorsys

#* Classes                                                                                                      

class case:
    def __init__(self,frame,nom,column,taille):
        self.Nom=Label(frame,text=nom,bg=color_bg,font=('ARIAL',taille, BOLD))
        self.Nom.grid(row=0, column=column)
        self.entry=Entry(frame)
        self.entry.grid(row=1, column=column)

class button_frame:
    def __init__(self,frame,nom,command,pos,size):
        posx,posy=pos
        sizex,sizey=size
        self.button=Button(frame,text=nom,command=command, bg=color_bts,font=("Helvetica", 10,'bold'),width=sizex,height=sizey)
        self.button.place(x=posx,y=posy)
        if nom=='CPG1':
            self.button.place_forget()
            if 2 in persClasses:
                self.button.place(x=posx,y=posy)
        if nom=='CPG2':
            self.button.place_forget()
            if 1 in persClasses:
                self.button.place(x=posx,y=posy)
    def update_color(self):
        self.button.config(bg=color_bts)

#* Fonctions                                                                                                    



def Count():
    global count2
    count2+=1
    return count2


def compte():
    global count
    count=0


def tableau_cpg1():
    global dsCPG1_button, dsCPG2_button

    for widget in frame3.winfo_children():
        if widget != dsCPG1_button.button and widget != dsCPG2_button.button:
            widget.destroy()

    # Update the colors of the buttons
    dsCPG1_button.update_color()
    dsCPG2_button.update_color()



    tableau = ttk.Treeview(frame3, columns=('Date','Horaire','Titre','Salle'),show = 'headings',selectmode='browse',height=10)
    vsb = ttk.Scrollbar(frame3,orient="vertical",command=tableau.yview)
    tableau.tag_configure('T', font='Arial 15')
    vsb.configure(command=tableau.yview)
    tableau.configure(yscrollcommand=vsb.set)
    tableau.column('Date',width=250,anchor=CENTER)
    tableau.column('Horaire',width=250,anchor=CENTER)
    tableau.column('Titre',width=250,anchor=CENTER)
    tableau.column('Salle',width=250,anchor=CENTER)

    tableau.heading('Date', text='Date ',anchor=CENTER)
    tableau.heading('Horaire', text='Horaire ',anchor=CENTER)
    tableau.heading('Titre', text='Titre ',anchor=CENTER)
    tableau.heading('Salle', text='Salle ',anchor=CENTER)

    tableau.place(x=200,y=100)
    vsb.place(x=5,y=100,height=800)
    
    for i in range(len(eventsCPG1)):
        if 'DS' in eventsCPG1[i][4] or 'ds' in eventsCPG1[i][4] or 'Ds' in eventsCPG1[i][4] or 'artiel' in eventsCPG1[i][4] or 'onseil de classe' in eventsCPG1[i][4]:
            for j in range(len(Liste_des_salles)):
                    if Liste_des_salles[j][0]==eventsCPG1[i][7]:
                        yu=Liste_des_salles[j][1]
                        text_date=str(eventsCPG1[i][2])
                        text_date=text_date[8:10]+'/'+text_date[5:7]+'/'+text_date[0:4]
                        text_heure=str(eventsCPG1[i][2])
                        text_heure=text_heure[11:16]
            tableau.insert('', 'end', iid=Count(), values=(text_date, text_heure, eventsCPG1[i][1], yu),tags='T')
    tableau.column('#0', stretch=True)
    

def tableau_cpg2():
    for widget in frame3.winfo_children():
        widget.destroy()
    dsCPG1_button = button_frame(frame3, "CPG1", tableau_cpg1, (0,0),(10,1))
    dsCPG2_button = button_frame(frame3, "CPG2", tableau_cpg2, (0,30),(10,1)) 
    tableau = ttk.Treeview(frame3, columns=('Date','Horaire','Titre','Salle'),show = 'headings',selectmode='browse',height=10)
    vsb = ttk.Scrollbar(frame3,orient="vertical",command=tableau.yview)
    tableau.tag_configure('T', font='Arial 15')
    vsb.configure(command=tableau.yview)
    tableau.configure(yscrollcommand=vsb.set)
    tableau.column('Date',width=250,anchor=CENTER)
    tableau.column('Horaire',width=250,anchor=CENTER)
    tableau.column('Titre',width=250,anchor=CENTER)
    tableau.column('Salle',width=250,anchor=CENTER)

    tableau.heading('Date', text='Date ',anchor=CENTER)
    tableau.heading('Horaire', text='Horaire ',anchor=CENTER)
    tableau.heading('Titre', text='Titre ',anchor=CENTER)
    tableau.heading('Salle', text='Salle ',anchor=CENTER)

    tableau.place(x=200,y=100)
    vsb.place(x=5,y=100,height=800)
    
    for i in range(len(eventsCPG2)):
        if 'DS' in eventsCPG2[i][4] or 'ds' in eventsCPG2[i][4] or 'Ds' in eventsCPG2[i][4] or 'artiel' in eventsCPG2[i][4] or 'onseil de classe' in eventsCPG2[i][4]:
            for j in range(len(Liste_des_salles)):
                    if Liste_des_salles[j][0]==eventsCPG2[i][7]:
                        yu=Liste_des_salles[j][1]
                        text_date=str(eventsCPG2[i][2])
                        text_date=text_date[8:10]+'/'+text_date[5:7]+'/'+text_date[0:4]
                        text_heure=str(eventsCPG2[i][2])
                        text_heure=text_heure[11:16]
            tableau.insert('', 'end', iid=Count(), values=(text_date, text_heure, eventsCPG2[i][1], yu),tags='T')
    tableau.column('#0', stretch=True)
  




def salleget(p):
    
    b=-1
    if p==1:
        a=(Salle.entry.get(),)
    else:
        a=(Salle2.entry.get(),)
    cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = 'SELECT SalleID FROM SALLE'
    cursor.execute(req)
    L = cursor.fetchall()
    req = 'SELECT Nom FROM SALLE'
    cursor.execute(req)
    L2 = cursor.fetchall()
    for i in L2:
        b+=1
        if i==a:
            a=L[b][0]    
    cnx.close()
    return(a)
            
def ajouter_personne():
    global a
    if personnesb.get()!='':
        a+=[personnesb.get()]
        #print(a)
        personnesb.delete(0, END)

def ajouter_personne2():
    global countP
    global a
    countP+=1
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = 'SELECT Nom FROM PERSONNES'
    cursor.execute(req)
    L = cursor.fetchall()
    for i in a:
        k=0
        for k,j in enumerate(L):
            #print(i,j)
            if i==j[0]:
                #print('là')
                req = "INSERT INTO PARTICIPE (ParticipeID, EventID_ext, PersID_ext) VALUES (%s, %s, %s)"
                infos = (countP, count1, k+1)
                cursor.execute(req,infos)
                cnx.commit()
                countP+=1
            
    a=[]



        


def entries(window,pos):
    posx,posy=pos
    ajouter_f = Frame(window,bg=color_bg)
    ajouter_f.place(x=posx,y=posy)
    if window!= frame2:
        global Titre
        Titre = case(ajouter_f,'Titre',0,11)
        global Debut
        Debut = case(ajouter_f,'Debut',2,11)
        global Fin
        Fin = case(ajouter_f,'Fin',3,11)
        global Categorie,Categorieb
        Categorie=Label(ajouter_f,text='Categorie',bg=color_bg,font=('ARIAL',11, BOLD))
        Categorie.grid(row=0,column=4)
        ff2=StringVar()
        Categorieb = ttk.Combobox(ajouter_f, textvariable=ff2)

        # get first 3 letters of every month name
        Categorieb['values'] = ['Ds','partiels','jour férié','conseil de classe','autre']
        Categorieb['state']='readonly'
       
        Categorieb.grid(row=1,column=4)
        global Salle
        Salle = case(ajouter_f,'Salle',5,11)
        global Description
        Description = case(ajouter_f,'Description',6,11)
    else:
        global Titre2
        Titre2 = case(ajouter_f,'Titre',0,19)
        global Debut2
        Debut2 = case(ajouter_f,'Debut',2,19)
        global Fin2
        Fin2 = case(ajouter_f,'Fin',3,19)
        global Categorie2,Categorie2b
        Categorie2b=Label(ajouter_f,text='Categorie',bg=color_bg,font=('ARIAL',19, BOLD))
        Categorie2b.grid(row=0,column=4)
        ff=StringVar()
        Categorie2 = ttk.Combobox(ajouter_f, textvariable=ff)

        # get first 3 letters of every month name
        Categorie2['values'] = ['Ds','partiels','jour férié','conseil de classe','autre']
        Categorie2['state']='readonly'
       
        Categorie2.grid(row=1,column=4)
        
        global Salle2
        Salle2 = case(ajouter_f,'Salle',5,19)
        global Description2
        Description2 = case(ajouter_f,'Description',6,19)

def setup():
    canvas = Canvas(frame2, width=fenetreWidth, height=fenetreHeight, bg =color_bg)
    canvas.pack()
    canvas.create_line(1000, 0, 1000, fenetreHeight)
    entries(frame2,(50,100))
    affichage_nom_colonnes_entries()
    



def insert_event_in_bdd():
    global count1
    global countPG
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    count1+=1
    countPG+=1
    req = "INSERT INTO EVENTS (EventID, Titre, Date_debut, Date_fin, Categorie, Reserve, Description, Salle_ID_ext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    infos = (count1, Titre2.entry.get(), Debut2.entry.get(), Fin2.entry.get(), Categorie2.get(), salle_check.get(), Description2.entry.get(), salleget(2))
    cursor.execute(req,infos)
    cnx.commit()
    req = 'SELECT Nom FROM GROUPES'
    cursor.execute(req)
    L = cursor.fetchall()
    for k,j in enumerate(L):
        #print(k,j)
        if selected_groupe.get()==j[0]:
            M=k+1
            #print(M)
            
    if selected_groupe.get()!='JUNIA':
       
        req = "INSERT INTO PARTICIPE_GROUPES (ParticipeID_g, EventID_ext, ClasseID_ext) VALUES (%s, %s, %s)"
        infos = (countPG, count1, M)
        cursor.execute(req,infos)
        cnx.commit()
        countPG+=1
    else:
        req = "INSERT INTO PARTICIPE_GROUPES (ParticipeID_g, EventID_ext, ClasseID_ext) VALUES (%s, %s, %s)"
        infos = (countPG, count1, 100)
        cursor.execute(req,infos)
        cnx.commit()
        countPG+=1
    cnx.close()
    refresh()
    Titre2.entry.delete(0, END)
    Fin2.entry.delete(0, END)
    Debut2.entry.delete(0, END)
    Description2.entry.delete(0, END)
    Salle2.entry.delete(0, END)
    



def affichage_nom_colonnes_entries():
    global selected_groupe
    global count
    if count ==0:
        global personnesb
        count=1
        
        cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
        cursor = cnx.cursor()
        req ="SELECT NOM FROM GROUPES"
        cursor.execute(req)
        A=cursor.fetchall()
        selected_groupe = StringVar()
        month_cb = ttk.Combobox(frame2, textvariable=selected_groupe)

        # get first 3 letters of every month name
        month_cb['values'] = A
        #print(month_cb)
        month_cb['state']='readonly'
        # place the widget
        month_cb.place(x=775,y=200)
        month_cb.bind('<<ComboboxSelected>>') 
        global salle_check
        salle_check = IntVar()
        Checkbutton(frame2,text='salle réservée ', variable = salle_check,onvalue = 1, offvalue = 0, bg= color_bg).place(x=250,y=200)
        personnes=Label(frame2,text='ajouter une personne',)    
        personnes.place(x=50,y=300)
        personnesb=Entry(frame2)
        personnesb.place(x=50, y=325)
        Button(frame2,text='ajouter la personne',command=ajouter_personne).place(x=50,y=350)
        Titre2.Nom.grid(row=1, column=4),Debut2.Nom.grid(row=1, column=6),Fin2.Nom.grid(row=1, column=7),Categorie2b.grid(row=1, column=8),Salle2.Nom.grid(row=1, column=9),Description2.Nom.grid(row=1, column=11),Debut2.entry.grid(row=2, column=6),Fin2.entry.grid(row=2, column=7),Titre2.entry.grid(row=2, column=4),Categorie2.grid(row=2, column=8),Salle2.entry.grid(row=2, column=9),Description2.entry.grid(row=2, column=11)
        #bouton retour qui s'efface lui et les étiquettes
        ajout_button = Button(frame2, text="ajouter l'événement", command =insert_event_in_bdd, bg=color_bts)
        ajout_button.place(x=50,y=200)






def setup2():
    global v,v2,e,e2,e3
    box = ttk.Frame(Co)
    box.grid(row=6, column=3)
    Label(text="Nom",bg=color_bg).grid(row=2, column=1, padx=10, pady=5) 
    Label(text="Prénom",bg=color_bg).grid(row=3, column=1, padx=10, pady=5)
    Label(text="Mot de passe",bg=color_bg).grid(row=4, column=1, padx=10, pady=5) 
    Label(text="  ",bg=color_bg).grid(row=1, column=1, padx=10, pady=5) 
    Label(text="  ",bg=color_bg).grid(row=5, column=1, padx=10, pady=5) 

    v = StringVar()   #importation de la zone de saisie StringVar
    v2 = StringVar()
    v3 = StringVar()
    e = Entry(Co, textvariable=v, width=50)
    e2 = Entry(Co, textvariable=v2, width=50)
    e3 = Entry(Co, textvariable=v3, width=50)
    e.grid(row=2, column=2, padx=10, pady=5),e2.grid(row=3, column=2, padx=10, pady=5),e3.grid(row=4, column=2, padx=10, pady=5)    #insertion de la zone de saisie
    Button(Co, text="Annuler", command = Co.destroy, background=color_bts).grid(row=6, column=1, padx=10, pady=5)
    Button(Co, text="Valider", command = verification, background=color_bts).grid(row=6, column=3, padx=10, pady=5)
    
    Co.bind('<Return>',verification)


def verification(*a):
    global lancer1
    global persID
    global persCat
    #print("xqsdq",L)
    for i in range (len(L)):
        if e.get() == L[i][1] and e2.get()==L[i][2] and e3.get()==L[i][4]:
            lancer1=True
            persID=i+1
            persCat=L[persID-1][5]
            Co.destroy()
   

    if lancer1==False:
        champ_label = Label(Co, text="Identifiants incorrects !!!",background="red")
        champ_label.grid(row=5, column=2, padx=10, pady=5)
        champ_label.after(2000, champ_label.destroy)


def defPerms ():
    global persCat
    global perms
    if persCat == 1: # prof
        perms = 1
    elif persCat == 2: # élève
        perms = 0
    elif persCat == 3: # admin
        perms = 2




def create_day_boxes(parent,now):
    global color_bg
    a=70
    current_month = now.month
    
    current_year = now.year
    nb_jours = calendar.monthrange(current_year,current_month)[1]

    events_of_month1=events_of_month(persEvents,current_month,current_year)

    events = [[] for _ in range(nb_jours)]
    for i in events_of_month1:
        i[1]=i[1].day
 
        events[i[1]-1]+=[i[0]]

    # Récupération du jour actuel
    #on récupère le numéro dans la semaine du premier jour du mois
    first_day = datetime(current_year, current_month, 1).weekday()
    #print(first_day)
    
    
    # Boucle pour créer les cases de chaque jour
    day_box = Frame(parent,bg=color_bg)
        
    day_box.grid(row=nb_jours//7, column=nb_jours%7)
    for i in range(nb_jours):   
        
        # Récupération du nom du jour
        day_name = datetime.strftime(datetime(current_year, current_month, i+1), '%A')
        # Ajout d'un bouton pour chaque case
        if len(events[i])==0:
            color=color_bg
            couleur_rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
            couleur_hsv = colorsys.rgb_to_hsv(*[c / 255 for c in couleur_rgb])
            
            couleur_hsv_clair = (couleur_hsv[0], max(0,couleur_hsv[1]*0.4), couleur_hsv[2])
            couleur_rgb_clair = tuple(round(c * 255) for c in colorsys.hsv_to_rgb(*couleur_hsv_clair))
            color = f"#{couleur_rgb_clair[0]:02x}{couleur_rgb_clair[1]:02x}{couleur_rgb_clair[2]:02x}"



        else:
            if a*len(events[i])>240:
                color='#%02x%02x%02x' % (255,0,0)
            else:
                color='#%02x%02x%02x' % (255,240-(a*len(events[i])),0)
            for j in range(len(events[i])):
                
                if 'acance'in events[i][j][4] or 'érié' in events[i][j][4]:
                    color='LIGHTBLUE'
        button = Button(day_box, text="{} {}".format(day_name, i+1),font=('Arial',11, BOLD), activebackground=color_bg,anchor="n", command=lambda day=i+1: show_day_events(day, events), background=color,width=20,height=7)
        button_text = button.cget("text")   
        for j in range(len(events[i])):
            button_text+="\n"+events[i][j][1]
        button.config(text=button_text)
        i+=first_day
        button.grid(row=i//7, column=i%7)

def eventsDetails(event):
    global event_details_window
    event_details_window = Toplevel(fenetre)
    event_details_window.title("Event details")
    event_details_window.geometry("775x500+325+275")
    event_details_window.config(bg=color_bg)
    if perms ==2:
        entries(event_details_window,(10,300))
    # Ajout d'un label pour afficher les événements
    event_label = Label(event_details_window, text='Titre: '+event[1],font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=10)
    event_label = Label(event_details_window, text='Date de début: '+str(event[2]),font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=40)
    event_label = Label(event_details_window, text='Date de fin: '+str(event[3]),font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=70)
    event_label = Label(event_details_window, text='Catégorie: '+event[4],font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=100)
    if event[5]==False:
        event_label = Label(event_details_window, text='Réservé: non',font=('Arial',11, BOLD),bg=color_bg)
    else :
        event_label = Label(event_details_window, text='Réservé: oui',font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=130)
    event_label = Label(event_details_window, text='Description: '+event[6],font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=160)
    for i in range(len(Liste_des_salles)):
        if Liste_des_salles[i][0]==event[7]:
            event_label = Label(event_details_window, text='Lieu: '+Liste_des_salles[i][1],font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=190)
    a=''
    #print(Liste_des_liaisons_groupes,event)
    for i in range(len(Liste_des_liaisons_groupes)):
        if Liste_des_liaisons_groupes[i][1]==event[0]:
            for j in range(len(Liste_des_groupes)):
                if Liste_des_groupes[j][0]==Liste_des_liaisons_groupes[i][2]:
                    a+=Liste_des_groupes[j][1]+'  '
    event_label = Label(event_details_window, text='Groupe: '+a,font=('Arial',11, BOLD),bg=color_bg)
    event_label.place(x=10,y=220)


    if perms>=1:
        Button(event_details_window, text="Delete", command = lambda: [supprimerEvent(event[0]),event_details_window.destroy()],background=color_bts).place(x=300,y=450)
        Button(event_details_window, text="Modify", command = lambda: [modifierEvent(event[0])],background=color_bts).place(x=50,y=450)

def supprimerEvent(eventID):
    #print(eventID)
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()

    req = "DELETE FROM PARTICIPE WHERE EventID_ext=%s"
    id=(str(eventID),)
    cursor.execute(req,id)
    cnx.commit()

    req = "DELETE FROM PARTICIPE_GROUPES WHERE EventID_ext=%s"
    id=(str(eventID),)
    cursor.execute(req,id)
    cnx.commit()

    req = "DELETE FROM EVENTS WHERE EventID=%s"
    id=(str(eventID),)
    cursor.execute(req,id)
    cnx.commit()
    cnx.close()
    refresh()

def modifierEvent(eventID):
    #print(eventID)
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = "SELECT* FROM EVENTS WHERE EventID=%s"
    id=(str(eventID),)
    cursor.execute(req,id)
    liste=cursor.fetchall()
    print(liste[0][1],liste[0][2],liste[0][3])
    print(liste)
    if ((Debut.entry.get()=='') or (Debut.entry.get()==' ')):
        A=liste[0][2]
    else:
        A=Debut.entry.get()

    if ((Fin.entry.get()=='') or (Fin.entry.get()==' ')):
        B=liste[0][3]
    else:
        B=Fin.entry.get()
    if ((Titre.entry.get()=='') or (Titre.entry.get()==' ')):
        C=liste[0][1]
    else:
        C=Titre.entry.get()
    if ((Categorieb.get()=='') or (Categorieb.get()==' ')):
        D=liste[0][4]
    else:
        D=Categorieb.get()
    if ((Description.entry.get()=='') or (Description.entry.get()==' ')):
        E=liste[0][6]
    else:
        E=Description.entry.get()
    if ((Salle.entry.get()=='') or (Salle.entry.get()==' ')):
        F=liste[0][7]
    else:
        F=salleget(1)
    id=str(eventID)
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    cursor.execute("UPDATE EVENTS SET Titre= '%s', Date_debut= '%s', Date_fin= '%s', Categorie = '%s', Description=' %s', Salle_ID_ext='%s' WHERE EventID=%s" % (C, A, B, D,E,F,id))
    cnx.commit()
    refresh()
    Titre.entry.delete(0, END)
    Fin.entry.delete(0, END)
    Debut.entry.delete(0, END)
    Description.entry.delete(0, END)
    Salle.entry.delete(0, END)
    cnx.close()
    day_events_window.destroy(),event_details_window.destroy()

def show_day_events(day, events):
    day-=1
    global day_events_window
    day_events_window = Toplevel(fenetre)
    day_events_window.title("Events for day {}".format(day+1))
    day_events_window.geometry("300x300+600+250")
    day_events_window.config(bg=color_bg)
    # Ajout d'un label pour afficher les événements
    
    if len(events[day])>=1:
        box = Frame(day_events_window)
        box.grid(row=len(events[day]), column=2)
        for i in range(len(events[day])):
            event_label = Label(day_events_window, text=events[day][i][1], bg=color_bg,font=('Arial',11, BOLD))
            event_button = Button(day_events_window, command=lambda: eventsDetails(events[day][i]), height=1,width=1,background="gray")
            event_button.grid(row=i, column=1, padx=10, pady=5)
            event_label.grid(row=i, column=2)
    else :
        event_label = Label(day_events_window, text="No events for this day", bg=color_bg,font=('Arial',11, BOLD))
        event_label.pack()
def previous_month():
    global dt
    for widget in days_frame.winfo_children():
        widget.destroy()
    update_month(labelMonth,-1)
    create_day_boxes(days_frame,dt)

def next_month():
    global dt
    for widget in days_frame.winfo_children():
        widget.destroy()
    update_month(labelMonth,1)
    create_day_boxes(days_frame,dt)

def update_month(label,add):
    global dt
    dt = dt.add(months=add)
    label.config(text=dt.format("MMMM YYYY"))
    
def events_of_month(events, month, year):
    result = []
    for event in events:

        if (event[2].date().month == month and event[2].date().year==year) or(event[3].date().month == month and event[3].date().year==year):
            if event[2].date() != event[3].date():
                for h in range(event[2].date().day,event[3].date().day+1):
                    result.append([event, datetime(year,month,h)])
            else:
                result.append([event, event[2].date()])
    
    return result

def change_color():
    global color_bg
    global color_bts
    global cycle_color
    cycle_color+=1
    if cycle_color==4:
        cycle_color=1
    if cycle_color==1:
        color_bg=color_bg1
        color_bts=color_bts1
    if cycle_color==2:
        color_bg=color_bg2
        color_bts=color_bts2
    if cycle_color==3:
        color_bg=color_bg3
        color_bts=color_bts3
    refresh()

def refresh():
    global persEvents, persID, DBevents, cursor
    global Liste_des_liaisons_groupes, Liste_des_groupes, labelMonth
    global frame1, frame2, frame3

    cnx = MC.connect(user='289285', password='BDDaccess3!', host='mysql-bdd-isen-planning.alwaysdata.net', database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req2 = str("SELECT * FROM EVENTS")
    cursor.execute(req2)
    DBevents = cursor.fetchall()
    getEvents()

    req = 'SELECT * FROM PARTICIPE_GROUPES'
    cursor.execute(req)
    Liste_des_liaisons_groupes = cursor.fetchall()

    req = 'SELECT * FROM GROUPES'
    cursor.execute(req)
    Liste_des_groupes = cursor.fetchall()

    getEventsCPG()

    for widget in days_frame.winfo_children():
        widget.destroy()

    create_day_boxes(days_frame, dt)

    next_month_button.update_color()
    previous_month_button.update_color()
    refresh_button.update_color()
    change_color_button.update_color()
    dsCPG2_button.update_color()
    dsCPG1_button.update_color()

    labelMonth.config(bg=color_bg)
    frame1.config(bg=color_bg)
    frame2.config(bg=color_bg)
    frame3.config(bg=color_bg)

    frame1.update_idletasks()
    frame2.update_idletasks()
    frame3.update_idletasks()

    cnx.close()

    
def getEventsCPG():
    global eventsCPG1
    global eventsCPG2
    eventsCPG1 = []
    eventsCPG2 = []
    for ev in Liste_des_liaisons_groupes:
        if ev[2] in [1,3,4,5,100]:
            eventsCPG2.append(ev[1])
        if ev[2] in [2,3,4,5,100]:
            eventsCPG1.append(ev[1])
    for numerocpg in range(len(eventsCPG1)):
        for ev in range(len(DBevents)):
            if DBevents[ev][0] == eventsCPG1[numerocpg]:
                eventsCPG1[numerocpg] = DBevents[ev]
    for numerocpg in range(len(eventsCPG2)):
        for ev in range(len(DBevents)):
            if DBevents[ev][0] == eventsCPG2[numerocpg]:
                eventsCPG2[numerocpg] = DBevents[ev]
    #print("events CPG1 = ",eventsCPG1)
    #print("events CPG2 = ",eventsCPG2)

def getEvents():

    global persEvents
    persEvents = []

    if perms == 2:
        persEvents=DBevents
        return


    #print("persID=",persID,persCat)
    req = "SELECT EventID FROM EVENTS INNER JOIN PARTICIPE ON EventID=PARTICIPE.EventID_ext WHERE PersID_ext = %s"
    cursor.execute(req, (str(persID),))
    Y = cursor.fetchall()
    for i in range(len(Y)):
        Y[i]=Y[i][0]
    #print("Y=",Y)

    req = "SELECT EventID FROM EVENTS INNER JOIN PARTICIPE_GROUPES ON EventID=PARTICIPE_GROUPES.EventID_ext INNER JOIN GROUPES ON PARTICIPE_GROUPES.ClasseID_ext=GROUPES.ClasseID INNER JOIN APPARTENIR ON ClasseID=APPARTENIR.Goupe_ID_ext WHERE APPARTENIR.PersID_A_ext = %s"
    cursor.execute(req, (str(persID),))
    Z = cursor.fetchall()
    for i in range(len(Z)):
        Z[i]=Z[i][0]
    #print("Z=",Z)

    
    for i in range(len(DBevents)):
        if DBevents[i][0] in Y or DBevents[i][0] in Z:
            persEvents.append(DBevents[i])
    #print("persEvents=",persEvents)
    

#* Exploitation                                                                             

cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

cursor = cnx.cursor()
req = 'SELECT * FROM PERSONNES'
cursor.execute(req)
L = cursor.fetchall()
#print(L)




req='SELECT * FROM SALLE'
cursor.execute(req)
Liste_des_salles = cursor.fetchall()

req='SELECT * FROM PARTICIPE_GROUPES'
cursor.execute(req)
Liste_des_liaisons_groupes = cursor.fetchall()

req='SELECT * FROM GROUPES'
cursor.execute(req)
Liste_des_groupes = cursor.fetchall()

req='SELECT * FROM APPARTENIR'
cursor.execute(req)
Liste_des_liaisons_appartenir = cursor.fetchall()

j="'2023-03-01'"
req2=str("SELECT * FROM EVENTS")
cursor.execute(req2)
DBevents = cursor.fetchall()
a=[]



#- colors

# background color
code_color_r_1, code_color_g_1, code_color_b_1 = 200,250,200
color_bg1='#%02x%02x%02x' % (code_color_r_1, code_color_g_1, code_color_b_1)
code_color_r_1, code_color_g_1, code_color_b_1 = 250,200,200
color_bg2='#%02x%02x%02x' % (code_color_r_1, code_color_g_1, code_color_b_1)
code_color_r_1, code_color_g_1, code_color_b_1 = 200,200,250
color_bg3='#%02x%02x%02x' % (code_color_r_1, code_color_g_1, code_color_b_1)
color_bg=color_bg1
cycle_color = 1



# button color
code_color_r_2, code_color_g_2, code_color_b_2 = 150,255,150
color_bts1='#%02x%02x%02x' % (code_color_r_2, code_color_g_2, code_color_b_2)
code_color_r_2, code_color_g_2, code_color_b_2 = 255,150,150
color_bts2='#%02x%02x%02x' % (code_color_r_2, code_color_g_2, code_color_b_2)
code_color_r_2, code_color_g_2, code_color_b_2 = 150,150,255
color_bts3='#%02x%02x%02x' % (code_color_r_2, code_color_g_2, code_color_b_2)
color_bts=color_bts1








lancer1 = False
Co = Tk()
Co.title('Connexion')
setup2()
Co.geometry("+600+350")
Co.config(bg=color_bg)
Co.mainloop()
if lancer1 :
    
    
    defPerms()
    #print("perms=",perms)
    #print(persCat,'ICIIIIIIIIIIIIIIIIIIIIII')
    if persCat == 2:
        persClasses = []
        #print('                                 eded    ',Liste_des_liaisons_appartenir)
        for i in range(len(Liste_des_liaisons_appartenir)):
            if Liste_des_liaisons_appartenir[i][1] == persID:
                persClasses += [Liste_des_liaisons_appartenir[i][2]]
    else :
        persClasses = [1,2]


    getEventsCPG()
    getEvents()
    #print(persEvents)



    


    


    fenetre = Tk()
    fenetre.title('planning')
    fenetre.config(bg=color_bg)
    fenetreHeight = 950
    fenetreWidth = 1800
    fenetre.geometry("{}x{}+50+50".format(fenetreWidth, fenetreHeight))
    fenetre.attributes('-fullscreen', False)
    fenetre.resizable(width=False, height=False)

    fenetre.update()

    notebook = ttk.Notebook(fenetre)
    notebook.grid(row=0,column=0, sticky= 'NW')
    
    # create frames

    frame1= Frame(notebook, width=fenetreWidth, height=fenetreHeight, bg=color_bg)
    frame2= Frame(notebook, width=fenetreWidth, height=fenetreHeight, bg=color_bg)
    frame3= Frame(notebook, width=fenetreWidth, height=fenetreHeight, bg=color_bg)   
    
    # add frames to notebook

    notebook.add(frame1, text='Planning')
    if perms == 2:
        notebook.add(frame2, text='Ajouter un événement')
    notebook.add(frame3, text='Planning des DS')
    
    count=0
    
    global count1
    req = 'SELECT EventID FROM EVENTS'
    cursor.execute(req)
    G = cursor.fetchall()
    for i in range(len(G)):
        G[i]=G[i][0]
    count1=max(G)
    global countPG
    req = 'SELECT ParticipeID_g FROM PARTICIPE_GROUPES'
    cursor.execute(req)
    G = cursor.fetchall()
    for i in range(len(G)):
        G[i]=G[i][0]
    countPG=max(G)
    req = 'SELECT ParticipeID FROM PARTICIPE'
    cursor.execute(req)
    G = cursor.fetchall()
    for i in range(len(G)):
        G[i]=G[i][0]
    countP=max(G)

    widthF = fenetre.winfo_width()
    heightF = fenetre.winfo_height()
    placementF = (widthF-1250)/2
    pixel = PhotoImage(width=1, height=1)
    
    count2=0
    #print("countPG=",countPG)
    #print(G)
    dt = pendulum.now() 

    style1=ttk.Style()
    style1.configure("Treeview.Heading", font=(None, 20))
  



    
    labelMonth = Label(frame1, text=dt.format("MMMM YYYY"),font=("Helvetica", 23,'bold'), background=color_bg, foreground='grey')
    labelMonth.place(x=fenetreWidth/2-92,y=10)
    
    
    

    days_frame = ttk.Frame(frame1, width=250, height=200)
    days_frame.grid(row=0, column=0, padx=fenetreWidth/2-655, pady=fenetreHeight/2-420)

    update_month(labelMonth,0)
    create_day_boxes(days_frame,dt)
    
    next_month_button = button_frame(frame1, "Next Month", next_month, (fenetreWidth-180,350),(15,1))
    previous_month_button = button_frame(frame1, "Previous Month", previous_month, (60,350),(15,1)) 
    refresh_button = button_frame(frame1, "Refresh", refresh, (30,20),(15,1))
    change_color_button = button_frame(frame1, "", change_color, (5,20),(1,1))

    dsCPG2_button =  button_frame(frame3, "CPG2", tableau_cpg2, (0,30),(10,1))
    dsCPG1_button = button_frame(frame3, "CPG1", tableau_cpg1, (0,0),(10,1))


    

    cnx.close()

    setup()
    fenetre.mainloop()

