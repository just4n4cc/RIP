import sys
import math

def isFloat(par):
    try:
        float(par)
        return True
    except ValueError:
        return False

def getCoeff(index, coef):
    try:
        s = sys.argv[index]
    except:
        s = input("Введите коэффициент {} \n".format(coef))
    while not isFloat(s):
       print("Ошибка. Введите коэффициент {} заново".format(coef))
       s = input()
    return float(s)

def calcRoots(a, b, c):
    roots = []
    D = b*b - 4*a*c
    print(D)
    if D < 0:
        return roots
    D2 = (-b + math.sqrt(D)) / (2*a)
    D3 = (-b - math.sqrt(D)) / (2*a)
    if D2 < 0 and D3 < 0:
        return roots
    if D2 >= 0:
        roots.append(math.sqrt(D2))
        roots.append(-roots[len(roots)-1])
    if D3 >= 0:
        roots.append(math.sqrt(D3))
        roots.append(-roots[len(roots)-1])
    return list(set(roots))

def main():
    a = getCoeff(1, 'a')
    b = getCoeff(2, 'b')
    c = getCoeff(3, 'c')
    print(a, b, c)
    result = calcRoots(a,b,c)
    num = len(result)
    if num == 0:
        print("\nНет корней")
    elif num == 1:
        print("\n{} корень: \n{}".format(num, result[0]))
    else:
        print("\n{} корня:".format(num))
        for item in result:
            print(round(item, 3))

if __name__ == "__main__":
    main()
