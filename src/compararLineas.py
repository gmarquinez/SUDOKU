def compararLineas(sudoku):
    for x in sudoku:
        for num in x:
            contarNumero = x.count(num)
            if contarNumero > 1:
                return False
    return True





   

