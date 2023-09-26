k  = int(input('k-'))
f  = int(input('f-'))
c = int(input('c-'))
if k <f+c and f<k+c and c<k+f:
        print('существование возможно')
else:
        print('существование не возможно')