from Domain.rezervare import get_id
from Logic.crud import adaugare, read
from Logic.undo_redo import do_redo, do_undo
def test_undo_redo():
    rezervari=[]
    undo_lst=[]
    redo_lst=[]
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da', undo_lst, redo_lst)
    rezervari=do_undo(undo_lst,redo_lst,rezervari)
    assert len(rezervari)==2
    for elem in rezervari:
        if get_id(elem) == 1 or get_id(elem) == 2:
            assert True
    rezervari=do_undo(undo_lst,redo_lst,rezervari)
    assert len(rezervari)==1
    assert read(rezervari,1) is not None
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 0
    assert do_undo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari) == 0
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da', undo_lst, redo_lst)
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari)==3
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 1
    assert read(rezervari,1) is not None
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 2
    assert read(rezervari,1) is not None
    assert read(rezervari,2) is not None
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 3
    assert read(rezervari, 1) is not None
    assert read(rezervari, 2) is not None
    assert read(rezervari,3) is not None
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari) == 1
    assert read(rezervari, 1) is not None
    rezervari = adaugare(rezervari, 4, 'r4', 'business', 1000, 'Nu', undo_lst, redo_lst)
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari)==2
    assert read(rezervari, 1) is not None
    assert read(rezervari, 4) is not None
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==1
    assert read(rezervari, 1) is not None
    rezervari = do_undo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==0
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    rezervari = do_redo(undo_lst, redo_lst, rezervari)
    assert len(rezervari)==2
    assert read(rezervari, 1) is not None
    assert read(rezervari, 4) is not None
    assert do_redo(undo_lst, redo_lst, rezervari) is None
    assert len(rezervari) == 2



