def sort_helper(tpl_item):
    return tpl_item[1]

number=int(input("Give the number of tuples: "))
lst=[]
for item in range(number):
    tpl1=int(input("give the first number "))
    tpl2=int(input("give the second number "))
    tpl=(tpl1,tpl2)
    lst.append(tpl)
print(lst)

result=sorted(lst,key=sort_helper)
print(result)


