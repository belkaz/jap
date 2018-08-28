def Negatives ( arr ) :
    rezArr = []
    indArr = []
    sum0 = 0   
    for i in range ( len ( arr ) ):
        if arr[i] == 1:            
            if len ( arr[sum0 : i] ) > 0:  
                rezArr.append ( len( arr[sum0 : i]) )    
                indArr.append ( sum0 )                           
            sum0 = i + 1   
    if len ( rezArr ) > 0:
        rezArr.append ( len( arr[sum0 : len ( arr )]) )    
        indArr.append ( sum0 )                         
    return [indArr , rezArr]

# на входе строка, на выходе два массива - индексы начала пустых диапозонов
# и размер данных диапозонов
# если подать пустой диапозон - пустые массивы

