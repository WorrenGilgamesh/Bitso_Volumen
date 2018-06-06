import sys, os
import re

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
        precio=re.search(r'(price=.\d+.\d+)', line).group()
        precio= float(re.search(r'(\d+.+)', precio).group())
        monto=re.search(r'(amount=.\d*.\d+)', line).group()
        monto= float(re.search(r'(\d+.+)', monto).group())
        margen+= precio*monto

    return margen*0.01
print 'btc_mxn:' ,volBitsoHistorial2('btc_mxn')
print 'eth_mxn:' ,volBitsoHistorial('eth_mxn')
print 'xrp_mxn:' ,volBitsoHistorial('xrp_mxn')
print 'ltc_mxn:' ,volBitsoHistorial('ltc_mxn')
print 'bch_mxn:' ,volBitsoHistorial('bch_mxn')
print 'Total:', volBitsoHistorial2('btc_mxn')+volBitsoHistorial('eth_mxn')+volBitsoHistorial('xrp_mxn')+volBitsoHistorial('ltc_mxn')+volBitsoHistorial('bch_mxn')
