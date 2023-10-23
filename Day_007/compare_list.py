def list_compare(list1,list2) :
    result = True;
    for i in range (0,len(list1)):
        if list1[i] != list2[i]:
            result = False;
    return result;

list1 = [2,3,5,9,10]
list2 = [2,3,5,90,10]
print(list_compare(list1 , list2))