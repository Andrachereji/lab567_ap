from Domain.rezervare import get_id,get_nume,get_pret,get_checkin,creeaza_rezervare
def modificare_clasa(lst_rezervari, nume,undo_lst,redo_lst):
    '''
    Inlocuieste clasa rezervarilor facute pe numele "nume" cu o clasa superioara
    :param lst_rezervari: lista de rezervari
    :param nume:numele a caror rezervari vor fi modificate
    :param undo_lst:pastreaza lista de rezervari nemodifiata
    :param redo_lst:reface modificarile daca s-a facut undo inainte
    :return: o lista cu modificarea clasei rezervailor facute pe numele "nume"
    '''
    if nume=='':
        raise ValueError('Nu ati introdus nici un nume')
    ok=0
    for rezervare in lst_rezervari:
        if get_nume(rezervare)==nume:
            ok=1
    if ok==0:
        raise ValueError('Nu exista rezervari pe acest nume')
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_nume(rezervare)==nume:
             new_rezervare=creeaza_rezervare(get_id(rezervare), get_nume(rezervare),'business',get_pret(rezervare),get_checkin(rezervare))
             new_rezervari.append(new_rezervare)
        else:
            new_rezervari.append(rezervare)
    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return new_rezervari