def is_even(input_list):
    '''
    This function calculates the asser of equation ax^2+bx+x=0
    input_list:list[int]
    return: tuple(List[int])
    '''
    is_ev=[]
    not_ev=[]
    for i in input_list:
        if not type(i)==int:
            return None
        elif i%2==1:
            not_ev.append(i)
        else:
            is_ev.append(i)
    return (is_ev,not_ev)

assert is_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2,4,6,8,10],[1,3,5,7,9])
assert is_even([]) == ([],[])
assert is_even([1,2,3,'e',4,5]) == None
print('ok')