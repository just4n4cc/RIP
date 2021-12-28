class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.ignore_case = False if len(kwargs) == 0 else kwargs.get('ignore_case')
        self.unique = set()

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            elem = self.items[self.index]
            self.index = self.index + 1
            check = str(elem).lower() if (isinstance(elem, str) and self.ignore_case) else elem
            if check not in self.unique:
                self.unique.add(check)
                return elem

    def __iter__(self):
        return self


def main():
    data = ['AA', 'aa', 'dd', 'Aa', 7]
    for i in Unique(data, ignore_case=True):
        print(i)


if __name__ == "__main__":
    main()
