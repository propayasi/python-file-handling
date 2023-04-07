import pickle


#creation
f=open('studentthing.dat','wb+')
stu={}
ask=int(input('press 1 to input values'))
while ask==1:
    name=input('enter a name ')
    rollno=int(input('rollno'))
    mark=float(input('marks'))
    stu['name']=name
    stu['rollno']=rollno
    stu['mark']=mark
    pickle.dump(stu,f)
    ask=int(input('press 1 to continue putting in values'))
#reading and modification
f.seek(0)
try:
    while True:
        pos=f.tell()
        post=pickle.load(f)
        if post['mark']>81:
          post['mark']+=2
          f.seek(pos)
          pickle.dump(post,f)
except EOFError:
    print('all records have been read')
f.seek(0)
ASK=int(input('1 if u want to read all the values'))
if ASK==1:

    try:
        while True:
            p=pickle.load(f)
            print(p)
    except EOFError:
        print('all done')
f.close()











