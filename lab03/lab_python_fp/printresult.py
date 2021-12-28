from typing import List

def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res=func(*args, **kwargs)
        if isinstance(res, List):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for k, v in res.items():
                print(k, '=', v)
        else:
            print(res)
        return res
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
