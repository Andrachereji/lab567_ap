from Domain.rezervare import get_nume,get_pret
def suma_preturilor_dupa_nume(rezervari):
    '''
    Determina suma tuturor preturilor rezervarilor facute pe acelasi nume
    :param rezervari: lista de rezervari
    :return: un dictionar cu suma preturilor pentru fiecare nume
    '''
    result={}
    for i in range(len(rezervari)):
       name=get_nume(rezervari[i])
       if name in result:
           pass
       else:
           result[name] = get_pret(rezervari[i])
           for j in range(i + 1, len(rezervari)):
               if name == get_nume(rezervari[j]):
                   result[name] = result[name] + get_pret(rezervari[j])

    return result





