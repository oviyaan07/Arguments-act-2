def cube(num):
    return (num*num*num)
def by_3(num):
    if num%3==0:
        return cube(num)
    else:
        return False
a=by_3(6)
print (a)