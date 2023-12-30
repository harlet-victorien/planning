from tkinter import *
import mysql.connector as MC
import pandas as pd
def jj():
    req='SELECT * FROM PERSONNES '
    cursor.execute(req)
    L=cursor.fetchall()
    for i in range (len(L)):
        L[i]=L[i][0]
    x=max(L)+1
    df = pd.read_excel(r'C:\Users\V\Desktop\donnees.xlsx')
    data = df.values.tolist()
    for i,k in enumerate(data):
        req1 = "INSERT INTO PERSONNES (PersID, Nom, prenom, email, mot_de_passe, CategorieID_ext) VALUES (%s, %s, %s, %s, %s, %s)"
        infos =(x+i,k[0],k[1],str(k[1])+'.'+str(k[0])+'@junia.student.com',k[3],1)
        cursor.execute(req1,infos)
        cnx.commit()
cnx = MC.connect(user='289285', password='BDDaccess3!',host='mysql-bdd-isen-planning.alwaysdata.net',database='bdd-isen-planning_2')
cursor = cnx.cursor()
Co = Tk()
Co.title('Entrée de données')
Co.geometry("600x100+600+350")
Co.config(bg='LIGHT BLUE')
Label(text='Insérez un ficher "donnees.xslx" dans le dossier du programme puis appuyez sur le bouton').pack()
Button(command=jj,width=10,bg='blue',text='Lancer').pack()
Co.mainloop()