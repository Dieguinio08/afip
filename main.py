import pyautogui
import calendar
import datetime
from PIL import Image
from time import sleep
from datetime import date


cuentaPantallas=[0,0,0,0,0,0,0,0,0,0,0,0]
meses=[]
def InicializarMeses():
    hoy = date.today()
    for y in range(2015,2022):
        for m in range(1,13):
            d=str(calendar.monthrange(y, m)[1])
            mes=str(m)
            anio=str(y)
            if (len(mes)<2):
                mes="0"+mes
            meses.append("01/"+mes+"/"+anio+" - "+d+"/"+mes+"/"+anio)
            if mes==hoy.strftime("%m") and anio==hoy.strftime("%Y"):
                break

def PantallaInicial():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(1300, 320, 400, 400))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("inicial.png").getdata()
    cuentaPantallas[0]+=1
    return(comparar (img, original))    

def PantallaCUIT():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(1200, 320, 400, 170))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("IngresarCUIT.png").getdata()
    cuentaPantallas[1]+=1
    return(comparar (img, original))    

def PantallaClave():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(1200, 320, 400, 170))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("IngresarClave.png").getdata()
    cuentaPantallas[2]+=1
    return(comparar (img, original))

def PantallaPrincipal():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(320, 140, 500, 70))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("Principal.png").getdata()
    cuentaPantallas[3]+=1
    return(comparar (img, original))    

def PantallaMisComprobantes():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(320, 140, 500, 70))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("MisComprobantes.png").getdata()
    return(comparar (img, original))

def PantallaMisComprobantesEmitidos():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(350, 500, 60, 60))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("MisComprobantesEmitidos.png").getdata()
    return(comparar (img, original))

def PantallaMisComprobantesEmitidosEncontrados():
    pyautogui.moveTo(5, 500, duration = 0)
    temp=pyautogui.screenshot(region=(450, 660, 30, 30))
    temp.save("temp.png")
    img = Image.open("temp.png").getdata()
    original=Image.open("MisComprobantesEmitidosEncontrados.png").getdata()
    return(comparar (img, original))

def comparar (img, original): 
    d = 0
    for pixel_a, pixel_b in zip(img, original):
        if pixel_a != pixel_b:
            d += 1
    if d < 10:
        return (True)
    else:
        return (False)
def buscarNaranja(x):
    rto=(0,0)
    img=pyautogui.screenshot(region=(x, 200, 1, 750))
    img.save("temp.png")
    img= Image.open("temp.png").getdata()
    naranja=(255,150,50)
    i=0
    for y in range(749):
        c=0,y
        px=img.getpixel(c)
        if px==naranja:
            i=y+200   
            break
    if i>0:
        rto=(x,i)
    return rto
def descargarMes(mes):
    sleep(1)
    if PantallaMisComprobantes()==True:
        pyautogui.click(500, 500)
    if PantallaMisComprobantesEmitidos()==True:
        pyautogui.click(450, 520)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(mes)
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["enter"])
    if PantallaMisComprobantesEmitidosEncontrados()==True:
        pyautogui.click(450, 660)
        pyautogui.click(400, 400)


def descargarMisComprobantes():
    sleep(1)
    if PantallaInicial()==True:
        pyautogui.click(1500, 550)
    if PantallaCUIT()==True :
        pyautogui.click(1400, 550)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite(cuit)
        pyautogui.typewrite(["enter"])
    if PantallaClave()==True:
        pyautogui.typewrite(["enter"])
    if PantallaPrincipal()==True:
        pyautogui.hotkey("ctrl", "f")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.typewrite("Mis Comprobantes")
        columnas=[450,900,1400]
        for j in columnas:
            c=buscarNaranja(j)
            if c!=(0,0):
                pyautogui.click(c)
                break
    if PantallaMisComprobantes()==True:
        for i in meses:
            descargarMes(i)

        if i==len(meses):
            quit()

    
#end_date = datetime.datetime(2010,1,1)
#start_date = datetime.datetime(2010, 1, 1)

#num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

#print(num_months)
cuit="27375517936"
pyautogui.hotkey("alt", "tab")

#print(hoy.strftime("%Y"))
   
#i=calendar.monthrange(2021, 1)
#print(i[1])

InicializarMeses()
for i in range(8):
    descargarMisComprobantes()

#img=pyautogui.screenshot(region=(400, 400, 30, 30))
#img.show()
#img.save("MisComprobantesEmitidosEncontrados.png")

#pixel_values = list(img.getdata())
#print(pixel_values)
#c = x, y = 1, 1
#px=img.getpixel(c)
#255,150,50
#print(px)
#img.save("temp.png")
#img= Image.open('current_screen.png').getdata()
#img.show()
