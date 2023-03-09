#  1.  Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

#  2.  Aprašykite tikslo funkciją f(x) = (x2−a)2/b−1, čia a ir b – studento knygelės numerio “1*1**ab” skaitmenys.

#  3   Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10−4 
#      bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4. (0.0004)

#  4.  Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.
#      Vizualizuokite tikslo funkciją ir bandymo taškus.
    #################################
    #                             - #
    # -                        -    #
    #   -                   -       #
    #      -   -   -  -  -          #
    # |        |        |         | #
    # a        x1      x1         b #
    #################################
#is pavyzdzio:
#l = 0, r = 10, pi = gr, 
# L = r - 0
from cProfile import label
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
 #for golden slice and interval slice

def f(x):
    return (math.pow((math.pow(x,2)-4),2))/6

def printData(a, intervalA, intervalx1, intervalXm, intervalx2, intervalB, fx1Reiksme, fxmReiksme, fx2Reiksme):
       if a == "gold":
            print("A: ", intervalA)
            print("X1: ", intervalx1)
            print("X2: ", intervalx2)
            print("B: ", intervalB)
            print("Fx1: ", fx1Reiksme)
            print("Fx2: ", fx2Reiksme)
       elif a == "split":
            print("A: ", intervalA)
            print("X1: ", intervalx1)
            print("Xm: ", intervalXm)
            print("X2: ", intervalx2)
            print("B: ", intervalB)
            print("Fx1: ", fx1Reiksme)
            print("Fxm", fxmReiksme)
            print("Fx2: ", fx2Reiksme)

def goldenSearch(intervalA, intervalB):
    #for c in range(10):
    GR = (math.sqrt(5) - 1)/2
    for iteratorius in range(100):
        print("iteracija nr:", iteratorius+1)
        L = intervalB - intervalA  # GR * (Intervalo pabaiga - Intervalo pradzia) # CIA YRA L
        intervalx1 = intervalB - GR * L
        intervalx2 = intervalA + GR * L
        fx1Reiksme = f(intervalx1)
        fx2Reiksme = f(intervalx2)
        round(fx1Reiksme, 4)
        round(fx2Reiksme, 4)
        printData("gold",intervalA, intervalx1, intervalx2, 0 ,intervalB, fx1Reiksme,0, fx2Reiksme)
        if(L < 0.0001):
            break
        if fx1Reiksme < fx2Reiksme:
            intervalB = intervalx2   
        elif fx1Reiksme > fx2Reiksme:
            intervalA = intervalx1
def firstDegreeDerivative(x):
    #x = symbols('x')
   ## f = (math.pow((math.pow(x,2)-4),2))/6
    #f = (((x*x)-4)*((x*x)-4))/6
    #fderivative = f.diff(x)

    return ((2*x*((x**2)-4))/3)
    print(fderivative)
def secondDegreeDerivative(x):
    return (((6*x**2)-8))/3
#def derivative1(skaicius):
#    x = symbols('x')
#    #f = ((math.pow((math.pow(x,2)-4),2))/6)
#    f = (((x**2)-4)**2)/6
#    fderivative = f.diff(x)
#    fderivative2 = fderivative.diff(x)
#    return fderivative
#def derivative2(skaicius):
#    x = symbols('x')
#    x=skaicius
#    #f = ((math.pow((math.pow(x,2)-4),2))/6)
#    f = (((x**2)-4)**2)/6
#    fderivative = f.diff(x)
#    #fderivative2 = fderivative.diff(x)
#    return fderivative
#def newtonsMethod2(x0):
##Xi+1 = xi - (f'(xi))/(f''(xi))
#    
#    for iteratorius in range(1000):
#        print("iteracija: ", iteratorius+1)
#        print(x0)
#        theOneBefore = x0
#        x0 = theOneBefore - ((derivative1(theOneBefore))/(derivative2(theOneBefore)))
#        zingsnioIlgis = theOneBefore - x0
#        print("Zingsnio ilgis: ", zingsnioIlgis)
#        if(zingsnioIlgis < 0.0004):
#            break
#
def newtonsMethod1(x0):
#Xi+1 = xi - (f'(xi))/(f''(xi))
    
    for iteratorius in range(1000):
        print("iteracija: ", iteratorius+1)
        print(f"reiksme x{iteratorius} : ", x0)
        theOneBefore = x0
        x0 = theOneBefore - ((firstDegreeDerivative(theOneBefore))/(secondDegreeDerivative(theOneBefore)))
        zingsnioIlgis = theOneBefore - x0
        print("Zingsnio ilgis: ", zingsnioIlgis)
        if(zingsnioIlgis < 0.0002):
            break





def sectionSearch(intervalA, intervalB):
    # intervalA = l  # intervalB = r
    for iteratorius in range(50):
        print("iteracija nr:", iteratorius+1)
        intervalxm = (intervalA+intervalB)/2
        L = intervalB - intervalA
        intervalx1 = intervalA + (L/4)
        intervalx2 = intervalB - (L/4)
        fx1Reiksme = f(intervalx1)
        fx2Reiksme = f(intervalx2)
        fxmReiksme = f(intervalxm)
        printData("split",intervalA, intervalx1, intervalxm, intervalx2, intervalB, fx1Reiksme,fxmReiksme, fx2Reiksme) 
        if fx1Reiksme < fxmReiksme:
            intervalB = intervalxm
            intervalxm = intervalx1
        elif fx2Reiksme < fxmReiksme:
            intervalA = intervalxm
            intevalxm = intervalx2
        elif fx1Reiksme >= fxmReiksme and fx2Reiksme >= fxmReiksme:
            intervalA = intervalx1
            intervalB = intervalx2
        else:
             print("Klaida")
        if(L < 0.000001):
            break


def plot_goldSection(a, b, x1, x2):

        #plot x1 point
    xlist = np.linspace(1.6,2.3, num = 100)
    fxfunc = np.vectorize(f)
    ylist = fxfunc(xlist)
    #plt.ylim(-50,50)
    #plt.figure(dpi = 120)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 1.6))
    ax.spines['bottom'].set_position(('data', 0.0))
    #ax.spines['top'].set_bounds((0,5.25))
    ax.spines['right'].set_color('0')
    ax.spines['top'].set_color('0')
    plt.ylim(0,0.1)
    plt.plot(xlist, ylist)
    plt.grid()

    plt.plot(a,f(a),'go',label='a')
    plt.plot([a,a],[0,f(a)],'k', color = "g", label='_nolegend_')


    plt.plot(x1,f(x1),'ro',label='x1')
    plt.plot([x1,x1],[0,f(x1)],'k',color = "r",label='_nolegend_')
    

    plt.plot(x2,f(x2),'bo',label='x2')
    plt.plot([x2,x2],[0,f(x2)],'k', color = "b", label='_nolegend_')


    plt.plot(b,f(b),'yo',label='b')
    plt.plot([b,b],[0,f(b)],'k', color = "y", label='_nolegend_')

    plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$",f"a = {a}", f"x1 = {x1}", f"x2 = {x2}", f"b = {b}"])
    #plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$,"])

    plt.xlabel("X ašis", labelpad = 40)
    plt.ylabel("y ašis")
    plt.title("Auksinis pjūvis, 8 iteracija")
    plt.show()


def plot_sectionSearch(a, b, x1, xm ,x2):

        #plot x1 point
    xlist = np.linspace(1.95,2.035, num = 100)
    fxfunc = np.vectorize(f)
    ylist = fxfunc(xlist)
    #plt.ylim(-50,50)
    #plt.figure(dpi = 120)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 1.95))
    ax.spines['bottom'].set_position(('data', 0.0))
    #ax.spines['top'].set_bounds((0,5.25))
    ax.spines['right'].set_color('0')
    ax.spines['top'].set_color('0')
    plt.ylim(0,0.008)
    plt.plot(xlist, ylist)
    plt.grid()

    plt.plot(a,f(a),'go',label='a')
    plt.plot([a,a],[0,f(a)],'k', color = "g", label='_nolegend_')


    plt.plot(x1,f(x1),'ro',label='x1')
    plt.plot([x1,x1],[0,f(x1)],'k',color = "r",label='_nolegend_')
    
    plt.plot(xm,f(xm),'co',label='xm')
    plt.plot([xm,xm],[0,f(xm)],'k', color = "c", label='_nolegend_')

    plt.plot(x2,f(x2),'bo',label='x2')
    plt.plot([x2,x2],[0,f(x2)],'k', color = "b", label='_nolegend_')

    plt.plot(b,f(b),'yo',label='b')
    plt.plot([b,b],[0,f(b)],'k', color = "y", label='_nolegend_')

    #plt.plot(x1,f(x1),'ro',label='x1')
    #plt.plot([x1,x1],[0,f(x1)],'k')

    plt.xlabel("X ašis", labelpad = 40)
    plt.ylabel("y ašis")
    plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$",f"a = {a}", f"x1 = {x1}",f"xm = {xm}", f"x2 = {x2}", f"b = {b}"], prop = {'size': 8})
    #plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$"])
    plt.title("Intervalo Dalijimas pusiau, 8 iteracija")
    plt.show()


    #plt.plot(xlist,ylist)
    #for iteratorius in range(100):
    #    temp += 0.1
    #    print(temp)
    #    #arrayX.append(temp)
    #    #arrayY.append(f(temp))
    #plot(xlist, ylist)
    #plt.xlabel('x - axis')
    #plt.ylabel('y - label')
    #plt.title('my first graph naxui!')
    #plt.show()
def plotNewton(x0, x1):

        #plot x1 point
    xlist = np.linspace(1.9997,2.0005, num = 100)
    fxfunc = np.vectorize(f)
    ylist = fxfunc(xlist)
    #plt.ylim(-50,50)
    #plt.figure(dpi = 120)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 1.9997))
    ax.spines['bottom'].set_position(('data', 0.0))
    #ax.spines['top'].set_bounds((0,5.25))
    ax.spines['right'].set_color('0')
    ax.spines['top'].set_color('0')
    plt.ylim(0,0.0000005)
    plt.plot(xlist, ylist)
    plt.grid()

    plt.plot(x0,f(x0),'go',label='a')
    plt.plot([x0,x0],[0,f(x0)],'k', color = "g", label='_nolegend_')

    plt.plot(x1,f(x1),'ro',label='x1')
    plt.plot([x1,x1],[0,f(x1)],'k',color = "r",label='_nolegend_')
    
    # plt.plot(xm,f(xm),'co',label='xm')
    # plt.plot([xm,xm],[0,f(xm)],'k', color = "c", label='_nolegend_')

    # plt.plot(x2,f(x2),'bo',label='x2')
    # plt.plot([x2,x2],[0,f(x2)],'k', color = "b", label='_nolegend_')

    # plt.plot(b,f(b),'yo',label='b')
    # plt.plot([b,b],[0,f(b)],'k', color = "y", label='_nolegend_')

    #plt.plot(x1,f(x1),'ro',label='x1')
    #plt.plot([x1,x1],[0,f(x1)],'k')

    plt.xlabel("X ašis", labelpad = 40)
    plt.ylabel("y ašis")
    plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$",f"x5 = {x0}", f"x6 = {x1}"])
    #plt.legend([r"f(x) = $\frac{(x^2 - 4)^2}{6}$"])
    plt.title("Niutono metodas, 6 iteracija")
    plt.show()

#goldenSearch(0, 10)
#sectionSearch(0,10)
#plot_sectionSearch(1.953125 , 2.03125 ,1.97265625 , 1.9921875 , 2.01171875)
#print(firstDegreeDerivative())
#func2 = secondDegreeDerivative(func)
#newtonsMethod1(5)
#newtonsMethod2(5)
#plot_something()
plotNewton(2.000251, 2.000000047)
#sectionSearch(0,10)
#plot_goldSection(1.803398,2.147817,1.934955,2.016261)
