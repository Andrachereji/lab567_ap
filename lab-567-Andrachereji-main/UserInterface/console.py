from Logic.crud import adaugare,read,modificare,stergere
from Domain.rezervare import get_str,get_id,get_nume,get_pret,get_checkin,get_clasa,creeaza_rezervare
from Logic.trecere_clasa_superioara import modificare_clasa
from Logic.ieftinire_rezervari import get_ieftinire_rezervari
from Logic.pret_maxim_clase import get_pret_max_clase
from Logic.ordonare_dupa_pret import ordonare
from Logic.afisare_suma_pret_dupa_nume import suma_preturilor_dupa_nume
from Logic.undo_redo import do_undo,do_redo
def show_menu():
    print('1.CRUD')
    print('2.Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara')
    print('3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit')
    print('4.Determinarea prețului maxim pentru fiecare clasă.')
    print('5. Ordonarea rezervărilor descrescător după preț')
    print('6.Afișarea sumelor prețurilor pentru fiecare nume')
    print('u.Undo')
    print('r.Redo')
    print('X.Exit')
def handle_adaugare(rezervari,undo_lst,redo_lst):
    try:
        id=int(input('Dati id-ul rezervarii'))
        nume =input('Dati numele rezervarii')
        clasa =input('Dati clasa la care se face rezervarea')
        pret = float(input('Dati pretul rezervarii'))
        checkin =input('Precizati cu Da/Nu starea checkin-ului la aceasta rezervare')
        return adaugare(rezervari, id, nume, clasa, pret, checkin,undo_lst,redo_lst)
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari
def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))
def handle_show_details(rezervari):
    id_rezervare=int(input('Dati id-ul rezervarii pentru care doriti detalii'))
    rezervare=read(rezervari,id_rezervare)
    print(f'nume:{get_nume(rezervare)}')
    print(f'clasa:{get_clasa(rezervare)}')
    print(f'pret:{get_pret(rezervare)}')
    print(f'checkin:{get_checkin(rezervare)}')
def handle_modificare(rezervari,undo_lst,redo_lst):
    try:
        id = int(input('Dati id-ul rezervarii care se actualizeaza'))
        nume = input('Dati noul nume')
        clasa = input('Dati noua clasa la care se face rezervarea')
        pret = float(input('Dati noul pret'))
        checkin = input('Precizati cu Da/Nu starea checkin-ului la aceasta noua rezervare')
        return modificare(rezervari, creeaza_rezervare(id,nume,clasa,pret,checkin),undo_lst,redo_lst)
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari
def handle_stergere(rezervari,undo_lst,redo_lst):
    try:
        id = int(input('Dati id-ul rezervarii care se va sterge'))
        return stergere(rezervari,id,undo_lst,redo_lst)
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari

def handle_crud(rezervari,undo_lst,redo_lst):
    while True:
        print('1.Adaugare')
        print('2.Modificare')
        print('3.Stergere')
        print('a.Afisare')
        print('d.Detalii rezervare')
        print('b.Revenire')
        optiune=input('Optiunea aleasa:')
        if optiune=='1':
            rezervari=handle_adaugare(rezervari,undo_lst,redo_lst)
        elif optiune=='2':
            rezervari=handle_modificare(rezervari,undo_lst,redo_lst)
        elif optiune=='3':
            rezervari=handle_stergere(rezervari,undo_lst,redo_lst)
        elif optiune=='a':
            handle_show_all(rezervari)
        elif optiune=='d':
            handle_show_details(rezervari)
        elif optiune=='b':
            break
        else:
            print('Optiune invalida')
    return rezervari
def handle_modificare_clasa(rezervari,undo_lst,redo_lst):
    try:
        nume=input('Dati numele a caror rezervari vor fi modificate:')
        rezervari=modificare_clasa(rezervari,nume,undo_lst,redo_lst)
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari
def handle_ieftinire_rezervari(rezervari,undo_lst,redo_lst):
    try:
        procentaj=int(input('Dati procentajul cu care se vor ieftini rezervarile'))
        rezervari=get_ieftinire_rezervari(rezervari,procentaj,undo_lst,redo_lst)
        return rezervari
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari
def handle_pret_max_clasa(rezervari):
    result=get_pret_max_clase(rezervari)
    for clasa in result:
        print(f'{clasa}:{result[clasa]}')
def handle_ordonare(rezervari):
    rezervari=ordonare(rezervari)
    return rezervari
def handle_suma_nume(rezervari):
    result=suma_preturilor_dupa_nume(rezervari)
    for name in result:
        print(f'{name}:{result[name]}')
def handle_undo(rezervari,undo_lst,redo_lst):
    undo_result=do_undo(undo_lst,redo_lst,rezervari)
    if undo_result:
        return undo_result
    return rezervari
def handle_redo(rezervari,undo_lst, redo_lst):
    redo_result = do_redo(undo_lst, redo_lst,rezervari)
    if redo_result:
        return redo_result
    return rezervari

def run_UI(rezervari,undo_lst,redo_lst):
    while True:
        handle_show_all(rezervari)
        show_menu()
        optiune=input('Optiunea aleasa:')
        if optiune=='1':
            rezervari=handle_crud(rezervari,undo_lst,redo_lst)
        elif optiune=='2':
            rezervari=handle_modificare_clasa(rezervari,undo_lst,redo_lst)
        elif optiune=='3':
            rezervari=handle_ieftinire_rezervari(rezervari,undo_lst,redo_lst)
        elif optiune=='4':
            handle_pret_max_clasa(rezervari)
        elif optiune=='5':
            handle_ordonare(rezervari)
        elif optiune=='6':
            handle_suma_nume(rezervari)
        elif optiune=='u':
            rezervari=handle_undo(rezervari,undo_lst,redo_lst)
        elif optiune=='r':
            rezervari=handle_redo(rezervari,undo_lst,redo_lst)
        elif optiune=='x':
            break
        else:
            print('Optiune invalida')
    return rezervari
