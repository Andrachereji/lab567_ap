from Tests.test_crud import test_adaugare, test_read, test_modificare,test_stergere
from Tests.test_trecere_clasa_superioara import test_modificare_clasa
from Tests.test_ieftinire_rezervari import test_ieftinire
from Tests.test_pret_maxim_clase import test_pret_max_clase
from Tests.test_ordonare_pret import test_ordonare
from Tests.test_suma_pret_nume import test_suma_preturilor_dupa_nume
from Tests.teste_undo_redo import test_undo_redo
from UserInterface.console import run_UI
from Logic.crud import adaugare
from UserInterface.command_line_console import handle_comand_line
def main():
    rezervari = []
    undo_lst=[]
    redo_lst=[]
    rezervari = adaugare(rezervari, 1, 'r1', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 2, 'r2', 'economy', 350, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 3, 'r3', 'economy_plus', 500, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 4, 'r4', 'business', 1000, 'Nu', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 5, 'r5', 'economy', 260, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 6, 'r5', 'economy', 100, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 7, 'r3', 'economy', 200, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 8, 'r1', 'economy', 240, 'Da', undo_lst, redo_lst)
    rezervari = adaugare(rezervari, 9, 'r2', 'economy', 440, 'Da', undo_lst, redo_lst)
    print("1. Pentru meniu vechi")
    print("2. Pentru meniu nou cmd")
    optiune = input("Alegeti tipul de meniu pe care vreti sa il folositi:")
    while True:
        if optiune == '1':
            rezervari = run_UI(rezervari,undo_lst,redo_lst)
        elif optiune=='2':
            rezervari = handle_comand_line(rezervari,undo_lst,redo_lst)
        else:
            print('optiune invalida')

if __name__ == '__main__':
    test_adaugare()
    test_read()
    test_modificare()
    test_stergere()
    test_modificare_clasa()
    test_ieftinire()
    test_pret_max_clase()
    test_ordonare()
    test_suma_preturilor_dupa_nume()
    test_undo_redo()
    main()