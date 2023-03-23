from Logic.pret_maxim_clase import get_pret_max_clase
from Domain.rezervare import creeaza_rezervare
def get_data():
    return [
        creeaza_rezervare(1, 'r1', 'economy', 200, 'Da'),
        creeaza_rezervare(2, 'r2', 'business', 1200, 'Da'),
        creeaza_rezervare(3, 'r3', 'economy', 500, 'Nu'),
        creeaza_rezervare(4, 'r4', 'economy_plus', 800, 'Da'),
        creeaza_rezervare(5, 'r5', 'business', 1400, 'Nu'),
        creeaza_rezervare(6,'r6','economy_plus',600,'Nu')
    ]
def test_pret_max_clase():
    rezervari=get_data()
    maxime=get_pret_max_clase(rezervari)
    assert maxime['economy']==500
    assert maxime['business']==1400
    assert maxime['economy_plus']==800