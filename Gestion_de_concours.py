from tkinter import *
from tkinter import messagebox
from enregostrement import run
pff=Tk()
pff.title("Concours")
pff.geometry("800x400")
pff.minsize(200,200)
pff.config(bg="#FED823")
#--------------------------------------------------------------------------------------------------------------
def admis():
    try:
        f=open("Concours.txt","r")
        contenu=f.readlines()
        f.close()
    except:
        contenu=[]
    fiche=open("Admis.txt","a")
    for i in contenu:
        sépare=i.split(";")
        if sépare[-1]=="admis\n":
            fiche.write(i)
    fiche.close()

def attente():
    try:
        atnt=open("Admis.txt","r")
        line=atnt.readlines()
        atnt.close()
    except:
        line=[]
    fichier=open("Attente.txt","a")
    for j in line:
        select=j.split(";")
        sage=select[-2]
        if int(sage)>=30:
            fichier.write(select[0]+";"+select[1]+";"+select[2]+"\n")
            fichier.close()

def statistiques():
    try:
        to=open("Concours.txt","r")
        tal=to.readlines()
        to.close()
    except:
        tal=[]
    total=len(tal)
    #----------------
    try:
        ad=open("Admis.txt","r")
        mis=ad.readlines()
        ad.close()
    except:
        mis=[]
    admis=len(mis)
    #----------------
    ref=0
    for l in tal:
        sep=l.split(";")
        if sep[-1]=="refuse\n":
            ref=+1
    #----------------
    jour=0
    for k in tal:
        rep=k.split(";")
        if rep[-1]=="ajourne\n":
            jour=+1
    if total == 0:
        stat = 0
        stat2 = 0
        stat3 = 0
    else:
        stat=(admis/total)*100
        stat2=(ref/total)*100
        stat3=(jour/total)*100
    admission=str(stat)+"%"
    refus=str(stat2)+"%"
    ajournation=str(stat3)+"%"
    messagebox.showinfo("Statistiques","Les Admis"+admission+"\nLes refusés"+refus+"\nLes ajournés"+ajournation,icon ='info')
    #----------------
    

def supprimer():
    try:
        sup=open("Admis.txt","r")
        satr=ad.readlines()
        sup.close()
    except:
        satr=[]
    for x in satr:
        lsep=x.split(";")
        suppr=lsep[-2]
        if int(suppr)<30:
            save=[]
            save.append(j)
            sup=open("Admis.txt","w")
            sup.writelines(save)
            sup.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
titre=Label(pff,text='Gestion des candiadats',fg='blue',bg='#FED823',font='Arial 28 bold').pack()
frame1=Frame(pff,bg='blue').pack()
frame2=Frame(pff,bg='blue').pack()
saisie=Button(frame1,text='Saisir un candiadat',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=lambda: run(pff)).pack()
admis=Button(frame1,text='Les admis',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=admis).pack()
attente=Button(frame2,text="Liste d'attente",fg='blue',bg='#21CFF9',font='Arial 14 bold',command=attente).pack()
statistiques=Button(frame2,text='Statistiques',fg='blue',bg='#21CFF9',font='Arial 14 bold',command=statistiques).pack()

def crée_par():
   messagebox.showinfo("Créé par",
                       "Ilyas ISMAILI ALAOUI\nNé le 28/11/2010\nElève de la 1er année du cycle secondaire collégial",
                       icon ='info')
créé_par=Button(frame1,text='Créé par !?',fg='blue',bg='#FED823',font='Arial 14 bold',command=crée_par).pack(padx=15,pady=15)

label1=Label(pff,text='Projet de fin de formation organisé par',fg='white',bg='#FED823',font='Arial 12 bold').pack()
label1=Label(pff,text="l'Association Marocaine de Professeurs d'Informatiques",fg='white',bg='#FED823',font='Arial 12 bold').pack()
pff.mainloop()
