from Logic.ordonare_dupa_pret import ordonare
from Domain.rezervare import get_pret,creeaza_rezervare
def get_data():
    return [
        creeaza_rezervare(1, 'r1', 'economy', 200, 'Da'),
        creeaza_rezervare(2, 'r2', 'business', 1200, 'Da'),
        creeaza_rezervare(3, 'r3', 'economy', 500, 'Nu'),
        creeaza_rezervare(4, 'r4', 'economy_plus', 800, 'Da'),
        creeaza_rezervare(5, 'r5', 'business', 1400, 'Nu'),
        creeaza_rezervare(6,'r6','economy_plus',600,'Nu')
    ]
def test_ordonare():
    rezervari=get_data()
    result=ordonare(rezervari)
    assert get_pret(result[2])<get_pret(result[1])
    assert get_pret(result[0])>get_pret(result[5])