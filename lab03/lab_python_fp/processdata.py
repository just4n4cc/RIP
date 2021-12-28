import json
import sys
from unique import Unique
from printresult import print_result
from field import field
from genrandom import gen_random
from cmtimer import cm_timer_1

path = '../data_light.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return (sorted(Unique(list(field(arg, 'job-name')), ignore_case=True), key=str.lower))

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('Программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list((f"{j} зарплата {s} р" for j, s in zip(arg, gen_random(len(arg), 100000, 200000))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
