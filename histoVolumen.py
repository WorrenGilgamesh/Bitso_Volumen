import bitso
import sys, os
import re
import time
import threading

def historialVolumen(moneda):
    api = bitso.Api()
    pathname = os.path.dirname(sys.argv[0])
    nombre = 'volumen_'+moneda+'.txt'
    trades = api.trades(moneda,limit = '100')

    for p in reversed(trades):
        print p
        with open(pathname+"/"+nombre, 'a') as f:
            print >> f, p
        f.close()

    def difer(num):
        f2 = open( pathname+"/"+nombre,"r" )
        line = f2.readlines()
        linea=line[-num]
        linea=re.search(r'(tid=.\d*)', linea).group()
        id= int(re.search(r'(\d+)', linea).group())
        diferencia= trades[num-1].tid-id
        #print trades[num-1].tid, id
        return diferencia

    while 1>0:
        trades = api.trades(moneda,limit = '100')
        num=1
        difer(num)
        print num
        with open(pathname+"/num.txt", 'a') as d:
            d.write(moneda+': '+str(num)+'\n')
        d.close()
        while difer(num)!=0:
            difer(num)
            with open(pathname+"/"+nombre, 'a') as f:
                f.write(str(trades[num-1])+'\n')
            f.close()
            num+=1
        time.sleep(25)



t1 = threading.Thread(target=historialVolumen, args=('btc_mxn',))
t2 = threading.Thread(target=historialVolumen, args=('eth_mxn',))
t3 = threading.Thread(target=historialVolumen, args=('xrp_mxn',))
t4 = threading.Thread(target=historialVolumen, args=('ltc_mxn',))
t5 = threading.Thread(target=historialVolumen, args=('bch_mxn',))
t6 = threading.Thread(target=historialVolumen, args=('xrp_btc',))
t7 = threading.Thread(target=historialVolumen, args=('eth_btc',))
t8 = threading.Thread(target=historialVolumen, args=('bch_btc',))
t9 = threading.Thread(target=historialVolumen, args=('ltc_btc',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()