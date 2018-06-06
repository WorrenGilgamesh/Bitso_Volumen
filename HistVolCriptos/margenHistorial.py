import sys, os
import re
import time
import datetime

def volBitsoHistorial(moneda):
    
    pathname = os.path.dirname(sys.argv[0])
    nombre = 'volumen_'+moneda+'.txt'
    f2 = open( pathname+nombre,"r" )
    margen = 0.0
    for line in f2:
        #print line
        precio=re.search(r'(price=.\d+.\d+)', line).group()
        precio= float(re.search(r'(\d+.+)', precio).group())
        monto=re.search(r'(amount=.\d*.\d+)', line).group()
        monto= float(re.search(r'(\d+.+)', monto).group())
        margen+= precio*monto

    return margen*0.01

def volBitsoHistorial2(moneda):
    
    pathname = os.path.dirname(sys.argv[0])
    nombre = 'volumen_'+moneda+'.txt'
    f2 = open( pathname+"/"+nombre,"r" )
    margen = 0.0
    for line in f2:
        #print line
        precio=re.search(r'(price=.\d+.\d+)', line)
        if precio != None:
            precio=precio.group()
            precio= float(re.search(r'(\d+.+)', precio).group())
        monto=re.search(r'(amount=.\d*.\d+)', line)
        if monto != None:
            monto=monto.group()
            monto= float(re.search(r'(\d+.+)', monto).group())
            margen+= precio*monto
    return margen

pathname = os.path.dirname(sys.argv[0])
while True:
    with open(pathname+"/ganacias.txt", 'a') as d:
        d.write(str(datetime.datetime.now())+'\n')
        d.write('btc_mxn: ' +str(volBitsoHistorial2('btc_mxn')*0.01)+'\n')
        d.write('eth_mxn: ' +str(volBitsoHistorial2('eth_mxn')*0.01)+'\n')
        d.write('xrp_mxn: ' +str(volBitsoHistorial2('xrp_mxn')*0.008)+'\n')
        d.write('ltc_mxn: ' +str(volBitsoHistorial2('ltc_mxn')*0.005)+'\n')
        d.write('bch_mxn: ' +str(volBitsoHistorial2('bch_mxn')*0.005)+'\n')
        d.write('Total: '+str(volBitsoHistorial2('btc_mxn')*0.01+volBitsoHistorial2('eth_mxn')*0.01+volBitsoHistorial2('xrp_mxn')*0.008+volBitsoHistorial2('ltc_mxn')*0.005+volBitsoHistorial2('bch_mxn')*0.005)+'\n')
        d.close()
    time.sleep(60*60)
