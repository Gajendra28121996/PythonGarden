##Give a name to ur list [] << means u have to store number of data in list
friends=["Gajendra","Stan Lee","Enstine","Iron Man","Skarlett Jhonson"]
#List Index:  0     ,    1     ,    2    ,      3   .          4 
print(friends)
## Access Array Value
print("Your index Holds : "+friends[-4])
## -1 : Skarlett Jhonson
## -2 : Iron Man
## -3 : Enstine
## -4 : Stan Lee
## -5 : Gajendra
## Its called Negative Index in python refered as last element, second last  and so on....

## Exception of first element u want to print all following element the use semi colon after ur exception
print(friends[1:])
## Print in a particular Range of list [Print from : Except this Element]
print(friends[1:3])
##Update list Element 
friends[1]='God'
print(friends[1])