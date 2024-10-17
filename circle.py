import math

def area(r):
    ''' 
    Вычисляет площадь оркужности радиуса r
    по формуле:
        area = pi * r^2

        Входные данные:
            double r : радиус окружности

        Выходные данные:
            double area : площадь оружности
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Вычисляет длину окружности 
    радиуса r по формуле:
        perimeter = 2 * pi * r

        Входные данные:
            double r : радиус окружности
        
        Выходные данные:
            double perimeter : длина окружности радиуса r
    '''
    return 2 * math.pi * r