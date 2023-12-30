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

def classeget():
    b=-1
    a=(Classeb.get(),)
    cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = 'SELECT ClasseID FROM GROUPES'
    cursor.execute(req)
    L = cursor.fetchall()
    req = 'SELECT Nom FROM GROUPES'
    cursor.execute(req)
    L2 = cursor.fetchall()
    for i in L2:
        b+=1
        if i==a:
            a=L[b][0]    
    cnx.close()
    return(a)
            

    

def setup():

    Quitter = Button(fenetre,text='Quitter',command=Quitter2)
    Quitter.place(x=widthF-100,y=heightF-100)


    fenetre.bind("<Key>", f)


    deroulant= Frame(fenetre)
    deroulant.place(x=0,y=0)
    ajouter_f = Frame(fenetre)
    ajouter_f.place(x=50,y=fenetreHeight-150)
    #etiquettes
    global Titre
    Titre=Label(ajouter_f,text='Titre')
    Titre.grid(row=0, column=0)
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
    Debut.grid_forget(), Fin.grid_forget(),Titre.grid_forget(),Categorie.grid_forget(),Salle.grid_forget(),Classe.grid_forget(),Classeb.grid_forget(),Description.grid_forget(), Debutb.grid_forget(), Finb.grid_forget(),Salleb.grid_forget(),Categorieb.grid_forget(), Titreb.grid_forget(),Descriptionb.grid_forget()
    menuDeroulant = Menubutton(deroulant, text='Menu', width='20', borderwidth=2, bg='gray', activebackground='green',relief = RAISED)
    menuDeroulant.grid()
    menuDeroulant1 = Menu(menuDeroulant)
    if perms > 0 :
        menuDeroulant1.add_command(label='Ajouter un événement', command = Ajouter_cours)
    menuDeroulant1.add_command(label='Planning de DS', command = planning_ds)

    # Attribution du menu déroulant au menu Affichage

    menuDeroulant.configure(menu=menuDeroulant1)


    


#menu déroulant
def ajouter_event():
    global count1
    cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
    cursor = cnx.cursor()
    req = "INSERT INTO EVENTS (EventID, Titre, Date_debut, Date_fin, Categorie, Reserve, Description, Salle_ID_ext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    infos = (count1, Titreb.get(), Debutb.get(), Finb.get(), Categorieb.get(), False, Descriptionb.get(), classeget())
    cursor.execute(req,infos)
    cnx.commit()
    cnx.close()
    count1+=1
    Titreb.delete(0, END)
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
        Titre.grid(row=1, column=4),Debut.grid(row=1, column=6),Fin.grid(row=1, column=7),Categorie.grid(row=1, column=8),Salle.grid(row=1, column=9),Classe.grid(row=1, column=10),Description.grid(row=1, column=11),Debutb.grid(row=2, column=6),Finb.grid(row=2, column=7),Titreb.grid(row=2, column=4),Categorieb.grid(row=2, column=8),Salleb.grid(row=2, column=9),Classeb.grid(row=2, column=10),Descriptionb.grid(row=2, column=11)
        #bouton retour qui s'efface lui et les étiquettes
        Ajouter_event = Button(fenetre, text="ajouter l'événement", command =ajouter_event)
        Ajouter_event.place(x=50,y=fenetreHeight-80)
        Retour = Button(fenetre, text='Retour', command = lambda : [Ajouter_event.place_forget(),Titre.grid_forget(),Classe.grid_forget(),Classeb.grid_forget(),Titreb.grid_forget(),Categorie.grid_forget(),Categorieb.grid_forget(),Description.grid_forget(),Descriptionb.grid_forget(),Salle.grid_forget(),Salleb.grid_forget(),Titre.grid_forget(),Retour.place_forget(),compte(), Debut.grid_forget(), Fin.grid_forget(), Debutb.grid_forget(), Finb.grid_forget()])
        Retour.place(x=50,y=fenetreHeight-50)





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






def setup2():
    global v,v2,e,e2


    v = StringVar()   #importation de la zone de saisie StringVar
    v2 = StringVar()
    e = Entry(Co, textvariable=v, width=50, fg="black")
    e2 = Entry(Co, textvariable=v2, width=50, fg="black")
    e.pack(),e2.pack()    #insertion de la zone de saisie
    Button(Co, text="Annuler", command = Co.destroy).pack(side=LEFT)
    Button(Co, text="Valider", command = verification).pack(side=RIGHT)
    
    Co.bind('<Return>',verification)


def verification(*a):
    global lancer1
    global persID
    global persCat
    for i in range (len(L)):
        if e.get() == L[i][2] and e2.get()==L[i][4]:
            lancer1=True
            persID=i
            persCat=L[persID][5]
            Co.destroy()
   

    if lancer1==False:
        champ_label = Label(Co, text="Identifiants incorrects !!!",background="red")
        champ_label.pack()
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

    events_of_month1=events_of_month(DBevents,current_month,current_year)

    events = [[] for _ in range(nb_jours)]
    for i in events_of_month1:
        i[1]=i[1].day
 
        events[i[1]-1]+=[i[0]]

    # Récupération du jour actuel
    
    
    
    # Boucle pour créer les cases de chaque jour

    for i in range(nb_jours):   
        day_box = ttk.Frame(parent)
        day_box.grid(row=i//7, column=i%7)
        # Récupération du nom du jour
        day_name = datetime.strftime(datetime(current_year, current_month, i+1), '%A')
        # Ajout d'un bouton pour chaque case
        if len(events[i])==0:
            color='#888888'
        else:
            if a*len(events[i])>240:
                color='#%02x%02x%02x' % (255,0,0)
            else:
                color='#%02x%02x%02x' % (255,240-(a*len(events[i])),0)
        button = Button(day_box, text="{} {}".format(day_name, i+1),font=('Arial',7), activebackground='green',anchor="n", command=lambda day=i+1: show_day_events(day, events), background=color,width=20,height=8)
        button_text = button.cget("text")
        for j in range(len(events[i])):
            button_text+="\n"+events[i][j][1]
        button.config(text=button_text)
        button.pack()
    
def eventsDetails(event):
    event_details_window = Toplevel(fenetre)
    event_details_window.title("Event details")
    event_details_window.geometry("400x300+550+300")
    # Ajout d'un label pour afficher les événements
    for i in range(len(event)):

        event_label = ttk.Label(event_details_window, text=event[i])
        event_label.place(x=10,y=10+30*i)

def show_day_events(day, events):
    day-=1
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



#* Exploitation                                                                             

cnx = MC.connect(user='289285_eleve', password='BDDaccesseleve',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')

cursor = cnx.cursor()
req = 'SELECT * FROM PERSONNES'
cursor.execute(req)
L = cursor.fetchall()



j="'2023-03-01'"
req2=str("SELECT * FROM EVENTS")

cursor.execute(req2)
DBevents = cursor.fetchall()





lancer1 = False
Co = Tk()
Co.title('Connexion')
setup2()
Co.geometry("300x100+600+350")
Co.mainloop()
if lancer1 :

    defPerms()

    fenetre = Tk()
    fenetre.title('planning')
    fenetreHeight = 900
    fenetreWidth = 1400
    fenetre.geometry("{}x{}+50+50".format(fenetreWidth, fenetreHeight))
    fenetre.attributes('-fullscreen', False)
    fenetre.resizable(width=False, height=False)

    fenetre.update()

    #- variables                        
    count=0
   
    global count1
    req = 'SELECT EventID FROM EVENTS'
    cursor.execute(req)
    G = cursor.fetchall()
    count1=G[-1][0]+1
    widthF = fenetre.winfo_width()
    heightF = fenetre.winfo_height()
    placementF = (widthF-1250)/2
    pixel = PhotoImage(width=1, height=1)
    color='#B1FF7D'
    count2=0

    dt = pendulum.now()



    print(persID)
    print(L[persID][1],L[persID][2])
    print(persCat)





    labelMonth = Label(fenetre, text=dt.format("MMMM YYYY"),font=("Helvetica", 20))
    labelMonth.place(x=fenetreWidth/2-100,y=50)
    
    update_month(labelMonth,0)
    

    days_frame = ttk.Frame(fenetre, width=250, height=200)
    days_frame.grid(row=0, column=0, padx=fenetreWidth/2-450, pady=fenetreHeight/2-350)

    create_day_boxes(days_frame,dt)
    next_month_button = Button(fenetre, text="Next Month", command=next_month, width=15, background='#228822')
    previous_month_button = Button(fenetre, text="Previous Month", command=previous_month, width=15, background='#228822')

    next_month_button.place(x=fenetreWidth-180,y=350)
    previous_month_button.place(x=60,y=350)

    





    setup()
    fenetre.mainloop()

#-pour delete une ligne
# import mysql.connector as MC
# cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
# cursor = cnx.cursor()
# req = "DELETE FROM EVENTS WHERE EventID=5"
# cursor.execute(req)
# cnx.commit()
# cnx.close()