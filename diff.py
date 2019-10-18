def index_by_newlines(a, sign):
    return [ [i, v, sign] for i,v in enumerate(a.split("\n")) ]


def diff(a, b):
    # separate left and right into arrays indexed by line
    a = index_by_newlines(a, '-')
    b = index_by_newlines(b, '+')

    # remove matching lines
    for va in a[:]:
        for vb in b:
            if va[1] == vb[1]:
                a.remove(va)
                b.remove(vb)
                continue

    # print in line index order with right or left symbols, + or -
    c = a + b
    c.sort(key=lambda v: v[0])
    return c

a = """a
b
c"""

b = """a
a
x
b"""

for v in diff(a,b):
    print(v[2] + v[1])
