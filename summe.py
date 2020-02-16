"""Autorin: Fischer Michele"""
"""Serie2:"""
"""Programm zur Berechnung von Partialsummen anhand zwei verschiedener Algorithmen.
Untersuchen der berechneten Werte anhand der unterschiedlich verwendeter Gleitkommazahlen und verschiedener grosser Werte fuer die Anzahl der Summanden."""

"""importieren notwendiger Bibliotheken"""
import math
import numpy as np
import scipy
from scipy import misc
import pandas


def sumalgi(folge, dt):
    """Algorithmus zur Aufsummierung nach Reihenfolge der Indizes
        
        **Parameter**
            folge: list
                Folge die aufsummiert wird
            dt: dtype 
                Datentyp in dem die Berechnung statt findet
            
        **Output**
            Summe: dtype=dt
    """
    n = len(folge)
    S = 0
    for i in xrange(n):
        if np.isnan(dt(folge[i])) == False and np.isinf(dt(folge[i])) == False:
            if np.isinf(dt(S) + dt(folge[i])) == False:
                S = dt(S) + dt(folge[i])
    return S


def sumalgii(folge, dt):
    """Algorithmus zur Aufsummierung nach Reihenfolge der Groesse der Betraege der Eintraege
    ype = ['f
        **Parameter**
            folge: list
                Folge die aufsummiert wird
            dt: dtype 
                Datentyp in dem die Berechnung statt findet
            
        **Output**
            Summe: dtype=dt
    """
    n = len(folge)
    folge = sorted(folge, key=abs)
    S = 0
    for i in xrange(n):
        if np.isnan(dt(folge[i])) == False and np.isinf(dt(folge[i])) == False:
            if np.isinf(dt(S) + dt(folge[i])) == False:
                S = dt(S) + dt(folge[i])
    return S


def pZerlegung(folge):
    """Entpackt die positiven Terme aus der zu aufsummierende Folge
        
        **Parameter**
            folge: list
                Folge die zu zerlegen ist
        
        **Output**
            fp: list
                Teilfolge der positiven Terme aus der eingegebenen Folge
    
    """
    f = np.array(folge)
    fp = list(np.extract(f > 0, f))
    return fp

def nZerlegung(folge):
    """Entpackt die negativen Terme aus der zu aufsummierenden Folge
        
        **Parameter**
            folge: list
                Folge die zu zerlegen ist
        
        **Output**
            fp: list
                Teilfolge der negativen Terme aus der eingegebenen Folge
    
    """
    f = np.array(folge)
    fn = list(np.extract(f < 0, f))
    return fn



    
"""Verwendung name- main- Methode"""
if __name__=='__main__':
    
    print("")
    
    print(" Das von Ihnen ausgefuehrte Programm 'summe.py' beinhaltet zwei verschiedene Algorithmen,\n anhand derer Sie die Summation von Partialsummen ausfuehren koennen, auch kann eine Untersuchung zu den verschiedenen *floating point* - Typen ausgewaehlt werden.")
    print("")
    
    schalter = True
    while schalter:
        while True:
            aufgabe = raw_input("Welche Aufgabe moechten Sie durchfuehren? Bitte geben Sie \n '0' fuer ein vorbereitetes Testbeispiel ein,  \n '1' fuer das Berechnen der Partialsumme der harmonischen Reihe, \n '2' fuer das Berechnen der Approximationen zur exp(x) und 1/exp(-x) mit zwei vordefinierten Algorithmen (i) und (ii), \n '3' fuer die Summation der Approximationen anhand Algorithmen (i) und (ii) und auch Algorithmus (iii) der zunaechst die negativen und positiven Beitraege getrennt voneinander mittels des zweiten Algorithmuses aufsummiert, \n 'U' fuer die  Untersuchung fuer die relative Abweichung mit drei verschiedenen Datentypen bei derer der letzte Summand dem vorletzten Summanden gleicht: \n")
            if aufgabe == '0' or aufgabe == '1' or aufgabe == '2' or aufgabe == '3' or aufgabe == 'U':
                break
                
        
        """der Benutzer kann nun die Anzahl der Summanden anhand von k eingeben"""
        while True and aufgabe != 'U':
            Dt = raw_input("Bitte geben Sie einen von den folgenden floating- Datentypen an, den Sie benutzen moechten. Zur Auswahl stehen Ihnen '16', '32', '64', 'alle': ")
            if Dt == '16':
                Dt = [np.float16]
                break
            if Dt == '32':
                Dt = [np.float32]
                break
            if Dt == '64':
                Dt = [np.float64]
                break
            if Dt == 'alle':
                Dt = [np.float16, np.float32, np.float64]
                break
            
        while True and aufgabe != '0' and aufgabe != 'U':
            if aufgabe == '1':
                print("")
                print("(Sie haben die exakten Werte der ersten 10 Partialsummen der harmonischen Reihe zum Vergleich zur Verfuegung.) ")
            try:
                while True:
                    k = int(raw_input("Geben Sie die Summenlaenge als ganze Zahl ein: "))
                    if k < 0:
                        print("Die Summenlaenge muss positiv sein.")
                    if k >= 0:
                        break
                break
            except ValueError:
                print("Dies war keine ganze Zahl.")
            
        
        """der Benutzer kann jetzt eine reelle Zahl eingeben """
        while True and (aufgabe == '2' or aufgabe == '3' or aufgabe == 'U'):
            try:
                strx = raw_input("Geben eine reelle Zahl x ein fuer die Approximation zur Exponentialfunktion e^x: ")
                real = float(strx)
                break
            except ValueError:
                print("Dies war keine reelle Zahl.")
        if aufgabe == '0':
            k = 150
            strx = 50
            
            print("k = 150 und x = 50")
        
        """nun werden fuer verschiedene floating datentypen  die errechneten Ergebnisse ausgegeben"""

        if aufgabe == '1' or aufgabe == '0':
            
            print("")
            print("zur Aufgabe 2.1.1:")
            for dt in Dt:
                
                """Formel fuer die harmonische Reihe"""
                harmReihe = [dt(1.0)/dt(i) for i in xrange(1,k+1,1)]
                    
                """Anwenden der 2 Algorithmen auf die harmonische Reihe"""

                piHarmReihe = sumalgi(harmReihe, dt)
                piiHarmReihe = sumalgii(harmReihe, dt)
                
                """Ausgabe der Ergebnisse"""
                print("")
                print("Die Summe der harmonischen Reihe mit den zwei verschiedenen Summationsalgorithmen fuer Datentyp " + str(dt) + " gleicht ")
                print(['%70.40f' % elem for elem in [piHarmReihe, piiHarmReihe]])
                
                if k in range(1, 11, 1):
                    while True:
                        abw = raw_input("Moechten Sie diese Approximationen mit dem exakten Wert der Partialsumme vergleichen? Geben Sie 'ja' oder 'nein' ein: ")
                        if abw == 'ja':
                            H = [dt(1.0), dt(3.0/2.0), dt(11.0/6.0), dt(25.0/12.0), dt(137.0/60.0), dt(49.0/20.0), dt(363.0/140), dt(761.0/280), dt(7129.0/2520), dt(7381.0/2520)]
                            print("Der exakte Wert ist " + str(H[k-1]))
                            print("Die Abweichungen lauten " + str([dt(piHarmReihe - H[k-1]), dt(piiHarmReihe - H[k-1])]))
                            print("")
                            break
                        if abw == 'nein':
                            break
                else:
                    print("Sie haben innerhalb diesem Programm keine Moeglichkeit diese berechneten Werte mit dem exakten Wert der Partialsumme der harmonischen Reihe zu vergleichen.")
            
                
            while True and aufgabe != '0':
                print("")
                nochmal = raw_input("Moechten Sie das Programm weiter ausfuehren? Geben Sie 'ja' oder 'nein' ein: ")
                if nochmal == 'ja':
                    print("")
                    break
                if nochmal == 'nein':
                    schalter = False
                    break
                
            
                

        """Festlegen der reellen Zahl fuer die verschiedenen floating point Typen"""
        if aufgabe == '2' or aufgabe == '3' or aufgabe == '0':
            
            for dt in Dt:
                x = dt(strx)
                """die zwei angegebenen Approximationen der Exponentialfunktion"""
                    
                try:
                    listyk = [np.power(x, i, dtype=dt)/dt(np.math.factorial(i)) for i in xrange(k+1)]
                    listYk = [np.power(-1,i, dtype=dt)*np.power(x, i, dtype=dt)/dt(np.math.factorial(i)) for i in xrange(k+1)]
                except OverflowError:
                    listyk = [np.power(x, i, dtype=dt)/dt(scipy.misc.factorial(i, exact=False)) for i in xrange(k+1)]
                    listYk = [np.power(-1,i, dtype=dt)*np.power(x, i, dtype=dt)/dt(scipy.misc.factorial(i, exact=False)) for i in xrange(k+1)]
                for y in listyk + listYk:
                        if np.isnan(y) == True:
                            print("")
                            print("Achtung! Die Zahlen x^i und i! wurden zu gross und sind in diesem Datentyp nicht darstellbar. Deshalb werden diese Terme als inf/inf = nan dargestellt. ")
                            break
                

                """Anwendung der 2 Algorithmen auf jede der Approximationen"""
                yki = sumalgi(listyk, dt)
                #print listyk, yki
                ykii = sumalgii(listyk, dt)
                #print ykii
                Yki = 1/sumalgi(listYk, dt)
                Ykii = 1/sumalgii(listYk, dt)
                
                ex = np.exp(dt(strx))
                
                pandas.set_option('display.max_colwidth', -1)
                
                if aufgabe == '2':
                    print("")
                    print("zur Aufgabe 2.1.2:")
                    dataA = np.array([['%64.40f' % elem for elem in [yki, ykii]],['%64.40f' % elem for elem in [Yki, Ykii]]])
                    dataAb = np.array([['%64.40f' % elem for elem in [yki-ex, ykii-ex]],['%64.40f' % elem for elem in [Yki-ex, Ykii-ex]]])

                    Auswertung = pandas.DataFrame(dataA, ['Approx. exp(x)', 'Approx. 1/exp(-x)'], ['Summationsalgorithmus(i)', 'Summationsalgorithmus(ii)'])
                    Abweichung = pandas.DataFrame(dataAb, ['Approx. exp(x) - exakter Wert exp(x)', 'Approx. 1/exp(-x) - exakter Wert exp(x)'], ['Summationsalgorithmus(i)', 'Summationsalgorithmus(ii)'])
                
                    """Ausgabe der errechneten Naeherung und des exakten Wertes in Python"""
            
                    print("")
                    print("Fuer Datentyp " + str(dt) + " lauten die Approximationen")
                    print(Auswertung)
                    
                    print("")
                    print("Fuer Datentyp " + str(dt) + " lauten die Abweichungen zum exakten Wert von e^x")
                    print(Abweichung)
                    
                
                if aufgabe == '3' or aufgabe == '0':
                    print("")
                    print("zur Aufgabe 2.1.3:")
                    
                    listykn = nZerlegung(listyk)
                    listykp = pZerlegung(listyk)
                    
                    listYkn = nZerlegung(listYk)
                    listYkp = pZerlegung(listYk)
                    
                    yk3ii = sumalgii(listykn, dt) + sumalgii(listykp, dt)
                    
                    Yk3ii = 1/(sumalgii(listYkn, dt) + sumalgii(listYkp, dt))

                    
                    dataA = np.array([['%64.40f' % elem for elem in [yki, ykii, yk3ii]],['%64.40f' % elem for elem in [Yki, Ykii, Yk3ii]]])
                    dataAb = np.array([['%64.40f' % elem for elem in [yki-ex, ykii-ex, yk3ii-ex]],['%64.40f' % elem for elem in [Yki-ex, Ykii-ex, Yk3ii-ex]]])

                    
                    Auswertung = pandas.DataFrame(dataA, ['Approx. exp(x)', 'Approx. 1/exp(-x)'], ['Summationsalgorithmus(i)', 'Summationsalgorithmus(ii)', 'Summationsalgorithmus(iii)'])
                    Abweichung = pandas.DataFrame(dataAb, ['Approx. exp(x) - exakter Wert exp(x)', 'Approx. 1/exp(-x) - exakter Wert exp(x)'], ['Summationsalgorithmus(i),', 'Summationsalgorithmus(ii)', 'Summationsalgorithmus(iii)'])
                
                    """Ausgabe der errechneten Naeherung und des exakten Wertes in Python"""
            
                    print("")
                    print("Fuer Datentyp " + str(dt) + " lauten die Approximationen")
                    print(Auswertung)
                    
                    print ("")
                    print("Fuer Datentyp " + str(dt) + " lauten die Abweichungen zum exakten Wert von e^x")
                    print(Abweichung)

            
                
            while True and aufgabe != '0':
                print("")
                nochmal = raw_input("Moechten Sie das Programm weiter ausfuehren? Geben Sie 'ja' oder 'nein' ein: ")
                if nochmal == 'ja':
                    print("")
                    break
                if nochmal == 'nein':
                    schalter = False
                    break
        
        if aufgabe == 'U' or aufgabe == '0':
            print("")
            print("Untersuchung:")
            
            for dt in [np.float16, np.float32, np.float64]:

                x = dt(strx)
                
                k = 0
                new = sumalgii([np.power(x, i, dtype=dt)/dt(np.math.factorial(i)) for i in xrange(k+1)], dt)
                old = 0
                while new != old:
                    old = new
                    k = k + 1
                    
                    try:
                        new = sumalgii([np.power(x, i, dtype=dt)/dt(np.math.factorial(i)) for i in xrange(k+1)], dt)
                    except OverflowError:
                        new = [np.power(x, i, dtype=dt)/dt(scipy.misc.factorial(i, exact=False)) for i in xrange(k+1)]
                        
                try:
                    a = np.power(x, k, dtype=dt)/dt(np.math.factorial(k))
                except OverflowError:
                    a = np.power(x, k, dtype=dt)/dt(scipy.misc.factorial(k, exact=False))
                        
                    
                print("")
                print("k_* fuer Datentyp " + str(dt) + " ist " + str(k-1))
                
                print("Die relative Abweichung fuer die Approximation exp(x) und dem exakten Wert anhand des ersten Algorithmuses, bei der die beiden letzten Summen (y_k*) gleich (y_k+1*), ist: ")  
                print('%70.40f' % a)
                
            while True:
                print("")
                nochmal = raw_input("Moechten Sie das Programm weiter ausfuehren? Geben Sie 'ja' oder 'nein' ein: ")
                if nochmal == 'ja':
                    print("")
                    break
                if nochmal == 'nein':
                    schalter = False
                    break
        
            
            
        
    



