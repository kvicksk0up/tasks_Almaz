def fibonac():
    lst=[0,1]
    i=-1
    while i<100:
        lst.append(lst[-1]+lst[-2])
        i+=1
    print(lst)
fibonac()

