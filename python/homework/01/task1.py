import math
def func(a, b, c):
    '''
    This function calculates the asser of equation ax^2+bx+x=0
    a:float b:float c: float
    return: tuple or None
    '''
    D = b ** 2 - 4 * a * c
    if a == 0:
        if b == 0:
            return None
        else:


            return( x )
    elif D < 0:
        return None
    elif D > 0:
        x1 = ( - b - math.sqrt(D)) / (2 * a)
        x2 = ( - b + math.sqrt(D)) / (2 * a)
        return ( x1, x2 )
    else:
        x = - b / ( 2 * a )
        return ( x )

    
assert func(-2,1,1) == (1,-0.5)
assert func(1,1,1) == None
assert func(1,2,1) == (-1)
print('ok')