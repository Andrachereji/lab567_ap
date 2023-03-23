from Domain.rezervare import get_pret,get_clasa
def get_pret_max_clase(lst_rezervari):
    '''
    Determina pretul maxim pentru fiecare clasa
    :param lst_rezervari: lista de rezervari
    :return: un dictionar cu maximele pentru fiecare clasa
    '''
    result={}
    maxbusiness=0
    maxeconomy=0
    maxeconomyplus=0
    for rezervare in lst_rezervari:
        if get_clasa(rezervare)=='business':
            maxbusiness=max(maxbusiness,get_pret(rezervare))
        elif get_clasa(rezervare)=='economy':
            maxeconomy=max(maxeconomy,get_pret(rezervare))
        else:
            maxeconomyplus=max(maxeconomyplus,get_pret(rezervare))
    return {
        'economy':maxeconomy,
        'business':maxbusiness,
        'economy_plus':maxeconomyplus
    }