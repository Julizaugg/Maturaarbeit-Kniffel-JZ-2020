import random, time

block = {}
block = {'1er':'' , '2er':'' , '3er':'' , '4er':'', '5er':'' , '6er':'' , 'Drei Gleiche':'' , 'Vier Gleiche':'' , 'Full House':'' , 'Kleine Strasse':'' , 'Grosse Strasse':'' , 'Chance':'' , 'Kniffel':''}
bonus = {'Bonus':0}

def würfeln(n):
    wurf = []
    for i in range(n):
        wurf.append(random.randint(1,6))
    wurf.sort(reverse=True)
    return wurf   

def prüfen(n):           
    zahl1 = wurf.count(1)
    zahl2 = wurf.count(2) 
    zahl3 = wurf.count(3) 
    zahl4 = wurf.count(4) 
    zahl5 = wurf.count(5)
    zahl6 = wurf.count(6)
    time.sleep(.5)
    analyse=[zahl1,zahl2,zahl3,zahl4,zahl5,zahl6]
    analyse.sort(reverse=True)
#    print(analyse, end="")
    Paar = False
    ZPaar = False
    Kniffel = False
    DGleiche = False
    VGleiche = False
    FHouse = False
    GStrasse = False
    KStrasse = False
    Einlinge = False
    if analyse[0] == 5:
        print("Du hast ein Kniffel!")
        Kniffel = True
    elif analyse[0] == 4:
        print("Du hast vier Gleiche")
        VGleiche = True
    elif analyse[0] == 3 and analyse[1] == 2:
        print("Du hast ein Full House")
        FHouse = True
    elif analyse[0] == 3:
        print("Du hast drei Gleiche")
        DGleiche = True
    elif analyse[0] == 1 and ((wurf[0] == 6 and wurf[4] == 2) or (wurf[0] == 5 and wurf[4] == 1)):
        print("Du hast eine grosse Strasse")
        GStrasse = True
    elif ((analyse[0] == 1) and ((wurf[0] == 6 and wurf[3] == 3) or (wurf[1] == 4 and wurf[4] == 1))) or ((analyse[0] == 2 and analyse[1] == 1) and ((wurf[0] == 6 and wurf[4] == 3) or (wurf[0] == 5 and wurf[4] == 2) or (wurf[0] == 4 and wurf[4] == 1))):
        print("Du hast eine kleine Strasse")
        KStrasse = True
    elif analyse[0] == 2 and analyse[1] == 2:
        print("Du hast zwei Paare")
        ZPaar = True
    elif analyse[0] == 2:
        print("Du hast ein Paar")
        Paar = True
    else:
        print("Du hast nur Einlinge")
        Einlinge = True
    if (Paar == True or ZPaar == True or Einlinge == True) and (versuch == 2 or versuch == 3):
        print("Da es keine Felder für diese Kombination hat, gibt es auch keine Strategien und Wahrscheinlichkeiten dafür.")
    else:
        print("Die Wahrscheinlichkeit im " + str(versuch) + ". Wurf beträgt dazu:")
    if Paar == True:
        if versuch == 1:
            print("90.741%")        
    elif ZPaar == True:
        if versuch == 1:
            print("27.006%")
    elif Kniffel == True:
        if versuch == 1:
            print("0.077%")
        elif versuch == 2:
            print("1.264%")
        elif versuch == 3:
            print("4.605%")
    elif DGleiche == True:
        if versuch == 1:
            print("21.296%")
        elif versuch == 2:
            print("49.525%")
        elif versuch == 3:
            print("71.363%")
    elif VGleiche == True:
        if versuch == 1:
            print("2.006%")
        elif versuch == 2:
            print("12.437%")
        elif versuch == 3:
            print("27.426%")
    elif FHouse == True:
        if versuch == 1:
            print("3.858%")
        elif versuch == 2:
            print("19.123%")
        elif versuch == 3:
            print("36.289%")
    elif GStrasse == True:
        if versuch == 1:
            print("3.086%")
        elif versuch == 2:
            print("12.974%")
        elif versuch == 3:
            print("26.110%")
    elif KStrasse == True:
        if versuch == 1:
            print("15.432%")
        elif versuch == 2:
            print("41.179%")
        elif versuch == 3:
            print("61.544%")
    else:
        if Einlinge == True:
            if versuch == 1:
                print("9.259%")
            
    print("Oberer Block: ", end=" ")
    if zahl1>0:
        print(zahl1,"Einer ", end=" ")
    if zahl2>0:
        print(zahl2,"Zweier ", end=" " )
    if zahl3>0:
        print(zahl3,"Dreier ", end=" ")       
    if zahl4>0:
        print(zahl4,"Vierer ", end=" ")
    if zahl5>0:
        print(zahl5,"Fünfer ", end=" ")
    if zahl6>0:
        print(zahl6,"Sechser ", end=" ")
    print()
    print("Chance:",sum(wurf))
    
        
print("Willkommen")
time.sleep(.5)
print("Spielen wir doch eine Partie Kniffel!")
time.sleep(.5)
print('Hier ist der leere Spielblock', block)
time.sleep(.5)

runde = 1
while runde <14:
    print()
    print(str(runde)+'. Runde')
    print("1. Wurf:")
    versuch =1
    wurf=würfeln(5)
    print(wurf)
    prüfen(wurf)
    
    input_user = ""
    while input_user != "0" and versuch <3:      
      input_user = input("Welchen Würfel noch einmal würfeln? -> Stelle angeben [1.."+str(len(wurf))+"] falls zufrieden: '0' ") 
      erlaubte_Eingaben=["0","1","2","3","4","5"]               
      if input_user in erlaubte_Eingaben and int(input_user) in range(1,len(wurf)+1): 
          del(wurf[int(input_user)-1])                           
          print('Verbleibende Würfel: ',wurf,)                          
      if (input_user=="0" and len(wurf)<5):                      
        wurf_neu=würfeln(5-len(wurf))                          
        versuch+=1
        print()
        print(str(versuch)+". Wurf:",wurf_neu)                   
        wurf=wurf+wurf_neu                                      
        wurf.sort(reverse=True)
        print(wurf)                                              
        prüfen(wurf)
        input_user = ""

    Eintrag = 0    
    print('Als was willst du diesen Wurf verwerten?')
    print(block)
    print('Entweder Feld eingeben oder mit "Streichen" ein Feld streichen lassen')
    zahl1 = wurf.count(1) 
    zahl2 = wurf.count(2) 
    zahl3 = wurf.count(3) 
    zahl4 = wurf.count(4) 
    zahl5 = wurf.count(5)
    zahl6 = wurf.count(6)
    analyse=[zahl1,zahl2,zahl3,zahl4,zahl5,zahl6] 
    analyse.sort(reverse=True)
    while Eintrag == 0:
        input_user = input("Eingabe: ")
        if input_user == 'Kniffel':
            if analyse[0] == 5:
                if block['Kniffel'] == '':
                    block['Kniffel'] = 50
                    print('Kniffel eingetragen')
                    Eintrag = 1   
                else:
                    print('Kniffel schon vergeben')
            else:
                print('Du hast gar keinen Kniffel')
        elif input_user == 'Vier Gleiche':
            if analyse[0] >= 4:
                if block['Vier Gleiche'] == '':
                    block['Vier Gleiche']= sum(wurf)
                    print('Vier Gleiche eingetragen')
                    Eintrag = 1
                else:
                    print('Vier Gleiche schon vergeben')
            else:
                print('Du hast gar keine vier Gleichen')
        elif input_user == 'Drei Gleiche':
            if analyse[0] >= 3: 
                if block['Drei Gleiche'] == '':
                    block['Drei Gleiche']= sum(wurf)
                    print('Drei Gleiche eingetragen')
                    Eintrag = 1
                else:
                    print('Drei Gleiche schon vergeben')
            else:
                print('Du hast gar keine drei Gleiche')
        elif input_user == 'Grosse Strasse':
            if analyse[0] == 1 and ((wurf[0] == 6 and wurf[4] == 2) or (wurf[0] == 5 and wurf[4] == 1)):
                if block['Grosse Strasse'] == '':
                    block['Grosse Strasse']= 40
                    print('Grosse Strasse eingetragen')
                    Eintrag = 1
                else:
                    print('Grosse Strasse schon vergeben')
            else:
                print('Du hast gar keine grosse Strasse')
        elif input_user == 'Kleine Strasse':
            if (analyse[0] == 1 and ((wurf[0] == 6 and wurf[3] == 3) or (wurf[1] == 4 and wurf[4] == 1) or (wurf[0] == 6 and wurf[4] == 2) or (wurf[0] == 5 and wurf[4] == 1))) or ((analyse[0] == 2) and (analyse[1] == 1) and ((wurf[0] == 6 and wurf[4] == 3) or (wurf[0] == 5 and wurf[4] == 2) or (wurf[0] == 4 and wurf[4] == 1))):
                if block['Kleine Strasse'] == '':
                    block['Kleine Strasse']= 30
                    print('Kleine Strasse eingetragen')
                    Eintrag = 1
                else:
                    print('Kleine Strasse schon vergeben')
            else:
                print('Du hast gar keine kleine Strasse')
        elif input_user == '1er':
            if block['1er'] == '':
                block['1er'] = zahl1
                print ('1er eingetragen')
                Eintrag = 1
            else:
                print('1er schon vergeben')
        elif input_user == '2er':
            if block['2er'] == '':
                block['2er'] = 2*zahl2
                print ('2er eingetragen')
                Eintrag = 1
            else:
                print('2er schon vergeben')
        elif input_user == '3er':
            if block['3er'] == '':
                block['3er'] = 3*zahl3
                print ('3er eingetragen')
                Eintrag = 1
            else:
                print('3er schon vergeben')
        elif input_user == '4er':
            if block['4er'] == '':
                block['4er'] = 4*zahl4
                print ('4er eingetragen')
                Eintrag = 1
            else:
                print('4er schon vergeben')
        elif input_user == '5er':
            if block['5er'] == '':
                block['5er'] = 5*zahl5
                print ('5er eingetragen')
                Eintrag = 1
            else:
                print('5er schon vergeben')
        elif input_user == '6er':
            if block['6er'] == '':
                block['6er'] = 6*zahl6
                print ('6er eingetragen')
                Eintrag = 1
            else:
                print('6er schon vergeben')
        elif input_user == 'Chance':
            if block['Chance'] == '':
                block['Chance'] = sum(wurf)
                print('Chance eingetragen')
                Eintrag = 1
            else:
                print ('Chance schon vergeben')
        elif input_user == 'Full House':
            if analyse[0] == 3 and analyse[1] == 2:
                if block['Full House'] == '':
                    block['Full House'] = 25
                    print('Full House eingetragen')
                    Eintrag = 1
                else:
                    print('Full House schon vergeben')
            else:
                print('Du hast gar kein Full House')
        elif input_user == 'Streichen':
            print('Welches Feld möchtest du streichen?')
            input_user = input("Streichen: ")
            if input_user == '1er':
                if block['1er'] == '':
                    block['1er'] = 0
                    print('1er gestrichen')
                    Eintrag = 1
                else:
                    print('1er bereits verwertet/gestrichen')
            elif input_user == '2er':
                if block['2er'] == '':
                    block['2er'] = 0
                    print('2er gestrichen')
                    Eintrag = 1
                else:
                    print('2er bereits verwertet/gestrichen')
            elif input_user == '3er':
                if block['3er'] == '':
                    block['3er'] = 0
                    print('3er gestrichen')
                    Eintrag = 1
                else:
                    print('3er bereits verwertet/gestrichen')
            elif input_user == '4er':
                if block['4er'] == '':
                    block['4er'] = 0
                    print('4er gestrichen')
                    Eintrag = 1
                else:
                    print('4er bereits verwertet/gestrichen')
            elif input_user == '5er':
                if block['5er'] == '':
                    block['5er'] = 0
                    print('5er gestrichen')
                    Eintrag = 1
                else:
                    print('5er bereits verwertet/gestrichen')
            elif input_user == '6er':
                if block['6er'] == '':
                    block['6er'] = 0
                    print('6er gestrichen')
                    Eintrag = 1
                else:
                    print('6er bereits verwertet/gestrichen')
            elif input_user == 'Kniffel':
                if block['Kniffel'] == '':
                    block['Kniffel'] = 0
                    print('Kniffel gestrichen')
                    Eintrag = 1
                else:
                    print('Kniffel bereits verwertet/gestrichen')
            elif input_user == 'Vier Gleiche':
                if block['Vier Gleiche'] == '':
                    block['Vier Gleiche'] = 0
                    print('Vier Gleiche gestrichen')
                    Eintrag = 1
                else:
                    print('Vier Gleiche bereits verwertet/gestrichen')
            elif input_user == 'Drei Gleiche':
                if block['Drei Gleiche'] == '':
                    block['Drei Gleiche'] = 0
                    print('Drei Gleiche gestrichen')
                    Eintrag = 1
                else:
                    print('Drei Gleiche bereits verwertet/gestrichen')
            elif input_user == 'Full House':
                if block['Full House'] == '':
                    block['Full House'] = 0
                    print('Full House gestrichen')
                    Eintrag = 1
                else:
                    print('Full House bereits verwertet/gestrichen')
            elif input_user == 'Grosse Strasse':
                if block['Grosse Strasse'] == '':
                    block['Grosse Strasse'] = 0
                    print('Grosse Strasse gestrichen')
                    Eintrag = 1
                else:
                    print('Grosse Strasse bereits verwertet/gestrichen')
            elif input_user == 'Kleine Strasse':
                if block['Kleine Strasse'] == '':
                    block['Kleine Strasse'] = 0
                    print('Kleine Strasse gestrichen')
                    Eintrag = 1
                else:
                    print('Kleine Strasse bereits verwertet/gestrichen')
            elif input_user == 'Chance':
                if block['Chance'] == '':
                    block['Chance'] = 0
                    print('Chance gestrichen')
                    Eintrag = 1
                else:
                    print('Chance bereits verwertet/gestrichen')
            else: print('Dieses Feld gibt es nicht! Bitte erneut "Streichen" eingeben oder normale Eingabe tätigen')
        else:
            print('Dieses Feld gibt es nicht! Bitte anderes Feld wählen')
            print(block)
    runde+=1
    time.sleep(1)
print('Sehr gut, du bist nun fertig')
print(block)
if block['1er']+block['2er']+block['3er']+block['4er']+block['5er']+block['6er'] >= 63:
    print('Toll, du hast den Bonus von 35 erzielt!')
    bonus['Bonus'] = 35
else:
    print('Du hast den Bonus leider nicht geschafft')
print('Gesamtpunktzahl: ')
print(block['Kniffel']+block['Vier Gleiche']+block['Drei Gleiche']+block['Chance']+block['Full House']+block['1er']+block['2er']+block['3er']+block['4er']+block['5er']+block['6er']+block['Kleine Strasse']+block['Grosse Strasse']+bonus['Bonus'])
print('Danke fürs Spielen!')