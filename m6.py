def alphabet():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 1
    for i in a:
        print(i, "-", b, end = ', ')
        b += 1
alphabet()
def spisok():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 1

    q={}
    for i in a:
        q[b]=i
        b+=1
    print(q)
spisok()
