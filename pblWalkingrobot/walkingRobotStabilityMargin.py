# z座標についてはRunTimeErrorが発生してしまうためコメントアウトしているが、安定性判別には無視してしまっても構わない。

from tokenize import PlainToken
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

M = 0.5
md = 0.1
ml1 = 0.1
ml2 = 0.1

L = 0.13
D = 0.1
d = 0.06
l1 = 0.07
l2 = 0.14
e = 0.0

def legCrdin(type, c, phi):
    if type == "dg":
        if c == "x":
            leg = d*np.sqrt(1-(e/L)**2)*np.sin(phi)/2
        elif c == "y":
            leg = -d*np.sqrt(1-(e/L)**2)*np.cos(phi)/2
        #else:
            #leg = 0

        return leg

    elif type == "d":
        if c == "x":
            leg = d*np.sqrt(1-(e/L)**2)*np.sin(phi)
        elif c == "y":
            leg = -d*np.sqrt(1-(e/L)**2)*np.cos(phi)
        #else:
            #leg = 0

        return leg

    elif type == "l1g":
        if c == "x":
            x = legCrdin("d", "x", phi)
            leg = x + np.sqrt(2)*l1*np.sin(phi)*np.sqrt(1-(e/L)**2)/4
        elif c == "y":
            y = legCrdin("d", "y", phi)
            leg = y - np.sqrt(2)*l1*np.cos(phi)*np.sqrt(1-(e/L)**2)/4
        #else:
            #z = legCrdin("d", "z", phi)
            #leg = z + np.sqrt(2)*l1/4

        return leg
    
    elif type == "l1":
        if c == "x":
            x = legCrdin("d", "x", phi)
            leg = x + np.sqrt(2)*l1*np.sin(phi)*np.sqrt(1-(e/L)**2)/2
        elif c == "y":
            y = legCrdin("d", "y", phi)
            leg = y - np.sqrt(2)*l1*np.cos(phi)*np.sqrt(1-(e/L)**2)/2
        #else:
            #z = legCrdin("d", "z", phi)
            #leg = z + np.sqrt(2)*l1/2
        
        return leg

    elif type == "l2g":
        if c == "x":
            x = legCrdin("l1", "x", phi)
            leg = x - l2*np.sqrt(1-(e/L)**2)*np.sin(phi)*((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))/2
        elif c == "y":
            y = legCrdin("l1", "y", phi)
            leg = y + l2*np.sqrt(1-(e/L)**2)*np.cos(phi)*((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))/2
        #else:
            #z = legCrdin("l1", "z", phi)
            #leg = z - l2*np.sqrt(1-((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))**2)/2

        return leg

    else:
        if c == "x":
            x = legCrdin("l1", "x", phi)
            leg = x - l2*np.sqrt(1-(e/L)**2)*np.sin(phi)*((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))
        elif c == "y":
            y = legCrdin("l1", "y", phi)
            leg = y + l2*np.sqrt(1-(e/L)**2)*np.cos(phi)*((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))
        #else:
            #z = legCrdin("l1", "z", phi)
            #leg = z - l2*np.sqrt(1-((l1*np.sqrt(2)*(1-np.sin(phi))/(2*l2*np.sin(phi))))**2)

        return leg

def gCrdin(c):
    g = (md*(legCrdin("dg", c, phiFR)+legCrdin("dg", c, phiFL)+legCrdin("dg", c, phiBR)+legCrdin("dg", c, phiBL)) + ml1*(legCrdin("l1g", c, phiFR)+legCrdin("l1g", c, phiFL)+legCrdin("l1g", c, phiBR)+legCrdin("l1g", c, phiBL)) + ml2*(legCrdin("l2g", c, phiFR)+legCrdin("l2g", c, phiFL)+legCrdin("l2g", c, phiBR)+legCrdin("l2g", c, phiBL)))/(M+4*md+4*ml1+4*ml2)

    return g

phiFR = np.array([pi/2, 5*pi/6, 2*pi/3,  2*pi/3, 2*pi/3, pi/2])
phiFL = np.array([-2*pi/3, -2*pi/3, -pi/2, -pi/2, -5*pi/6, -2*pi/3])
phiBR = np.array([pi/2, pi/2, pi/3, pi/3, pi/6, pi/2])
phiBL = np.array([-pi/3, -pi/3, -pi/6, -pi/2, -pi/2, -pi/3])

xlegFR = D*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "x", phiFR)*np.sqrt(1-(e/L)**2)
ylegFR = L*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "y", phiFR)*np.sqrt(1-(e/L)**2)
#zlegFR = legCrdin("l2", "z", phiFR)
xlegFL = -D*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "x", phiFL)*np.sqrt(1-(e/L)**2)
ylegFL = L*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "y", phiFL)*np.sqrt(1-(e/L)**2)
#zlegFL = legCrdin("l2", "z", phiFL)
xlegBR = D*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "x", phiBR)*np.sqrt(1-(e/L)**2)
ylegBR = -L*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "y", phiBR)*np.sqrt(1-(e/L)**2)
#zlegBR = legCrdin("l2", "z", phiBR)
xlegBL = -D*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "x", phiBL)*np.sqrt(1-(e/L)**2)
ylegBL = -L*np.sqrt(1-(e/L)**2)/2 + legCrdin("l2", "y", phiBL)*np.sqrt(1-(e/L)**2)
#zlegBL = legCrdin("l2", "z", phiBL)

xg = gCrdin("x")
yg = gCrdin("y")
#zg = gCrdin("z")

def plotStability(num):
    if num == 0 or num == 3:
        xNum = [xlegFR[num], xlegFL[num], xlegBL[num], xlegBR[num], xlegFR[num]]
        yNum = [ylegFR[num], ylegFL[num], ylegBL[num], ylegBR[num], ylegFR[num]]
    elif num == 1:
        xNum = [xlegFL[num], xlegBL[num], xlegBR[num], xlegFL[num]]
        yNum = [ylegFL[num], ylegBL[num], ylegBR[num], ylegFL[num]]
    elif num == 2:
        xNum = [xlegFR[num], xlegFL[num], xlegBR[num], xlegFR[num]]
        yNum = [ylegFR[num], ylegFL[num], ylegBR[num], ylegFR[num]]  
    elif num == 4:
        xNum = [xlegFR[num], xlegBL[num], xlegBR[num], xlegFR[num]]
        yNum = [ylegFR[num], ylegBL[num], ylegBR[num], ylegFR[num]]
    elif num == 5:
        xNum = [xlegFR[num], xlegFL[num], xlegBL[num], xlegFR[num]]
        yNum = [ylegFR[num], ylegFL[num], ylegBL[num], ylegFR[num]]

    ax[num].plot(xg[num], yg[num], marker = ".", markersize = 5)
    ax[num].plot(xNum, yNum)
    plt.xlim(-0.5, 0.5)
    plt.ylim(-0.5, 0.5)

def calculateMargin(num):
    if num == 0 or num == 3:
        mgn = (xg[num]*(ylegFL[num]-ylegFR[num])-yg[num]*(xlegFL[num]-xlegFR[num])+xlegFL[num]*ylegFR[num]-xlegFR[num]*ylegFL[num])/np.sqrt((ylegFL[num]-ylegFR[num])**2+(xlegFL[num]*ylegFR[num]-xlegFR[num]*ylegFL[num])**2)
    elif num == 1 or num == 2:
        mgn = (xg[num]*(ylegFL[num]-ylegBR[num])-yg[num]*(xlegFL[num]-xlegBR[num])+xlegFL[num]*ylegBR[num]-xlegBR[num]*ylegFL[num])/np.sqrt((ylegFL[num]-ylegBR[num])**2+(xlegFL[num]*ylegBR[num]-xlegBR[num]*ylegFL[num])**2)
    else:
        mgn = (xg[num]*(ylegFR[num]-ylegBL[num])-yg[num]*(xlegFR[num]-xlegBL[num])+xlegFR[num]*ylegBL[num]-xlegBL[num]*ylegFR[num])/np.sqrt((ylegFR[num]-ylegBL[num])**2+(xlegFR[num]*ylegBL[num]-xlegBL[num]*ylegFR[num])**2)

    return mgn

print("e = " + str(e))

fig, ax = plt.subplots(1, 6, figsize = (15,5))
for i in range(6):
    plotStability(i)
    margin = calculateMargin(i)
    print("xg = " + str(xg[i]))
    print("yg = " + str(yg[i]))
    print("margin" + str(i) + ": " + str(margin))
    print("\n")
plt.show()