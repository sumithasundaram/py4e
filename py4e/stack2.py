import re

if __name__ =="__main__":

    sum = 0
    # fname=("/home/superadmin/PycharmProjects/py4e/stack.txt")
    fn = open("/home/superadmin/PycharmProjects/py4e/stack1.txt", 'r+')
    f = fn.readlines()
    # print(f)
    l=[]
    for line in f:
        # print(line)
        numbers = re.findall(r'\d+',line)
        # print(numbers)
        if len(numbers) > 0:
            l.append(numbers)

    # print(l)
    mylist = l
    for x in mylist:
        # print(x)
        for y in x:
             # print(type(y))
             y = int(y)
             sum += y
    print(sum)




    #print(type(l))
    #b = sum(l)
    '''
    sum=0
    for i in l:
        print(i)
        if len(i) > 0:
            sum = sum+i
    print(sum)
    '''

































