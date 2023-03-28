trusis = 1
pari_nakamaja_paaudze = 0
pusgads = 0
gads = pusgads * 2
jaunie_trusi = 0
pari_kopa = 1
paris =  1

for x in range (5):
    jaunie_trusi += paris*2
    pari_kopa += jaunie_trusi
    pari_nakamaja_paaudze += pari_kopa + paris
    print ("Kopā būs",pari_kopa*2, "truši")    