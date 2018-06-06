import bitso
import sys, os
import re
import time

api = bitso.Api()
pathname = os.path.dirname(sys.argv[0])

def creaDoc(moneda):
    nombre = 'volumen_'+moneda+'.txt'
    trades = api.trades(moneda,limit = '100')
    for p in reversed(trades):
        with open(pathname+"/"+nombre, 'a') as f:
            print >> f, p
        f.close()

def historialVolumen(moneda):
    nombre = 'volumen_'+moneda+'.txt' 
    
    #creaDoc(moneda)
    
    def difer(trades,indice):
        f2 = open( pathname+"/"+nombre,"r" )
        line = f2.readlines() #lee todas las lineas en el archivo
        linea=line[-1]  # ultima linea documento (ultima transaccion historial)
        linea=re.search(r'(tid=.\d*)', linea).group()
        id= int(re.search(r'(\d+)', linea).group())
        diferencia= trades[0+indice].tid-id
        return diferencia

    while True:
        trades = api.trades(moneda,limit = '100')
        num=difer(trades,0)
        #print 'diferencia ',num
        if num !=0 and num<101: #encuentra una diferencia y entra
            with open(pathname+"/num.txt", 'a') as d:
                d.write(moneda+': '+str(num)+'\n')
            d.close()
            indice=1
            while difer(trades,indice) !=0:
                    indice+=1
            indice-=1
            while indice>=0:
                with open(pathname+"/"+nombre, 'a') as f:
                    f.write(str(trades[indice])+'\n')
                f.close()
                indice-=1       
        time.sleep(5)

historialVolumen('xrp_mxn')