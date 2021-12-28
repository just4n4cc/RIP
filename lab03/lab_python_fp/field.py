def field(items, *args):
    assert len(args) > 0
    for i in items:
        if len(args)==1:
            if i.get(args[0])!=None:
                yield i.get(args[0])
        else:
            res=[]
            for key in args:
                res.append(dict.fromkeys([key], i.get(key) ) )if i.get(key)!=None else None
            if res!=[]:
                yield res
