def buoy(LTS, c):
    valc = LTS[c]
    j=c
    print("c:",c, "- valc:", valc )

    while (j>0) and (valc < LTS[j-1]):
        j = j - 1

    pCible = j
    if (pCible<c):
        del LTS[c]
        LTS.insert(pCible, valc)

    print(LTS)
    return


def triliste(LTS):
    N = len(LTS)
    for i in range(1, N):
        buoy(LTS,i)
    return


'''
chi = [11,15,2,19,17,6,4,1]
triliste(chi)
print('le resultat est : ', chi)

'''


