

print('1) Create a new file \n2) Display the file\n3) Add a new item to the file\n')

lst=input('Make a selection 1, 2 or 3: ')

if lst!='1' and lst!='2' and lst!='3' :
    print('Make a selection 1, 2 or 3!')

elif lst=='1':
    p=input('Print item name: ')
    file=open('Subject.txt','w')
    file.write(p +'\n')
    file.close()

elif lst=='2':
    file = open('Subject.txt', 'r')
    print(file.read())

elif lst=='3':
    pnew=input('Enter new item: ')
    file = open('Subject.txt', 'a')
    file.write(pnew + '\n')
    file.close()
    file=open('Subject.txt', 'r')
    print(file.read())
    file.close()









