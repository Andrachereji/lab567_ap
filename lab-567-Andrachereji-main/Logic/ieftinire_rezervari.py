from Domain.rezervare import get_checkin,get_pret,creeaza_rezervare,get_id,get_nume,get_clasa
def get_ieftinire_rezervari(lst_rezervari, procentaj,undo_lst,redo_lst):
    '''
    Iefineste rezervarile la care checkin-ul este facut cu procentajul "procentaj"
    :param lst_rezervari:lista de rezervari
    :param procentaj:procentajul cu care se face ieftinirea (intre 0 si 100)
    :param undo_lst:pastreaza lista cu rezervarile nemodificate
    :param redo_lst:reface modificarile daca s-a facut undo inainte
    :return:o lista cu modificatrile cerute
    '''
    if not (0<=procentaj<=100):
        raise ValueError('procentajul trebuie sa fie intre 0 si 100')
    result=[]
    for rezervare in lst_rezervari:
        if get_checkin(rezervare)=='Da':
            new_pret=get_pret(rezervare)-((procentaj/100) * get_pret(rezervare))
            new_rezervare = creeaza_rezervare(get_id(rezervare), get_nume(rezervare),get_clasa(rezervare),new_pret,
                                              get_checkin(rezervare))
            result.append(new_rezervare)
        else:
            result.append(rezervare)
    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return result


