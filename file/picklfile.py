import pickle,Student

f=open("student.dat","wb+")
s=Student.Student(123,"Maish",89)
pickle.dump(s,f)

obj=pickle.load(f)
obj.display()