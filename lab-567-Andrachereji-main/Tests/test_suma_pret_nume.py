from Logic.afisare_suma_pret_dupa_nume import suma_preturilor_dupa_nume
from Domain.rezervare import creeaza_rezervare
def get_data():
    return [
        creeaza_rezervare(1, 'r1', 'economy', 200, 'Da'),
        creeaza_rezervare(2, 'r2', 'business', 1200, 'Da'),
        creeaza_rezervare(3, 'r1', 'economy', 500, 'Nu'),
        creeaza_rezervare(4, 'r2', 'economy_plus', 800, 'Da'),
        creeaza_rezervare(5, 'r1', 'business', 1400, 'Nu'),
        creeaza_rezervare(6,'r2','economy_plus',600,'Nu')
    ]
def test_suma_preturilor_dupa_nume():
    rezervari=get_data()
    result=suma_preturilor_dupa_nume(rezervari)
    assert result['r1']==2100
    assert result['r2']==2600
