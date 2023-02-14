import Examples14th


#so this represents list created from any source. could be from reading a file
names= ["S one",'S two','S three']
gpas = [3.5,3.26,3.78]

#this is just a for loop that appends each object to a list, the objects dont have names you can reference them by but they have index locations
#i can access any individual student now by doing students[0] or so on
students = [Examples14th.Student(n,q) for n,q in zip(names,gpas)]

#this is just creating the course and everything after this is normal shit
course = Examples14th.Course(students)
deans_list = course.get_deans_list()

for s in deans_list:
    print(f'{s.get_last()}\t{s.get_gpa()}')


