from Tests.test_crud import get_data
from Logic.crud import read
from Domain.rezervare import get_clasa
from Logic.trecere_clasa_superioara import modificare_clasa
from Logic.undo_redo import do_redo,do_undo
def test_modificare_clasa():
    rezervari=get_data()
    nume='r1'
    undo_lst=[]
    redo_lst=[]
    r_clasa=read(rezervari,1)
    r_modificata=modificare_clasa(rezervari,nume,undo_lst,redo_lst)
    r_modificata=do_undo(undo_lst,redo_lst,r_modificata)
    r_new_clasa = read(r_modificata, 1)
    assert get_clasa(r_clasa)==get_clasa(r_new_clasa)
    r_modificata=do_redo(undo_lst,redo_lst,r_modificata)
    r_new_clasa = read(r_modificata, 1)
    if get_clasa(r_clasa)!='business':
        assert get_clasa(r_clasa)!=get_clasa(r_new_clasa)
    else:
        assert get_clasa(r_clasa) == get_clasa(r_new_clasa)
    try:
        modificare_clasa(rezervari,'',[],[])
        assert False
    except ValueError:
        assert True