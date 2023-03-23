from Tests.test_crud import get_data
from Logic.ieftinire_rezervari import get_ieftinire_rezervari
from Logic.crud import read
from Logic.undo_redo import do_redo, do_undo
from Domain.rezervare import get_pret
def test_ieftinire():
    rezervari = get_data()
    undo_lst=[]
    redo_lst=[]
    modificare_rezervari=get_ieftinire_rezervari(rezervari,10,undo_lst,redo_lst)
    modificare_rezervari=do_undo(undo_lst,redo_lst,modificare_rezervari)
    rezervare_veche=read(rezervari,1)
    rezervare_noua=read(modificare_rezervari,1)
    assert get_pret(rezervare_veche)==get_pret(rezervare_noua)
    modificare_rezervari = do_redo(undo_lst, redo_lst, modificare_rezervari)
    rezervare_noua = read(modificare_rezervari, 1)
    assert get_pret(rezervare_veche)>get_pret(rezervare_noua)
    try:
        _=get_ieftinire_rezervari(rezervari,10000,undo_lst,redo_lst)
        assert False
    except ValueError:
        assert True

