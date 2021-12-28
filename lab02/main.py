from  lab_python_oop.circle import Circle 
from  lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    rec = Rectangle('красный', 2, 3)
    circ = Circle('розовый', 4)
    sq = Square('синий', 5)
    print(rec)
    print(circ)
    print(sq)

if __name__ == "__main__":
    main()
