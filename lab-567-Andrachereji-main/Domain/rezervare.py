def creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin):
    '''
    Creeaza o rezervare la o companie aeriana
    :param id_rezervare:id-ul rezerevarii, trebuie sa fie unic
    :param nume:numele clientului care face rezervarea, nenul
    :param clasa:clasa la care este repartizat clientul (ecnomy/economy plus/buisness)
    :param pret:pretul rezervarii
    :param checkin:daca este facut checkin (Da/Nu)
    :return:o rezervare
    '''
    return (id_rezervare,nume,clasa,pret,checkin)
def get_id(rezervare):
    '''
    Getter pentru id-ul rezervarii
    :param rezervare: rezervarea
    :return:id-ul rezervarii date ca parmetru
    '''
    return rezervare[0]
def get_nume(rezervare):
    '''
    Getter pentru numele din rezervare
    :param rezervare: rezervarea
    :return: numele rezervarii dat ca parametru
    '''
    return rezervare[1]
def get_clasa(rezervare):
    '''
    Getter pentru clasa selectata in rezervare
    :param rezervare: rezervarea
    :return: clasa selectata in rezervare data ca parametru
    '''
    return rezervare[2]
def get_pret(rezervare):
    '''
    Getter pentru pretul rezervarii
    :param rezervare: rezervarea
    :return: pretul rezervarii dat ca parametru
    '''
    return rezervare[3]
def get_checkin(rezervare):
    '''
    Getter pentru verificarea checkin-ului din rezervare
    :param rezervare: rezervarea
    :return: checkinul facut dat ca prametru
    '''
    return rezervare[4]
def get_str(rezervare):
    return f'Rezervarea cu id-ul:{get_id(rezervare)} facuta de clientul:{get_nume(rezervare)} clasa:{get_clasa(rezervare)} pretul:{get_pret(rezervare)} checkin:{get_checkin(rezervare)}'

