'''__author__ = 'Merlin'
grade =input ("enter score:")
# print(type(grade))
grade = float(grade)
if( grade >= 0.9):
    print("grade A:")
elif(grade >= 0.8):
     print("grade B:")
elif(grade >= 0.7):
    print("grade C:")
elif(grade >= 0.6 ):
    print("grate D:")
else:
    print("grade F:")
print (grade)
'''

grade =input ("enter score:")
# print(type(grade))
grade = float(grade)
# print(grade)
# print(type(grade)
if((grade <= 0) or (grade >= 1)):
    print("error")
else:
    if( grade >= 0.9):
       print("A")
    elif(grade >= 0.8):
        print("B")
    elif(grade >= 0.7):
        print("C")
    elif(grade >= 0.6 ):
        print("D")
    else:
        print("F")
        print (grade)
