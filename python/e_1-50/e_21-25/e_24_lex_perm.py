def gen_lex_perm(arr):
    assert type(arr) is list
    assert type(arr[0]) is int
    arr = sorted(arr)
    to_int = lambda x: int(''.join([str(_) for _ in x]))
    expand = lambda arr: []
    yield 


print([_ for _ in gen_lex_perm([0,1,2])])

