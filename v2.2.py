q = int(input('q: '))
w = int(input('w: '))
e = int(input('e: '))

if (q > w and q < e) or (q > e and q < w):
        print(q)
elif (w > q and w < e) or (w > e and w < q):
        print(w)
elif (e > q and e < w) or (e > w and e < q):
        print(e)
elif q == w or q== e or w == e:
        print('error')