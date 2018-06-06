import sys, os
import re

def promedio():
    pathname = os.path.dirname(sys.argv[0])
    nombre = '/num.txt'
    f2 = open( pathname+nombre,"r" )
    tiempo=0.0
    tiempoSuperior=0.0
    intercambios=0.0
    contador=0
    monedaSuperior=0
    for line in f2:
        moneda=line.strip().split(':')
        if  moneda[0]== 'btc_mxn' or moneda[0]=='eth_mxn' or moneda[0]=='xrp_mxn':
            tiempo+=5
            monedaSuperior+=float(moneda[1])
            tiempoSuperior+=5
        elif moneda[0]=='ltc_btc' or moneda[0]=='ltc_mxn':
            tiempo+=30
        elif moneda[0]=='bch_btc' or moneda[0]=='bch_mxn' or moneda[0]=='eth_btc' or moneda[0]=='xrp_btc':
            tiempo+=20
        intercambios+=float(moneda[1])
        contador+=1
    print tiempo
    print intercambios
    return intercambios/tiempo, monedaSuperior/tiempoSuperior

def montoTotal(moneda):
    pathname = os.path.dirname(sys.argv[0])
    nombre = '/volumen_'+moneda+'.txt'
    f2 = open( pathname+nombre,"r" )
    margen = 0.0
    count =0
    for line in f2:
        monto=re.search(r'(amount=.\d*.\d+)', line)
        if monto != None:
            monto=monto.group()
            monto= float(re.search(r'(\d+.+)', monto).group())
            margen+=monto
            count+=1
    return moneda,margen,count

def precioTotal(moneda):
    pathname = os.path.dirname(sys.argv[0])
    nombre = '/volumen_'+moneda+'.txt'
    f2 = open( pathname+nombre,"r" )
    margen = 0.0
    for line in f2:
        precio=re.search(r'(price=.\d+.\d+)', line)
        if precio != None:
            precio=precio.group()
            precio= float(re.search(r'(\d+.+)', precio).group())
            margen+=precio
    return moneda,margen

def awitchMoneda():
    pathname = os.path.dirname(sys.argv[0])
    nombre = '/num.txt'
    f2 = open( pathname+nombre,"r" )
    for line in f2:
        moneda=line.strip().split(':')
        if  moneda== 'btc_mxn':
            pass
        elif moneda=='eth_mxn':
            pass
        elif moneda=='xrp_mxn':
            pass
        elif moneda=='ltc_mxn':
            pass
        elif moneda=='bch_mxn':
            pass
        elif moneda=='ltc_btc':
            pass
        elif moneda=='bch_btc':
            pass
        elif moneda=='eth_btc':
            pass
        elif moneda=='xrp_btc':
            pass

def promedioGanaciaHour():
    pathname = os.path.dirname(sys.argv[0])
    nombre = '/ganacias.txt'
    f2 = open( pathname+nombre,"r" )
    tiempo=0.0
    ganacia=0.0
    for line in f2:
        moneda=line.strip().split(':')
        if  moneda[0]== 'Total':
            ganacia+=float(moneda[1])
            tiempo+=1
    return ganacia,tiempo

tiempo=0.0    
#print promedio()
print ('moneda montoTotal Num Transacciones')
moneda=('btc_mxn','eth_mxn','xrp_mxn','ltc_btc','ltc_mxn','bch_mxn','bch_btc','eth_btc','xrp_btc')
for m in moneda:
    print montoTotal(m)
    print precioTotal(m)
    tiempo= montoTotal(m)[2]*5
    print 'cantidad en circulacion promedio',montoTotal(m)[1]/tiempo
    print 'precio promedio',precioTotal(m)[1]/montoTotal(m)[2]
    print('===================')

print promedioGanaciaHour()
print promedioGanaciaHour()[0]/promedioGanaciaHour()[1]+2