def esCuadrado(sudoku):

    assert isinstance(sudoku, list)
    numerosColumna = len (sudoku)
    for fila in sudoku:

        numerosFila = len(fila)
        if numerosFila == numerosColumna:
            continue
        else:
            return False
    return True



    


