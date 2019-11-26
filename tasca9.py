#-*- coding: utf8 -*-
#4523

#40 / 2 = 20
#40 / 2 = 10
from multiprocessing import Pool
from datetime import datetime

def primers(num):
    for i in range(2, num/3):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    pool = Pool(processes=8)
    l = range(4000000, 4000100)
    start = datetime.now()

    for i in pool.map(primers,l):
        for j in l:

            print i,j
    print datetime.now() - start



#1 = 04.852186
#2 = 03.531473
#3 = 02.311786
#4 = 01.699859
#5 = 01.585318
#6 = 01.537248
#7 = 01.536813
#8 = 01.544057


# Al executar els diversos els diversos processos podem observar com s'executa cada
# veguada més rápid. Al principi la millora és molt dràstica, però cada cop que
# s'executa entra en un rendiment decreixent i cada cop la millora en el temps
# d'execució és menor.
