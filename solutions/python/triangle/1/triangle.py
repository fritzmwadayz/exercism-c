def equilateral(sides):
    a, b, c = sides

    if _validate(sides):
        if a == b and b == c:
            return True
    return False


def isosceles(sides):
    a, b, c = sides
        
    if _validate(sides) == True:
        if a == b or a == c or b == c:
            return True 
    return False

def scalene(sides):
    a, b, c = sides
    
    if _validate(sides) == True:
        if a != b and a != c and b != c:
            return True
    return False

def _validate(sides):
    '''Helper function that ensures the triangle is valid.'''
    a, b, c = sides
    
    if a==0 or b==0 or c==0:
        return False

    if a + b >= c and b + c >= a and a + c >= b:
        return True