def hello_dingfabrik():
    print('Hallo "Leute", Dingfabrik')
   
hello_dingfabrik()

# funktion hat keinen Rückgabewert,
# a ist daher none
a = hello_dingfabrik()
print(a)

def funktion_mit_parameter(irgendein_text):
    print(irgendein_text*2)
    
funktion_mit_parameter("Hallo Welt")
funktion_mit_parameter("Hallo Welt")

def funktion_mit_parameter2(irgendein_text="Hallo Felix"):
    print(irgendein_text*2)
    
funktion_mit_parameter2()
funktion_mit_parameter2("Hallo Uwe")

def funktion_mit_parameter3(irgendein_text="Hallo Felix", anzahl=2):
    print(irgendein_text*anzahl,"\n")
    print("\n")
    
funktion_mit_parameter3()
funktion_mit_parameter3(irgendein_text="Hallo Dingfabrik")
funktion_mit_parameter3("1234")
funktion_mit_parameter3(anzahl=3)
funktion_mit_parameter3(irgendein_text="Hallo Dingfabrik\n", anzahl=5)

# Jetzt: Funktionen mit Rückgabewert

def addiere(zahl1, zahl2):
    return zahl1 + zahl2

print(addiere(2, 5)**2)
abc = addiere(20, 50)
print(abc)

def teile(zahl1, zahl2):
    return zahl1 // zahl2, zahl1 % zahl2

e, r = teile(9,2)

print("teile:", e, r)

x = 25
y = 10
x, y = y, x
print(x, y)



