import pickle
f = open('Bin.dat','wb+')
stu = {}
while True:
    rno = int(input('Enter roll no.'))
    n = input('Enter name:')
    m = float(input('Enter marks:'))
    stu['roll no.'] = rno
    stu['Name'] = n
    stu['Marks']= m
    pickle.dump(stu,f)
    z = input('Do you want to continue?:')
    if z == 'n':
        break
    
x = int(input('Enter roll no. for searching'))
f.seek(0)
flag=0
try:
    while True:
    
        l = pickle.load(f)
        if l['roll no.']== x:
            print('record found')
            print(l)
            flag = 1
