from Domain.rezervare import get_pret
def ordonare(rezervari):
    '''
    Ordoneaza rezervarile descrescator dupa pret
    :param rezervari: lista de rezervari
    :return: o lista cu rezervarile in ordine descrescatoare dupa pret
    '''
    result=rezervari
    for i in range(len(result)-1):
        for j in range(i+1,len(result)):
            if get_pret(result[i])<get_pret(result[j]):
                new=result[i]
                result[i]=result[j]
                result[j]=new
    return result

