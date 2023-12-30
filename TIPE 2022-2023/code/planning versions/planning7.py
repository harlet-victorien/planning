from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import *
import mysql.connector as MC
import random as r
from datetime import datetime
import calendar
import pendulum


#* Fonctions                                                                                                    


def f(event):
    if event.keysym == "c":
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        fenetre.config(bg=color_bg)


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
        

        if int(len(L[i]))==5:
            tableau.insert('', 'end', iid=Count(), values=('',L[i][0],L[i][1], L[i][2], L[i][3],L[i][4]))
        else:
            tableau.insert('', 'end', iid=Count(), values=('',L[i][0],L[i][1], L[i][2], L[i][3],L[i][4], L[i][5], L[i][6]))
#on crée la fonction qui va permettre de créer un tableau avec les données de la base de données en reprenant les ds de tous les persEvents

def tableau_ds_pers():
    tableau = ttk.Treeview(fenetre_planning, columns=('Date','Horaire','Matière','Salle'),show = 'headings')
    tableau.column('Date',width=150,anchor=CENTER)
    tableau.column('Horaire',width=150,anchor=CENTER)
    tableau.column('Matière',width=150,anchor=CENTER)
    tableau.column('Salle',width=150,anchor=CENTER)

    tableau.heading('Date', text='Date ',anchor=CENTER)
    tableau.heading('Horaire', text='Horaire ',anchor=CENTER)
    tableau.heading('Matière', text='Matière ',anchor=CENTER)
    tableau.heading('Salle', text='Salle ',anchor=CENTER)

    tableau.place(x=50,y=50)
    for i in range(len(persEvents)):
        if 'DS' in persEvents[i][4] or 'ds' in persEvents[i][4] or 'Ds' in persEvents[i][4]:
            for j in range(len(Liste_des_salles)):
                 if Liste_des_salles[i][0]==persEvents[i][7]:
                    yu=Liste_des_salles[i][1]
                    text_date=str(persEvents[i][2])
                    text_date=text_date[8:10]+'/'+text_date[5:7]+'/'+text_date[0:4]
                    text_heure=str(persEvents[i][2])
                    text_heure=text_heure[11:16]
            tableau.insert('', 'end', iid=Count(), values=(text_date, text_heure, persEvents[i][1], yu))


def compte():
    global count
    count=0

def salleget():
    b=-1
    a=(Salleb.get(),)
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
        print(a)
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
            print(i,j)
            if i==j[0]:
                print('là')
                req = "INSERT INTO PARTICIPE (ParticipeID, EventID_ext, PersID_ext) VALUES (%s, %s, %s)"
                infos = (countP, count1, k+1)
                cursor.execute(req,infos)
                cnx.commit()
                countP+=1
            
    a=[]

def entries(window):
    if window==fenetre:
        ajouter_f = Frame(window,bg=color_bg)
        ajouter_f.place(x=50,y=fenetreHeight-150)
        #etiquettes
        global Titre
        Titre=Label(ajouter_f,text='Titre',bg=color_bg)
        Titre.grid(row=0, column=0)
        global Debut
        Debut=Label(ajouter_f,text='Debut',bg=color_bg)
        Debut.grid(row=0, column=2)
        global Fin
        Fin=Label(ajouter_f,text='Fin',bg=color_bg)
        Fin.grid(row=0, column=3)
        global Categorie
        Categorie=Label(ajouter_f,text='Categorie',bg=color_bg)
        Categorie.grid(row=0, column=4)
        global Salle
        Salle=Label(ajouter_f,text='Salle',bg=color_bg)
        Salle.grid(row=0, column=5)
        global Description
        Description=Label(ajouter_f,text='Description',bg=color_bg)
        Description.grid(row=0, column=6)

        #cases pour boutons
        global Titreb
        Titreb=Entry(ajouter_f)
        Titreb.grid(row=1, column=0)
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
        global Descriptionb
        Descriptionb=Entry(ajouter_f)
        Descriptionb.grid(row=1, column=6)
    else:
        ajouter_f = Frame(window,bg=color_bg)
        ajouter_f.place(x=10,y=300)
        Titre2=Label(ajouter_f,text='Titre',bg=color_bg)
        Titre2.grid(row=0, column=0)
        Debut2=Label(ajouter_f,text='Debut',bg=color_bg)
        Debut2.grid(row=0, column=2)
        Fin2=Label(ajouter_f,text='Fin',bg=color_bg)
        Fin2.grid(row=0, column=3)
        Categorie2=Label(ajouter_f,text='Categorie',bg=color_bg)
        Categorie2.grid(row=0, column=4)
        Salle2=Label(ajouter_f,text='Salle',bg=color_bg)
        Salle2.grid(row=0, column=5)
        Description2=Label(ajouter_f,text='Description',bg=color_bg)
        Description2.grid(row=0, column=6)

        #cases pour boutons
        global Titreb2
        Titreb2=Entry(ajouter_f)
        Titreb2.grid(row=1, column=0)
        global Debutb2
        Debutb2=Entry(ajouter_f)
        Debutb2.grid(row=1, column=2)
        global Finb2
        Finb2=Entry(ajouter_f)
        Finb2.grid(row=1, column=3)
        global Categorieb2
        Categorieb2=Entry(ajouter_f)
        Categorieb2.grid(row=1, column=4)
        global Salleb2
        Salleb2=Entry(ajouter_f)
        Salleb2.grid(row=1, column=5)
        global Descriptionb2
        Descriptionb2=Entry(ajouter_f)
        Descriptionb2.grid(row=1, column=6)

def setup():

    entries(fenetre)
    Quitter = Button(fenetre,text='Quitter',command=Quitter2, background=color_bts,font=("Helvetica", "10", "bold"))
    Quitter.place(x=widthF-100,y=heightF-100)
    deroulant= Frame(fenetre)
    deroulant.place(x=0,y=0)

    fenetre.bind("<Key>", f)


    
    Debut.grid_forget(), Fin.grid_forget(),Titre.grid_forget(),Categorie.grid_forget(),Salle.grid_forget(),Description.grid_forget(), Debutb.grid_forget(), Finb.grid_forget(),Salleb.grid_forget(),Categorieb.grid_forget(), Titreb.grid_forget(),Descriptionb.grid_forget()
    menuDeroulant = Menubutton(deroulant, text='Menu', width='20', borderwidth=2, bg='LIGHTGREY', activebackground=color_bts,relief = RAISED, font=("Helvetica", "10", "bold"))
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    if perms > 0 :
        menuDeroulant1.add_command(label='Ajouter un événement', command = Ajouter_cours)
    menuDeroulant1.add_command(label='Planning de DS', command = planning_ds)
    menuDeroulant1.add_command(label='Refresh', command = refresh)

    # Attribution du menu déroulant au menu Affichage

    menuDeroulant.configure(menu=menuDeroulant1)


    


#menu déroulant
def ajouter_event():
    global count1
    global countPG
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    count1+=1
    countPG+=1
    req = "INSERT INTO EVENTS (EventID, Titre, Date_debut, Date_fin, Categorie, Reserve, Description, Salle_ID_ext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    infos = (count1, Titreb.get(), Debutb.get(), Finb.get(), Categorieb.get(), salle_check, Descriptionb.get(), salleget())
    cursor.execute(req,infos)
    cnx.commit()
    req = 'SELECT Nom FROM GROUPES'
    cursor.execute(req)
    L = cursor.fetchall()
    for k,j in enumerate(L):
        print(k,j)
        if selected_groupe.get()==j[0]:
            M=k+1
            print(M)
            
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
    Titreb.delete(0, END)
    Finb.delete(0, END)
    Debutb.delete(0, END)
    Descriptionb.delete(0, END)
    Salleb.delete(0, END)
    Categorieb.delete(0, END)

def Ajouter_cours():
    global selected_groupe
    global count
    if count ==0:
        global personnesb
        count=1
        groupes_event = Toplevel(fenetre)
        groupes_event.title("groupes événement")
        groupes_event.geometry("400x500+950+400")
        
        personnes_frame = Frame(groupes_event)
        personnes_frame = Frame(groupes_event)
        personnes_frame.place(x=250,y=20)
        cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
        cursor = cnx.cursor()
        req ="SELECT NOM FROM GROUPES"
        cursor.execute(req)
        A=cursor.fetchall()
        selected_groupe = StringVar()
        month_cb = ttk.Combobox(groupes_event, textvariable=selected_groupe)

        # get first 3 letters of every month name
        month_cb['values'] = A
        print(month_cb)
        month_cb['state']='readonly'
        # place the widget
        month_cb.place(x=15,y=20)
        month_cb.bind('<<ComboboxSelected>>') 
        global salle_check
        salle_check = IntVar()
        Checkbutton(groupes_event,text='salle réservée ', variable = salle_check,onvalue = 1, offvalue = 0,command= lambda :[print(salle_check,bool(salle_check))]).place(x=250,y=133)
        personnes=Label(personnes_frame,text='ajouter une personne',)
        personnes.grid(row=0, column=0)
        personnesb=Entry(personnes_frame)
        personnesb.grid(row=1,column=0)
        Button(groupes_event,text='ajouter la personne',command=ajouter_personne).place(x=250,y=70)
        Titre.grid(row=1, column=4),Debut.grid(row=1, column=6),Fin.grid(row=1, column=7),Categorie.grid(row=1, column=8),Salle.grid(row=1, column=9),Description.grid(row=1, column=11),Debutb.grid(row=2, column=6),Finb.grid(row=2, column=7),Titreb.grid(row=2, column=4),Categorieb.grid(row=2, column=8),Salleb.grid(row=2, column=9),Descriptionb.grid(row=2, column=11)
        #bouton retour qui s'efface lui et les étiquettes
        Ajouter_event = Button(fenetre, text="ajouter l'événement", command =ajouter_event, bg=color_bts)
        Ajouter_event.place(x=50,y=fenetreHeight-80)
        Retour = Button(fenetre, text='Retour',bg=color_bts, command = lambda : [groupes_event.destroy(),Ajouter_event.place_forget(),Titre.grid_forget(),Titreb.grid_forget(),Categorie.grid_forget(),Categorieb.grid_forget(),Description.grid_forget(),Descriptionb.grid_forget(),Salle.grid_forget(),Salleb.grid_forget(),Titre.grid_forget(),Retour.place_forget(),compte(), Debut.grid_forget(), Fin.grid_forget(), Debutb.grid_forget(), Finb.grid_forget(),])
        Retour.place(x=50,y=fenetreHeight-50)





def Quitter3():
    fenetre_planning.destroy()

def planning_ds():
    global fenetre_planning
    fenetre_planning =Tk()
    fenetre_planning.title('Planning DS')
    fenetre_planning.geometry('1400x600')
    fenetre_planning.config(background=color_bg)
    Menu_planning = Frame(fenetre_planning)
    Menu_planning.place(x=0,y=0)

    Quitter = Button(fenetre_planning,text='Quitter',command=Quitter3, background=color_bts, font=("Helvetica", "10", "bold"))
    Quitter.place(x=1280,y=550)
    menuDeroulant = Menubutton(Menu_planning, text='Menu', width='20', borderwidth=2, bg='LIGHTGREY', activebackground=color_bts,relief = RAISED)
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    menuDeroulant1.add_command(label='Planning DS personnel', command = tableau_ds_pers)
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
    print("xqsdq",L)
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
    print(first_day)
    
    
    # Boucle pour créer les cases de chaque jour
    day_box = Frame(parent,bg=color_bg)
        
    day_box.grid(row=nb_jours//7, column=nb_jours%7)
    for i in range(nb_jours):   
        
        # Récupération du nom du jour
        day_name = datetime.strftime(datetime(current_year, current_month, i+1), '%A')
        # Ajout d'un bouton pour chaque case
        if len(events[i])==0:
            color=color_bg
            color='#%02x%02x%02x' % (code_color_r_1+(255-code_color_r_1)//2, code_color_g_1+(255-code_color_g_1)//2, code_color_b_1+(255-code_color_b_1)//2)
            
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
    entries(event_details_window)
    # Ajout d'un label pour afficher les événements
    event_label = ttk.Label(event_details_window, text='Titre: '+event[1],font=('Arial',11, BOLD))
    event_label.place(x=10,y=10)
    event_label = ttk.Label(event_details_window, text='Date de début: '+str(event[2]),font=('Arial',11, BOLD))
    event_label.place(x=10,y=40)
    event_label = ttk.Label(event_details_window, text='Date de fin: '+str(event[3]),font=('Arial',11, BOLD))
    event_label.place(x=10,y=70)
    event_label = ttk.Label(event_details_window, text='Catégorie: '+event[4],font=('Arial',11, BOLD))
    event_label.place(x=10,y=100)
    if event[5]==False:
        event_label = ttk.Label(event_details_window, text='Réservé: non',font=('Arial',11, BOLD))
    else :
        event_label = ttk.Label(event_details_window, text='Réservé: oui',font=('Arial',11, BOLD))
    event_label.place(x=10,y=130)
    event_label = ttk.Label(event_details_window, text='Description: '+event[6],font=('Arial',11, BOLD))
    event_label.place(x=10,y=160)
    for i in range(len(Liste_des_salles)):
        if Liste_des_salles[i][0]==event[7]:
            event_label = ttk.Label(event_details_window, text='Lieu: '+Liste_des_salles[i][1],font=('Arial',11, BOLD))
    event_label.place(x=10,y=190)
    a=''
    print(Liste_des_liaisons_groupes,event)
    for i in range(len(Liste_des_liaisons_groupes)):
        if Liste_des_liaisons_groupes[i][1]==event[0]:
            for j in range(len(Liste_des_groupes)):
                if Liste_des_groupes[j][0]==Liste_des_liaisons_groupes[i][2]:
                    a+=Liste_des_groupes[j][1]+'  '
    event_label = ttk.Label(event_details_window, text='Groupe: '+a,font=('Arial',11, BOLD))
    event_label.place(x=10,y=220)

    """ for i in range(1,len(event)):

        event_label = ttk.Label(event_details_window, text=event[i])
        event_label.place(x=10,y=10+30*i) """
    #bouton pour supprimer l'event
    if perms>=1:
        Button(event_details_window, text="Delete", command = lambda: [supprimerEvent(event[0]),event_details_window.destroy()],background=color_bts).place(x=300,y=450)
        Button(event_details_window, text="Modify", command = lambda: [modifierEvent(event[0]),day_events_window.destroy(),event_details_window.destroy()],background=color_bts).place(x=50,y=450)

def supprimerEvent(eventID):
    print(eventID)
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
    id=str(eventID)
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    cursor.execute("UPDATE EVENTS SET Titre= '%s', Date_debut= '%s', Date_fin= '%s', Categorie = '%s', Description=' %s' WHERE EventID=%s" % (Titreb2.get(),Debutb2.get(), Finb2.get(), Categorieb2.get(), Descriptionb2.get(),id))
    cnx.commit()
    refresh()
    Titreb2.delete(0, END)
    Finb2.delete(0, END)
    Debutb2.delete(0, END)
    Descriptionb2.delete(0, END)
    Salleb2.delete(0, END)
    Categorieb2.delete(0, END)
    cnx.close()

def show_day_events(day, events):
    day-=1
    global day_events_window
    day_events_window = Toplevel(fenetre)
    day_events_window.title("Events for day {}".format(day+1))
    day_events_window.geometry("300x300+600+250")
    # Ajout d'un label pour afficher les événements
    
    if len(events[day])>=1:
        box = ttk.Frame(day_events_window)
        box.grid(row=len(events[day]), column=2)
        for i in range(len(events[day])):
            event_label = ttk.Label(day_events_window, text=events[day][i][1])
            event_button = Button(day_events_window, command=lambda: eventsDetails(events[day][i]), height=1,width=1,background="gray")
            event_button.grid(row=i, column=1, padx=10, pady=5)
            event_label.grid(row=i, column=2)
    else :
        event_label = ttk.Label(day_events_window, text="No events for this day")
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

def refresh():
    global persEvents
    global persID
    global DBevents
    global cursor
    global Liste_des_liaisons_groupes
    global Liste_des_groupes
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

    cursor = cnx.cursor()
    req2=str("SELECT * FROM EVENTS")

    cursor.execute(req2)
    DBevents = cursor.fetchall()
    getEvents()
    req='SELECT * FROM PARTICIPE_GROUPES'
    cursor.execute(req)
    Liste_des_liaisons_groupes = cursor.fetchall()
    req='SELECT * FROM GROUPES'
    cursor.execute(req)
    Liste_des_groupes = cursor.fetchall()
    for widget in days_frame.winfo_children():
        widget.destroy()
    create_day_boxes(days_frame,dt)

    cnx.close()
    


def getEvents():

    global persEvents
    persEvents = []

    if perms == 2:
        persEvents=DBevents
        return


    print("persID=",persID,persCat)
    req = "SELECT EventID FROM EVENTS INNER JOIN PARTICIPE ON EventID=PARTICIPE.EventID_ext WHERE PersID_ext = %s"
    cursor.execute(req, (str(persID),))
    Y = cursor.fetchall()
    for i in range(len(Y)):
        Y[i]=Y[i][0]
    print("Y=",Y)

    req = "SELECT EventID FROM EVENTS INNER JOIN PARTICIPE_GROUPES ON EventID=PARTICIPE_GROUPES.EventID_ext INNER JOIN GROUPES ON PARTICIPE_GROUPES.ClasseID_ext=GROUPES.ClasseID INNER JOIN APPARTENIR ON ClasseID=APPARTENIR.Goupe_ID_ext WHERE APPARTENIR.PersID_A_ext = %s"
    cursor.execute(req, (str(persID),))
    Z = cursor.fetchall()
    for i in range(len(Z)):
        Z[i]=Z[i][0]
    print("Z=",Z)

    
    for i in range(len(DBevents)):
        if DBevents[i][0] in Y or DBevents[i][0] in Z:
            persEvents.append(DBevents[i])
    print("persEvents=",persEvents)
    

#* Exploitation                                                                             

cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

cursor = cnx.cursor()
req = 'SELECT * FROM PERSONNES'
cursor.execute(req)
L = cursor.fetchall()
print(L)




req='SELECT * FROM SALLE'
cursor.execute(req)
Liste_des_salles = cursor.fetchall()

req='SELECT * FROM PARTICIPE_GROUPES'
cursor.execute(req)
Liste_des_liaisons_groupes = cursor.fetchall()

req='SELECT * FROM GROUPES'
cursor.execute(req)
Liste_des_groupes = cursor.fetchall()

j="'2023-03-01'"
req2=str("SELECT * FROM EVENTS")
cursor.execute(req2)
DBevents = cursor.fetchall()
a=[]



#- colors

# background color
code_color_r_1, code_color_g_1, code_color_b_1 = 200,250,203
color_bg='#%02x%02x%02x' % (code_color_r_1, code_color_g_1, code_color_b_1)

# button color
code_color_r_2, code_color_g_2, code_color_b_2 = 150,255,150
color_bts='#%02x%02x%02x' % (code_color_r_2, code_color_g_2, code_color_b_2)









lancer1 = False
Co = Tk()
Co.title('Connexion')
setup2()
Co.geometry("+600+350")
Co.config(bg=color_bg)
Co.mainloop()
if lancer1 :
    
    
    defPerms()
    print("perms=",perms)


    getEvents()
    print(persEvents)



    


    


    fenetre = Tk()
    fenetre.title('planning')
    fenetre.config(bg=color_bg)
    fenetreHeight = 950
    fenetreWidth = 1800
    fenetre.geometry("{}x{}+50+50".format(fenetreWidth, fenetreHeight))
    fenetre.attributes('-fullscreen', False)
    fenetre.resizable(width=False, height=False)

    fenetre.update()

    
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
    print("countPG=",countPG)
    print(G)
    dt = pendulum.now() 





    labelMonth = Label(fenetre, text=dt.format("MMMM YYYY"),font=("Helvetica", 20,'bold'), background=color_bg, foreground='grey')
    labelMonth.place(x=fenetreWidth/2-90,y=50)
    
    
    

    days_frame = ttk.Frame(fenetre, width=250, height=200)
    days_frame.grid(row=0, column=0, padx=fenetreWidth/2-655, pady=fenetreHeight/2-380)
    update_month(labelMonth,0)
    create_day_boxes(days_frame,dt)
    next_month_button = Button(fenetre, text="Next Month", command=next_month, width=15, background=color_bts,font=("Helvetica", 10,'bold'))
    previous_month_button = Button(fenetre, text="Previous Month", command=previous_month, width=15, background=color_bts,font=("Helvetica", 10,'bold'))

    next_month_button.place(x=fenetreWidth-180,y=350)
    previous_month_button.place(x=60,y=350)
    my_notebook= ttk.Notebook(fenetre)
    my_notebook.grid()
    #Create Tabs
    tab1= ttk.Frame(my_notebook)
    my_notebook.add(tab1, text= "Tab 1")
    tab2= ttk.Frame(my_notebook)
    my_notebook.add(tab2, text= "Tab2")

    



    cnx.close()

    setup()
    fenetre.mainloop()

