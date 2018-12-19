def extendList(val, list=[]):
    list.append(val)
    return list
#List list=[] allocation is done when we execute function like pelow before the print function
#
list2 = extendList(123,[])
list3 = extendList('a')
# list=['a']
print("list1 = %s "% extendList(10))
print "list2 = %s" % list2
print "list3 = %s" % list3
# list=['a', 10]

### Here we have already defiend that list is Empty each time when function alled list initialized to empty

def extendList(val, list=None):
    if list is None:
       list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
