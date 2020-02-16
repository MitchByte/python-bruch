#Autor: Michele Fischer
#12.11.2017

####################################################
## Definition von Klassen und Funktionen
####################################################




def ggt(a, b):
    """Bestimmt den groessten gemeinsamen Teiler zweier nicht-negativen Zahlen mittels dem klassischen Euklidischen Algorithmus
    """
    if a == 0:
        return b
    else:
        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a



class Bruch:
    """ Klasse, die aus zwei ganzen Zahlen einen Bruch erstellt.
    
    **Parameter**
        zaehler: int
            Der Zaehler des Bruches
        nenner: int
            Der Nenner des Bruches
    
    **Attribute**
        zaehler: int
            Der Betrag des Zaehlers des gekuerzten Bruches
        nenner: int
            Der Betrag des Nenners des gekuerzten Bruches
        vorzeichen: int
            1 falls der Bruch positiv ist, -1 falls der Bruch negativ ist
    
    """
    
    def __init__(self, zaehler, nenner):
        """
        Ein Bruch Objekt erschaffen, um dann die Attribute direkt aus dem Input zu lesen, und dann den Bruch im gekuerzten Format darzustellen
        """
        
        self.zaehler = abs(zaehler)
        self.nenner = abs(nenner)
        if zaehler*nenner < 0:
            self.vorzeichen = -1
        else:
            self.vorzeichen = 1  
 
        
        self.__kuerzen()
        
        
    def __kuerzen(self):
        """Den Bruch erst in eine ganze Zahl und eigentlichen Bruch zerlegen, dann wird mittels einer Funktion, die den ggT zweier nicht-negativen Zahlen berechnet, der eigentliche Bruch gekuerzt. Zuletzt wird die ganze Zahl und der gekuerzte eigentliche Bruch wieder zusammen in Bruch Format dargestellt.
        
        **Gibt zurueck**
            Bruch Objekt
                den gekuerzten Bruch
        
        """
            
        ganze = 0
        
        while self.zaehler - self.nenner >= 0:
            ganze = ganze + 1
            self.zaehler = self.zaehler - self.nenner
        #im Falle Bruch gleich ganze Zahl
        if self.zaehler == 0:
            self.zaehler = ganze
            self.nenner = 1
        #wenn nicht
        else:
        	
            #kuerzen
            g = ggt(self.nenner, self.zaehler)
            if g != 1:                        
            	self.nenner = self.nenner/g
            	self.zaehler = self.zaehler/g
        
        
            self.zaehler = ganze*self.nenner + self.zaehler
            
            
    #  Quelle http://gertingold.github.io/eidprog/objektorientiert.html
    def __str__(self):
        """Magic methode, die definiert, wie der Rechner den Bruch dem User raepresentiert.
        
        Gibt Bruch angemessen als ganze Zahl oder ganze Zahl dividiert durch ganze Zahl an. 
        
        **Gibt zurueck**
            str
                String, der das Objekt beschreibt
        
        """
        if self.nenner!=1:
            return "{}/{}".format(self.zaehler*self.vorzeichen, self.nenner)
        else:
            return str(self.zaehler*self.vorzeichen)    
        
    def __add__(self, other):
        """Definiert wie man zwei Brueche zusammen addiert.
        
        **Gibt zurueck**
            Bruch
                die Summe der zwei Brueche
        """
        
        if isinstance(other, Bruch) == True:
            nenner = self.nenner * other.nenner
            zaehler = self.vorzeichen*self.zaehler*other.nenner + other.vorzeichen*other.zaehler*self.nenner
        
        return Bruch(zaehler, nenner)
        
        
    def __sub__(self, other):
        """Definiert, wie man einen Bruch von einem anderen subtrahiert
        
        Tauscht das Vorzeichen des zu subtrahierenden Bruches um, und verwendet dann die Funktion fuer die Addition.
        
        **Gibt zurueck**
            Bruch   
                die Summe der zwei Brueche
        
        """
        
        if isinstance(other, Bruch) == True:
            newVorzeichen = -other.vorzeichen
            
        return self + Bruch(newVorzeichen*other.zaehler, other.nenner)
            
        
        
    def __mul__(self, other):
        """Definiert, wie man einen Bruch mit einem anderen Bruch oder einer ganzen Zahl multipiliziert.
        
        **Gibt zurueck**
            Bruch
                der Produkt der zwei Zahlen
        """
        
        if isinstance(other, Bruch) == True:
            nenner = self.nenner*other.nenner
            zaehler = self.zaehler*other.zaehler
            vorzeichen = self.vorzeichen*other.vorzeichen
        if isinstance(other, int) == True:
            nenner = self.nenner
            zaehler = other * self.zaehler
            vorzeichen = self.vorzeichen
        
        return Bruch(vorzeichen*zaehler, nenner)
        
        
    def __rmul__(self, other):
        """Definiert Multiplikation in die andere Richtung.
        
        **Gibt zurueck**
            Bruch
                der Produkt der zwei Zahlen
        
        """
        
        if isinstance(other, Bruch) == True:
            nenner = self.nenner*other.nenner
            zaehler = self.zaehler*other.zaehler
            vorzeichen = self.vorzeichen*other.vorzeichen
        if isinstance(other, int) == True:
            nenner = self.nenner
            zaehler = other * self.zaehler
            vorzeichen = self.vorzeichen
        
        return Bruch(vorzeichen*zaehler, nenner)
    
        
    def __div__(self,other):
        """Definiert Division zwischen zwei Bruechen
        
        Tauscht Nenner und Zaehler des Divisors um, und verwendet dann die Funktion fuer Multiplikation.
        
        **Gibt zurueck**
            Bruch
                den Quotient der zwei Brueche
        """
        
        if isinstance(other, Bruch) == True:
            return self*Bruch(other.nenner*other.vorzeichen, other.zaehler)
        
        
    def __le__(self, other):
        """Bestimmt ob ein Bruch kleiner gleich einem anderen Bruch oder einer reellen Zahl ist.
        
        **Gibt zurueck**
            bool
                True ,wenn der Bruch kleiner gleich ist, False ,wenn der Bruch groesser ist.
        """
        
        if isinstance(other, Bruch) == True:
            test = self - other
            if test.zaehler*test.vorzeichen <= 0:
                return True
            else:
                return False
        else:
            zaehler = float(self.zaehler*self.vorzeichen)
            nenner = float(self.nenner)
            test = zaehler/nenner - float(other)
            if test <= 0:
                return True
            else:
                return False
            
#################################################
## Testing 
#################################################


if __name__ == "__main__":  
    
    import sys
    
    print("Dieses Programm dient zur Herstellung von Bruechen, welche durch den Benutzer eingegeben werden koennen. Zuerst kann ein Testbeispiel eingesehen werden. Weiter kann der Benutzer seine eingegebenen Brueche mit verschiedenen Operationen wie Multiplikation, Addition usw. versehen. Auch eine Ordnungsrelation kann hergestellt werden. ")
    print("")
    
    """Gibt dem User die Moeglichkeit einen vorbereitetes Beispiel der Klasse und Funktionen durchzufuehren.
    
    """
    schalter = True
    while schalter:
        
        beispiel = str(raw_input("Moechten Sie ein vorbereitetes Testbeispiel sehen? Bitte geben Sie 'ja' oder 'nein' ein: "))
        if beispiel == 'ja':
            schalter = False
            beispielBruch1 = Bruch(-3, 6)
            beispielBruch2 = Bruch(15, -5)
        
            print("Bruch(-3, 6) = " + str(beispielBruch1))
            print("Bruch(15, -5) = " + str(beispielBruch2))
        
            print(str(beispielBruch1) + " + " + str(beispielBruch2) + " = " + str(beispielBruch1 + beispielBruch2))
            print(str(beispielBruch1) + " - " + str(beispielBruch2) + " = " + str(beispielBruch1 - beispielBruch2))
            print(str(beispielBruch1) + " * " + str(beispielBruch2) + " = " + str(beispielBruch1 * beispielBruch2))
            print(str(beispielBruch1) + " / " + str(beispielBruch2) + " = " + str(beispielBruch1 / beispielBruch2))
            print(str(beispielBruch1) + " <= " + str(beispielBruch2) + " = " + str(beispielBruch1 <= beispielBruch2))
        
            print(str(beispielBruch1) + " * 2 = " + str(beispielBruch1 * 2))
            print(str(beispielBruch1) + " <= 1 = " + str(beispielBruch1 <= 1))
        
            print("Jetzt koennen Sie das Programm selbst testen.")
            
            
        if beispiel == 'nein':
            schalter = False
            
    schalter = True
    
    while schalter:
        test = raw_input("Moechten Sie das Programm selbst ausfuehren? Bitte geben Sie 'ja' oder 'nein' ein: ")
        if test == 'ja':
            schalter = False
        if test == 'nein':
            sys.exit()

    schalter = True
    
    while schalter:
      try:
        zaehler = int(raw_input("Bitte geben Sie eine ganze Zahl fuer den Zaehler ein: "))
        schalter = False
      except ValueError:
        print("Dies war keine ganze Zahl, bitte versuchen Sie es noch einmal.")
        
    schalter = True 
        
    while schalter or nenner == 0:
        try:
            nenner = int(raw_input("Bitte geben Sie eine ganze Zahl ungleich 0 fuer den Nenner ein: "))
            schalter = False 
        except ValueError:
            print("Dies war keine ganze Zahl.")
        if nenner== 0:
            print("Diese Zahl ist nicht von 0 verschieden.")
    

    userBruch1 = Bruch(zaehler, nenner)
    print("userBruch1 = " + str(userBruch1))
    
    #Teil 3.3 zuende machen:
    #Moechten Sie einen zweiten Bruch herstellen?
    #wenn ja, dann userBruch2 definieren und Funktionen waehlen
    #wenn nein, dann * oder <= testen
    
    schalter = True
    while schalter:
        
        zweiter = str(raw_input("Moechten Sie einen zweiten Bruch erstellen? Geben Sie 'ja' oder 'nein' ein: "))
    
        if zweiter == 'ja':
            while schalter:
                try:
                    zaehler = int(raw_input("Bitte geben Sie eine ganze Zahl fuer den Zaehler ein: "))
                    schalter = False
                except ValueError:
                    print("Dies war keine ganze Zahl, bitte versuchen Sie es noch einmal.")
        
            schalter = True 
        
            while schalter or nenner == 0:
                try:
                    nenner = int(raw_input("Bitte geben Sie eine ganze Zahl ungleich 0 fuer den Nenner ein: "))
                    schalter = False 
                except ValueError:
                    print("Dies war keine ganze Zahl.")
                if nenner== 0:
                    print("Diese Zahl ist nicht von 0 verschieden.")
    

            userBruch2 = Bruch(zaehler, nenner)
            print("userBruch2 = " + str(userBruch2))
        
            schalter = True
            while schalter:
                #Welche Funktion moechten Sie testen?
                f = str(raw_input("Welche Funktion moechten Sie testen? Waehlen Sie '*', '+', '-', '/' oder '<=': "))
        
                #if schleife fuer input(+, -, *, / oder <=)

                if f == '*':
                    schalter = False
                    r = userBruch1 * userBruch2
                    print("userBruch1 * userBruch2 = " + str(r))
            
                if f == '<=':
                    schalter = False
                    l = userBruch1 <= userBruch2
                    print("userBruch1 <= userBruch2 is " + str(l))
            
                if f == '+':
                    schalter = False
                    p = userBruch1 + userBruch2
                    print("userBruch1 + userBruch2 = " + str(p))
                
                if f == '-':
                    schalter = False
                    s1 = userBruch1 - userBruch2
                    print("userBruch1 - userBruch2 = " + str(s1))
                    schalter = True
                    while schalter:
                        u = str(raw_input("Diese Funktion ist nicht kommutativ. Moechten Sie den userBruch1 - userBruch2 rechnen? Geben Sie 'ja' oder 'nein' ein: " ))
                        if u == 'ja':
                            s2 = userBruch2 - userBruch1
                            print("userBruch2 - userBruch1 = " + str(s2))
                            schalter = False
                        if u == 'nein':
                            schalter = False

            
                if f == '/':
                    schalter = False
                    
                    while userBruch2.zaehler == 0:
                        print("Division durch 0 is nicht definiert.")
                        print("Bitte geben Sie nochmal userBruch2 ein.")
                        schalter = True
                        while schalter:
                            try:
                                zaehler = int(raw_input("Bitte geben Sie eine ganze Zahl fuer den Zaehler ein: "))
                                schalter = False
                            except ValueError:
                                print("Dies war keine ganze Zahl, bitte versuchen Sie es noch einmal.")
                    
                        schalter = True 
                    
                        while schalter or nenner == 0:
                            try:
                                nenner = int(raw_input("Bitte geben Sie eine ganze Zahl ungleich 0 fuer den Nenner ein: "))
                                schalter = False 
                            except ValueError:
                                print("Dies war keine ganze Zahl.")
                            if nenner== 0:
                                print("Diese Zahl ist nicht von 0 verschieden.")

                        userBruch2 = Bruch(zaehler, nenner)
                        print("userBruch2 = " + str(userBruch2))
                        
                    d1 = userBruch1 / userBruch2
                    print("userBruch1 / userBruch2 = " + str(d1))
                    
                    switch = True
                    while switch == True:
                        u = str(raw_input("Diese Funktion ist nicht kommutativ. Moechten Sie den userBruch2 / userBruch1 berechnen? Geben Sie 'ja' oder 'nein' ein: " ))
                        if u == 'ja':
                            while userBruch1.zaehler == 0:
                                print("Division durch 0 is nicht definiert.")
                                print("Bitte geben Sie nochmal userBruch2 ein.")
                                schalter = True
                                while schalter:
                                    try:
                                        zaehler = int(raw_input("Bitte geben Sie eine ganze Zahl fuer den Zaehler ein: "))
                                        schalter = False
                                    except ValueError:
                                        print("Dies war keine ganze Zahl, bitte versuchen Sie es noch einmal.")
                            
                                schalter = True 
                            
                                while schalter or nenner == 0:
                                    try:
                                        nenner = int(raw_input("Bitte geben Sie eine ganze Zahl ungleich 0 fuer den Nenner ein: "))
                                        schalter = False 
                                    except ValueError:
                                        print("Dies war keine ganze Zahl.")
                                    if nenner== 0:
                                        print("Diese Zahl ist nicht von 0 verschieden.")

                                userBruch1 = Bruch(zaehler, nenner)
                                print("userBruch1 = " + str(userBruch1))
                                
                            switch = False
                            d2 = userBruch2/userBruch1
                            print("userBruch2 / userBruch1 = " + str(d2))
                            
                        if u == 'nein':
                            switch = False
        
        
        if zweiter == 'nein':
        
            while schalter:
                f = str(raw_input("Welche Funktion moechten Sie testen? Waehlen Sie '*' oder '<=': "))
                
                if f == '*':
                    
                    while schalter:
                        try:
                            x = int(raw_input("Geben Sie die ganze Zahl ein, mit der Ihr userBruch1 zu multiplizieren ist: "))
                            m = userBruch1 * x
                            print("userBruch1 * " + str(x) + " = " + str(m))
                            schalter = False
                        except ValueError:
                            print("Dies war keine ganze Zahl.")
                            
                    
                    
                if f == '<=':
                    while schalter:
                        try:
                            x = str(raw_input("Geben Sie die reelle Zahl ein, mit der Ihr userBruch1 zu vergleichen ist: "))
                            l = userBruch1 <= x
                            print("userBruch1 <= " + str(x) + " is " + str(l))
                            schalter = False
                        except ValueError:
                            print("Dies war keine reelle Zahl.")

                            
                    
                    
           
        
       
    
    
    
    

    




        
    
        


