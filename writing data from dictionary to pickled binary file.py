n=int(input("How many students data you want to save: "))
d={} #empty dict
for i in range(n):
    print("\nEnter data for", i+1, "student")
    name= input("Enter student name: ")
    marks=float(input("Enter students marks: "))
    d[name]=marks #keeps adding new key value pairs in the dictionary d
    
import pickle
f=open("csmarks.dat", "wb")
pickle.dump(d,f)
f.close()
