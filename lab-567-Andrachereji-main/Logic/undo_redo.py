def do_undo(undo_lst,redo_lst,current_lst):
    '''
    Sterge ultima operatie facuta
    :param undo_lst: lista dupa stergere
    :param redo_lst: lista dinaintea stergerii
    :param current_lst: lista curenta
    :return: lista dupa ce a avut loc undo
    '''
    if undo_lst:
        redo_lst.append(current_lst)
        return undo_lst.pop()
    return None
def do_redo(undo_lst, redo_lst,current_lst):
    '''
    Revine la operatiunea dinaintea stergerii
    :param undo_lst: lista dupa stergere
    :param redo_lst: lista dinaintea stergerii
    :param current_lst: lista curenta
    :return: lista dupa ce a avut loc redo
    '''
    if redo_lst:
        top_redo=redo_lst.pop()
        undo_lst.append(current_lst)
        return top_redo
    return None

