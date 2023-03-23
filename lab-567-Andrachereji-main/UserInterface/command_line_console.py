from Logic.crud import adaugare,stergere
from Domain.rezervare import get_str
def show_menu():
    print('pentru adaugarea unuei noi rezervari scrieti:')
    print('add, id:un numar intreg, nume, clasa:economy/economy_plus/business, pret:un numar float, checkin:Da daca checkin-ul s-a facut sau Nu in caz contrar')
    print('pentru stergerea unuei rezervari scrieti: delete, id:un numar intreg')
    print('pentru afisarea tuturor datelor scrieti: showall')
    print('comenzile sunt separate prin ";"')
    print('pentru iesire scrieti: i')

def handle_comand_line(rezervari,undo_lst,redo_lst):
    while True:
        show_menu()
        optiune=input('Dati sirul de comenzi dorite:')
        if optiune=='i':
            break
        else:
            comenzi=optiune.split(';')
            for elemente in comenzi:
                date = elemente.split(',')
                if date[0] == 'add':
                    try:
                        rezervari=adaugare(rezervari, int(date[1]), date[2], date[3], float(date[4]), date[5],undo_lst,redo_lst)
                    except ValueError as ve:
                        print("Eroare", ve)
                elif date[0] == 'delete':
                    try:
                        rezervari = stergere(rezervari, int(date[1]),undo_lst,redo_lst)
                    except ValueError as ve:
                        print("Eroare", ve)
                elif date[0]=='showall':
                       for rezervare in rezervari:
                           print(get_str(rezervare))
                else:
                    print('optiune invalida')




