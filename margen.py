import bitso
import datetime
import decimal

api = bitso.Api()
def volBitso(moneda):
    trades = api.trades(moneda,limit = '100')
    def transHora(trades):
        trades2=[]
        tiempo1=trades[0].created_at
        for p in trades:
            tiempo2= p.created_at
            dif=tiempo1 - tiempo2
            trades2.append(p)
            if dif.seconds//3600 ==1:
                return trades2

    def margen(trades):
        margen =decimal.Decimal(0.0)
        montoT=decimal.Decimal(0.0)
        for p in trades:
            precio= p.price
            monto = p.amount
            montoT+=p.amount
            margen+= precio*monto
        #return margen*decimal.Decimal(0.1), montoT #exacto
        #return float(margen*decimal.Decimal(0.1)), float(montoT) #aproximado
        return float(margen*decimal.Decimal(0.1))
    return margen(transHora(trades))

print 'btc_mxn:' ,volBitso('btc_mxn')
print 'eth_mxn:' ,volBitso('eth_mxn')
print 'xrp_mxn:' ,volBitso('xrp_mxn')
print 'ltc_mxn:' ,volBitso('ltc_mxn')
print 'bch_mxn:' ,volBitso('bch_mxn')
print 'Total:', volBitso('btc_mxn')+volBitso('eth_mxn')+volBitso('xrp_mxn')+volBitso('ltc_mxn')+volBitso('bch_mxn')
