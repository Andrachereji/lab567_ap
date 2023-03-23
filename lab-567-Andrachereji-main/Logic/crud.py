from Domain.rezervare import creeaza_rezervare, get_id, get_nume,get_pret,get_checkin,get_clasa

def adaugare(lst_rezervari, id_rezervare, nume, clasa, pret, checkin,undo_lst, redo_lst):
    '''
    Adauga o noua rezervare la lista
    :param lst_rezervari:lista de rezervari
    :param id_rezervare:id-ul rezervarii
    :param nume:numele rezervarii
    :param clasa:clasa rezervasrii(economy/economy plus/buisness)
    :param pret:pretul rezervarii
    :param checkin:verificare checkin(Da/Nu)
    :param undo_lst:pastreaza lista initiala
    :param redo_lst:reface modificarile daca s-a facut undo inainte
    :return:lista de rezervari dupa adaugarea noi rezervari
    '''
    if read(lst_rezervari,id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')
    rezervare=creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return lst_rezervari + [rezervare]
def read(lst_rezervari, id_rezervare=None):
    '''
    Citeste o rezervare din "baza de date"
    :param lst_rezervari:lista de rezervari
    :param id_rezervare:id-ul rezervarii dorite
    :return:-rezervarea cu id-ul id_rezervare daca exista
            -toata lista de rezervari daca id_rezervare=None
            -None daca nu exista o rezervare cu id_rezervare
    '''
    if not id_rezervare:
        return lst_rezervari
    rezervare_cu_id=None
    for rezervare in lst_rezervari:
        if get_id(rezervare)==id_rezervare:
            rezervare_cu_id=rezervare
    if rezervare_cu_id:
        return rezervare_cu_id
    return None
def modificare(lst_rezervari, new_rezervare,undo_lst, redo_lst):
    '''
    Modifica o rezervare
    :param lst_rezervari:lista de rezervari
    :param new_rezervare:rezervarea care se va modifica, id-ul trebiue sa fie unul existent!
    :param undo_lst:pastreaza rezervarile nemodificate
    :param redo_lst:reface modificarile daca s-a facut undo inainte
    :return:o lista cu rezervarea modificata
    '''
    if read(lst_rezervari,get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {get_id(new_rezervare)} pe care sa o modificam')
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare)!=get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return new_rezervari

def stergere(lst_rezervari, id_rezervare,undo_lst,redo_lst):
    '''
    Sterge din lista de rezervari o rezervare cu un id dat
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii pe care dorim sa o stergem
    :param undo_lst:pastreaza lista cu rezervarile initiale
    :param redo_lst:reface modificarile daca s-a facut undo inainte
    :return: o lista fara rezervarea cu id-ul id_rezervare
    '''
    if read(lst_rezervari,id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare} pe care sa o stergem')
    new_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare)!=id_rezervare:
            new_rezervari.append(rezervare)
    undo_lst.append(lst_rezervari)
    redo_lst.clear()
    return new_rezervari



