import hashlib

def hdiff(seq, ind):
    return [ [i, ind, hashlib.sha1(v).hexdigest(), v] for i,v in enumerate(seq) ]

def hsort(i):
    return i[2]

def isort(i):
    return i[0]

def diff(left, right):
    hs = hdiff(left, '-') + hdiff(right, '+')

    rows_by_hash = {}
    for h in hs:
        rows_by_hash.setdefault(h[2], []).append(h)

    single_rows = []
    for h in rows_by_hash:
        if len(rows_by_hash[h]) == 1:
           single_rows += rows_by_hash[h]

    single_rows.sort(key=isort)
    return [ l[1] + l[3] for l in single_rows ]

left = 'a b c a d e f'.split()
right = 'x a b c'.split()
print(left)
print(right)
print(diff(left, right))
