import re

test_string="dgsfbdslnceaij"
inlist= re.findall(".",test_string)
outlist=[]
for element in inlist:
    if inlist.index(element)%2 ==0 :
        element= element.upper()
        outlist.append(element)
    else:
        element= element.lower()
        outlist.append(element)


outstring="".join(outlist)

print(outstring)







