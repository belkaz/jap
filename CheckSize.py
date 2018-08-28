import Ca

def checkSize ( arr, cols ):
    rezArr = Ca.Negatives(arr)
            
    for j in range ( len ( rezArr[1] )):
        PosOfInsert = 0   
        for i in range ( len ( cols )):
            if rezArr[1][j] >= cols[i]:
                    PosOfInsert += 1 
        if PosOfInsert == 0:
            for i in range ( rezArr[0][j], rezArr[0][j] + rezArr[1][j] ):
                arr[i] = 1

    print ( arr )


# на входе массив и надор данных для размещения
# на выходе массив без ячеек, дипазон которых не подходит
checkSize([0,0,1,0,1],[1, 2])